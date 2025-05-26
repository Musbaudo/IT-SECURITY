import socket

def scan_ports(target, start_port, end_port):
    print(f"Scanning ports on {target}...\n")
    try:
        # Resolve target IP address
        target_ip = socket.gethostbyname(target)

    except socket.gaierror:
        print("Hostname could not be resolved.")
        return

    try:
        # Scan ports within the specified range
        for port in range(start_port, end_port + 1):
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout for the connection attempt
            socket.setdefaulttimeout(1)

            # Attempt to connect to the target IP and port
            result = s.connect_ex((target_ip, port))

            # If the connection was successful, print the port is open
            if result == 0:
                try:
                    # Attempt to retrieve the service name
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown"

                print(f"Port {port} is open\t-->\t{service}")
            s.close()

    except KeyboardInterrupt:
        print("\nExiting program.")
        exit()

    except socket.error:
        print("Couldn't connect to server.")
        exit()


if __name__ == "__main__":
    target_host = input("Enter target hostname or IP address: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    scan_ports(target_host, start_port, end_port)