import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

def main():
    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind socket to server address and port
    sock.bind((SERVER_IP, SERVER_PORT))

    print(f"UDP Chat Server started on {SERVER_IP}:{SERVER_PORT}")

    while True:
        # Receive message from client
        data, addr = sock.recvfrom(1024)
        print(f"\nMessage from {addr[0]}:{addr[1]}: {data.decode('utf-8')}")

if __name__ == "__main__":
    main()
