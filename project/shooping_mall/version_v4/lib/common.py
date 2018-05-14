# -*- encoding: utf-8 -*-

import logging.config
from conf import settings

def auth(func):
    from core import app
    def wrapper(*args, **kwargs):
        if not app.USER:
            print('\033[31m用户未登录，跳转至登陆！\033[0m')
            app.login()
            return
        return func(*args, **kwargs)
    return wrapper

def get_logger(name=__name__):
    logging.config.dictConfig(settings.LOGGING_CONFIG)
    return logging.getLogger(name)



