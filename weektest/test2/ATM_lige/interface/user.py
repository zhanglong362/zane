
import os
from db import db_handler
from conf import setting
from lib import common

logger_user=common.get_logger('User')


def get_userinfo_interface(name):

   user_dic= db_handler.select(name)
   return user_dic



def register(name,password,account=15000):
    '''
    注册接口
    :param name:
    :param password:
    :param account:
    :return:
    '''
    #拼出用户字典
    user_dic = {'name': name, 'password': password, 'locked': False, 'account': account, 'creidt': account,'bankflow':[]}
    #将字典写入文件
    db_handler.update(user_dic)
    logger_user.info('%s 注册成功' %name)


def lock_user_interface(name):
    '''
    锁定用户接口
    :param name:
    :return:
    '''
    user_dic=get_userinfo_interface(name)
    user_dic['locked']=True
    db_handler.update(user_dic)