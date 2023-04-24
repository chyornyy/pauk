# ПАУК - Changelog

## Version 1.0.0 (2023-04-24)
This is the initial release of the program.

### Added
1. Ping scanning and port scanning functionality.
2. Telegram integration that sends the scan results to a specified chat.
3. IP address range and port range arguments in CIDR and hyphen/comma-separated format respectively.
4. Telegram bot token and chat ID arguments for integration.
5. Debugging option to enable debug information.
6. Progress bar using the tqdm package to display progress during the scan.
7. Retrieval of IP information using the ipinfo.io API.
8. Operating system detection using nmap.

#### The following functions have been added:
- parse_arguments(): Parses command line arguments.
- main(): The main function that performs ping and port scanning, retrieves IP information, and sends the results to a Telegram chat.
- ping(ip_address): Function that pings an IP address to check if it is up.
- scan_ports(ip_address, port_range, args, port_bar): Function that scans ports for an IP address.

#### The following packages have been imported:
- argparse
- ipaddress
- socket
- subprocess
- requests
- tqdm
- aiogram
- nmap3

### Changed
None.
### Deprecated
None.
### Removed
None.
### Fixed
None.
### Security
None.

Note: This program is distributed under the MIT license.