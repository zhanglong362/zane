from socket import *
import time

s = socket()
s.bind(('127.0.0.1', 8080))
s.listen(5)
s.setblocking(False)

r_list = []
w_list = []
while True:
    time.sleep(0.5)
    try:
        conn, addr = s.accept()
        r_list.append(conn)
    except BlockingIOError:
        print('可以去干其它活了')
        print('rlist: ', len(r_list))

        # 收消息
        del_rlist = []
        for conn in r_list:
            data = conn.recv(1024)
            if not data:
                del_rlist.append(conn)
                continue
            w_list.append((conn, data))


        # 发消息
        del_wlist = []
        for item in w_list:
            try:
                conn = item[0]
                res = item[1]
                conn.send(res)
                del_wlist.append(item)
            except BlockingIOError:
                continue
            except ConnectionResetError:
                conn.close()
                del_wlist.append(item)

            for conn in del_rlist:
                r_list.remove(conn)
            for item in del_wlist:
                w_list.remove(item)


