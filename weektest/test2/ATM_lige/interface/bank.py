
from db import db_handler

from lib import common

logger_bank=common.get_logger('Bank')
def get_account(name):
    '''
    查询name的账户余额接口
    :param name:
    :return:
    '''
    user_dic=db_handler.select(name)
    return user_dic['account']

def withdraw_interface(name,account):
    '''
    取款接口
    :param name:
    :param account:
    :return:
    '''
    user_dic = db_handler.select(name)
    user_dic['account']-=account*1.05
    #保存流水
    user_dic['bankflow'].append('%s transfer %s yuan'%(name,account))
    db_handler.update(user_dic)
    #记录日志
    logger_bank.info('%s 取款 %s' %(name,account))



def repay_interface(name,account):
    '''
    还款接口
    :param name:
    :param account:
    :return:
    '''
    user_dic=db_handler.select(name)
    user_dic['account']+=account
    #记录流水
    user_dic['bankflow'].append('%s repay %s yuan' % (name, account))
    db_handler.update(user_dic)
    #记录日志
    logger_bank.info('%s repay %s'%(name,account))


def transfer_interface(from_user,to_user,account):
    '''
    转账接口
    :param from_user:
    :param to_user:
    :param account:
    :return:
    '''
    from_user_dic=db_handler.select(from_user)
    to_user_dic=db_handler.select(to_user)

    from_user_dic['account']-=account
    to_user_dic['account']+=account
    #记录流水
    from_user_dic['bankflow'].append('%s 转账 %s 元 给 %s' % (from_user,account,to_user))
    to_user_dic['bankflow'].append('%s 收到 %s转账 %s 元' % (to_user,from_user,account,))
    db_handler.update(from_user_dic)
    db_handler.update(to_user_dic)
    #写日志
    logger_bank.info('%s transfer %s yuan to %s'%(from_user,account,to_user))

def check_bankflow_interface(name):
    '''
    查看银行流水接口
    :param name:
    :return:
    '''
    user_dic=db_handler.select(name)
    return user_dic['bankflow']