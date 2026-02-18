# Python Network Port Scanner

## Overview
This project is a TCP port scanner built using Python’s socket module.  
It scans common ports on a target machine and identifies open services.

## Features
- TCP connection-based scanning
- Common port identification (FTP, SSH, HTTP, DNS, etc.)
- Scan duration tracking
- Error handling for invalid hosts

## Technologies Used
- Python 3
- socket module
- datetime module

## How It Works
The scanner attempts to establish TCP connections to specified ports.
If a connection is successful, the port is marked as open.

## Example Usage
Enter target IP address: 127.0.0.1

## Disclaimer
This project is developed for educational purposes only.
Only scan systems you own or have permission to test.

## Sample Output

Scanning target: 127.0.0.1
--------------------------------
[OPEN] Port 8000 - HTTP-Alt
--------------------------------
Scan completed in 0:00:02.134567