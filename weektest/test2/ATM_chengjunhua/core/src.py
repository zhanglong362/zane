from  interface import user
from lib import common
from interface  import bank
import time


logger1=common.get_logger('ATM')

users={'name':None,
      'status':False}




# print('注册')
def register():
    if users['status']:
        print('您已登陆！')
        return
    while True:
        name=input('请输入用户名>>:').strip()
        if user.file(name):
            print('该用户已注册!')
            choice = input('退出请输入q>>: ').strip()
            if choice == 'q': return
            continue
        pwd1=input('请输入密码>>: ').strip()
        pwd2=input('请再次输入密码>>:').strip()
        if pwd1 != pwd2 :
            print('两次密码不一致，请重新输入')
            continue
        user.update_user(name,pwd1)
        print('注册成功！')
        break

# print('登陆')
def login():
    while True:
        if users['status']:
            print('您已登陆,无需重复登陆！')
            return
        name=input('请输入用户名>>: ').strip()
        pwd=input('请输入用户密码>>: ').strip()
        user_dic = user.file(name)
        if not user_dic:
            print('该用户不存在')
            continue
        if user_dic['lock']:
            print('该用户已锁定')
            choice = input('退出请输入q>>: ').strip()
            if choice=='q':break
            continue
        if pwd == user_dic['password']:
            print('登陆成功！')
            users['name']=name
            users['status']=True
            return
        count=1
        while True:
            if count>=3:
                print('用户已锁定')
                user.lock_user_interface(name)
                return
            count+=1
            print('密码不正确,请重新输入，%s次后将锁定！'%(3-count))
            pwd = input('请输入用户密码>>: ').strip()
            if pwd == user_dic['password']:
                print('登陆成功！')
                users['name'] = name
                users['status'] = True
                return

# print('查看余额')
@common.login_auth
def look_money():
    user_dic = user.file(users['name'])
    print('''
        尊敬的：%s
        您的余额为：%s
        您的信用额度还剩：%s'''%(user_dic['name'],user_dic['balance'],user_dic['account']))
    choice = input('退出请输入q>>: ').strip()
    if choice == 'q':return

# print('转账')
@common.login_auth
def transfer_accounts():
    while True:
        user_self = user.file(users['name'])
        side_name=input('请输入收款账号>>: ').strip()
        user_side=user.file(side_name)
        if not user_side:
            print('该用户不存在！')
            continue
        if side_name==users['name']:
            print('不能转给自己！')
            continue
        money=input('请输入转账金额>>: ').strip()
        if not money.isdigit():
            print('钱必须是数字！')
            continue
        money=int(money)
        if user_self['balance'] < money:
            print('傻叉钱你没那么多钱！')
            continue
        user_self['balance']-=money
        user_side['balance']+=money
        bank.update_money(user_self)
        bank.update_money(user_side)
        debug=('%s向%s转账%s成功!'%(user_self['name'],user_side['name'],money))
        logger1.debug(debug)
        choice = input('退出请输入q>>: ').strip()
        if choice == 'q': return

# print('还款')
@common.login_auth
def repayment():
    while True:
        user_self=user.file(users['name'])
        account=15000-user_self['account']
        print('您本期需要还款的金额为:%s'%account)
        money=input('请输入还款金额: ').strip()
        if not money.isdigit():
            print('钱必须是数字！')
            continue
        money = int(money)
        if user_self['balance'] < money:
            print('傻叉钱你没那么多钱！')
            continue
        user_self['balance']-=money
        user_self['account']+=money
        bank.update_money(user_self)
        debug=('%s还款%s,当前信用可用额度为:%s'%(user_self['name'],money,user_self['account']))
        logger1.debug(debug)
        choice = input('退出请输入q>>: ').strip()
        if choice == 'q': return


# print('取款')
@common.login_auth
def draw_money():
    while True:
        money=input('请输入取款金额: ').strip()
        user_self = user.file(users['name'])
        if not money.isdigit():
            print('钱必须是数字！')
            continue
        money = int(money)
        if user_self['account'] < money:
            print('傻叉钱你没那么多额度了！')
            continue
        money1=(money*0.05)
        money2=money-money1
        user_self['account'] -= money
        user_self['balance'] += money2
        bank.update_money(user_self)
        debug = ('%s提现：%s,当前信用可用额度为:%s 手续费:%s' % (user_self['name'],money2,user_self['account'],money1))
        logger1.debug(debug)
        choice = input('退出请输入q>>: ').strip()
        if choice == 'q': return


def illegality():
    print('非法输入!')



dic={'1':register,
     '2':login,
     '3':look_money,
     '4':transfer_accounts,
     '5':repayment,
     '6':draw_money,
     }

def run():
    while True:
        print('''
                1、注册
                2、登陆
                3、查看余额
                4、转账
                5、还款
                6、取款
                ''')
        choice=input('输入序号选择功能，q退出>>: ').strip()
        if choice=='q':break
        function=dic[choice] if choice in dic else illegality
        function()
