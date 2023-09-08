import socket
import pyfiglet
b=pyfiglet.figlet_format("LEVI-THE_CODER")
print(b)
def scan_ports(target, start_port, end_port):
    open_ports = [] 
    print(f"Scanning target: {target}")
    print("Scanning in progress...")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((target, port))
        print(f"Scanning port {port}...")
        if result == 0:
            open_ports.append(port)
        sock.close()

    if len(open_ports) > 0:
        print("Open ports:")
        for port in open_ports:
            print(f"Port {port}: Open")
    else:
        print("No open ports found.")

# Prompt user for input
target_ip = input("Enter the target IP address: ")
start_port = 1
end_port = 65535

scan_ports(target_ip,start_port,end_port)
