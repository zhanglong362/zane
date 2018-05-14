# -*- encoding: utf-8 -*-

from db import db_handler

def new_arrival(code, name, price, good_file='goods'):
    good_info = db_handler.read(good_file)
    if not good_info:
        good_info = {'name': good_file}
    good_info[code] = {
        'name': name,
        'price': price
    }
    if db_handler.write(good_info):
        return True, '商品%s新品上架成功！' % name
    else:
        return False, '商品%s新品上架失败！' % name

def get_shooping_cart_info(name):
    info = db_handler.read(name)
    if info:
        return info['shopping_cart']

def get_good_info(good_file='goods'):
    good_info = db_handler.read(good_file)
    good_info.pop('name')
    return good_info

def join_shopping_cart(name, good, code, price, count):
    info = db_handler.read(name)
    if good in info['shopping_cart']:
        info['shopping_cart'][good]['count'] += count
    else:
        info['shopping_cart'][good] = {
            'code': code,
            'price': price,
            'count': count
        }
    if db_handler.write(info):
        return True, '商品 %s x %s 加入购物车成功！' % (good, count)
    else:
        return False, '商品 %s x %s 加入购物车失败！' % (good, count)

def pay(name):
    info = db_handler.read(name)
    shopping_cart = info['shopping_cart']
    if not shopping_cart:
        return False, '用户%s购物车列表为空' % name
    cost = 0
    for k, v in shopping_cart.items():
        cost += (v['price'] * v['count'])
    if (info['balance'] + info['credit_balance']) < cost:
        return False, '用户%s账户余额不足，结账失败！' % name
    if info['balance'] >= cost:
        info['balance'] -= cost
    if (info['balance'] + info['credit_balance']) >= cost:
        if info['balance'] != 0:
            info['balance'] = 0
        info['credit_balance'] -= (cost - info['balance'])
        info['bill'] += (cost - info['balance'])
    if db_handler.write(info):
        return True, '用户%s付款%s元，结账成功！'
    else:
        return False, '系统异常，结账失败！' % name
