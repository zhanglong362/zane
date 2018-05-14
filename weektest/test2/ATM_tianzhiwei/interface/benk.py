from db import db_hand
from lib import common
logger_benk=common.logger('Benk')
def get_account(name):
    return db_hand.select(name)
def transfer_money(out_name,in_name,account):
    dic=db_hand.select(out_name)
    dic['account']-=account
    dict=db_hand.select(in_name)
    dict['account']+=account
    dic['write_log'].append('%s给%s转账，%s 人民币'%(out_name,in_name,account))
    dict['write_log'].append('%s收到%s的转账，%s 人民币' % (in_name, out_name,account))
    db_hand.add(out_name,dic)
    db_hand.add(in_name,dict)
    logger_benk.info('%s给%s转账，%s 人民币'%(out_name,in_name,account))
def out_money(name,account):
    dic=db_hand.select(name)
    dic['account']-=account*1.05
    dic['write_log'].append('%s提现了%s 人民币'%(name,account))
    db_hand.add(name,dic)
    logger_benk.info('%s提现了%s 人民币'%(name,account))
def in_money(name,account):
    dic=db_hand.select(name)
    dic['account'] += account
    dic['write_log'].append('%s还款%s 人民币' % (name, account))
    db_hand.add(name, dic)
    logger_benk.info('%s还款%s 人民币' % (name, account))



