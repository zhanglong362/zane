# -*- encoding: utf-8 -*-

from conf import settings
from lib import common

def register():
    print('注册 ...')

def login():
    print('登陆 ...')
    with open(settings.DB_FILE, encoding='utf-8') as f:
        for line in f:
            print(line.strip('\n'))

def shopping():
    print('购物 ...')

def pay():
    print('支付...')

def transfer():
    print('转账 ...')
    common.logger('转账啦！...')

def run():
    while True:
        print('''
            1  注册
            2  登陆
            3  购物
            4  支付
            5  转账
        ''')
        action = input('请输入操作编码 >>: ').strip()
        if action == '1':
            register()
        elif action == '2':
            login()
        elif action == '3':
            shopping()
        elif action == '4':
            pay()
        elif action == '5':
            transfer()
        else:
            print('操作编码非法！')
