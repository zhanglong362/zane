# 一、编写用户注册函数，实现功能
# 1、在函数内接收用户输入的用户名、密码、余额
#     要求用户输入的用户名必须为字符串，并且保证用户输入的用户名不与其他用户重复
#     要求用户输入两次密码，确认输入一致
#     要求用户输入的余额必须为数字
# 2、要求注册的用户信息全部存放于文件中

config = 'users.txt'
with open(r'%s' % config, 'a') as f:
    pass

def get_config():
    users = {}
    with open(r'%s' % config) as f:
        for u in f:
            u = u.strip('\n').split('|')
            n, p, b = u
            users[n] = {'password': p, 'balance': b}
    return users

def update_config(name, password, balance):
    with open(r'%s' % config, 'a') as f:
        user = '%s|%s|%s\n' % (name, password, balance)
        f.write(user)
    print('用户注册成功！')

def get_name():
    while True:
        users = get_config()
        name = input('input username >>: ').strip()
        if not name.isalpha():
            print('name must be string!')
            continue
        if name in users:
            print('user %s is alread registered!' % name)
            continue
        return name

def get_password():
    while True:
        pwd1 = input('input password >>: ')
        pwd2 = input('input password again >>: ')
        if pwd1 != pwd2:
            print('password and confirm password inconsistent!')
            continue
        return pwd1

def get_balance():
    while True:
        balance = input('input balance >>: ').strip()
        if not balance.isdigit():
            print('please enter an integer!')
            continue
        balance = int(balance)
        return balance

def register():
    name = get_name()
    password = get_password()
    balance = get_balance()
    update_config(name, password, balance)

register()



# 二、编写用户转账函数，实现功能
# 1、传入源账户名（保证必须为str）、目标账户名（保证必须为str）、转账金额（保证必须为数字）
# 2、实现源账户减钱，目标账户加钱

import os

config = 'users.txt'
with open(r'%s' % config, 'a') as f:
    pass

def get_config():
    users = {}
    with open(r'%s' % config) as f:
        for u in f:
            u = u.strip('\n').split('|')
            n, p, b = u
            users[n] = {'password': p, 'balance': b}
    return users

def update_transfer_amount(account, transfer_amount, mode):
    with open(r'%s' % config) as f1, \
            open(r'%s.swap' % config, 'w') as f2:
        for line in f1:
            user = line.strip('\n').split('|')
            if mode == 'reduce':
                if int(user[-1]) < transfer_amount:
                    print('账户余额不足！')
                    return
                user[-1] = str(int(user[-1]) - transfer_amount)
                user = '|'.join(user) + '\n'
                f2.write(user)
            elif mode == 'increase':
                user[-1] = str(int(user[-1]) + transfer_amount)
                user = '|'.join(user) + '\n'
                f2.write(user)
                print('转账成功！')
    os.remove(config)
    os.rename('%s.swap' % config, config)

def get_account(word):
    while True:
        account = input('%s >>: ' % word).strip()
        if not account.isalpha():
            print('account must be string!')
            continue
        return account

def get_transfer_amount():
    while True:
        transfer_amount = input('transfer amount').strip()
        if not transfer_amount.isdigit():
            print('please enter an integer!')
            continue
        transfer_amount = int(transfer_amount)
        return transfer_amount

def transfer():
    src_account = get_account('source account')
    dst_account = get_account('destination account')
    transfer_amount = get_transfer_amount()
    if update_transfer_amount(src_account, transfer_amount, 'reduce'):
        update_transfer_amount(dst_account, transfer_amount, 'increase')

transfer()

# 三、编写用户验证函数，实现功能
# 1、用户输入账号，密码，然后与文件中存放的账号密码验证
# 2、同一账号输错密码三次则锁定
# 3、这一项为选做功能：锁定的账号，在五分钟内无法再次登录
#     提示：一旦用户锁定，则将用户名与当前时间写入文件,例如: egon:1522134383.29839
#         实现方式如下：
#
#     import time
#
#     current_time=time.time()
#     current_time=str(current_time) #当前的时间是浮点数，要存放于文件，需要转成字符串
#     lock_user='%s:%s\n' %('egon',current_time)
#
#     然后打开文件
#     f.write(lock_user)
#
#     以后再次执行用户验证功能，先判断用户输入的用户名是否是锁定的用户，如果是，再用当前时间time.time()减去锁定的用户名后
#     的时间，如果得出的结果小于300秒，则直接终止函数，无法认证，否则就从文件中清除锁定的用户信息，并允许用户进行认证

# # 永久禁止登陆版本
import os
config = 'db.txt'
with open(r'%s' % config, 'a') as f:
    pass

def get_config():
    users = {}
    with open(r'%s' % config) as f:
        for line in f:
            if line:
                line = line.strip('\n').split('|')
                n, p, l = line
                users[n] = {'password': p, 'islock': l}
    return users

def update_config(name, islock):
    with open(r'%s' % config) as f1, \
            open(r'%s.swap' % config, 'w') as f2:
        for line in f1:
            if name in line:
                line = line.strip('\n').split('|')
                line[-1] = islock
                line = '|'.join(line) + '\n'
            f2.write('%s' % line)
    os.remove(config)
    os.rename('%s.swap' % config, config)

def get_name():
    while True:
        users = get_config()
        name = input('用户名 >>: ').strip()
        if not name.isalpha():
            print('用户名必须是字符串！')
            continue
        if name not in users:
            print('用户名不存在！')
            continue
        if users[name]['islock'] == 'lock':
            print('禁止登陆,用户已锁定！')
            continue
        return name

def login():
    login_count = {}
    while True:
        users = get_config()
        name = get_name()
        if name not in login_count:
            login_count[name] = 0
        password = input('密码 >>: ')
        if password != users[name]['password']:
            print('密码错误！')
            login_count[name] += 1
            if login_count[name] == 3:
                print('尝试次数过多，锁定用户！')
                update_config(name, 'lock')
        if name in users and password == users[name]['password']:
            print('登陆成功！')
            return 'success'

login()

# 禁止登陆5分钟版本
# 永久禁止登陆版本
import os
import time
import datetime

config = 'db.txt'
with open(r'%s' % config, 'a') as f:
    pass

def get_config():
    users = {}
    with open(r'%s' % config) as f:
        for line in f:
            if line:
                line = line.strip('\n').split('|')
                n, p, t = line
                users[n] = {'password': p, 'locktime': float(t)}
    return users

def update_config(name, locktime):
    with open(r'%s' % config) as f1, \
            open(r'%s.swap' % config, 'w') as f2:
        for line in f1:
            if name in line:
                line = line.strip('\n').split('|')
                line[-1] = str(locktime)
                line = '|'.join(line) + '\n'
            f2.write('%s' % line)
    os.remove(config)
    os.rename('%s.swap' % config, config)

def get_name():
    while True:
        users = get_config()
        name = input('用户名 >>: ').strip()
        if not name.isalpha():
            print('用户名必须是字符串！')
            continue
        if name not in users:
            print('用户名不存在！')
            continue
        dt = datetime.datetime.fromtimestamp(users[name]['locktime'])
        unlock_time = dt + datetime.timedelta(minutes=5)
        current_time =  datetime.datetime.now()
        if current_time <= unlock_time:
            print('禁止登陆,用户已锁定！')
            continue
        return name

def login():
    login_count = {}
    while True:
        users = get_config()
        name = get_name()
        if name not in login_count:
            login_count[name] = 0
        password = input('密码 >>: ')
        if password != users[name]['password']:
            print('密码错误！')
            login_count[name] += 1
            if login_count[name] == 3:
                print('尝试次数过多，锁定用户！')
                locktime = time.time()
                update_config(name, locktime)
        if name in users and password == users[name]['password']:
            print('登陆成功！')
            return 'success'

login()



