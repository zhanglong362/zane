#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

goods = {
    'mac': {
        'price': 20000
    },
    'lenovo': {
        'price': 10000
    },
    'apple': {
        'price': 200
    },
    'tesla': {
        'price': 1000000
    }
}
line = '='*25
config = 'db.txt'
tag = True
while tag:
    users = {}
    with open(config, 'a') as f:
        pass
    with open(config, 'r') as f:
        for u in f:
            u = u.strip('\n').split('|')
            if u:
                n, p, i, x, a = u
                d = {n: {'password': p, 'phone': i, 'sex': x, 'age': a, 'money': 0, 'goods': {}}}
                users.update(d)
    print(line)
    print('\n1  注册用户\n2  登陆购物\n')
    print(line)
    action = input('选择操作 >>: ').strip()
    if action == 'quit':
        tag = False
        continue
    elif action == '1':
        while tag:
            register = False
            print('请输入注册信息！')
            phone = input('手机 >>: ').strip()
            if phone == 'quit':
                tag = False
                continue
            for p in users.values():
                if phone == p['phone']:
                    print('手机号 %s 已经注册！' % phone)
                    register = True
                    break
            if register:
                continue
            name = input('用户名 >>: ').strip()
            if name == 'quit':
                tag = False
                continue
            password = input('密码 >>: ')
            if password == 'quit':
                tag = False
                continue
            sex = input('性别 >>: ').strip()
            if sex == 'quit':
                tag = False
                continue
            age = input('年龄 >>: ').strip()
            if age == 'quit':
                tag = False
                continue
            user = '%s|%s|%s|%s|%s' % (name, password, phone, sex, age)
            with open(config, 'a') as f:
                f.write('%s\n' % user)
            print('%s 注册成功！' % name)
            break
    elif action == '2':
        i = 0
        while tag:
            print('请输入用户名和密码！')
            name = input('用户名 >>: ').strip()
            if name == 'quit':
                tag = False
                continue
            if name not in users:
                print('\033[31m用户名不存在，请先注册后登陆！\033[0m')
                break
            pwd = input('密码 >>: ')
            if pwd == 'quit':
                tag = False
                continue
            if pwd != users[name]['password']:
                print('密码错误！')
                i += 1
                if i == 3:
                    print('尝试次数过多，锁定用户')
                    tag = False
                continue
            if name in users and pwd == users[name]['password']:
                print('登陆成功！')
            while tag:
                salary = input('请输入工资 >>: ').strip()
                if salary == 'quit':
                    tag = False
                    continue
                if not salary.isdigit():
                    print('工资无效，请输入整数')
                    continue
                else:
                    salary = int(salary)
                users[name]['money'] = salary
                break
            while tag:
                print(line)
                gd = {}
                for k, v in enumerate(goods):
                    print('%-6s %-10s %-10s' % (k, v, goods[v]['price']))
                    gd[str(k)] = v
                print(line)
                code = input('请选择要购买的商品编号 >>: ').strip()
                if code == 'quit':
                    tag = False
                    continue
                if code not in gd:
                    print('输入商品编号非法！')
                    continue
                else:
                    good = gd[code]
                count = input('请选择要购买的商品数量 >>: ').strip()
                if count == 'quit':
                    tag = False
                    continue
                if not count.isdigit():
                    print('数量无效，请输入整数')
                    continue
                else:
                    count = int(count)
                if users[name]['money'] >= goods[good]['price'] * count:
                    users[name]['money'] = users[name]['money'] - ( goods[good]['price'] * count )
                    print('商品 %s 购买成功！' % good)
                    if good not in users[name]['goods']:
                        users[name]['goods'][good] = count
                    else:
                        users[name]['goods'][good] = users[name]['goods'][good] + count
                    print('已购商品：%s 账户余额: %s' % (users[name]['goods'], users[name]['money']))
                else:
                    print('\033[31m账户余额不足！\033[0m')
                    continue
                cmd = input('是否继续购物? y/n >>: ').strip().lower()
                if cmd == 'n' or cmd == 'quit':
                    print('用户名: %s\n购买商品: %s\n账户余额: %s' % (name, users[name]['goods'], users[name]['money']))
                    tag = False
    else:
        print('输入编码非法！')