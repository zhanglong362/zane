import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 8080))

while True:
    client_data, client_addr = server.recvfrom(1024)
    print(client_data.decode('utf-8'), client_addr)
    server.sendto(client_data.upper(), client_addr)







