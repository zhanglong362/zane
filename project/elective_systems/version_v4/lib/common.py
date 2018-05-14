# -*- encoding: utf-8 -*-

import os
import logging.config
from conf import settings

def auth(role):
    from core import admin, teacher, student
    def handler(func):
        def wrapper(*args, **kwargs):
            if admin.USER['name'] or teacher.USER['name'] or student.USER['name']:
                return func(*args, **kwargs)
            print('\033[31m请先登录！\033[0m')
            if role == 'admin':
                admin.login()
            if role == 'teacher':
                teacher.login()
            if role == 'student':
                student.login()
        return wrapper
    return handler

def get_logger(name=__name__):
    logging.config.dictConfig(settings.LOGGING_CONFIG)
    return logging.getLogger(name)

def get_object_list(obj_type):
    obj_path = os.path.join(settings.DB_PATH, obj_type)
    return os.listdir(obj_path)








