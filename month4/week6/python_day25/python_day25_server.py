# -*- encoding: utf-8 -*-

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 获取空的TCP套接字对象
s.bind(('127.0.0.1', 8080))          # 绑定端口
s.listen(5)                          # 启动监听
while True:
    conn, client_addr = s.accept()   # 等待连接
    print('客户端： ', client_addr)
    conn.send('欢迎访问服务器！'.encode('utf-8'))
    while True:
        try:
            print('接收消息中 ..')
            msg = conn.recv(1024)    # 接收消息 1024 字节最大限制
            print('\033[31m新消息: %s\033[0m' % msg.decode('utf-8'))
            if msg.decode('utf-8') == 'quit':
                conn.send('Goodbye!'.encode('utf-8'))
            data = input('>>>>: ').strip()
            conn.send(data.encode('utf-8'))
        except ConnectionAbortedError as e:
            print('ConnectionAbortedError: %s' % e)
            break
        except ConnectionResetError as e:
            print('ConnectionResetError: %s' % e)
            break
        except Exception as e:
            print('Exception: %s' % e)
            break
    conn.close()
s.close()



















