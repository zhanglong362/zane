# 1. 基于TCP的套接字
import socket
import struct
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(1)

while True:
    try:
        conn, client_addr = server.accept()
        print(client_addr)
        while True:
            try:
                length_bytes = conn.recv(4)
                if not length_bytes: break
                length = struct.unpack('i', length_bytes)[0]

                header_bytes = conn.recv(length)
                if not header_bytes: break
                header = json.loads(header_bytes.decode('utf-8'))
                print('header: %s' % header)

                data_bytes = conn.recv(header['data_size'])
                data = json.loads(data_bytes.decode('utf-8'))
                if not data: break
                print('data: %s' % data)
                # conn.send(data.upper())
            except Exception:
                break
    finally:
        conn.close()
server.close()


