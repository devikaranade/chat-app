import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

def main():
    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        # Get user input
        message = input("Enter your message: ")

        # Send message to server
        sock.sendto(message.encode('utf-8'), (SERVER_IP, SERVER_PORT))

if __name__ == "__main__":
    main()
