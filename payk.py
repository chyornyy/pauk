from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import argparse
import ipaddress
import nmap3
import socket
import subprocess
import requests
import tqdm

nmap = nmap3.Nmap()


def parse_arguments():
    parser = argparse.ArgumentParser(description='Scan a range of IP addresses for open ports and send the results to Telegram.')
    parser.add_argument('ip_range', help='IP address range to scan in CIDR format')
    parser.add_argument('--ports', '-p', default='1-65535', help='Port range to scan, separated by a hyphen (e.g. 1-1024), or a comma-separated list of ports (e.g. 80,443)')
    parser.add_argument('--token', '-t', required=True, help='Telegram bot token')
    parser.add_argument('--chat', '-c', required=True, help='Telegram chat ID')
    parser.add_argument('--debug', '-d', action='store_true', help='Enable debugging information')
    args = parser.parse_args()
    try:
        ip_range = ipaddress.ip_network(args.ip_range)
    except ValueError:
        parser.error('Invalid IP address range')

    # Validate the port range or list of ports
    if '-' in args.ports:
        start_port, end_port = args.ports.split('-')
        if not start_port.isdigit() or not end_port.isdigit() or int(start_port) < 1 or int(end_port) > 65535 or int(start_port) > int(end_port):
            parser.error('Invalid port range')
    else:
        port_list = args.ports.split(',')
        for port in port_list:
            if not port.isdigit() or int(port) < 1 or int(port) > 65535:
                parser.error('Invalid port list')

    return args


def main():
    args = parse_arguments()
    # Clear the results dictionary and the progress bar
    results = {}

    # Parse the IP address and port range
    ip_range = ipaddress.ip_network(args.ip_range)
    if not ip_range:
        print("Please enter a valid IP address range.")
        return

    if '-' in args.ports:
        start_port, end_port = map(int, args.ports.split('-'))
        port_range = range(start_port, end_port + 1)
    else:
        port_range = [int(port) for port in args.ports.split(",")]

    # Set up the Telegram bot
    bot_token = args.token
    chat_id = args.chat
    bot = Bot(token=bot_token)
    dispatcher = Dispatcher(bot)

    # Parse the port range only once
    port_range = list(port_range)

    # Perform ping scanning only if IP address is valid
    try:
        socket.inet_aton(str(ip_range[0]))
    except socket.error:
        if args.debug:
            print(f'Invalid IP address: {ip_range[0]}')
        return

    # Loop through each IP address in the range and perform ping and port scanning
    total_ips = ip_range.num_addresses
    with tqdm.tqdm(total=total_ips, desc='Scanning IPs') as progress_bar:
        for ip_address in ip_range:
            if args.debug:
                print(f'Scanning IP: {ip_address}')

            # Perform ping scanning
            is_up = ping(str(ip_address))
            if not is_up:
                if args.debug:
                    print(f'Host is down: {ip_address}')
                progress_bar.update(1)
                continue

            # If the IP address is live, perform port scanning
            with tqdm.tqdm(total=len(port_range), desc=f'Scanning ports of {ip_address}') as port_bar:
                open_ports = scan_ports(str(ip_address), port_range, args, port_bar)

            # Collect the IP information using ipinfo.io API
            response = requests.get(f"https://ipinfo.io/{ip_address}/json")
            data = response.json()

            # Determine the Operating System
            os_info = get_os_info(str(ip_address))
            message = ""
            if open_ports:
                message += f"IP Address {ip_address} is live.\nOpen ports: {open_ports}\n\n"
                message += f"City: {data['city']}\nRegion: {data['region']}\nCountry: {data['country']}\n"
                message += f"Timezone: {data['timezone']}\nPostal: {data['postal']}\n\n"
                if 'hostname' in data:
                    message += f"Hostname: {data['hostname']}\n"
                else:
                    message += "Hostname: Unknown\n"
                message += f"Organization: {data['org']}\n\n"
                message += f"OS: {os_info}"

                if args.debug:
                    print(message)
                    try:
                        async def send_message():
                            await bot.send_message(chat_id=chat_id, text=message)
                        executor.start(dispatcher, send_message())
                    except Exception as e:
                        if args.debug:
                            print(f"Error sending message to Telegram: {str(e)}")
                print("Scan complete.")


def ping(ip_address):
    ping_cmd = ['ping', '-c', '1', '-W', '1', ip_address]
    ping_response = subprocess.run(ping_cmd, capture_output=True)
    return ping_response.returncode == 0


def scan_ports(ip_address, port_range, args, port_bar):
    open_ports = []
    for port in port_range:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            try:
                s.connect((ip_address, port))
                open_ports.append(port)
            except (socket.timeout, ConnectionRefusedError):
                pass
            except Exception as e:
                if args.debug:
                    print(f"Error scanning port {port} of {ip_address}: {e}")
        port_bar.update(1)
    return open_ports


def get_os_info(ip_address):
    default_value = 'Unknown'
    try:
        result = nmap.nmap_os_detection(ip_address)
        if ip_address in result:
            os_matches = result[ip_address].get('osmatch', [])
            if os_matches:
                os_info = os_matches[0]['name']
            else:
                os_info = default_value
        else:
            os_info = default_value
    except nmap3.exceptions.NmapExecutionFailed:
        os_info = default_value
    return os_info


if __name__ == '__main__':
    main()
