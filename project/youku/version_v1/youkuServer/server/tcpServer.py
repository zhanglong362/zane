# -*- encoding: utf-8 -*-

import os
import time
import socket
import struct
import json
from conf import settings
from lib import common
from interface import admin_api, user_api
from concurrent.futures import ThreadPoolExecutor

server_pool = ThreadPoolExecutor(50)


class TcpServer:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.server.bind(settings.server_address)
            self.server.listen(settings.backlog)
        except Exception as e:
            raise Exception(e)

    def __del__(self):
        self.server.close()


def done_load(res):
    res = res.result()
    common.show_green(res)


def send_vidoe(self, data):
    file_path = os.path.join(settings.video_path, data['file_name'])
    data_len_bytes = struct.pack('i', len(data['file_size']))
    self.client.send(data_len_bytes)
    with open(r'%s' % file_path, 'rb') as f:
        for line in f:
            self.client.send(line)
    return 'Send video %s complete!' % data['file_name']


def receive_video(self, conn, data, buffer_size=1024):
    data_len_bytes = self.client.recv(4)
    data_length = struct.unpack('i', data_len_bytes)[0]
    file_path = os.path.join(settings.video_path, data['file_name'])
    with open(r'%s' % file_path, 'ab') as f:
        recv_size = 0
        while recv_size < data_length:
            last_size = data_length - recv_size
            if last_size < buffer_size:
                buffer_size = last_size
            recv_data = self.client.recv(buffer_size)
            recv_size += len(recv_data)
            f.write(recv_data)
    data = {
        'message': 'Receive video %s complete!' % data['file_name']
    }
    conn.send(conn, data)
    return data['message']


def recv_data(conn):
    data_len_bytes = conn.recv(4)
    data_length = struct.unpack('i', data_len_bytes)[0]

    data_bytes = conn.recv(data_length)
    data = json.loads(data_bytes.decode('utf-8'))

    if data['is_file']:
        server_pool.submit(receive_video, conn, data).add_done_callback(done_load)
    return data


def send_data(conn, data):
    data_bytes = json.dumps(data).encode('utf-8')
    data_len_bytes = struct.pack('i', len(data_bytes))

    conn.send(data_len_bytes)
    conn.send(data_bytes)

    if data['is_file']:
        server_pool.submit(send_vidoe, data).add_done_callback(done_load)


def dispatch(params):
    admin_func = {
        'login': admin_api.login,
        'register': admin_api.register,
        'release_announcement': admin_api.release_announcement,
        'upload_video': admin_api.upload_video,
        'remove_video': admin_api.remove_video
    }
    user_func = {
        'login': user_api.login,
        'register': user_api.register
    }
    if params['role'] == 'admin':
        result = admin_func[params['api']](params)
        return result
    if params['role'] == 'user':
        result = user_func[params['api']](params)
        return result


def handle(conn):
    while True:
        try:
            params = recv_data(conn)
            if not params:
                conn.close()
                return
            result = dispatch(params)
            send_data(result)
        except Exception as e:
            print('Exception: %s' % e)
            conn.close()
            return 


def run(poll_interval=0.05):
    sock = TcpServer()
    while True:
        conn, client_address = sock.server.accept()
        print('connect from: %s' % client_address)
        server_pool.submit(handle, conn)
        time.sleep(poll_interval)
