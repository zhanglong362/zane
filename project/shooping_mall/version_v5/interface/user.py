# -*- encoding: utf-8 -*-

from db import db_handler


def login(name, password):
    info = db_handler.read(name)
    if not info:
        return False, '用户%s不存在！' % name
    if password == info['password']:
        return True, '用户%s登陆成功！' % name
    else:
        return False, '用户%s登陆失败，密码错误！' % name

def register(name, password, credit_limit=15000):
    info = {
        'name': name,
        'password': password,
        'balance': 0,
        'credit_balance': credit_limit,
        'credit_limit': credit_limit,
        'bill': 0,
        'shopping_cart': {},
        'flow': [],
    }
    if db_handler.write(info):
        return True, '用户%s注册成功！' % name
    else:
        return False, '用户%s注册失败！' % name

def get_balance_info(name):
    info = db_handler.read(name)
    if info:
        return info['balance'], info['credit_balance'], info['credit_limit']

def get_bill_info(name):
    info = db_handler.read(name)
    if info:
        return info['bill']

def get_flow_info(name):
    info = db_handler.read(name)
    if info:
        return info['flow']


