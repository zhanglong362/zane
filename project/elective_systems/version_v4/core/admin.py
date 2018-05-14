# -*- encoding: utf-8 -*-

from lib import common
from interface import admin_api

USER = {'name': None}
ROLE = 'admin'

def login():
    print('\033[32m登陆\033[0m')
    while True:
        name = input('请输入登陆用户名 >>: ').strip()
        if name == 'q': break
        password = input('请输入登陆密码 >>: ').strip()
        if password == 'q': break
        flag, msg = admin_api.login(name, password)
        if flag:
            print('\033[32m%s\033[0m' % msg)
            USER['name'] = name
            return
        else:
            print('\033[31m%s\033[0m' % msg)

def register():
    print('\033[32m注册\033[0m')
    while True:
        name = input('请输入注册用户名 >>: ').strip()
        if name == 'q': break
        password = input('请输入注册密码 >>: ').strip()
        if password == 'q': break
        password2 = input('请确认注册密码 >>: ').strip()
        if password2 == 'q': break
        if password != password2:
            print('\033[31m两次输入密码不一致！\033[0m')
            continue
        flag, msg = admin_api.register(name, password)
        if flag:
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

@common.auth(ROLE)
def create_school():
    print('\033[32m创建学校\033[0m')
    while True:
        name = input('请输入学校名称 >>: ').strip()
        if name == 'q': break
        address = input('请输入学校地址 >>: ').strip()
        if address == 'q': break
        flag, msg = admin_api.create_school(USER['name'], name, address)
        if flag:
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

@common.auth(ROLE)
def choose_school():
    while True:
        schools = common.get_object_list('school')
        print('-' * 30)
        for k, v in enumerate(schools):
            print('%-4s%-10s' % (k, v))
        print('-' * 30)
        choice = input('请选择学校编号 >>: ').strip()
        if choice == 'q': break
        if not choice.isdigit():
            print('\033[31m选择编号必须是数字！\033[0m')
            continue
        choice = int(choice)
        if choice < 0 or choice > len(schools):
            print('\033[31m选择编号超出范围！\033[0m')
        school_name = schools[choice]
        return school_name

@common.auth(ROLE)
def create_teacher():
    print('\033[32m创建老师\033[0m')
    while True:
        name = input('请输入老师名字 >>: ').strip()
        if name == 'q': break
        flag, msg = admin_api.create_teacher(USER['name'], name)
        if flag:
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

@common.auth(ROLE)
def create_course():
    print('\033[32m创建课程\033[0m')
    while True:
        school_name = choose_school()
        name = input('请输入课程名称 >>: ').strip()
        if name == 'q': break
        price = input('请输入课程价格 >>: ').strip()
        if price == 'q': break
        cycle = input('请输入课程周期 >>: ').strip()
        if cycle == 'q': break
        flag, msg = admin_api.create_course(USER['name'], name, price, cycle, school_name)
        if flag:
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

@common.auth(ROLE)
def check_school():
    print('\033[32m查看学校\033[0m')
    schools = common.get_object_list('school')
    print('=' * 30)
    for name in schools:
        print(admin_api.get_school_info(name))
        print('-' * 30)

@common.auth(ROLE)
def check_teacher():
    print('\033[32m查看老师\033[0m')
    teachers = common.get_object_list('teacher')
    print('=' * 30)
    for name in teachers:
        print(admin_api.get_teacher_info(name))
        print('-' * 30)

@common.auth(ROLE)
def check_course():
    print('\033[32m查看课程\033[0m')
    courses = common.get_object_list('course')
    print('=' * 30)
    for name in courses:
        print(admin_api.get_course_info(name))
        print('-' * 30)

def run():
    menu = {
        '1': [login, '登陆'],
        '2': [register, '注册'],
        '3': [check_school, '查看学校'],
        '4': [check_teacher, '查看老师'],
        '5': [check_course, '查看课程'],
        '6': [create_school, '创建学校'],
        '7': [create_teacher, '创建老师'],
        '8': [create_course, '创建课程']
    }
    while True:
        print('=' * 30)
        for k,v in menu.items():
            print('%-5s%-10s' % (k, v[1]))
        print('=' * 30)
        choice = input('请选择操作编号 >>: ').strip()
        if choice == 'q': break
        if choice not in menu:
            print('\033[31m操作编号非法！\033[0m')
            continue
        menu[choice][0]()
