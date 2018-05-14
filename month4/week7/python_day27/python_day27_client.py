import time
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        client.connect(('127.0.0.1', 8080))
    except OSError:
        print('等待3秒 ..')
        time.sleep(3)
    else:
        while True:
            msg = input('>>>: ').strip()
            if not msg: continue
            client.send(msg.encode('utf-8'))
            data = client.recv(1024)
            print(data.decode('utf-8'))
    finally:
        if client:
            client.close()



