# -*- encoding: utf-8 -*-

import sys
import logging.config
from conf import settings


def get_logger(name=__name__):
    logging.config.dictConfig(settings.LOGGING_CONFIG)
    return logging.getLogger(name)

def auth(func):
    def wrapper(*args, **kwargs):
        if not app.CURRENT_USER:
            print('用户未登录，请先登录！')
            app.login()
        else:
            return func(*args, **kwargs)
        return wrapper

def loggut(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res == 'quit':
            print('Goodbye!')
            sys.exit()
        else:
            return res
        return wrapper
