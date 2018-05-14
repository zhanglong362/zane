# -*- encoding: utf-8 -*-

import datetime
from db import modules
from lib import common

logger = common.get_logger('bank')

def recharge(name, amount):
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user = modules.User.get_obj_by_name(name)
    user.balance += amount
    user.flow.append((dt, '用户%s充值%s元' % (name, amount)))
    if user.save():
        logger.info('用户%s充值%s元成功！' % (name, amount))
        return True, '用户%s充值%s元成功！' % (name, amount)
    else:
        logger.info('用户%s充值%s元失败！' % (name, amount))
        return False, '用户%s充值%s元失败！' % (name, amount)

def transfer(name, payee, amount):
    obj_tran = modules.User.get_obj_by_name(name)
    if obj_tran.balance < amount:
        logger.info('用户%s账户金额不足，转账失败！' % name)
        return False, '用户%s账户金额不足，转账失败！' % name
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    obj_payee = modules.User.get_obj_by_name(payee)
    obj_tran.balance -= amount
    obj_tran.flow.append((dt, '用户%s给%s转账%s元' % (name, payee, amount)))
    if not obj_tran.save():
        return False, '用户%s给%s转账%s元失败！' % (name, payee, amount)
    logger.info('用户%s给%s转账%s元' % (name, payee, amount))
    obj_payee.balance += amount
    obj_payee.flow.append((dt, '用户%s收到%s转账%s元' % (payee, name, amount)))
    if not obj_payee.save():
        return False, '用户%s收取%s转账%s元失败！' % (payee, name, amount)
    logger.info('用户%s收到%s转账%s元成功！' % (payee, name, amount))
    return True, '用户%s给%s转账%s成功！' % (name, payee, amount)

def withdraw(name, amount):
    user = modules.User.get_obj_by_name(name)
    if user.credit_balance < (amount + amount * 0.05):
        logger.info('用户%s信用余额不足，取现%s失败！' % (name, amount))
        return False, '用户%s信用余额不足，取现%s失败！' % (name, amount)
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user.credit_balance -= (amount + amount * 0.05)
    user.balance += amount
    user.bill += (amount + amount * 0.05)
    user.flow.append((dt, '用户%s取现%s元' % (name, amount)))
    if user.save():
        logger.info('用户%s取现%s成功！' % (name, amount))
        return True, '用户%s取现%s成功！' % (name, amount)
    else:
        logger.info('用户%s取现%s失败！' % (name, amount))
        return True, '用户%s取现%s失败！' % (name, amount)

def repayment(name, amount):
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user = modules.User.get_obj_by_name(name)
    if user.bill > amount:
        user.balance -= amount
        user.bill -= amount
        user.credit_balance += amount
        user.flow.append((dt, '用户%s还款%s元' % (name, amount)))
        if not user.save():
            return False, '用户%s还款%s失败！' % (name, amount)
        logger.info('用户%s还款%s成功，还需%s还清本期账单！' % (name, amount, user.bill))
        return True, '用户%s还款%s成功，还需%s还清本期账单！' % (name, amount, user.bill)
    if user.bill <= amount:
        user.balance -= amount
        user.bill = 0
        user.credit_balance += amount
        user.flow.append((dt, '用户%s还款%s元' % (name, amount)))
        if not user.save():
            return False, '用户%s还款%s失败！' % (name, amount)
        logger.info('用户%s还款%s成功，本期账单已还清！' % (name, amount))
        return True, '用户%s还款%s成功，本期账单已还清！' % (name, amount)

