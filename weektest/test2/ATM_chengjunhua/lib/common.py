from core import src
from conf import settings
import logging
#检测是否登陆
def login_auth(fun):
    def wrapper(*args,**kwargs):
        if not src.users['status']:
            src.login()
        else:
            return fun(*args,**kwargs)
    return wrapper


#写日志
def get_logger(name):
    logging.config.dictConfig(settings.LOGGING_DIC)  # 导入上面定义的logging配置
    l1=logging.getLogger(name)
    return l1