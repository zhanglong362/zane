# -*- encoding: utf-8 -*-

from lib import common
from interface import user, bank

user_data = {'name': None}

def login():
    print('\033[32m登陆\033[0m')
    while 1:
        name = input('用户名 >>: ').strip()
        user_info = user.get_user_info(name)
        if not user_info:
            print('\033[33m用户未注册，请先注册再登录！\033[0m')
        pwd = input('密码 >>: ').strip()
        if pwd != user_info['pwd']:
            print('\033[32m密码错误！\033[0m')
            continue
        user_data['name'] = name
        print('\033[32m用户%s登陆成功！\033[0m' % name)
        return

def register():
    print('\033[32m注册\033[0m')
    while 1:
        name = input('用户名 >>: ').strip()
        user_info = user.get_user_info(name)
        if user_info:
            print('\033[33m用户已注册，请直接登陆！\033[0m')
        pwd = input('密码 >>: ').strip()
        pwd2 = input('密码 >>: ').strip()
        if pwd2 != pwd:
            print('\033[33m两次密码输入不一致！\033[0m')
            continue
        if user.register_user(name, pwd):
            print('\033[32m用户%s注册成功！\033[0m' % name)
        else:
            print('\033[31m用户%s注册失败！\033[0m' % name)
        return

@common.auth
def check_balance():
    print('\033[32m查看余额\033[0m')
    user_info = user.get_user_info(user_data['name'])
    print('-'*30)
    print('''\033[35m
    balance: %s
    credit_balance: %s
    credit_limit: %s\033[0m
    ''' % (user_info['balance'], user_info['credit_balance'], user_info['credit_limit']))
    print('-' * 30)

@common.auth
def check_bill():
    print('\033[32m查看账单\033[0m')
    user_info = user.get_user_info(user_data['name'])
    print('-' * 30)
    if user_info['bill'] == 0:
        print('\033[35m本期账单为0元！\033[0m')
    else:
        print('\033[35m本期账单为%s元！\033[0m' % user_info['bill'])
    print('-' * 30)

@common.auth
def check_detailed_list():
    print('\033[32m查看流水\033[0m')
    user_info = user.get_user_info(user_data['name'])
    print('-' * 30)
    if not user_info['detailed_list']:
        print('\033[35m没有银行流水！\033[0m')
    for dt, flow in user_info['detailed_list']:
        print('\033[35m %s %s\033[0m' % (dt, flow))
    print('-' * 30)

@common.auth
def transfer():
    print('\033[32m转账\033[0m')
    while 1:
        name = input('收款人账户 >>: ').strip()
        if name == user_data['name']:
            print('\033[31m用户%s不能给自己转账！\033[0m' % name)
            continue
        user_info = user.get_user_info(name)
        if not user_info:
            print('\033[31m收款人账户%s不存在！\033[0m' % name)
            continue
        while 1:
            amount = input('请输入转账金额 >>: ').strip()
            if not amount.isdigit():
                print('\033[32m转账金额必须是数字！\033[0m')
                continue
            amount = int(amount)
            break
        if bank.transfer(user_data['name'], name, amount):
            print('\033[32m用户%s给账户%s转账%s成功！\033[0m' % (user_data['name'], name, amount))
        else:
            print('\033[31m用户%s账户余额不足，转账失败！\033[0m' % user_data['name'])
        return

@common.auth
def withdraw():
    print('\033[32m取现\033[0m')
    while True:
        amount = input('请输入取现金额 >>: ').strip()
        if not amount.isdigit():
            print('\033[32m转账金额必须是数字！\033[0m')
            continue
        amount = int(amount)
        break
    if bank.withdraw(user_data['name'], amount):
        print('\033[32m用户%s取现成功！\033[0m' % user_data['name'])
    else:
        print('\033[31m用户%s取现失败！\033[0m' % user_data['name'])


@common.auth
def repayment():
    print('\033[32m还款\033[0m')
    user_info = user.get_user_info(user_data['name'])
    if user_info['bill'] == 0:
        print('\033[35m本期账单为0元！\033[0m')
    else:
        print('\033[35m本期账单为%s元！\033[0m' % user_info['bill'])
    while True:
        amount = input('请输入还款金额 >>: ').strip()
        if not amount.isdigit():
            print('\033[32m转账金额必须是数字！\033[0m')
            continue
        amount = int(amount)
        break
    if bank.payment(user_data['name'], amount):
        print('\033[32m用户%s还款成功！\033[0m' % user_data['name'])
    else:
        print('\033[31m用户%s还款成功！\033[0m' % user_data['name'])

def run():
    menu = {
        '1': [login, '登陆'],
        '2': [register, '注册'],
        '3': [check_balance, '查看余额'],
        '4': [check_bill, '查看账单'],
        '5': [check_detailed_list, '查看流水'],
        '6': [transfer, '转账'],
        '7': [withdraw, '取现'],
        '8': [repayment, '还款']
    }
    while 1:
        print('=' * 30)
        for k,v in menu.items():
            print('%-5s %-10s' % (k, v[1]))
        print('='*30)
        choice = input('请输入操作编码 >>: ').strip()
        if choice == 'q':
            break
        if choice not in menu:
            print('操作非法！')
            continue
        menu[choice][0]()

