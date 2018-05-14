from interface import user
from lib import common
from interface import benk
dict={
    'name':None,
    'state':False
}
def register():
    print('注册')
    if dict['state']:
        print('已登陆')
        return
    while True:
        name=input('用户名>>:').strip()
        if not user.get_info(name):
            password=input('密码>>:').strip()
            password1=input('确认密码>>:').strip()
            if password==password1:
                user.write_info(name,password)
                break
            else:
                print('密码不一致')
        else:
            print('该用户已存在')

def login():
    print('登陆')
    if dict['state']:
        print('已登陆')
        return
    count=0
    while True:
        name = input('用户名>>:').strip()
        dic=user.get_info(name)
        if count==3:
            user.write_state(name)
            print('账户已被锁定')
            break
        if dic:
            password=input('输入密码>>:').strip()
            if password==dic['password'] and not dic['state1']:
                dict['name']=name
                dict['state']=True
                print('登陆成功')
                break
            else:
                print('密码错误')
                count+=1
        else:
            print('该用户不存在')
@common.login_
def transfer():
    print('转账')
    while True:
        name=input('转账对象>>:').strip()
        if name=='q':
            break
        if name==dict['name']:
            print('不能给自己转账')
            continue
        if benk.get_account(name):
            account=input('金额>>:').strip()
            if account.isdigit():
                dic=benk.get_account(dict['name'])
                account=int(account)
                if account<=dic['account']:
                    benk.transfer_money(dict['name'],name,account)
                    break
                else:
                    print('余额不足')
            else:
                print('请输入数字类型')
        else:
            print('对象不存在')
@common.login_
def withdraw():
    print('提现')
    while True:
        account=input('提现金额>>:').strip()
        if account=='q':
            break
        if account.isdigit():
            dic=benk.get_account(dict['name'])
            account=int(account)
            if account*1.05<=dic['account']:
                benk.out_money(dict['name'],account)
                break
            else:
                print('余额不足')
        else:
            print('请输入数字类型')
@common.login_
def inquiry():
    print('查询')
    dic=benk.get_account(dict['name'])
    print(dic['account'])
@common.login_
def flowlog():
    print('流水日志')
    dic = user.get_info(dict['name'])
    for line in dic['write_log']:
        print(line)
@common.login_
def bank_money():
    print('还款')
    while True:
        account = input('还款金额>>:').strip()
        if account == 'q':
            break
        if account.isdigit():
            account=int(account)
            benk.in_money(dict['name'],account)
            break
        else:
            print('请输入数字')
dic_name={
    '1':register,
    '2':login,
    '3':transfer,
    '4':withdraw,
    '5':inquiry,
    '6':flowlog,
    '7':bank_money
}
def run():
    while True:
        print('''
        1.注册
        2.登陆
        3.转账
        4.提现
        5.查询
        6.流水日志
        7.还款
        输入q 则退出功能
        ''')
        choice=input('请输入编码>>:').strip()
        if choice=='q':
            break
        if not choice.isdigit():
            print('请输入数字')
        if choice in dic_name:
            dic_name[choice]()