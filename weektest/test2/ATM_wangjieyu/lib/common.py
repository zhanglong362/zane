import logging.config
from core import src
from  conf import setting

def login_auth(func):
    def wrapper(*args, **kwargs):
        if not src.panduan['is_auth']:
            print('没有登录')
            src.login()
        else:
            return func(*args, **kwargs)

    return wrapper

def get_logger(name):
    logging.config.dictConfig(setting.LOGGING_DIC)
    logger = logging.getLogger(name)
    return logger


