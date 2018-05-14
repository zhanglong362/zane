# -*- encoding: utf-8 -*-

from db import db_handler


def get_user_info_api(name):
    return db_handler.read(name)

def register_user_api(name, pwd, credit=15000):
    user_info = {
        'name': name,
        'pwd': pwd,
        'lock': False,
        'balance': 0,
        'credit': credit
    }
    db_handler.write(user_info)

def modify_user_api(user_info):
    db_handler.write(user_info)


