# 一、函数版购物车程序
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class Shopping():
    def __init__(self):
        self.single = '-'*50
        self.double = '='*50
        self.config = 'db.txt'
        self.tag = True
        self.login = None
        self.users = self.get_config()
        self.goods = {
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

    def get_config(self):
        users = {}
        with open(r'%s' % self.config, 'a') as f:
            pass
        with open(r'%s' % self.config) as f:
            for u in f:
                if u:
                    u = u.strip('\n').split('|')
                    name, pwd, phone, sex, age = u
                    user = {name: {'password': pwd, 'phone': phone, 'sex': sex, 'age': age, 'money': 0, 'goods': {}}}
                    users.update(user)
        return users

    def update_config(self, user):
        with open(r'%s' % self.config, 'a') as f:
            f.write('%s|%s|%s|%s|%s\n' % user)

    def check_phone(self, phone):
        for k in self.users.values():
            if phone == k['phone']:
                return True

    def interactive(self, words, number=None, password=None):
        s = input('%s >> : ' % words)
        if not password:
            s = s.strip()
        if s == 'quit' or s == 'n':
            self.tag = False
        if number:
            if s.isdigit():
                return int(s)
            else:
                print('请输入整数！')
                return
        return s

    def auth(self, name, password):
        if name not in self.users:
            print('用户名不存在！')
            return
        if password != self.users[name]['password']:
            print('密码错误！')
            return
        if name in self.users and password == self.users[name]['password']:
            print('登陆成功！')
            return name

    def main(self):
        while self.tag:
            print(self.double)
            print('1  注册用户 \n2  登陆购物')
            print(self.double)
            action = self.interactive('请选择操作')
            if not self.tag:
                continue
            if action == '1':
                while self.tag:
                    phone = self.interactive('手机')
                    if not self.tag:
                        continue
                    if self.check_phone(phone):
                        print('该手机号已注册！')
                        continue
                    username = self.interactive('用户名')
                    if not self.tag:
                        continue
                    password = self.interactive('密码', password=True)
                    if not self.tag:
                        continue
                    sex = self.interactive('性别')
                    if not self.tag:
                        continue
                    age = self.interactive('年龄')
                    if not self.tag:
                        continue
                    user = (username, password, phone, sex, age)
                    self.update_config(user)
                    print('用户 %s 注册成功！' % name)
                    break
            elif action == '2':
                i = 0
                while self.tag:
                    name = self.interactive('用户名')
                    if not self.tag:
                        continue
                    password = self.interactive('密码', password=True)
                    if not self.tag:
                        continue
                    self.login = self.auth(name, password)
                    if not self.login:
                        i += 1
                        if i == 3:
                            print('尝试次数过多！')
                            self.tag = False
                        continue
                    while self.tag:
                        salary = self.interactive('请输入工资', number=True)
                        if not self.tag:
                            continue
                        if salary:
                            self.users[name]['money'] = salary
                            break
                    while self.tag:
                        print(self.single)
                        for k, v in self.goods.items():
                            print('商品编号：%-6s 商品名称：%-10s 商品价格：%-10s' % (k, v['name'], v['price']))
                        print(self.single)
                        while self.tag:
                            code = self.interactive('请选择要购买的商品编号')
                            if not self.tag:
                                continue
                            if code not in self.goods:
                                print('输入商品编号非法！')
                                continue
                            good = self.goods[code]['name']
                            price = self.goods[code]['price']
                            break
                        while self.tag:
                            count = self.interactive('请选择要购买的商品数量', number=True)
                            if not self.tag:
                                continue
                            if count:
                                break
                        if self.users[name]['money'] >= (price * count):
                            self.users[name]['money'] -= (price * count)
                            print('商品 %s x %s 已加入购物车！' % (good, count))
                            if good not in self.users[name]['goods']:
                                self.users[name]['goods'][good] = count
                            else:
                                self.users[name]['goods'][good] += count
                            print('已购商品：%s 账户余额: %s' % (self.users[name]['goods'], self.users[name]['money']))
                        else:
                            print('\033[31m账户余额不足！\033[0m')
                        while self.tag:
                            cmd = self.interactive('是否继续购物? y/n')
                            if not self.tag:
                                print('用户名: %s\n购买商品: %s\n账户余额: %s' % (name, self.users[name]['goods'], self.users[name]['money']))
                                continue
                            if cmd == 'y':
                                break
            else:
                print('输入操作编码无效！')
            print(self.double)

if __name__ == '__main__':
    Shopping().main()





#
#
# # 二、函数练习
# # 1、写函数，，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作
# import os
#
# def modify_file(name, src_str, dst_str):
#     name_tmp = '%s.swap' % name
#     src_str = src_str.encode('utf-8')
#     dst_str = dst_str.encode('utf-8')
#     with open(r'%s' % name, 'rb') as f1, \
#         open(r'%s' % name_tmp, 'wb') as f2:
#         for line in f1:
#             if src_str in line:
#                 line = line.replace(src_str, dst_str)
#             f2.write(line)
#     os.remove(name)
#     os.rename(name_tmp, name)
#
# # 2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
# def data_count(str):
#     count = {
#         'string': 0,
#         'number': 0,
#         'space': 0,
#         'other': 0
#     }
#     for s in str:
#         if s.isalpha():
#             count['string'] += 1
#         elif s.isdigit():
#             count['number'] += 1
#         elif s.isspace():
#             count['space'] += 1
#         else:
#             count['other'] += 1
#     return count
#
# # 3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# def check_lenth(data):
#     if isinstance(data, int):
#         l = 1
#     else:
#         l = len(data)
#     if l > 5:
#         print('data: %s 长度大于5' % data)
#     else:
#         print('data: %s 长度不大于5' % data)
#
# # 4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def truncate_list(inp_list):
#     if len(inp_list) > 2:
#         inp_list = inp_list[:2]
#     return inp_list
#
# # 5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
#
# def create_list(inp_list):
#     if len(inp_list) > 1:
#         inp_list = inp_list[1:-1:2]
#         return inp_list
#     else:
#         print('列表没有奇数位元素！')
#
# # 6、写函数，检查字典的每一个value的长度, 如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
# # PS: 字典中的value只能是字符串或列表
# def modify_dict(dic):
#     for k,v in dic.items():
#         if len(v) > 2:
#             dic[k] = v[:2]
#     return dic
#
# # 7、编写认证功能函数，注意：后台存储的用户名密码来自于文件
# # 假设账户密码存储方式是 用户名|密码|phone|sex|age\n
#
# config='db.txt'
#
# def get_config(config):
#     users = {}
#     with open(r'%s' % config) as f:
#         for u in f:
#             u = u.split('|').strip('\n')
#             name, pwd, phone, sex, age = u
#             user = {name: {'password': pwd, 'phone': phone, 'sex': sex, 'age': age}}
#             users.update(user)
#     return users
#
# def auth(username, password):
#     users = get_config(config)
#     if username not in users:
#         print('用户名不存在！')
#         return
#     if username in users and password != users[username]:
#         print('密码错误！')
#         return
#     if username in users and password == users[username]:
#         print('登陆成功！')
#         return True
#
# auth(username, password)
#
# # 8、编写注册功能函数，将用户的信息储存到文件中
# config = 'db.txt'
#
# def interactive():
#     name = input('username >>: ').strip()
#     password = input('password >>: ')
#     phone = input('phone >>: ').strip()
#     sex = input('sex >>: ').strip()
#     age = input('age >>: ').strip()
#     return name, password, phone, sex, age
#
# def register():
#     name, password, phone, sex, age = interactive()
#     user = '%s|%s\n' % (name, password, phone, sex, age)
#     with open(r'%s' % config, 'wb') as f:
#         f.write(user.encode('utf-8'))
#
# register()
#
# # 9、编写查看用户信息的函数，用户的信息是事先存放于文件中的
# # 假设账户密码存储方式是 用户名|密码|phone|sex|age\n
# config = 'db.txt'
#
# def get_config(config):
#     users = {}
#     with open(r'%s' % config) as f:
#         for u in f:
#             u = u.split('|').strip('\n')
#             name, pwd, phone, sex, age = u
#             user = {name: {'password': pwd, 'phone': phone, 'sex': sex, 'age': age}}
#             users.update(user)
#     return users
#
# def auth(username, password):
#     users = get_config(config)
#     if username not in users:
#         print('用户名不存在！')
#     if username in users and password != users[username]:
#         print('密码错误！')
#     if username in users and password == users[username]:
#         print('登陆成功！')
#         return True
#
# def get_user_info(name, password):
#     users = get_config(config)
#     if auth(username, password) == 'successful':
#         for k in users[username]:
#             phone = k['phone']
#             sex = k['sex']
#             age = k['age']
#         print('用户名：%s phone：%s sex: %s age: %s' % (username, phone, sex, age))
#
# get_user_info(name, password)

