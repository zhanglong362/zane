# -*- encoding: utf-8 -*-

import os

server_address = ('127.0.0.1', 8080)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
download_path = os.path.join(BASE_DIR, 'data', 'download')
upload_path = os.path.join(BASE_DIR, 'data', 'upload')
