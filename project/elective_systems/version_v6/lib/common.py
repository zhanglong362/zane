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

def get_logger(name=__name__):
    logging.config.dictConfig(settings.LOGGING_CONFIG)
    return logging.getLogger(name)

def get_object_list(type_name):
    type_path = os.path.join(settings.BASE_DB, type_name)
    if not os.path.exists(type_path):
        return
    return os.listdir(type_path)


