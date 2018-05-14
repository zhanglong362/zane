import logging.config
from conf import settings
from core import src
def logger(name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger = logging.getLogger(name)
    return logger
def login_(fuck):
    def inner(*args,**kwargs):
        if not src.dict['state']:
            src.login()
        else:
            return fuck(*args,**kwargs)
    return inner
