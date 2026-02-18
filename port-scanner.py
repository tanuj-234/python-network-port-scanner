import socket
from datetime import datetime

target = input("Enter target IP address: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid IP address or hostname.")
    exit()

common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    443: "HTTPS"
}

print(f"\nScanning target: {target_ip}")
print("Scanning started at:", datetime.now())
print("-" * 50)

start_time = datetime.now()

for port in common_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = sock.connect_ex((target_ip, port))
    
    if result == 0:
        print(f"Port {port} ({common_ports[port]}) is OPEN")

    sock.close()

end_time = datetime.now()
total_time = end_time - start_time

print("-" * 50)
print("Scanning completed at:", end_time)
print("Total scan duration:", total_time)
