import socket

def make_connection(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            print(f"Connected to {host} on port {port}")
    except Exception as e:
        print(f"Failed to connect to {host} on port {port}: {e}")

# Successful connection
make_connection("webpros.com", 80) 

# Unsuccessful connection
make_connection("127.0.0.1", 4343)
