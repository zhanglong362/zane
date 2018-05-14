# -*- encoding: utf-8 -*-

from db import db_handler

def get_good_info(good_file='goods'):
    good_info = db_handler.read(good_file)
    good_info.pop('name')
    return good_info

def get_shopping_cart_info(name):
    info = db_handler.read(name)
    return info['shopping_cart']

def join_shopping_cart(name, code, good, price, count):
    info = db_handler.read(name)
    if good in info['shopping_cart']:
        info['shopping_cart'][code]['count'] += count
    else:
        info['shopping_cart'][code] = {
            'good': good,
            'price': price,
            'count': count
        }
    if db_handler.write(info):
        return True, '商品 %s x %s 加入购物车成功！' % (good, count)
    else:
        return True, '商品 %s x %s 加入购物车失败！' % (good, count)

def pay(name):
    info = db_handler.read(name)
    cost = 0
    for good in info['shopping_cart'].values():
        cost += (good['price'] * good['count'])
    if (info['balance'] + info['credit_balance']) < cost:
        return False, '用户%s账户余额不足，结账失败！' % name
    if info['balance'] >= cost:
        info['balance'] -= cost
    if info['balance'] < cost and (info['balance'] + info['credit_balance']) >= cost:
        info['credit_balance'] -= (cost - info['balance'])
        info['bill'] += (cost - info['balance'])
        if info['balance'] != 0:
            info['balance'] = 0
    if db_handler.write(info):
        return True, '用户%s结账%s成功！' % (name, cost)
    else:
        return True, '用户%s结账%s失败！' % (name, cost)

def flush_shopping_cart(name):
    info = db_handler.read(name)
    info['shopping_cart'] = {}
    if db_handler.write(info):
        return True, '用户%s购物车已清空！' % name
    else:
        return False, '用户%s购物车清空失败！' % name

def new_arrival(code, good, price, good_file='goods'):
    good_info = db_handler.read(good_file)
    good_info[code] = {
        'name': good,
        'price': price
    }
    if db_handler.write(good_info):
        return True, '新商品 %s 上架成功！' % good
    else:
        return False, '新商品 %s 上架失败！' % good

def modify_shopping_cart(name, code, count):
    info = db_handler.read(name)
    good = info['shopping_cart'][code]['good']
    if info['shopping_cart'][code]['count'] < count:
        return False, '删除商品%s数量过多，删除失败！' % good
    if info['shopping_cart'][code]['count'] == count:
        info['shopping_cart'].pop(code)
    if info['shopping_cart'][code]['count'] > count:
        info['shopping_cart'][code]['count'] -= count
    if db_handler.write(info):
        return True, '删除商品 %s x %s 成功！' % (good, count)
    else:
        return False, '删除商品 %s x %s 失败！' % (good, count)


