# -*- encoding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8080))
while True:
    msg = s.recv(1024)
    print('\033[31m新消息：%s\033[0m' % msg.decode('utf-8'))
    data = input('>>>>: ').strip()
    if msg.decode('utf-8') == 'Goodbye!':
        break
    s.send(data.encode('utf-8'))
    s.send()
    print('接收消息中 ..')
s.close()




