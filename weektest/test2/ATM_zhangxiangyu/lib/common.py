#coding:utf-8

import logging.config
from core import src
from conf import  settings

#装饰器
def login_auth(func):
    def wrapper(*args,**kwargs):
        if not src.user_info['is_auth']:
            src.login()
        else:
            return func(*args,**kwargs)
    return wrapper



def get_logger(name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    loger = logging.getLogger(name)
    return loger
