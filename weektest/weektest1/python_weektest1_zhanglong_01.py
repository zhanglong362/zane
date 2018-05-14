# 二、综合题
# 1. 编写登陆接口
# 	基础需求：（4分）
# 	•	让用户输入用户名密码
# 	•	认证成功后显示欢迎信息
# 	•	输错三次后退出程序
# 升级需求：（6分）
# 可以支持多个用户登录 (提示，通过列表存多个账户信息)
# 用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）

import os

config = 'db.txt'
with open(r'%s' % config, 'a') as f:
    pass

login_list = []
user_error_count = {}
while True:
    users = {}
    with open(r'%s' % config) as f:
        for u in f:
            if u:
                u = u.strip('\n').split('|')
                n, p, l = u
                users[n] = {'password': p, 'islock': l}
    name = input('username >>: ').strip()
    if name not in users:
        print('用户不存在！')
        continue
    if name in login_list:
        print('您已经是登录状态！')
        continue
    if users[name]['islock'] == 'lock':
        print('用户已锁定，禁止登陆！')
        continue
    pwd = input('password >>: ')
    if pwd != users[name]['password']:
        print('密码错误！')
        if name not in user_error_count:
            user_error_count[name] = 1
        else:
            user_error_count[name] += 1
        if user_error_count[name] == 3:
            print('尝试次数过多，用户锁定！')
            with open(r'%s' % config) as f1, \
                    open(r'%s.swap' % config, 'w') as f2:
                for line in f1:
                    if name in line:
                        line = line.strip('\n').split('|')
                        line[-1] = 'lock\n'
                        line = '|'.join(line)
                    f2.write(line)
            os.remove(config)
            os.rename('%s.swap' % config, config)
            break
    if name in users and pwd == users[name]['password']:
        print('欢迎您，%s！登陆成功！' % name)
        login_list.append(name)