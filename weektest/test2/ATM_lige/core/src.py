
import os
import json
from conf import setting
from lib import common

from interface import user

from interface import bank

user_data={
    'name':None,
    'is_auth':False
}

def login():
    if user_data['is_auth']:
        print('user is login')
        return
    print('登陆')
    count=0
    while True:

        name=input('please input your name').strip()

        #判断用户是否存在
        user_dic=user.get_userinfo_interface(name)
        if count==3:
            user.lock_user_interface(name)
            print('user is locked')
            break

        if user_dic:
            password=input('please input your password').strip()
            if user_dic['password'] == password and not user_dic['locked']:
                print('login sucess')
                user_data['name']=name
                user_data['is_auth']=True
                break
            else:
                count+=1
                print('password error,or locked')
                continue
        else:
            print('user not exisit')
            continue


def register():
    if user_data['is_auth']:
        print('user is login')
        return
    print('注册')
    while True:
        name=input('please input your name').strip()
        #判断用户是否存在
        if user.get_userinfo_interface(name):
            print('user is exisit')
            continue
        else:
            password=input('please input password').strip()
            conf_password=input('please config your password').strip()
            if password == conf_password:
                user.register(name,password)
                print('register success')
                break
            else:
                print('password not equles')
                continue


@common.login_auth
def check_balance():
    print('查询余额')
    account=bank.get_account(user_data['name'])

    print('您的余额是:%s'%account)

@common.login_auth
def transfer():
    print('转账')
    while True:
        to_user=input('please input transfer name>>:').strip()
        if to_user==user_data['name']:
            print('connot transfer to yourself ')
            continue
        if 'q'==to_user:break
        to_user_dic=user.get_userinfo_interface(to_user)
        if to_user_dic:
            transfer_account=input('please input transfer account>>:').strip()
            if transfer_account.isdigit():
                transfer_account=int(transfer_account)
                user_account=bank.get_account(user_data['name'])
                if user_account>=transfer_account:
                    bank.transfer_interface(user_data['name'],to_user,transfer_account)
                    break
                else:
                    print('account not enough')
                    continue
            else:
                print('must input number')
                continue
        else:
            print('user not exisit')
            continue

@common.login_auth
def repay():
    print('还款')
    while True:
        account=input('please input account(q to quit)>>:').strip()
        if 'q'==account:break
        if account.isdigit():
            account=int(account)
            bank.repay_interface(user_data['name'],account)
            break
        else:
            print('must input number')
            continue

@common.login_auth
def withdraw():
    print('取款')

    while True:
        account=input('please input withdraw account>>:').strip()
        if account.isdigit():
            user_account=bank.get_account(user_data['name'])
            account=int(account)
            if user_account>=account*1.05:
                bank.withdraw_interface(user_data['name'],account)
                print('withdraw success')
                break
            else:
                print('余额不足')
        else:
            print('只能输入数字')
            continue



@common.login_auth
def check_records():

    bankflow=bank.check_bankflow_interface(user_data['name'])

    for record in bankflow:
        print(record)

@common.login_auth
def shopping():
    pass

@common.login_auth
def check_shopping_cart():
    pass

func_dic = {
    '1': login,
    '2': register,
    '3': check_balance,
    '4': transfer,
    '5': repay,
    '6': withdraw,
    '7': check_records,
    '8': shopping,
    '9': check_shopping_cart
}

def run():
    while True:
        print('''
        1、登录
        2、注册
        3、查看余额
        4、转账
        5、还款
        6、取款
        7、查看流水
        8、购物
        9、查看购买商品
        ''')

        choice=input('please choice>>:').strip()
        if choice not in func_dic:continue

        func_dic[choice]()