# 🕷🕸 ПАУК (Spider)
CLI IP Scanner and Port Checker with Telegram Notifications

## 🚧 Disclaimer
The program provided is intended for educational and research purposes only. It may involve techniques that may violate the laws of information security and privacy of private data. The creators and maintainers of this program do not condone or support any illegal activities.

The program should only be used on authorized systems with explicit permission from the owner of the system. The user assumes all responsibility and risk for any actions taken using this program. The creators and maintainers of this program are not responsible for any damages or legal issues that may arise from the misuse of this program.

It is the responsibility of the user to ensure that their actions comply with all applicable laws and regulations regarding information security and privacy. This program should not be used to access or modify any private data without the explicit consent of the owner of that data.

By using this program, you agree to the terms and conditions outlined in this disclaimer.

## Prerequisites
- Python 3.6+
- pip3

## Installation

### Installation for Linux
1. Open a terminal and clone the repository to your local machine.
```
git clone https://github.com/chyornyy/pauk.git
```
2. Navigate to the project directory.
```
cd pauk
```
3. Run the setup script.
```
chmod +x setup.sh && ./setup.sh
```
### Installation for MacOS
1. Open a terminal and clone the repository to your local machine.
```
git clone https://github.com/chyornyy/pauk.git
```
2. Navigate to the project directory.
```
cd pauk
```
3. Run the setup script.
```
chmod +x setup.sh && ./setup.sh
```

### Installation for Windows
Note: The Windows installation option will come soon.

### Creating a Telegram Bot
1. Open the Telegram app.
2. Search for the ["BotFather"](https://t.me/BotFather) bot and start a conversation with it. 
3. Type /newbot and follow the prompts to create a new bot.
4. Once the bot is created, BotFather will provide you with a token. Save this token somewhere secure.
5. Go to your new bot and type /start.

### Getting the Chat ID
1. Open the Telegram app.
2. Search for the ["Get My ID"](https://t.me/getmyid_bot) bot and start a conversation with it.
3. Once you text something it will answer you:
```
Your user ID: <chat_id>
Current chat ID: <chat_id>
```

## Note: It is important to keep your bot token and chat ID secure, as they can be used to access your bot and potentially sensitive information.

## Usage
Activate virtual environment with
```
source venv/bin/activate
```
```
python3 pauk.py <ip_range> --ports <ports> --token <bot_token> --chat <chat_id> -d
```
#### The arguments are described below:
```
<ip_range>: This is a required argument that specifies the IP address range to scan. It should be in CIDR format.
```
```
--ports <ports>: This is an optional argument that allows you to specify a range of ports to scan. The ports can be separated by a hyphen (e.g. 1-1024) or a comma-separated list (e.g. 80,443).
```
```
--token <bot_token>: This is a required argument that specifies the Telegram bot token.
```
```
--chat <chat_id>: This is a required argument that specifies the chat ID of the user or group where you want to receive the notifications.
```
```
-d: This is an optional flag that enables debug mode.
```

### Here are some examples of how to use the program:
#### Example 1: Scan a range of IP addresses for open ports and send the results to a Telegram chat:
Suppose you want to scan a range of IP addresses and send the results to a Telegram chat. You can use this program by providing the IP address range and Telegram bot token and chat ID as arguments. Here is an example command:
```
python3 pauk.py 192.168.0.0/24 -p 80,443 -t <bot_token> -c <chat_id>
```
This command will scan the IP addresses in the range 192.168.0.0/24 on ports 80 and 443 and send the results to the specified Telegram chat.

#### Example 2: Scan a single IP address for open ports:
If you want to scan a single IP address for open ports, you can use this program by providing the IP address and port range as arguments. Here is an example command:
```
python3 pauk.py 192.168.0.1 -p 1-65535 -t <bot_token> -c <chat_id>
```
This command will scan the IP address 192.168.0.1 on all ports between 1 and 65535.

#### Example 3: Scan a range of IP addresses and ports and print the results and debugging info to the console:
If you want to print the results of the port scan to the console, you can use this program by providing the IP address range and port range as arguments. Here is an example command:
```
python3 pauk.py 192.168.0.0/24 -p 1-1024 -t <bot_token> -c <chat_id> -d
```
This command will scan the IP addresses in the range 192.168.0.0/24 on ports from 1 to 1024 and print the results to the console.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Development Team
#### [Aleksandr Chyornyy](https://github.com/chyornyy) - Backend