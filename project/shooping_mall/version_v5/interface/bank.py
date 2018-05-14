# -*- encoding: utf-8 -*-

import datetime
from db import db_handler

def get_datetime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def recharge(name, amount):
    dt = get_datetime()
    info = db_handler.read(name)
    info['balance'] += amount
    info['flow'].append((dt, '用户%s充值%s元' % (name, amount)))
    if db_handler.write(info):
        return True, '用户%s充值%s成功！' % (name, amount)
    else:
        return False, '用户%s充值%s失败！' % (name, amount)

def transfer(name, payee, amount):
    dt = get_datetime()
    info_tran = db_handler.read(name)
    if info_tran['balance'] < amount:
        return False, '用户%s账户余额不足，转账失败！' % name
    info_payee = db_handler.read(payee)
    info_tran['balance'] -= amount
    info_tran['flow'].append((dt, '用户%s转账%s元给用户%s' % (name, amount, payee)))
    info_payee['balance'] += amount
    info_payee['flow'].append((dt, '用户%s收款%s元从用户%s' % (payee, amount, name)))
    if db_handler.write(info_tran) and db_handler.write(info_payee):
        return True, '用户%s转账%s给用户%s成功！' % (name, amount, payee)
    else:
        return False, '用户%s转账%s给用户%s失败！' % (name, amount, payee)

def withdraw(name, amount, charge=0.05):
    dt = get_datetime()
    info = db_handler.read(name)
    if info['credit_balance'] < (amount + amount * charge):
        return False, '用户%s信用余额不足，取现失败！' % name
    info['credit_balance'] -= (amount + amount * charge)
    info['bill'] += (amount + amount * charge)
    info['balance'] += amount
    info['flow'].append((dt, '用户%s取现%s元' % (name, amount)))
    if db_handler.write(info):
        return True, '用户%s取现%s元成功！' % (name, amount)
    else:
        return False, '用户%s取现%s元失败！' % (name, amount)

def repay(name, amount):
    dt = get_datetime()
    info = db_handler.read(name)
    info['balance'] -= amount
    if info['bill'] <= amount:
        info['bill'] = 0
    else:
        info['bill'] -= amount
    info['credit_balance'] += amount
    info['flow'].append((dt, '用户%s还款%s元' % (name, amount)))
    if db_handler.write(info):
        return True, '用户%s还款%s元成功！' % (name, amount)
    else:
        return False, '用户%s还款%s元失败！' % (name, amount)

