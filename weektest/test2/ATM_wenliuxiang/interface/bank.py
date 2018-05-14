

from  db import db_handler
from lib  import common
logger_bank=common.get_logger('Bank')
def  get_account(name):
    user_dic = db_handler.select(name)
    return   user_dic['account']


def transfer_interface(from_user,to_user,account):
    from_user_dic = db_handler.select(from_user)
    to_user_dic = db_handler.select(to_user)

    from_user_dic['account']-=account
    to_user_dic['account']+=account

    from_user_dic['bankflow'].append('%s转账给谁%s￥给%s'  %(from_user,account,to_user))
    to_user_dic['bankflow'].append('%s收到%s转账  %s￥'  %(to_user,account,from_user))
    db_handler.update(from_user_dic)
    db_handler.update(to_user_dic)

    logger_bank.info('%s transfer %s yuan to %s' % (from_user, account, to_user))



def withdraw_interface(name,account):

    user_dic = db_handler.select(name)
    user_dic['account']-=account*1.05
    user_dic['bankflow'].append('%s transfer %s yuan'%(name,account))
    logger_bank.info('%s 取款 %s' %(name,account))



def repay_interface(name,account):

    user_dic=db_handler.select(name)
    user_dic['account']+=account

    user_dic['bankflow'].append('%s repay %s yuan' % (name, account))
    db_handler.update(user_dic)

    logger_bank.info('%s repay %s'%(name,account))


def check_bankflow_interfac(name):
    user_dic=db_handler.select(name)
    return user_dic

