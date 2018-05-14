# -*- encoding: utf-8 -*-

import logging.config
from conf import settings


def get_logger(name=__name__):
    logging.config.dictConfig(settings.LOGGING_CONFIG)
    return logging.getLogger(name)

def auth(name, role):
    from core import admin, teacher, student
    def handler(func):
        def wrapper(*args, **kwargs):
            if name:
                return func(*args, **kwargs)
            if role == 'admin':
                print('\033[31m请先登录！\033[0m')
                admin.login()
            if role == 'teacher':
                print('\033[31m请先登录！\033[0m')
                teacher.login()
            if role == 'student':
                print('\033[31m请先登录！\033[0m')
                student.login()
        return wrapper
    return handler

