# 4. 编写购物车程序，实现注册，登陆，购物，查看功能，数据基于文件存取（30分）

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
        'price': 100000
    }
}
config = 'users.txt'
with open(r'%s' % config, 'a') as f:
    pass

shopping_cart = {}
cookies = []
user_balance = {}
tag = True
logout = 'quit'
while tag:
    users = {}
    with open(r'%s' % config) as f:
        for u in f:
            if u:
                u = u.strip('\n').split('|')
                n, p, b = u
                users[n] = {'password': p, 'balance': int(b)}
    print('1  注册\n2  登陆\n3  购物\n4  购物车')
    action = input('请选择操作: ').strip()
    if action == logout:
        tag = False
        continue
    elif action == '1':
        # 注册
        while tag:
            name = input('请输入用户名 >>: ').strip()
            if name == logout:
                tag = False
                continue
            if name in users:
                print('用户已经注册，请直接登陆！')
                break
            password = input('请输入密码 >>: ')
            if password == logout:
                tag = False
                continue
            while tag:
                balance = input('请输入充值金额 >>: ').strip()
                if balance == logout:
                    tag = False
                    continue
                if not balance.isdigit():
                    balance = int(balance)
                    break
                print('请输入金额的整数！')
            if balance == logout:
                continue
            with open(r'%s' % config, 'a') as f:
                user = '%s|%s|%s\n' % (name, password, balance)
                f.write(user)
            print('用户%s注册成功！' % name)
            break
    elif action == '2':
        # 登陆
        while tag:
            name = input('请输入用户名 >>: ').strip()
            if name == logout:
                tag = False
                continue
            if name not in users:
                print('用户不存在！')
                continue
            if name in cookies:
                print('用户%s已经是登录状态！' % name)
                break
            password = input('请输入密码 >>: ')
            if password == logout:
                tag = False
                continue
            if password != users[name]['password']:
                print('密码错误！')
                continue
            if name in users and password == users[name]['password']:
                cookies.append(name)
                print('用户%s登陆成功！' % name)
                break
    elif action == '3':
        # 购物
        name = input('请输入用户名 >>: ').strip()
        if name == logout:
            tag = False
            continue
        if name not in cookies:
            print('请登陆后再进行购物！')
            continue
        balance = users[name]['balance']
        while tag:
            print('='*30)
            print('商品编号    商品名称    商品价格')
            for k,v in goods.items():
                print('%-10s %-10s %-10s' % (k, v['name'], v['price']))
            print('='*30)
            code = input('请选择商品编码 [结账:bill] >>: ').strip()
            if code == logout:
                tag = False
                continue
            if code == 'bill':
                print('请进入购物车结账！')
                break
            if code not in goods:
                print('商品编号非法！')
                continue
            while tag:
                count = input('请输入购买数量 >>: ').strip()
                if count == logout:
                    tag = False
                    continue
                if count.isdigit():
                    count = int(count)
                    break
                print('请输入数量的整数！')
            good = goods[code]['name']
            price = goods[code]['price']
            cost = price * count
            if balance >= cost:
                balance -= cost
                if name not in shopping_cart:
                    shopping_cart[name] = {}
                if good not in shopping_cart[name]:
                    shopping_cart[name][good] = {
                        'code': code,
                        'price': price,
                        'count': count
                    }
                else:
                    shopping_cart[name][good] = {
                        'code': code,
                        'price': price,
                        'count': shopping_cart[name][good]['count'] + count
                    }
                print('购物车: %s \n账户余额: %s' % (shopping_cart[name], balance))
            else:
                diff = cost - balance
                print('账户余额不足！商品 %s x %s 还需 %s 才能购买！' % (good, count, diff))
            user_balance[name] = balance
    elif action == '4':
        # 购物车
        name = input('请输入用户名 >>: ').strip()
        if name == logout:
            tag = False
            continue
        if name not in cookies:
            print('请登陆后再查看购物车！')
            continue
        cost = 0
        print('='*50)
        print('商品名称    商品编号    商品价格    商品数量\n')
        for k,v in shopping_cart[name].items():
            good, code, price, count = k, v['code'], v['price'], v['count']
            print('%-10s %-10s %-10s %-10s' % (good, code, price, count))
            cost += (price * count)
        print('\n商品总价: %s' % cost)
        print('账户余额: %s' % user_balance[name])
        print('='*50)
        buy = input('确认购买？y/n >>: ').strip()
        if buy == logout or buy == 'n':
            print('取消购物！')
            tag = False
            continue
        elif buy == 'y':
            with open(r'%s' % config) as f1, \
                    open(r'%s.swap' % config, 'w') as f2:
                for line in f1:
                    if name in line:
                        line = line.split('|')
                        line[-1] = '%s\n' % user_balance[name]
                        line = '|'.join(line)
                    f2.write(line)
            os.remove(config)
            os.rename('%s.swap' % config, config)
            print('购物成功，请耐心等待发货！')
            shopping_cart = {}
        else:
            print('输入操作非法！')
    else:
        print('操作编号非法！')