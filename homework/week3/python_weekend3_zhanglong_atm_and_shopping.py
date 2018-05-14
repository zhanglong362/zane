#!/usr/bin/env python3
#-*- encoding: utf-8 -*-

import os
import sys
import json
import logging
import datetime

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s  %(filename)s[line:%(lineno)d]:%(levelname)s:%(message)s',
                    datefmt='%Y-%b-%d,%H:%M:%S',
                    filename='check_atm_and_shopping.log',
                    filemode='w')

def auth(func):
    def wrapper(*args, **kwargs):
        if name in cookies:
            return func(*args, **kwargs)
        else:
            print('用户%s没有登录，请先登录！' % name)
            logging.warning('用户%s没有登录，请先登录！' % name)
            sys.exit()
    return wrapper

def order(func):
    def wrapper(*args, **kwargs):
        global cookies, shopping_cart
        res = func(*args, **kwargs)
        if res == 'quit':
            if shopping_cart:
                with open(r'shopping_cart.json.swap', 'w') as f:
                    json.dump(shopping_cart, f)
            os._exit(0)
        if res == 'order':
            print('请确认购物车并下单！')
            sys.exit()
        return res
    return wrapper

def check_file(path):
    if os.path.exists(path):
        return True

def get_user_info(name):
    with open(r'%s/user.json' % name) as f:
        user_info = json.load(f)
    return user_info

@auth
def update_user_info(name, user_info):
    with open(r'%s/user.json' % name, 'w') as f:
        json.dump(user_info, f)

@auth
def get_goods_info():
    with open(r'goods.json') as f:
        goods = json.load(f)
    return goods

def register(credit_limit=15000):
    print('>> \033[33m请输入注册信息！\033[0m')
    name = get_user_name('注册')
    if check_file('%s/user.json' % name):
        print('用户%s已经注册！' % name)
        return
    else:
        os.mkdir(name)
    password = get_password(True)
    with open(r'%s/user.json' % name, 'w') as f:
        user_info = {
            name: {
                'password': password,
                'balance': 0,
                'credit_limit': credit_limit,
                'credit_balance': credit_limit,
                'bill': 0
            }
        }
        json.dump(user_info, f)
    print('用户%s注册成功！' % name)
    return

@order
def get_user_name(word):
    while True:
        name = input('%s用户名 >>: ' % word).strip()
        if name == 'quit':
            return name
        if not name.isalpha():
            print('用户名必须是字符串！')
            continue
        return name

@order
def get_password(register=None):
    while True:
        password = input('密码 >>: ')
        if password == 'quit':
            return password
        if register:
            p = input('再次输入密码 >>: ')
            if password == 'quit':
                return password
            if p != password:
                print('两次输入的密码不一致！')
                continue
        return password

@order
def get_balance(word):
    while True:
        balance = input('请输入%s金额 >>: ' % word).strip()
        if balance == 'quit':
            return balance
        if not balance.isdigit():
            print('必须是金额的整数！')
            continue
        balance = int(balance)
        return balance

@order
def get_action():
    while True:
        code = input('请输入操作编码 >>: ').strip()
        return code

@order
def get_shopping_code(word):
    while True:
        code = input('请输入%s商品编码 >>: ' % word).strip()
        return code

@order
def get_shopping_count(word):
    while True:
        count = input('请输入%s数量 >>: ' % word).strip()
        if count == 'quit':
            return count
        if count.isdigit():
            count = int(count)
            return count
        print('请输入数量的整数！')

def login():
    global cookies
    while True:
        name = get_user_name('登陆')
        if name in cookies:
            print('用户%s已经是登陆状态！' % name)
            return name
        if not check_file('%s/user.json' % name):
            print('用户%s不存在！' % name)
            continue
        password = get_password()
        user = get_user_info(name)
        if password != user[name]['password']:
            print('密码错误！')
            continue
        if name not in cookies:
            cookies[name] = {}
        cookies[name]['balance'] = user[name]['balance']
        cookies[name]['credit_balance'] = user[name]['credit_balance']
        cookies[name]['credit_limit'] = user[name]['credit_limit']
        cookies[name]['bill'] = user[name]['bill']
        print('用户%s登陆成功！' % name)
        return name

@auth
def shopping():
    global cookies, shopping_cart
    balance = cookies[name]['balance']
    credit_balance = cookies[name]['credit_balance']
    credit_limit = cookies[name]['credit_limit']
    if name in shopping_cart:
        cost = 0
        for v in shopping_cart[name].values():
            price, count = v['price'], v['count']
            cost += price * count
        if balance >= cost:
            balance -= cost
        elif balance < cost and credit_balance >= cost:
            if credit_limit == 0:
                print('信用卡已冻结，无法使用信用卡购物！')
                print('账户余额不足，请进入购物车修改购买商品，或进行账户充值后继续购物！')
                return
            credit_balance -= cost
        elif balance < cost and (balance + credit_balance) >= cost:
            balance = 0
            credit_balance -= (cost - balance)
        else:
            diff = cost - (balance + credit_balance)
            print('账户余额: %s 信用卡余额: %s 购买购物车中的物品还需: %s' % (balance, credit_balance, diff))
            print('请进入购物车修改购买商品，或进行账户充值后继续购物！')
            return
    else:
        shopping_cart[name] = {}
    while True:
        print('=' * 30)
        print('商品编号    商品名称    商品价格')
        for k, v in goods.items():
            print('%-10s %-10s %-10s' % (k, v['name'], v['price']))
        print('=' * 30)
        print('[下单:order]')
        code = get_shopping_code('购买')
        if code not in goods:
            print('商品编号非法！')
            continue
        good = goods[code]['name']
        price = goods[code]['price']
        count = get_shopping_count('购买')
        cost = price * count
        if balance >= cost or credit_balance >= cost:
            if good not in shopping_cart[name]:
                total_count = count
            else:
                total_count += count
            shopping_cart[name][good] = {
                'code': code,
                'price': price,
                'count': total_count
            }
        if balance >= cost:
            balance -= cost
            print('购物车: %s \n账户余额: %s' % (shopping_cart[name], balance))
        elif balance < cost and credit_balance >= cost:
            if credit_limit == 0:
                print('信用卡已冻结，无法使用信用卡购物！')
                print('账户余额不足，请进入购物车修改购买商品，或进行账户充值后继续购物！')
                return
            credit_balance -= cost
            print('购物车: %s \n信用卡余额: %s' % (shopping_cart[name], credit_balance))
        else:
            diff = cost - (balance + credit_balance)
            print('账户余额: %s 信用卡余额: %s 购买商品 %s x %s 还需 %s' % (balance, credit_balance, good, count, diff))
            print('请账户充值或信用卡还款后继续购物！')
        cookies[name]['balance'] = balance
        cookies[name]['credit_balance'] = credit_balance

@auth
def shopping_cart_order():
    global cookies, shopping_cart
    while True:
        if name not in shopping_cart:
            shopping_cart[name] = {}
        print('1  查看购物车\n2  编辑购物车\n3  确认下单')
        print('退回上一层：back')
        action = get_action()
        if action == '1':
            cost = 0
            print('=' * 50)
            print('商品名称    商品编号    商品价格    商品数量\n')
            for k, v in shopping_cart[name].items():
                good, code, price, count = k, v['code'], v['price'], v['count']
                print('%-10s %-10s %-10s %-10s' % (good, code, price, count))
                cost += (price * count)
            print('\n商品总价: %s' % cost)
            print('账户余额: %s' % cookies[name]['balance'])
            print('信用卡余额: %s' % cookies[name]['credit_balance'])
            print('=' * 50)
        elif action == '2':
            while True:
                print('=' * 30)
                print('商品编号    商品名称    商品价格')
                for k, v in goods.items():
                    print('%-10s %-10s %-10s' % (k, v['name'], v['price']))
                print('=' * 30)
                code = get_shopping_code('删除')
                good = goods[code]['name']
                price = goods[code]['price']
                if good not in shopping_cart[name]:
                    print('购物车内无此商品: %s' % good)
                    continue
                count = get_shopping_count('删除')
                if count > shopping_cart[name][good]['count']:
                    print('请输入不大于购物车内商品数量的值！')
                    continue
                elif count == shopping_cart[name][good]['count']:
                    del shopping_cart[name][good]
                    cookies[name]['credit_balance'] += (price * count)
                    if cookies[name]['credit_balance'] > 15000:
                        cookies[name]['balance'] += (cookies[name]['credit_balance'] - 15000)
                        cookies[name]['credit_balance'] = 15000
                else:
                    shopping_cart[name][good]['count'] -= count
                    cookies[name]['credit_balance'] += (price * count)
                    if cookies[name]['credit_balance'] > 15000:
                        cookies[name]['balance'] += (cookies[name]['credit_balance'] - 15000)
                        cookies[name]['credit_balance'] = 15000
                print('购物车编辑完成！')
                break
        elif action == '3':
            cost = 0
            print('=' * 50)
            print('商品名称    商品编号    商品价格    商品数量\n')
            for k, v in shopping_cart[name].items():
                good, code, price, count = k, v['code'], v['price'], v['count']
                print('%-10s %-10s %-10s %-10s' % (good, code, price, count))
                cost += (price * count)
            print('\n商品总价: %s' % cost)
            print('账户余额: %s' % cookies[name]['balance'])
            print('信用卡余额: %s' % cookies[name]['credit_balance'])
            print('=' * 50)
            d = datetime.datetime.now().strftime('%Y%m')
            dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            user_order = {}
            with open(r'%s/%s_order.json' % (name, d), 'a') as f:
                user_order[name] = shopping_cart[name]
                user_order[name]['datetime'] = dt
                user_order[name]['cost'] = cost
                f.write(str(user_order)+'\n')
            print('下单成功，请尽快支付！')
            break
        elif action == 'back':
            return
        else:
            print('操作编码非法！')

@auth
def pay():
    with open(r'%s/user.json' % name) as f1, \
            open(r'%s/user.json.swap' % name, 'w') as f2:
        user_info = json.load(f1)
        user_info[name]['balance'] = cookies[name]['balance']
        user_info[name]['credit_balance'] = cookies[name]['credit_balance']
        json.dump(user_info, f2)
    os.remove('%s/user.json' % name)
    os.rename('%s/user.json.swap' % name, '%s/user.json' % name)
    print('支付成功，请耐心等待发货！')
    shopping_cart[name] = {}

@auth
def get_orders(d=datetime.datetime.now().strftime('%Y%m')):
    print('以下是%s消费订单信息: ' % d)
    if check_file('%s/%s_order.json' % (name, d)):
        with open(r'%s/%s_order.json' % (name, d)) as f:
            for line in f:
                print(line.strip())
    else:
        print('用户%s本月没有订单信息！\n' % name)

@auth
def withdraw_cash(amount):
    if cookies[name]['credit_limit'] == 0:
        print('信用卡已冻结，无法使用信用卡购物！')
        return
    if cookies[name]['credit_balance'] >= (amount + (amount * 0.05)):
        with open(r'%s/user.json' % name) as f1, \
                open(r'%s/user.json.swap' % name, 'w') as f2:
            user_info = json.load(f1)
            cookies[name]['credit_balance'] -= (amount + (amount * 0.05))
            cookies[name]['balance'] += amount
            user_info['balance'] =  cookies[name]['balance']
            user_info['credit_balance'] = cookies[name]['credit_balance']
            json.dump(user_info, f2)
        os.remove('%s/user.json' % name)
        os.rename('%s/user.json.swap' % name, '%s/user.json' % name)
        print('提现%s成功，手续费：%s！' % (amount, (amount * 0.05)))
        logging.info('提现%s成功，手续费：%s！' % (amount, (amount * 0.05)))
    else:
        print('信用卡没有足够的金额完成提现！')
        logging.warning('信用卡没有足够的金额完成提现！')

@auth
def transfer_amount(name, amount, mode):
    with open(r'%s/user.json' % name) as f1, \
            open(r'%s/user.json.swap' % name, 'w') as f2:
        user_info = json.load(f1)
        if mode == 'reduce':
            if user_info[name]['balance'] >= amount:
                user_info[name]['balance'] -= amount
            else:
                print('用户%s账户金额不足！' % name)
                logging.warning('用户%s账户金额不足！' % name)
                return
        elif mode == 'increase':
            user_info[name]['balance'] += amount
        json.dump(user_info, f2)
        os.remove('%s/user.json' % name)
        os.rename('%s/user.json.swap' % name, '%s/user.json' % name)
        return True

@auth
def transfer(src_name, dst_name, amount):
    if not check_file('%s/user.json' % src_name):
        print('账户%s不存在！' % src_name)
        logging.error('账户%s不存在！' % src_name)
        return
    if not check_file('%s/user.json' % dst_name):
        print('账户%s不存在！' % dst_name)
        logging.error('账户%s不存在！' % dst_name)
        return
    if transfer_amount(src_name, amount, 'reduce'):
        transfer_amount(dst_name, amount, 'increase')
        print('转账完成！')
        logging.info('转账完成！')

@auth
def repayment():
    with open(r'%s/user.json' % name) as f1, \
            open(r'%s/user.json.swap' % name, 'w') as f2:
        user_info = json.load(f1)
        money = get_balance('还款')
        if money < user_info['bill']:
            user_info['credit_balance'] += money
            diff = user_info['bill'] - money
            user_info['bill'] = diff
            print('用户%s还款成功，还需%s金额还清本期账单！' % (name, diff))
            logging.info('用户%s还款成功，还需%s金额还清本期账单！' % (name, diff))
        elif money == user_info['bill']:
            user_info['credit_balance'] += money
            user_info['bill'] = 0
            print('用户%s还款成功，本期账单已还清！' % name)
            logging.info('用户%s还款成功，本期账单已还清！' % name)
        elif money > user_info['bill']:
            user_info['credit_balance'] == user_info['credit_limit']
            user_info['balance'] += (money - user_info['bill'])
            user_info['bill'] = 0
            print('用户%s还款成功，本期账单已还清！多余金额已经充值到账户余额！' % name)
            logging.info('用户%s还款成功，本期账单已还清！多余金额已经充值到账户余额！' % name)

@auth
def credit_manege(action, amount=None):
    with open(r'%s/user.json' % name) as f1, \
            open(r'%s/user.json.swap' % name, 'w') as f2:
        user_info = json.load(f1)
        if action == 'up':
            user_info[name]['credit_limit'] += amount
            user_info[name]['credit_balance'] += amount
            print('用户%s信用卡提额%s完成！' % (name, amount))
            logging.info('用户%s信用卡提额%s完成！' % (name, amount))
        elif action == 'down':
            user_info[name]['credit_limit'] -= amount
            user_info[name]['credit_balance'] -= amount
            print('用户%s信用卡降额%s完成！' % (name, amount))
            logging.info('用户%s信用卡降额%s完成！' % (name, amount))
        elif action == 'freeze':
            user_info[name]['credit_limit'] = 0
            print('用户%s信用卡冻结完成！' % name)
            logging.info('用户%s信用卡冻结完成！' % name)
        elif action == 'back':
            return
        else:
            print('操作非法！')
        json.dump(user_info, f2)
    os.remove('%s/user.json' % name)
    os.rename('%s/user.json.swap' % name, '%s/user.json' % name)

@auth
def credit_bill():
    today = datetime.date.today()
    month = today.month
    day = today.day
    with open(r'%s/user.json' % name) as f1, \
            open(r'%s/user.json.swap' % name, 'w') as f2:
        user_info = json.load(f1)
        if day == '22':
            user_info['bill'] = user_info['bill'] + (user_info['credit_limit'] - user_info['credit_balance'])
            logging.info('%s-%s账单已生成！' % (month, day))
        if today >= '%s-10' % month:
            if user_info['bill'] != 0:
                user_info['bill'] = user_info['bill'] + (user_info['bill'] * 0.0005)
    json.dump(user_info, f2)
    os.remove('%s/user.json' % name)
    os.rename('%s/user.json.swap' % name, '%s/user.json' % name)

@auth
def credit():
    while True:
        print('1  管理信用卡\n2  账户转账\n3  查看订单')
        print('退回上一层: back')
        action = get_action()
        if action == '1':
            while True:
                print('1  信用卡提额\n2  信用卡降额\n3  信用卡冻结\n4  信用卡余额\n5  信用卡提现\n6  信用卡账单\n7  信用卡还款')
                print('退回上一层: back')
                operation = get_action()
                if operation == '1':
                    amount = get_balance('提额')
                    credit_manege('up', amount)
                elif operation == '2':
                    amount = get_balance('降额')
                    credit_manege('down', amount)
                elif operation == '3':
                    credit_manege('freeze')
                elif operation == '4':
                    if cookies[name]['credit_limit'] == 0:
                        credit_balance = 0
                        print('信用卡已冻结，无法使用信用卡！')
                    else:
                        credit_balance = cookies[name]['credit_balance']
                    print('信用卡可用余额: %s' % credit_balance)
                elif operation == '5':
                    amount = get_balance('提现')
                    withdraw_cash(amount)
                elif operation == '6':
                    bill = cookies[name]['bill']
                    print('本期信用卡账单: %s' % bill)
                elif operation == '7':
                    repayment()
                elif operation == 'back':
                    break
                else:
                    print('操作编码非法!')
        elif action == '2':
            src_name = get_user_name('源')
            dst_name = get_user_name('目标')
            amount = get_balance('转账')
            transfer(src_name, dst_name, amount)
        elif action == '3':
            get_orders()
        elif action == 'back':
            return
        else:
            print('操作编码非法!')


# 程序运行
config = 'users.txt'
users_count = {}
cookies = {}
shopping_cart = {}
if check_file(r'shopping_cart.json.swap'):
    with open(r'shopping_cart.json.swap') as f:
        data = json.load(f)
    shopping_cart = data
    os.remove('shopping_cart.json.swap')
while True:
    if datetime.datetime.now().strftime('%H:%M:%S') == '00:00:00':
        credit_bill()
    print('\n欢迎进入购物商城！\n1  注册\n2  登陆\n3  购物\n4  购物车\n5  支付\n6  atm')
    action = get_action()
    print(action)
    if action == '1':
        # 注册
        register()
    elif action == '2':
        # 登录
        login()
    elif action == '3':
        # 购物
        name = get_user_name('登陆')
        try:
            goods = get_goods_info()
            shopping()
        except SystemExit:
            pass
    elif action == '4':
        # 购物车
        name = get_user_name('登陆')
        try:
            shopping_cart_order()
        except SystemExit:
            pass
    elif action == '5':
        # 支付
        name = get_user_name('登陆')
        try:
            pay()
        except SystemExit:
            pass
    elif action == '6':
        # atm
        name = get_user_name('登陆')
        try:
            credit()
        except SystemExit:
            pass
    else:
        print('>> \033[31m操作编码非法！\033[0m')
