# ПАУК - ToDo-List

## This file lists the features and improvements that are planned for the future.

### Security
1. Add Disclaimer

### RunTime and efficiency optimization
1. Support Multithreading with automatic detection and manual input option
2. Support Multiprocessing with automatic detection and manual input option
3. Implement support for scanning multiple IP addresses at once

### Features
1. Colored output to terminal
2. Add support for scanning UDP ports
3. Implement a GUI interface for the program
4. Collecting even more info from ip
5. installation from .sh for linux
6. installation from .bat for windows

### Improvements
1. Add support for specifying the timeout value for scans
2. Improve the logging system to make it easier to debug issues
3. Improve the error handling and reporting system

### Bug Fixes
1. Fix issue where program crashes when scanning certain IP addresses
2. Fix issue where program incorrectly reports open ports as closed

### IP Scanning options
1. Scan Ips of certain country by flag
2. Scan only live-ips, without port scanning
3. Scan both Ips and Ports
4. Send every alive ip-address and ports or send bulks

### Ports Scanning options
1. Scan all ports (1-65535)
2. Scan main ports (1-1025)
3. Scan popular ports (21,22,23,25,53,80,110,111,135,139,143,389,443,445,993,995,1723,3306,3389,5900,8080)
4. Scan certain ports by flag (ssh=22,http=80,https=44s,etc.)

### Database integrations
1. Save scanning info in PostgreSQL, MySQL databases

### Output options
1. Send output to Discord
2. Send output by email
3. Save output as .csv
4. Save output as .json
5. Save output as .txt
6. Save output as .xslx

### Infrastructure
1. Run programm from Docker container