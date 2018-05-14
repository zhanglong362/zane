# -*- encoding: utf-8 -*-

from lib import common
from interface import common_api, admin_api


USER = {'name': None}
ROLE = 'admin'

def login():
    print('\033[32m登陆\033[0m')
    if USER['name']:
        print('\033[32m已登陆，不能重复登录！\033[0m')
    while True:
        name = input('请输入登陆名 >>: ').strip()
        pwd = input('请输入登陆密码 >>: ').strip()
        flag, msg = common_api.login(name, pwd, ROLE)
        if flag:
            USER['name'] = name
            print(msg)
            return
        else:
            print(msg)

def register():
    print('\033[32m注册\033[0m')
    if USER['name']:
        print('\033[32m已登陆，不能注册！\033[0m')
    while True:
        name = input('请输入注册用户名 >>: ').strip()
        pwd = input('请输入注册密码 >>: ').strip()
        pwd2 = input('请确认注册密码 >>: ').strip()
        if pwd != pwd2:
            print('\033[31m两次密码输入不一致！\033[0m')
            continue
        flag, msg = admin_api.register(name, pwd)
        if flag:
            print(msg)
            return
        else:
            print(msg)

@common.auth(USER['name'], ROLE)
def create_school():
    print('\033[32m创建学校\033[0m')
    while True:
        name = input('请输入学校名 >>: ').strip()
        addr = input('请输入学校地址 >>: ').strip()
        flag, msg = admin_api.create_school(name, addr)
        if flag:
            print(msg)
            return
        else:
            print(msg)

@common.auth(USER['name'], ROLE)
def create_teacher():
    print('\033[32m创建老师\033[0m')
    while True:
        name = input('请输入老师名 >>: ').strip()
        flag, msg = admin_api.create_teacher(name)
        if flag:
            print(msg)
            return
        else:
            print(msg)

@common.auth(USER['name'], ROLE)
def create_course():
    print('\033[32m创建课程\033[0m')
    while True:
        schools = admin_api.get_schools()
        print('-' * 30)
        d = {}
        for index, school in enumerate(schools):
            print('%-4s %-10s' % (index, school))
            d[str(index)] = school
        print('-' * 30)
        while True:
            choice = input('请选择校区编号 >>: ').strip()
            if choice not in d:
                print('选择校区编号非法！')
                continue
            school_name = d[choice]
            break
        name = input('请输入课程名 >>: ').strip()
        price = input('请输入课程价格 >>: ').strip()
        cycle = input('请输入课程周期 >>: ').strip()
        flag, msg = admin_api.create_course(name, price, cycle, school_name)
        if flag:
            print(msg)
            return
        else:
            print(msg)

def run():
    menu = {
        '1': [login, '登陆'],
        '2': [register, '注册'],
        '3': [create_school, '创建学校'],
        '4': [create_teacher, '创建老师'],
        '5': [create_course, '创建课程'],
    }
    while True:
        print('=' * 30)
        for k, v in menu.items():
            print('%-4s %-10s' % (k, v[1]))
        print('=' * 30)
        choice = input('请选择操作编号[q to exit] >>: ').strip()
        if choice == 'q':
            break
        if choice not in menu:
            print('\033[31m选择编号非法！\033[0m')
            continue
        try:
            menu[choice][0]()
        except Exception as e:
            print('\033[31merror from admin: %s\033[0m' % e)