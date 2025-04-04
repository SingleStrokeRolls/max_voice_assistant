import socket
import os

def do_send():
    # Set the server IP address and port number
    server_ip = '192.168.3.244'
    server_port = 8080

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    print("Connecting to server...")
    client_socket.connect((server_ip, server_port))

    # Send file
    print("Sending file...")

    file_path = 'output.wav'
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.send(data)

    print("File transfer complete.")

    # Close the connection
    client_socket.close()

