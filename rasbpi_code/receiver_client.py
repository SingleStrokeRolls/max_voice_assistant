import socket

def do_receive():
    server_ip = '192.168.3.178'
    server_port = 8079

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((server_ip, server_port))

    server_socket.listen(5)

    print("server started. Waiting...")
    client_socket, client_address = server_socket.accept()
    print(f"client connected: {client_address}")

    with open('test.wav', 'wb') as file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)
    print("Received.")
    client_socket.close()
    server_socket.close() 

