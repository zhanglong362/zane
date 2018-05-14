#coding:utf-8

from db import db_handler
from lib import common

user_loger = common.get_logger('User')

def get_userinfo_interface(name):
    return db_handler.select(name)


def user_pwd_interface(name,pwd,balance=15000):
    user_dic = {
        'name':name,
        'password':pwd,
        'locked':False,
        'account':balance,
        'limit':balance,
        'flow_log':[]
    }
    user_loger.info('%s用户注册成功！' % name)
    db_handler.update(user_dic)




def user_locked_interface(name):
    user_dic = db_handler.select(name)
    user_dic['locked'] = True
    db_handler.update(user_dic)
