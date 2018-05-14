# -*- encoding: utf-8 -*-

from interface inport user


def register():
    while True:
        name = input('请输入用户名 >>: ').strip()
        user_info = user.get_user_info_api(name)
        if user_info:
            print('用户%s已注册！' % name)
            return
        pwd = input('请输入密码 >>: ').strip()
        pwd2 = input('请确认密码 >>: ').strip()
        if pwd != pwd2:
            print('两次输入密码不一致！')
            continue
        register_user_api(name, pwd)
        print('用户%s注册成功！' % name)

def login():
    i = 0
    while True:
        name = input('请输入用户名 >>: ').strip()
        user_info = user.get_user_info_api(name)
        if not user_info:
            print('用户%s不存在！' % name)
            continue
        if user_info['lock']:
            print('用户%s已锁定，禁止登陆！' % name)
            continue
        pwd = input('请输入密码 >>: ').strip()
        if pwd != user_info['pwd']:
            print('密码错误！')
            i += 1
            if i == 3:
                print('尝试次数过多，锁定用户%s' % name)
                user_info['lock'] = True
                user.modify_user_api(user_info)
            continue
        print('用户%s登陆成功！' % name)

def run():
    while True:
        print('''
        1 登陆
        2 注册
        ''')

        chioce = input('请输入操作编码 >>: ').strip()
        if chioce == 'quit':
            print('Goodbye!')
            break
        if choice in operations:
            operations[choice]()
        else:
            print('操作编码非法！')


