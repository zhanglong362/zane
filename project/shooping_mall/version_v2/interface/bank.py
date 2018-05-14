# -*- encoding: utf-8 -*-

import datetime
from lib import common
from db import db_handler


logger = common.get_logger('bank')

def transfer_amount_api(transfer, payee, amount):
    transfer_info = db_handler.file_handler_read(transfer)
    if transfer_info['balance'] < amount:
        logger.warning('用户%s账户余额不足，转账失败！' % transfer_info['name'])
        return
    payee_info = db_handler.file_handler_read(payee)
    dt = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    transfer_info['balance'] -= amount
    transfer_info['detailed_list'].append((dt, '用户%s转账%s给%s' % (transfer, amount, payee)))
    payee_info['balance'] += amount
    payee_info['detailed_list'].append((dt, '用户%s收款%s从%s' % (payee, amount, transfer)))
    db_handler.file_handler_write(transfer_info)
    db_handler.file_handler_write(payee_info)
    return True

def repayment_bill_api(name, amount):
    user_info = db_handler.file_handler_read(name)
    user_info['balance'] -= amount
    user_info['credit_balance'] += amount
    user_info['bill'] -= amount
    dt = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    user_info['detailed_list'].append((dt, '用户%s还款%s元' % (name, amount)))
    logger.info('用户%s还款%s元' % (name, amount))
    db_handler.file_handler_write(user_info)
    return True

def widthraw_cash_api(name, amount):
    user_info = db_handler.file_handler_read(name)
    user_info['credit_balance'] -= (amount + amount*0.05)
    user_info['bill'] += (amount + amount*0.05)
    user_info['balance'] += amount
    dt = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    user_info['detailed_list'].append((dt, '用户%s取现%s元，手续费%s元' % (name, amount, amount*0.05)))
    logger.info('用户%s取现%s元，手续费%s元' % (name, amount, amount*0.05))
    db_handler.file_handler_write(user_info)
    return True


