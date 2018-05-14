import os
from socket import *
from threading import Thread,current_thread

def client():
    client = socket()
    client.connect(('127.0.0.1', 8080))

    while True:
        data = '%s hello' % current_thread.__name__
        client.send(data.encode('utf-8'))
        res = client.recv(1024)
        print(res.decode('utf-8'))

if __name__ == '__main__':
    for i in (500):
        t = Thread(target=client)
        t.start()









