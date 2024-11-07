import socket

def send_file(filename, host='127.0.0.1', port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    with open(filename, "rb") as file:
        a=file.read()
        client_socket.send(a)  
            

    print(f"File '{filename}' sent to server.")
    client_socket.close()

if __name__ == "__main__":
    filename = "file_to_send.txt"  
    send_file(filename)
