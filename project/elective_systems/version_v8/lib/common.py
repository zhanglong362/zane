# -*- encoding: utf-8 -*-

import os
import logging.config
from conf import settings

def auth(role):
    from core import admin, teacher, student
    def handler(func):
        def wrapper(*args, **kwargs):
            if role == 'admin' and not admin.CURRENT_USER:
                print('\033[31m管理员未登录，跳转至登陆！\033[0m')
                admin.login()
                return
            if role == 'teacher' and not teacher.CURRENT_USER:
                print('\033[31m老师未登录，跳转至登陆！\033[0m')
                teacher.login()
                return
            if role == 'student' and not student.CURRENT_USER:
                print('\033[31m学生未登录，跳转至登陆！\033[0m')
                student.login()
                return
            return func(*args, **kwargs)
        return wrapper
    return handler

def input_string(word):
    while True:
        string = input('%s >>: ' % word).strip()
        if not string:
            print('\033[31m不能是空字符！\033[0m')
            continue
        return string

def input_integer(word, score=False):
    while True:
        string = input('%s >>: ' % word).strip()
        if not string:
            print('\033[31m不能是空字符！\033[0m')
            continue
        if string == 'q':
            return string
        if not string.isdigit():
            print('\033[31m请输入数字！\033[0m')
            continue
        if score:
            return float(string)
        return int(string)

def get_object_list(type_name):
    type_path = os.path.join(settings.BASE_DB, type_name)
    if not os.path.exists(type_path) or not os.path.isdir(type_path):
        return
    return os.listdir(type_path)

def get_logger(name=__name__):
    logging.config.dictConfig(settings.LOGGING_CONFIG)
    return logging.getLogger(name)

