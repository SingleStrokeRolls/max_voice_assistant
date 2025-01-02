import socket
import os

def do_send():
    # 设置树莓派的IP地址和端口号
    server_ip = '192.168.3.178'
    server_port = 8080

    # 创建一个socket对象
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接到服务器
    print("connecting to server...")
    client_socket.connect((server_ip, server_port))

    # 发送文件
    print("Sending...")

    file_path = 'test.wav'
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.send(data)

    print("Sending Completed.")

    # 关闭连接
    client_socket.close()