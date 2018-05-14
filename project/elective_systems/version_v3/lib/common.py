# -*- encoding: utf-8 -*-

import logging.config
from conf import settings

def auth(name, role):
    from core import admin, teacher, student
    def handler(func):
        def wrapper(*args, **kwargs):
            if name:
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



