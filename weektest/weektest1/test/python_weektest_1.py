# 三、综合题
# 1. 编写基础登陆接口
import os
config = 'db.txt'
with open(r'%s' % config, 'a') as f:
    pass
i = 0
login_user_list = []
while True:
    users = {}
    with open(r'%s' % config) as f:
        for user in f:
            user = user.strip('\n').split('|')
            n, p, l = user
            users[n] = [p, l]
    name = input('用户名 >>: ').strip()
    pwd = input('密码 >>: ')
    if name not in users:
        print('用户名不存在!')
        continue
    if users[name][1] == 'lock':
        print('用户已锁定，禁止登陆！')
        continue
    if name in login_user_list:
        print('用户 %s 已经是登录状态！' % name)
        continue
    if pwd != users[name][0]:
        print('密码错误')
        i += 1
    if i == 3:
        with open(r'%s' % config, 'r') as f1, \
              open(r'%s.swap' % config, 'w') as f2:
            for line in f1:
                if name in line:
                    line = line.replace('unlock\n', 'lock\n')
                f2.write(line)
        os.remove(config)
        os.rename('%s.swap' % config, config)
        print('尝试次数过多！锁定用户！')
        break
    if name in users and pwd == users[name][0]:
        print('%s, 您已登陆成功！' % name)
        login_user_list.append(name)

# 2. 编写拷贝文件的程序
import sys
if len(sys.argv) == 3:
    src_file = sys.argv[1]
    dst_file = sys.argv[2]
else:
    print('params not valid!')
    sys.exit()
with open(r'%s' % src_file, 'rb') as f1, \
        open(r'%s' % dst_file, 'wb') as f2:
    for line in f1:
        f2.write(line)

# 3. 请用两种方式实现，将文件中的alex全部替换成SB的操作
# 第一种：
s1 = 'alex'
s2 = 'SB'
with open(r'a.txt', 'r') as f:
    data = f.read().repalce(s1, s2)
with open(r'a.txt', 'w') as f:
    f.write(data)
# 第二种：
import os
s1 = 'alex'.encode('utf-8')
s2 = 'SB'.encode('utf-8')
with open(r'a.txt', 'rb') as f1, open(r'a.txt.swap', 'wb') as f2:
    for line in f1:
        if s1 in line:
            line = line.replace(s1, s2)
        f2.write(line)
os.remove('a.txt')
os.rename('a.txt.swap', 'a.txt')

# 4. 编写购物车程序，实现注册，登陆，购物，查看功能，数据基于文件读取
import os

goods = {
            '1': {
                'name': 'mac',
                'price': 20000
            },
            '2': {
                'name': 'lenovo',
                'price': 10000
            },
            '3': {
                'name': 'apple',
                'price': 200
            },
            '4': {
                'name': 'tesla',
                'price': 1000000
            }
        }

users = {}
config = 'users.txt'
with open(r'%s' % config, 'a') as f:
    pass
with open(r'%s' % config) as f:
    for u in f:
        if u:
            u = u.strip('\n').split('|')
            n, p, b = u
            b = int(b)
            users[n] = {'password': p, 'balance': b}

tag = True
cookies = {}
shopping_cart = {}
while tag:
    print('1  注册用户\n2  用户登陆\n3  购买商品\n4  购物车')
    action = input('请选择操作 >>: ').strip()
    if action == 'quit':
        tag = False
        continue
    if action == '1':
        # 注册
        n = input('请输入用户名 >>: ').strip()
        if n == 'quit':
            tag = False
            continue
        if n in users:
            print('用户%s已经注册！' % n)
            continue
        p = input('请输入密码 >>: ')
        if p == 'quit':
            tag = False
            continue
        while tag:
            b = input('请输入充值金额 >>: ').strip()
            if b == 'quit':
                tag = False
                continue
            if b.isdigit():
                b = int(b)
                break
            print('请输入整数！')
        with open(r'%s' % config, 'a') as f:
            u = '%s|%s|%s' % (n, p, b)
            f.write(u)
        print('用户 %s 注册成功！' % n)
    elif action =='2':
        # 登陆
        while tag:
            n = input('请输入用户名 >>: ').strip()
            if n == 'quit':
                tag = False
                continue
            if n in cookies:
                print('用户%s已经登录！\n' % n)
                break
            p = input('请输入密码 >>: ')
            if p == 'quit':
                tag = False
                continue
            if n not in users:
                print('用户名不存在！')
                continue
            if p != users[n]['password']:
                print('密码错误！')
                continue
            if n in users and p == users[n]['password']:
                cookies[n] = users[n]
                print('用户 %s 登陆成功！\n' % n)
                break
    elif action == '3':
        # 购买
        n = input('请输入用户名 >>: ').strip()
        if n == 'quit':
            tag = False
            continue
        if n not in cookies:
            print('请先登录再购物！')
            continue
        while tag:
            print('='*30)
            print('编码   名称        价格')
            for k in goods:
                print('%-6s %-10s %-10s' % (k, goods[k]['name'], goods[k]['price']))
            print('='*30)
            code = input('请选择购买商品编码[结账:bill] >>: ').strip()
            if code == 'quit':
                tag = False
                continue
            if code == 'bill':
                print('请选择进入购物车结账！')
                break
            if code not in goods:
                print('商品编码非法！')
                continue
            while tag:
                count = input('请输入购买数量 >>: ').strip()
                if count == 'quit':
                    tag = False
                    continue
                if count.isdigit():
                    count = int(count)
                    break
                print('请输入整数！')
            good = goods[code]['name']
            price = goods[code]['price']
            cost = price * count
            if users[n]['balance'] >= cost:
                users[n]['balance'] -= cost
                if good not in shopping_cart:
                    shopping_cart[good] = [price, count]
                else:
                    shopping_cart[good] = [price, shopping_cart[good][1]+count]
                print('购物车: %s，账户余额: %s' % (shopping_cart, users[n]['balance']))
            else:
                diff = cost - users[n]['balance']
                print('账户余额不足！还需 %s 才能购买%s个 %s！' % (diff, count, good))
    elif action == '4':
        # 购物车，结账
        n = input('请输入用户名 >>: ').strip()
        if n == 'quit':
            tag = False
            continue
        if n not in cookies:
            print('请先登录再查看购物车！')
            continue
        cost = 0
        print('=' * 50)
        print('商品购物车：')
        for k, v in shopping_cart.items():
            good, price, count = k, v[0], v[1]
            print('购买商品：%-10s 商品价格: %-6s 购买数量: %-6s' % (good, price, count))
            cost += (price * count)
        print('\n商品总价：%s' % cost)
        print('账户余额：%s' % users[n]['balance'])
        print('=' * 50)
        buy = input('确认购买？y/n >>: ').strip()
        if buy == 'y':
            with open(r'%s' % config) as f1, \
                    open(r'%s.swap' % config, 'w') as f2:
                for line in f1:
                    if n in line:
                        line = line.split('|')
                        line[-1] = '%s\n' % str(users[n]['balance'])
                        line = '|'.join(line)
                    f2.write(line)
            os.remove(config)
            os.rename('%s.swap' % config, config)
            print('购买成功，请耐心等待发货！')
            shopping_cart = {}
        elif buy == 'n' or buy == 'quit':
            print('已取消购物！\n')
        else:
            print('输入操作非法！')
    else:
        print('输入编码非法！')