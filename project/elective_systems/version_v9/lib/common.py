# -*- encoding: utf-8 -*-

import os
import logging.config
from conf import settings


def login_auth(role):
    from core import admin, teacher, student
    def handler(func):
        def wrapper(*args, **kwargs):
            if role == 'admin' and not admin.CURRENT_USER:
                show_red('管理员未登录，跳转至登陆！')
                admin.login()
                return
            if role == 'teacher' and not teacher.CURRENT_USER:
                show_red('老师未登录，跳转至登陆！')
                teacher.login()
                return
            if role == 'student' and not student.CURRENT_USER:
                show_red('学生未登录，跳转至登陆！')
                student.login()
                return
            return func(*args, **kwargs)
        return wrapper
    return handler


def show_menu(menu):
    print('=' * 30)
    for k, v in menu.items():
        print('%-4s %-10s' % (k, v[1]))
    print('=' * 30)


def show_info(*args, **kwargs):
    print('-' * 30)
    if args:
        for k, v in enumerate(args):
            print('%-4s %-10s' % (k, v))
    if kwargs:
        for k, v in enumerate(kwargs):
            print('%-4s %-10s %-10s' % (k, v, kwargs[v]))
    print('-' * 30)

def show_red(word):
    print('\033[31m%s\033[0m' % word)


def show_green(word):
    print('\033[32m%s\033[0m' % word)


def input_string(word):
    while True:
        string = input('%s >>: ' % word).strip()
        if not string:
            show_red('不能输入空字符！')
        return string


def input_integer(word, is_float=False):
    while True:
        string = input('%s >>: ' % word).strip()
        if not string:
            show_red('不能输入空字符！')
            continue
        if string == 'q':
            return string
        if not string.isdigit():
            show_red('请输入数字！')
        if is_float:
            return float(string)
        return int(string)


def get_logger(name=__name__):
    logging.config.dictConfig(settings.LOGGING_CONFIG)
    return logging.getLogger(name)


def get_object_list(type_name):
    type_path = os.path.join(settings.BASE_DB, type_name)
    if not os.path.isdir(type_path):
        return
    return os.listdir(type_path)

def show_object_list(type_name):
    object_list = get_object_list(type_name)
    if not object_list:
        show_red('%s 列表为空！' % type_name.capitalize())
        return
    show_info(object_list)
    return object_list

def get_object_name(type_name=None, object_list=None):
    while True:
        if type_name and not object_list:
            object_list = show_object_list(type_name)
        choice = input_integer('请选择对象的编号')
        if choice == 'q':
            return
        if choice < 0 or choice > len(object_list):
            show_red('选择编号超出范围！')
            continue
        return object_list[choice]




