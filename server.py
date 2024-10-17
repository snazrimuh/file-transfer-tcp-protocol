import socket
import time

def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5001))
    server_socket.listen(1)
    
    print("Server is listening for connections...")
    
    while True:
        conn, addr = server_socket.accept()
        print(f"Connection established from {addr}")
        
        metadata = conn.recv(1024).decode('utf-8')
        file_name, file_size = metadata.split(',')
        file_size = int(file_size) 
        
        print(f"Receiving file: {file_name}, Size: {file_size} bytes")
        
        start_time = time.time()

        with open(file_name, 'w') as f:
            while True:
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break
                f.write(data)

        end_time = time.time()
        time_taken = end_time - start_time
        print(f"File '{file_name}' received in {end_time - start_time:} seconds")

        conn.close()

tcp_server()
