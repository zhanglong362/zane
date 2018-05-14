# -*- encoding: utf-8 -*-

from lib import common
from db import modules

logger = common.get_logger('user')

def login(name, password):
    user = modules.User.get_obj_by_name(name)
    if not user:
        return False, '用户%s不存在！' % name
    if password == user.password:
        logger.info('用户%s登陆成功！' % name)
        return True, '用户%s登陆成功！' % name
    else:
        logger.info('用户%s密码错误！' % name)
        return False, '用户%s密码错误！' % name

def register(name, password, credit_limit=15000):
    user = modules.User.get_obj_by_name(name)
    if user:
        return False, '用户%s不能重复注册！' % name
    user = modules.User.register(name, password, credit_limit)
    if user:
        logger.info('用户%s注册成功！' % name)
        return True, '用户%s注册成功！' % name
    else:
        logger.info('用户%s注册失败！' % name)
        return False, '用户%s注册失败！' % name

def get_balance_info(name):
    user = modules.User.get_obj_by_name(name)
    logger.info('用户%s获取账户余额信息！' % name)
    return user.check_balance()

def get_bill_info(name):
    user = modules.User.get_obj_by_name(name)
    logger.info('用户%s获取账户账单信息！' % name)
    return user.check_bill()

def get_flow_info(name, bill_date):
    user = modules.User.get_obj_by_name(name)
    logger.info('用户%s获取账户流水信息！' % name)
    return user.check_flow(bill_date)




