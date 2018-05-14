from socket import *
from gevent import monkey;monkey.patch_all()

def talk(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            print(data)
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()


def server(ip, port, backlog=5):
    s = socket()
    s.bind((ip, port))
    s.listen(backlog)

    while True:
        conn, addr = s.accept()
        print(addr)

        # 通信
        g = spawn(talk, conn)


    s.close()

if __name__ == '__main__':
    server('127.0.0.1', 8080)






