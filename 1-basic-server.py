import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))

server_socket.listen(1)
print("Server is listening on port 12345...")

client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

try:    
    message = client_socket.recv(1024).decode()
    print(f"Received from client: {message}")
    client_socket.send(message.encode())
    print(f"Echoed back to client: {message}")
finally:
    client_socket.close()
    server_socket.close()
    print("Server closed.")

