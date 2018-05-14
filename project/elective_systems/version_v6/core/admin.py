# -*- encoding: utf-8 -*-

from lib import common
from interface import admin_api

CURRENT_USER = None
ROLE = 'admin'

def login():
    global CURRENT_USER
    print('\033[32m登陆\033[0m')
    while True:
        name = input('请输入登陆用户名 >>: ').strip()
        if name == 'q': break
        password = input('请输入登陆密码 >>: ').strip()
        flag, msg = admin_api.login(name, password)
        if flag:
            CURRENT_USER = name
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

def register():
    print('\033[32m注册\033[0m')
    while True:
        name = input('请输入注册用户名 >>: ').strip()
        if name == 'q': break
        password = input('请输入注册密码 >>: ').strip()
        password2 = input('请确认注册密码 >>: ').strip()
        if password != password2:
            print('\033[31m两次密码输入不一致！\033[0m')
            continue
        flag, msg = admin_api.register(name, password)
        if flag:
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

@common.auth(ROLE)
def check_school():
    print('\033[32m查看学校\033[0m')
    schools = common.get_object_list('school')
    print('-' * 30)
    if not schools:
        print('\033[31m学校列表为空！\033[0m')
        return
    for k, name in enumerate(schools):
        print('%s %s' % (k, admin_api.get_school_info(CURRENT_USER, name)))
    print('-' * 30)


@common.auth(ROLE)
def check_teacher():
    print('\033[32m查看老师\033[0m')
    teachers = common.get_object_list('teacher')
    print('-' * 30)
    if not teachers:
        print('\033[31m老师列表为空！\033[0m')
        return
    for k, name in enumerate(teachers):
        print('%s %s' % (k, admin_api.get_teacher_info(CURRENT_USER, name)))
    print('-' * 30)

@common.auth(ROLE)
def check_course():
    print('\033[32m查看课程\033[0m')
    course = common.get_object_list('course')
    print('-' * 30)
    if not course:
        print('\033[31m课程列表为空！\033[0m')
        return
    for k, name in enumerate(course):
        print('%s %s' % (k, admin_api.get_course_info(CURRENT_USER, name)))
    print('-' * 30)

@common.auth(ROLE)
def create_school():
    print('\033[32m创建学校\033[0m')
    while True:
        name = input('请输入学习名称 >>: ').strip()
        if name == 'q': break
        address = input('请输入学校地址 >>: ').strip()
        flag, msg = admin_api.create_school(CURRENT_USER, name, address)
        if flag:
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

@common.auth(ROLE)
def create_teacher():
    print('\033[32m创建老师\033[0m')
    while True:
        name = input('请输入老师名字 >>: ').strip()
        if name == 'q': break
        flag, msg = admin_api.create_teacher(CURRENT_USER, name)
        if flag:
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)


def choose_school():
    schools = common.get_object_list('school')
    while True:
        print('-' * 30)
        for k,v in enumerate(schools):
            print('%-4s %-10s' % (k, v))
        print('-' * 30)
        choice = input('请为课程选择校区编号 >>: ').strip()
        if choice == 'q':
            return choice
        if not choice.isdigit():
            print('\033[31m学校编号必须是数字！\033[0m')
            continue
        choice = int(choice)
        if choice < 0 or choice > len(schools):
            print('\033[31m学校编号非法！\033[0m')
            continue
        return schools[choice]

@common.auth(ROLE)
def create_course():
    print('\033[32m创建课程\033[0m')
    while True:
        school_name = choose_school()
        if school_name == 'q': break
        name = input('请输入课程名称 >>: ').strip()
        price = input('请输入课程价格 >>: ').strip()
        cycle = input('请输入课程周期 >>: ').strip()
        flag, msg = admin_api.create_course(CURRENT_USER, name, price, cycle, school_name)
        if flag:
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

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
            print('%-4s %-10s' % (k, v[1]))
        print('=' * 30)
        choice = input('请选择操作编号 >>: ').strip()
        if choice == 'q': break
        if choice not in menu:
            print('\033[31m选择编号非法！\033[0m')
            continue
        menu[choice][0]()


