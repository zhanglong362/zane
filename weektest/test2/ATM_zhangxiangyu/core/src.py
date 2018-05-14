#coding:utf-8

from interface import user,bank
from lib import common

user_info = {
    'name':None,
    'is_auth':False
}

#登陆
def login():
    if user_info['is_auth']:
        return
    count = 0
    while True:
        name = input('请输入用户名或者q退出：').strip()
        name1 = user.get_userinfo_interface(name)
        if name == 'q':
            break
        if count==3:
            user.user_locked_interface(name)
            print('用户名被锁定！')
            break
        if not name1:
            print('用户名不存在！')
            continue
        pwd = input('请输入密码：').strip()
        if pwd == name1['password'] and name1['locked'] == False :
            user_info['name']= name
            user_info['is_auth']=True
            print('login success')
            break
        else:
            count+=1
            print('密码错误或者被锁定！')



#注册
def register():

    if user_info['is_auth']:
        return
    while True:

        uname = input('请输入用户名：').strip()
        #判断用户名是否存在
        user1 = user.get_userinfo_interface(uname)
        # if count == 3:
        #     continue
        if user1:
            print('用户名已存在')
            continue

        pwd1 = input('请输入密码：').strip()
        pwd2 = input('请确认密码：').strip()
        if pwd1 == pwd2:
            user.user_pwd_interface(uname,pwd1)
            print('success')
            break
        else:
            print('密码不一致!')






@common.login_auth
def check_bank():
    print('checking bank')
    account = bank.get_account(user_info['name'])
    print('%s的账户余额是%s'%(user_info['name'],account))


@common.login_auth
def transfer():
    while True:
        to_name = input('请输入转账目标用户：').strip()
        if to_name == user_info['name']:
            print('不可以转给自己！')
            continue
        account = input('输入转账金额：').strip()
        if account.isdigit():
            account = int(account)
            from_account = bank.get_account(user_info['name'])
            if from_account >=account:
                bank.transfer_interface(to_name,user_info['name'],account)
                print('转账成功！')
                break
            else:
                print('余额不足！')
        else:
            print('金额必须是数字！')



@common.login_auth
def repay():
    while True:
        account = input('请输入还款金额：').strip()
        if account.isdigit():
            account = int(account)
            bank.repay_interface(user_info['name'],account)
            break
        else:
            print('金额必须是数字！')

@common.login_auth
def withdraw():
    while True:

        account = input('请输入提现金额：  q退出！').strip()
        if account=='q':
            break

        if account.isdigit():
            account = float(account)
            account_user = bank.get_account(user_info['name'])
            if account_user > account*1.05:
                bank.withdraw(user_info['name'],account)
                print('提现成功！')
            else:
                print('账户金额不足！')
        else:
            print('金额必须是数字!')


@common.login_auth
def flow():
    user_dic = user.get_userinfo_interface(user_info['name'])
    for reduct in user_dic['flow_log']:
        print(reduct)

@common.login_auth
def shop():
    pass

@common.login_auth
def shopping_cart():
    pass


func_dic = {

    '1':login,
    '2':register,
    '3':check_bank,
    '4':transfer,
    '5':repay,
    '6':withdraw,
    '7':flow,
    '8':shop,
    '9':shopping_cart
}

def run():
    while True:

        print('''
            1 登陆
            2 注册
            3 查看账户额度
            4 转账
            5 还款
            6 提现
            7 查看流水
            8 购物车
            9 查看购物车

         ''')
        choice = input('请选择功能：').strip()
        if choice not in func_dic:continue

        func_dic[choice]()




