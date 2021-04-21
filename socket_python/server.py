import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

while True:
    client_socket, address = s.accept()
    print(f"connction from {address} established")
    client_socket.send(bytes("Welcome to DV Server World","utf-8"))
    client_socket.close()