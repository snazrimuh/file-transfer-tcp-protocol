import socket
import time
import os

def tcp_client(file_path):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.85.205', 5001))
    
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    metadata = f"{file_name},{file_size}"
    client_socket.send(metadata.encode('utf-8'))
    
    time.sleep(1)

    start_time = time.time()
    with open(file_path, 'r') as f:
        data = f.read(1024)
        while data:
            client_socket.send(data.encode('utf-8'))
            data = f.read(1024)

    client_socket.close()
    
    end_time = time.time()
    print(f"File '{file_name}' sent in {end_time - start_time:.2f} seconds, Size: {file_size} bytes")

tcp_client('file_1.txt')
tcp_client('file_2.txt')
tcp_client('file_3.txt')
tcp_client('file_4.txt')
