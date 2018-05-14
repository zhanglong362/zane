# -*- encoding: utf-8 -*-

import os
from conf import settings

def auth(role):
    from core import admin, user
    def handle(func):
        def wrapper(*args, **kwargs):
            if role == 'admin' and not admin.COOKIES['session_id']:
                show_red('用户未登录，跳转至登陆！')
                admin.login()
                return
            if role == 'user' and not user.COOKIES['session_id']:
                show_red('用户未登录，跳转至登陆！')
                user.login()
                return
            return func(*args, **kwargs)
        return wrapper
    return handle

def show_menu(menu):
    print('=' * 30)
    for k, v in menu.items():
        print('%-4s %-10s' % (k, v[1]))
    print('=' * 30)

def show_info(*args, **kwargs):
    print('=' * 30)
    if args:
        for i, key in enumerate(args):
            print('%-4s %-10s' % (i, key))
    if kwargs:
        for i, key in enumerate(kwargs):
            print('%-4s %-10s %-10s' % (i, key, kwargs[key]))
    print('=' * 30)

def show_red(word):
    print('\033[31m%s\033[0m' % word)

def show_green(word):
    print('\033[32m%s\033[0m' % word)

def input_string(word):
    while True:
        string = input('%s >>: ' % word).strip()
        if not string:
            show_red('不能输入空字符！')
            continue
        return string

def input_integer(word):
    while True:
        string = input('%s >>: ' % word).strip()
        if not string:
            show_red('不能输入空字符！')
            continue
        if string == 'q':
            return string
        if not string.isdigit():
            show_red('请输入数字！')
            continue
        return int(string)

def get_upload_video_list():
    return os.listdir(settings.upload_dir)

def get_file_size(file_name):
    return os.path.getsize(file_name)




