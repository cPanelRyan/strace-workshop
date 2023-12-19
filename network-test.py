import socket

def create_socket():
    try:
        host = '8.8.8.8'
        port = 53
        print(f"Successfully connected to {host} on port {port}")
        s.close()
    except PermissionError:
        print("Permission denied: Unable to create the socket.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_socket()
