# -*- encoding: utf-8 -*-

import logging.config
from conf import settings
from core import app

def auth(func):
    def wrapper(*args, **kwargs):
        if not app.user_data['name']:
            print('\033[31m用户未登录，请登录！\033[0m')
        else:
            return func(*args, **kwargs)
    return wrapper

def get_logger(name=__name__):
    logging.config.dictConfig(settings.LOGGING_CONFIG)
    return logging.getLogger(name)

