# -*- encoding: utf-8 -*-

import datetime
from lib import common
from db import db_handler

logger = common.get_logger('user')

def get_user_info_api(name):
    data = db_handler.file_handler_read(name)
    if data:
        logger.info('获取用户%s信息成功！' % name)
    else:
        logger.info('用户%s信息不存在！' % name)
    return data

def register_user_api(name, password, credit_limit=15000):
    user_info = {
        'name': name,
        'password': password,
        'role': 'user',
        'balance': 0,
        'credit_limit': credit_limit,
        'credit_balance': credit_limit,
        'detailed_list': [],
        'shopping_cart': {},
        'bill': 0
    }
    if db_handler.file_handler_write(user_info):
        logger.info('用户注册成功！')
        return True
    else:
        logger.warning('用户注册失败！')
        return

def modify_user_info_api(user_info):
    if db_handler.file_handler_write(user_info):
        logger.info('修改用户%s信息成功！' % user_info['name'])
        return True
    else:
        logger.warning('修改用户%s信息失败！' % user_info['name'])
        return

