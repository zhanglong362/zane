# -*- encoding: utf-8 -*-

import hmac
import datetime
from lib import common
from interface import user, bank

logger = common.get_logger('app')

CURRENT_USER = None
COOKIES = {}

def input_string(word):
    while True:
        string = input('%s >>: ' % word).strip()
        return string

def input_integer(word):
    while True:
        integer = input('%s >>: ' % word).strip()
        if not integer.isdigit():
            print('\033[31m请输入整数数字！\033[0m')
            continue
        return int(integer)

def get_md5_encode_api(string):
    h = hmac.new(b'shopping')
    h.update(string.encode('utf-8'))
    return h.hexdigest()

def register():
    print('\033[33m注册\033[0m')
    while True:
        name = input_string('请输入用户名')
        user_info = user.get_user_info_api(name)
        if user_info:
            print('用户已经注册，请直接登陆！')
            return
        password = input_string('请输入密码')
        pwd = input_string('请确认密码')
        if pwd != password:
            print('\033[31m两次输入密码不一致！\033[0m')
            continue
        password = get_md5_encode_api(password)
        if user.register_user_api(name, password):
            print('\033[32m用户%s注册成功！\033[0m' % name)
            return
        else:
            print('\033[31m用户%s注册失败！\033[0m' % name)

def login():
    print('\033[33m登陆\033[0m')
    global COOKIES, CURRENT_USER
    i = 0
    while True:
        name = input_string('请输入用户名')
        if name in COOKIES:
            print('用户%s已经登录！' % name)
            continue
        user_info = user.get_user_info_api(name)
        if not user_info:
            print('\033[31m用户%s未注册，请先注册！\033[0m' % name)
            continue
        password = input_string('请输入密码')
        password = get_md5_encode_api(password)
        if password != user_info['password']:
            print('\033[31m用户%s密码错误！\033[0m' % name)
            i += 1
            if i == 3:
                user_info['unlocktime'] = datetime.datetime.now() + datetime.timedelta(minutes=5)
                user.modify_user_info_api(user_info)
                i = 0
            continue
        COOKIES = {
            'name': name,
            'role': user_info['role']
        }
        CURRENT_USER = name
        print('\033[32m用户%s登陆成功！\033[0m' % name)
        return

def check_balance():
    print('\033[33m查看余额\033[0m')
    user_info = user.get_user_info_api(CURRENT_USER)
    balance = user_info['balance']
    credit_balance = user_info['credit_balance']
    credit_limit = user_info['credit_limit']
    print('余额信息'.center(26, '-'))
    print('''\033[32m
    账户余额：%s
    信用卡余额：%s
    信用卡额度：%s\033[0m
    ''' % (balance, credit_balance, credit_limit))

def check_credit_bill():
    print('\033[33m查看账单\033[0m')
    user_info = user.get_user_info_api(CURRENT_USER)
    print('账单信息'.center(26, '-'))
    if user_info['bill'] == 0:
        print('\033[32m用户%s本期账单为0元！\033[0m' % CURRENT_USER)
    else:
        print('\033[32m用户%s本期账单为%s元！\033[0m' % (CURRENT_USER, user_info['bill']))

def check_detailed_list():
    print('\033[33m查看流水\033[0m')
    dt = input_string('请输入年月(yyyy-mm)')
    user_info = user.get_user_info_api(CURRENT_USER)
    if user_info['detailed_list']:
        print((' %s 银行流水' % dt).center(26, '='))
        for i in user_info['detailed_list']:
            if dt in i[0]:
                print('%s %s' % (i[0], i[1]))
    else:
        print('\033[32m用户%s %s 无银行流水！\033[0m' % (CURRENT_USER, dt))

def transfer():
    print('\033[33m转账\033[0m')
    while True:
        payee = input_string('请输入收款账户')
        if payee == CURRENT_USER:
            print('用户%s不能转账给自己！' % CURRENT_USER)
            continue
        user_info = user.get_user_info_api(payee)
        if not user_info:
            print('还款账户%s不存在！' % payee)
            continue
        amount = input_integer('请输入转账金额')
        if bank.transfer_amount_api(CURRENT_USER, payee, amount):
            print('\033[32m用户%s转账 %s 到用户%s成功！\033[0m' % (CURRENT_USER, amount, payee))
        else:
            print('\033[31m用户%s账户余额不足，转账 %s 到用户%s失败！\033[0m' % (CURRENT_USER, amount, payee))
        return

def repayment():
    print('\033[33m还款\033[30m')
    print('本期账单'.center(26, '-'))
    user_info = user.get_user_info_api(CURRENT_USER)
    if user_info['bill'] == 0:
        print('\033[32m用户%s本期账单为0元！\033[0m' % CURRENT_USER)
        print('-' * 30)
        return
    print('\033[32m用户%s本期账单为%s元\033[0m' % (CURRENT_USER, user_info['bill']))
    print('-' * 30)
    amount = input_integer('请输入还款金额')
    if bank.repayment_bill_api(CURRENT_USER, amount):
        print('\033[32m用户%s还款%s元成功！\033[0m' % (CURRENT_USER, amount))
    print('-'*30)

def widthraw():
    print('\033[33m取现\033[0m')
    user_info = user.get_user_info_api(CURRENT_USER)
    amount = input_integer('请输入取现金额')
    if user_info['credit_balance'] < (amount + amount*0.05):
        print('\033[31m用户%s取现额度不足，取现失败！\033[0m' % CURRENT_USER)
        return
    if bank.widthraw_cash_api(CURRENT_USER, amount):
        print('\033[32m用户%s取现%s成功！\033[0m' % (CURRENT_USER, amount))

def run():
    while True:
        menu = {
            '1': [login, '登录'],
            '2': [register, '注册'],
            '3': [check_balance, '查看余额'],
            '4': [check_credit_bill, '查看账单'],
            '5': [check_detailed_list, '查看流水'],
            '6': [transfer, '转账'],
            '7': [repayment, '还款'],
            '8': [widthraw, '取现']
        }
        print('='*30)
        for k,v in menu.items():
            print('%-6s %-10s' % (k ,v[1]))
        print('=' * 30)
        choice = input_string('请输入操作编码')
        if choice not in menu:
            print('操作编码非法！')
            continue
        try:
            menu[choice][0]()
        except Exception as e:
            print('app error: %s' % e)
        except:
            pass
