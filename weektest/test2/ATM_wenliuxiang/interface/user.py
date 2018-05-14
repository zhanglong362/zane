
from db import db_handler
from conf import  setting
from lib import common
def get_userinfo_interfacen(name):
    user_dic=db_handler.select(name)
    return user_dic



def register(name,password,account=15000):
    user_dic={
        'name':name,
        'password':password,
        'locked':False,
        'account':account,
        'creidt':account,
        'bankflow':[]
    }
    db_handler.update(user_dic)
    common.get_logger(print('用户%s注册成功' % name))

def lock_user_interface(name):
    user_dic=get_userinfo_interfacen(name)
    user_dic['locked']=True
    db_handler.select(user_dic)