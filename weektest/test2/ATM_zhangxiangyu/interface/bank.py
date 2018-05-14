#coding:utf-8

from db import db_handler
from lib import common

bank_log = common.get_logger('Bank')

#查看余额
def get_account(name):
    user_dic = db_handler.select(name)
    return user_dic['account']


#transfer
def transfer_interface(to_user,from_user,account):
    to_user_dic = db_handler.select(to_user)
    from_user_dic = db_handler.select(from_user)

    to_user_dic['account'] +=account
    from_user_dic['account'] -=account

    from_user_dic['flow_log'].append(r'%s收到%s转账%s元' %(to_user,from_user,account))
    to_user_dic['flow_log'].append(r'%s向%s转账%s元' %(from_user,to_user,account))

    bank_log.info(r'%s收到%s转账%s元' % (to_user, from_user, account))
    bank_log.info(r'%s向%s转账%s元' % (from_user, to_user, account))

    db_handler.update(to_user_dic)
    db_handler.update(from_user_dic)





def repay_interface(name,account):
    user_dic = db_handler.select(name)
    user_dic['account'] +=account
    user_dic['flow_log'].append(r'%s还款%s成功！' %(name,account))
    bank_log.info( r'%s还款%s成功！' %(name,account))
    db_handler.update(user_dic)


def withdraw(name,account):
    user_dic = db_handler.select(name)
    user_dic['account'] -= account*1.05
    user_dic['flow_log'].append(r'%s提现%s成功！' % (name, account))
    bank_log.info( r'%s提现%s成功！' % (name, account))
    db_handler.update(user_dic)



