# -*- encoding: utf-8 -*-

from lib import common
from interface import admin_api

USER = {'name': None}
ROLE = 'admin'


def login():
    print('\033[32m登陆\033[0m')
    if USER['name']:
        print('\033[31m已登陆，不能重复登录！\033[0m')
    while 1:
        name = input('请输入登陆用户名 >>: ').strip()
        if name == 'q': break
        password = input('请输入登陆密码 >>: ').strip()
        flag, msg = admin_api.login(name, password)
        print(msg)
        if flag:
            USER['name'] = name
            return

def register():
    print('\033[32m注册\033[0m')
    if USER['name']:
        print('\033[31m已登陆，不能注册！\033[0m')
    while 1:
        name = input('请输入注册用户名 >>: ').strip()
        if name == 'q': break
        password = input('请输入注册密码 >>: ').strip()
        password2 = input('请输入注册密码 >>: ').strip()
        if password != password2:
            print('\033[31m两次输入密码不一致！\033[0m')
            continue
        flag, msg = admin_api.register(name, password)
        print(msg)
        if flag:
            return

@common.auth(USER['name'], ROLE)
def create_school():
    print('\033[32m创建学校\033[0m')
    while 1:
        name = input('请输入学校名称 >>: ').strip()
        if name == 'q': break
        addr = input('请输入学校地址 >>: ').strip()
        flag, msg = admin_api.create_school(name, addr)
        print(msg)
        if flag:
            return

@common.auth(USER['name'], ROLE)
def create_teacher():
    print('\033[32m创建老师\033[0m')
    while 1:
        name = input('请输入老师名字 >>: ').strip()
        if name == 'q': break
        flag, msg = admin_api.create_school(name)
        print(msg)
        if flag:
            return

@common.auth(USER['name'], ROLE)
def create_course():
    print('\033[32m创建课程\033[0m')
    while 1:
        schools = admin_api.get_schools()
        while 1:
            print('-' * 30)
            for k,v in enumerate(schools):
                print('%-4s %-10s' % (k, v))
            print('-' * 30)
            choice = input('请选择校区编号 >>: ').strip()
            if not choice.isdigit():
                print('编号必须是数字！')
                continue
            choice = int(choice)
            if choice <= 0 or choice > len(schools):
                print('编号超出范围！')
                continue
            school_name = schools[choice]
            break
        name = input('请输入课程名称 >>: ').strip()
        price = input('请输入课程价格 >>: ').strip()
        cycle = input('请输入课程周期 >>: ').strip()
        flag, msg = admin_api.create_school(name, price, cycle, school_name)
        print(msg)
        if flag:
            return

def run():
    menu = {
        '1': [login, '登陆'],
        '2': [register, '注册'],
        '3': [create_school, '创建学校'],
        '4': [create_teacher, '创建老师'],
        '5': [create_course, '创建课程']
    }
    while 1:
        print('=' * 30)
        for k,v in menu.items():
            print('%-4s %-10s' % (k, v[1]))
        print('=' * 30)
        choice = input('请选择功能编号[q to exit] >>: ').strip()
        if choice == 'q': break
        if choice not in menu:
            print('\033[31m选择编号非法！\033[0m')
            continue
        menu[choice][0]()
