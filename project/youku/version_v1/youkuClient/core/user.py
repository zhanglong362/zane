# -*- encoding: utf-8 -*-

from lib import common
from client import tcpClient
from conf import settings

COOKIES = {
    'role': 'admin',
    'name': None,
    'session_id': None
}
client = None

def login():
    common.show_green('登陆')
    if COOKIES['session_id']:
        common.show_red('用户不能重复登录')
        return
    while True:
        name = common.input_string('用户名')
        password = common.input_string('密码')
        params = {
            'api': 'login',
            'session_id': None,
            'data_size': None,
            'is_file': False,
            'role': 'admin',
            'name': name,
            'password': password
        }
        res = client.send_data(params)
        if res['flag']:
            COOKIES['session_id'] = res['session_id']
            COOKIES['name'] = name
            common.show_green(res['message'])
            return
        else:
            common.show_red(res['message'])

def register():
    common.show_green('注册')
    while True:
        name = common.input_string('注册用户名')
        password = common.input_string('注册密码')
        password2 = common.input_string('确认密码')
        if password != password2:
            common.show_red('两次输入密码不一致！')
            continue
        params = {
            'api': 'register',
            'session_id': None,
            'data_size': None,
            'is_file': False,
            'role': 'admin',
            'name': name,
            'password': password
        }
        res = client.send_data(params)
        if res['flag']:
            common.show_green(res['message'])
            return
        else:
            common.show_red(res['message'])

@common.auth(COOKIES['role'])
def release_announcement():
    common.show_green('发布公告')
    while True:
        announcement = common.input_string('公告名')
        content = common.input_string('公告内容')
        params = {
            'api': 'release_announcement',
            'session_id': COOKIES['session_id'],
            'data_size': None,
            'is_file': False,
            'role': 'admin',
            'announcement': announcement,
            'content': content
        }
        res = client.send_data(params)
        if res['flag']:
            common.show_green(res['message'])
            return
        else:
            common.show_red(res['message'])


def choose_upload_video():
    upload_video_list = common.get_upload_video_list()
    if not upload_video_list:
        common.show_red('当前无可上传视频！')
        return
    while True:
        common.show_info(*upload_video_list)
        choice = common.input_integer('请选择上传视频编号')
        if choice == 'q':
            return
        if choice<0 or choice>len(upload_video_list):
            common.show_red('选择编号非法！')
            continue
        return upload_video_list[choice]

@common.auth(COOKIES['role'])
def upload_video():
    common.show_green('上传视频')
    while True:
        file_name = choose_upload_video()
        if not file_name:
            return
        file_size = common.get_file_size(file_name)
        params = {
            'api': 'upload_video',
            'session_id': COOKIES['session_id'],
            'data_size': None,
            'is_file': True,
            'role': 'admin',
            'file_name': file_name,
            'file_size': file_size
        }
        res = client.send_data(params)
        if res['flag']:
            common.show_green(res['message'])
            return
        else:
            common.show_red(res['message'])

def get_online_video():
    params = {
        'api': 'get_online_video',
        'session_id': COOKIES['session_id'],
        'data_size': None,
        'is_file': False,
        'role': 'admin'
    }
    online_video_list = client.send_data(params)
    if not online_video_list:
        common.show_red('当前没有在线视频！')
        return
    while True:
        common.show_info(*online_video_list)
        choice = common.input_integer('请选择在线视频编号')
        if choice == 'q':
            return
        if choice < 0 or choice > len(online_video_list):
            common.show_red('选择编号非法！')
            continue
        return online_video_list[choice]

@common.auth(COOKIES['role'])
def remove_video():
    common.show_green('删除视频')
    while True:
        file_name = get_online_video()
        if not file_name:
            return
        params = {
            'api': 'remove_video',
            'session_id': COOKIES['session_id'],
            'data_size': None,
            'is_file': False,
            'role': 'admin',
            'file_name': file_name
        }
        res = client.send_data(params)
        if res['flag']:
            common.show_green(res['message'])
            return
        else:
            common.show_red(res['message'])

def run():
    global client
    client = tcpClient.TcpClient(settings.server_address)
    menu = {
        '1': [login, '登陆'],
        '2': [register, '注册'],
        '3': [release_announcement, '发布公告'],
        '4': [upload_video, '上传视频'],
        '5': [remove_video, '删除视频']
    }
    while True:
        common.show_green('按"q"登出')
        common.show_menu(menu)
        choice = common.input_string('请输入平台编号')
        if choice == 'q':
            common.show_red('logout!')
            return
        if choice not in menu:
            common.show_red('选择编号非法！')
            continue
        menu[choice][0]()