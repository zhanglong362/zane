# -*- encoding: utf-8 -*-

from lib import common
from interface import user, bank

USER = None

def login():
    global USER
    print('\033[32m登陆\033[0m')
    while True:
        name = input('登陆用户名 >>: ').strip()
        if name == 'q': break
        password = input('登陆密码 >>: ').strip()
        flag, msg = user.login(name, password)
        if flag:
            USER = name
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

def register():
    print('\033[32m注册\033[0m')
    while True:
        name = input('注册用户名 >>: ').strip()
        if name == 'q': break
        password = input('注册密码 >>: ').strip()
        password2 = input('确认注册密码 >>: ').strip()
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
def check_balance():
    print('\033[32m查看余额\033[0m')
    balance = user.get_balance_info(USER)
    print('-' * 30)
    print(balance)
    print('-' * 30)

@common.auth
def check_bill():
    print('\033[32m查看账单\033[0m')
    bill = user.get_bill_info(USER)
    print('-' * 30)
    print(bill)
    print('-' * 30)

@common.auth
def check_flow():
    print('\033[32m查看流水\033[0m')
    bill_date = input('请输入要查询的年月 >>: ').strip()
    flow = user.get_flow_info(USER, bill_date)
    print('-' * 30)
    if not flow:
        print('用户%s在%s没有流水！' % (USER, bill_date))
        return
    for k,v in flow:
        print(k, v)
    print('-' * 30)

@common.auth
def recharge():
    print('\033[32m充值\033[0m')
    while True:
        amount = input('请输入充值金额 >>: ').strip()
        if amount == 'q': break
        if not amount.isdigit():
            print('\033[31m转账金额必须是数字！\033[0m')
            continue
        amount = int(amount)
        flag, msg = bank.recharge(USER, amount)
        if flag:
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

@common.auth
def transfer():
    print('\033[32m转账\033[0m')
    while True:
        payee = input('请输入收款账户名 >>:').strip()
        if payee == 'q': break
        if not payee:
            print('\033[31m用户名不能为空！\033[0m')
            continue
        if payee == USER:
            print('\033[31m用户不能给自己转账！\033[0m')
            continue
        amount = input('请输入转账金额 >>: ').strip()
        if not amount.isdigit():
            print('\033[31m转账金额必须是数字！\033[0m')
            continue
        amount = int(amount)
        flag, msg = bank.transfer(USER, payee, amount)
        if flag:
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

@common.auth
def withdraw():
    print('\033[32m取现\033[0m')
    while True:
        amount = input('请输入取现金额 >>: ').strip()
        if amount == 'q': break
        if not amount.isdigit():
            print('\033[31m转账金额必须是数字！\033[0m')
            continue
        amount = int(amount)
        flag, msg = bank.withdraw(USER, amount)
        if flag:
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

@common.auth
def repayment():
    print('\033[32m还款\033[0m')
    while True:
        amount = input('请输入还款金额 >>: ').strip()
        if amount == 'q': break
        if not amount.isdigit():
            print('\033[31m转账金额必须是数字！\033[0m')
            continue
        amount = int(amount)
        flag, msg = bank.repayment(USER, amount)
        if flag:
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

def run():
    menu = {
        '1': [login, '登陆'],
        '2': [register, '注册'],
        '3': [check_balance, '查看余额'],
        '4': [check_bill, '查看账单'],
        '5': [check_flow, '查看流水'],
        '6': [recharge, '充值'],
        '7': [transfer, '转账'],
        '8': [withdraw, '取现'],
        '9': [repayment, '还款']
    }
    while True:
        print('=' * 30)
        for k,v in menu.items():
            print('%-4s %-10s' % (k, v[1]))
        print('=' * 30)
        choice = input('请选择操作编号 >>: ').strip()
        if choice == 'q': break
        if choice not in menu:
            print('\033[32m操作编号非法！\033[0m')
            continue
        menu[choice][0]()







