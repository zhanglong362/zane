
from core import src
import logging.config
from conf import setting

# user_data={
#     'name':None,
#     'is_auth':False
# }

def login_auth(func):
    def wrapper(*args,**kwargs):
        if not src.user_data['is_auth']:
            print('\033[45m必须先登陆，傻叉！！！\033[0m')
            src.login()
        else:
            return func(*args,**kwargs)
    return wrapper

def get_logger(name):
    logging.config.dictConfig(setting.LOGGING_DIC)  # 导入上面定义的logging配置
    logger = logging.getLogger(name)  # 生成一个log实例
    return logger

