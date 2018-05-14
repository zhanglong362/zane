# -*- encoding: utf-8 -*-

from lib import common
from interface import user, bank, shop

CURRENT_USER = None

def input_string(word):
    while True:
        string = input('%s >>: ' % word).strip()
        if not string:
            print('\033[32m输入不能是空！\033[0m')
            continue
        return string

def input_integer(word):
    while True:
        string = input('%s >>: ' % word).strip()
        if not string:
            print('\033[32m输入不能是空！\033[0m')
            continue
        if string == 'q':
            return string
        if not string.isdigit():
            print('\033[31m请输入数字！\033[0m')
        return int(string)

def login():
    global CURRENT_USER
    print('\033[32m登陆\033[0m')
    if CURRENT_USER:
        print('\033[31m用户不能重复登录！\033[0m')
        return
    while True:
        name = input_string('用户名')
        if name == 'q':
            break
        password = input_string('密码')
        if password == 'q':
            break
        flag, msg = user.login(name, password)
        if flag:
            CURRENT_USER = name
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

def register():
    print('\033[32m注册\033[0m')
    while True:
        name = input_string('用户名')
        if name == 'q':
            break
        password = input_string('密码')
        if password == 'q':
            break
        password2 = input_string('密码')
        if password2 == 'q':
            break
        if password != password2:
            print('\033[31m两次输入密码不一致！\033[0m')
            continue
        flag, msg = user.register(name, password)
        if flag:
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

@common.auth
def check_balance(show=True):
    if show:
        print('\033[32m查询余额\033[0m')
    balance_info = user.get_balance_info(CURRENT_USER)
    print('-' * 30)
    print('账户余额：%s \n信用余额：%s \n信用额度：%s' % balance_info)
    print('-' * 30)

@common.auth
def check_bill():
    print('\033[32m查询账单\033[0m')
    bill_info = user.get_bill_info(CURRENT_USER)
    print('-' * 30)
    print('您的本期账单是%s元' % bill_info)
    print('-' * 30)

@common.auth
def check_flow():
    print('\033[32m查询银行流水\033[0m')
    flow_info = user.get_flow_info(CURRENT_USER)
    if not flow_info:
        print('用户%s没有银行流水！' % CURRENT_USER)
        return
    print('-' * 30)
    for k,v in flow_info:
        print('%s, %s' % (k, v))
    print('-' * 30)

@common.auth
def recharge():
    print('\033[32m充值\033[0m')
    amount = input_integer('请输入充值金额')
    if amount == 'q':
        return
    flag, msg = bank.recharge(CURRENT_USER, amount)
    if flag:
        print('\033[32m%s\033[0m' % msg)
        return
    else:
        print('\033[31m%s\033[0m' % msg)

@common.auth
def transfer():
    print('\033[32m转账\033[0m')
    while True:
        name = input_string('请输入收款账户')
        if name == 'q':
            break
        if name == CURRENT_USER:
            print('\033[32m用户%s不能转账给自己！\033[0m' % name)
            continue
        amount = input_integer('请输入转账金额')
        flag, msg = bank.transfer(CURRENT_USER, name, amount)
        if flag:
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

@common.auth
def withdraw():
    print('\033[32m取现\033[0m')
    amount = input_integer('请输入取现金额')
    if amount == 'q':
        return
    flag, msg = bank.withdraw(CURRENT_USER, amount)
    if flag:
        print('\033[32m%s\033[0m' % msg)
        return
    else:
        print('\033[31m%s\033[0m' % msg)

@common.auth
def repay():
    print('\033[32m还款\033[0m')
    check_bill()
    amount = input_integer('请输入还款金额')
    if amount == 'q':
        return
    flag, msg = bank.repay(CURRENT_USER, amount)
    if flag:
        print('\033[32m%s\033[0m' % msg)
        return
    else:
        print('\033[31m%s\033[0m' % msg)

@common.auth
def check_shopping_cart(show=True):
    if show:
        print('\033[32m查看购物车\033[0m')
    shopping_cart_info = shop.get_shopping_cart_info(CURRENT_USER)
    if not shopping_cart_info:
        print('用户%s购物车列表为空！' % CURRENT_USER)
        return
    print('-' * 30)
    cost = 0
    for code, v in shopping_cart_info.items():
        cost += (v['price'] * v['count'])
        print('商品编码：%s 商品名称：%s 商品价格：%s 商品数量：%s' % (
            code, v['good'], v['price'], v['count']))
    print('商品总价：%s' % cost)
    check_balance(False)

@common.auth
def modify_shopping_cart():
    print('\033[32m编辑购物车\033[0m')
    while True:
        if not check_shopping_cart(False):
            return
        code = input_string('请输入要删除的商品编号')
        if code == 'q':
            break
        count = input_integer('请输入要删除的商品数量')
        if count == 'q':
            break
        flag, msg = shop.modify_shopping_cart(CURRENT_USER, code, count)
        if flag:
            print('\033[32m%s\033[0m' % msg)
        else:
            print('\033[31m%s\033[0m' % msg)

def get_good_info():
    good_info = shop.get_good_info()
    print('-' * 30)
    for k, v in good_info.items():
        print('%s %s %s' % (k, v['name'], v['price']))
    print('-' * 30)
    return good_info

@common.auth
def shopping():
    print('\033[32m购物\033[0m')
    while True:
        print('\033[35m输入pay结账\033[0m')
        good_info = get_good_info()
        code = input_string('请选择购买商品编号')
        if code == 'q':
            break
        if code == 'pay':
            pay()
            return
        if code not in good_info:
            print('\033[32m购物编号非法！\033[0m')
            continue
        good = good_info[code]['name']
        price = good_info[code]['price']
        count = input_integer('请输入购买商品数量')
        flag, msg = shop.join_shopping_cart(CURRENT_USER, code, good, price, count)
        if flag:
            print('\033[32m%s\033[0m' % msg)
        else:
            print('\033[31m%s\033[0m' % msg)

@common.auth
def pay():
    print('\033[32m结账\033[0m')
    while True:
        check_shopping_cart(False)
        confirm = input_string('是否确认结账？y/n')
        if confirm == 'q':
            break
        if confirm == 'n':
            print('\033[32m用户%s取消结账\033[0m' % CURRENT_USER)
            break
        if confirm == 'y':
            flag, msg = shop.pay(CURRENT_USER)
            if flag:
                print('\033[32m%s\033[0m' % msg)
                f, m = shop.flush_shopping_cart(CURRENT_USER)
                if f:
                    print('\033[32m%s\033[0m' % m)
                else:
                    print('\033[31m%s\033[0m' % m)
                return
            else:
                print('\033[31m%s\033[0m' % msg)

def new_arrival():
    print('\033[32m新品上架\033[0m')
    get_good_info()
    while True:
        code = input_string('请输入新商品编号')
        if code == 'q':
            break
        good = input_string('请输入新商品名称')
        if good == 'q':
            break
        price = input_integer('请输入新商品价格')
        if price == 'q':
            break
        flag, msg = shop.new_arrival(code, good, price)
        if flag:
            print('\033[32m%s\033[0m' % msg)
        else:
            print('\033[31m%s\033[0m' % msg)

@common.auth
def atm():
    menu = {
        '1': [check_balance, '查看余额'],
        '2': [check_bill, '查看账单'],
        '3': [check_flow, '查看银行流水'],
        '4': [recharge, '充值'],
        '5': [transfer, '转账'],
        '6': [withdraw, '取现'],
        '7': [repay, '还款']
    }
    while True:
        print('=' * 30)
        for k,v in menu.items():
            print('%-4s %-10s' % (k, v[1]))
        print('=' * 30)
        choice = input_string('请选择操作编号')
        if choice == 'q':
            break
        if choice not in menu:
            print('\033[31m选择编号非法！\033[0m')
            continue
        menu[choice][0]()

@common.auth
def mall():
    menu = {
        '1': [check_shopping_cart, '查看购物车'],
        '2': [modify_shopping_cart, '编辑购物车'],
        '3': [shopping, '购物'],
        '4': [pay, '结账']
    }
    while True:
        print('=' * 30)
        for k,v in menu.items():
            print('%-4s %-10s' % (k, v[1]))
        print('=' * 30)
        choice = input_string('请选择操作编号')
        if choice == 'q':
            break
        if choice not in menu:
            print('\033[31m选择编号非法！\033[0m')
            continue
        menu[choice][0]()

def run():
    menu = {
        '1': [login, '登陆'],
        '2': [register, '注册'],
        '3': [atm, 'ATM'],
        '4': [mall, '购物商城'],
    }
    while True:
        print('=' * 30)
        for k,v in menu.items():
            print('%-4s %-10s' % (k, v[1]))
        print('=' * 30)
        choice = input_string('请选择操作编号')
        if choice == 'q':
            break
        if choice == 'backdoor':
            print('\033[35mBackdoor -->  新品上架！！\033[0m')
            new_arrival()
            continue
        if choice not in menu:
            print('\033[31m选择编号非法！\033[0m')
            continue
        menu[choice][0]()







