# -*- encoding: utf-8 -*-

import os
import json
import struct
import socket
from lib import common
from conf import settings
from concurrent.futures import ThreadPoolExecutor

client_pool = ThreadPoolExecutor(5)

class TcpClient:
    def __init__(self, server_address):
        self.server_address = server_address
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client.connect(self.server_address)
        except Exception as e:
            raise Exception(e)

    def __del__(self):
        self.client.close()

    def done_load(self, res):
        res = res.result()
        common.show_green(res)

    def upload_vidoe(self, data):
        file_path = os.path.join(settings.upload_path, data['file_name'])
        data_len_bytes = struct.pack('i', len(data['file_size']))
        self.client.send(data_len_bytes)
        with open(r'%s' % file_path, 'rb') as f:
            for line in f:
                self.client.send(line)
        result = self.recv_data()
        return result['message']

    def download_video(self, data, buffer_size=1024):
        data_len_bytes = self.client.recv(4)
        data_length = struct.unpack('i', data_len_bytes)[0]
        file_path = os.path.join(settings.download_path, data['file_name'])
        with open(r'%s' % file_path, 'ab') as f:
            recv_size = 0
            while recv_size < data_length:
                last_size = data_length - recv_size
                if last_size < buffer_size:
                    buffer_size = last_size
                recv_data = self.client.recv(buffer_size)
                recv_size += len(recv_data)
                f.write(recv_data)
        return 'Download video %s complete!' % data['file_name']

    def recv_data(self):
        data_len_bytes = self.client.recv(4)
        data_length = struct.unpack('i', data_len_bytes)[0]

        data_bytes = self.client.recv(data_length)
        data = json.loads(data_bytes.decode('utf-8'))

        if data['is_file']:
            client_pool.submit(self.download_video, data).add_done_callback(self.done_load)
        return data

    def send_data(self, data):
        data_bytes = json.dumps(data).encode('utf-8')
        data_len_bytes = struct.pack('i', len(data_bytes))

        self.client.send(data_len_bytes)
        self.client.send(data_bytes)

        if data['is_file']:
            client_pool.submit(self.upload_vidoe, data).add_done_callback(self.done_load)
        return self.recv_data()


