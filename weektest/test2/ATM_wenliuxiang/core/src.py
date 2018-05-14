

from interface import user
from  lib  import common
from  interface import bank
user_data={
    'name':None,
    'is_auth':False
}

def login():
    if user_data['is_auth']:
        print('user is to')
        return
    count = 0
    while True:
        name = input('账号>>').strip()
        user_dic=user.get_userinfo_interfacen(name)
        if count ==3:
             user.lock_user_interface(name)
             print('账号已经锁定')
             break
        if user_dic:
            password = input('密码>>:').strip()
            if password == user_dic['password'] and not user_dic['locked']:
                print('登录成功')
                user_data['name']=name
                user_data['is_auth']=True
                break
            else:
                count+=1
                print('密码错误')
                break
        else:
            print('user is not  or  lock  ')
            continue


def register():
    if user_data['is_auth']:
        print('user is ')
        return
    while True:
        name = input('用户名').strip()
        if user.get_userinfo_interfacen(name):
            print('用户已存在')
            break
        else:
            password = input('请输入密码').strip()
            conf_password = input('请再次确认密码').strip()
            if password == conf_password:
                user.register(name,password)
                print('注册成功！！！！！')
                break
            else:
                print('两次密码不一致')
                continue


@common.login_auth
def check_balance():
    account=bank.get_account(user_data['name'])
    print('你的余额还剩下%s' % account)


@common.login_auth
def transfer():
    while True:
        to_user=input(print("\33[32;0m请输入转账的账号>>:\33[0m".center(40, "-"))).strip()
        if to_user==user_data['name']:
            print('不能转到自己的账户')
            continue
        if 'q'==to_user:break
        to_user_dic=user.get_userinfo_interfacen(to_user)
        if to_user_dic:
            transfer_account=input('转账金额').strip()
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
            print('user not exist')
            continue




@common.login_auth
def repay():
    while True:
        account=input('请输入还款金额(按q选择退出)').strip()
        if 'q'==account:break
        if account.isdigit():
            account=int(account)
            bank.repay_interface(user_data['name'],account)
            break
        else:
            print('must')
            continue


@common.login_auth
def withdraw():
    while True:
        account=input(print("\33[32;0m取款\33[0m".center(40, "-"))).strip()
        if 'q'==account:break
        if account.isdigit():
            user_account=bank.get_account(user_data['name'])
            account=int(account)
            if user_account>=account*1.05:
                bank.withdraw_interface(user_data['name'],account)
                print('取款成功')
                break
            else:
                print('余额不足')
        else:
            print('只能输入数字')
            continue



@common.login_auth
def check_recorse():
    bankflow=bank.check_bankflow_interfac(user_data['name'])
    for record in bankflow:
        print(record)


@common.login_auth
def shopping():
    pass


@common.login_auth
def shopping_cart():
    pass



func_dic = {
    '1':login,
    '2':register,
    '3':check_balance,
    '4':transfer,
    '5':repay,
    '6':withdraw,
    '7':check_recorse,
    '8':shopping,
    '9':shopping_cart,
}

def run():
    while True:
        print("""----------\33[35;1m欢迎来到美国银行ATM
        1、登录
        2、注册
        3、查看余额
        4、转账
        5、还款
        6、取款
        7、查看流水
        8、购物
        9、查看购买商品
   \33[0m----Welcome to the ATM-----------
        """)

        choice = input(("\33[32;0m请输入编号>>:\33[0m").center(40, "-")).strip()
        if choice not in func_dic:continue
        func_dic[choice]()

