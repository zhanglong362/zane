# -*- encoding: utf-8 -*-

from lib import common
from interface import common_api, admin_api

CURRENT_USER = None
ROLE = 'admin'

def login():
    global CURRENT_USER
    print('\033[32m登陆\033[0m')
    if CURRENT_USER:
        print('\033[31m不能重复登录！\033[0m')
        return
    while True:
        name = common.input_string('登陆用户名')
        if name == 'q':
            break
        password = common.input_string('登陆密码')
        if password == 'q':
            break
        flag, msg = common_api.login(name, password, ROLE)
        if flag:
            CURRENT_USER = name
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

def logout():
    global CURRENT_USER
    print('\033[31mGoodbye, %s!\033[0m' % CURRENT_USER)
    CURRENT_USER = None

def register():
    print('\033[32m注册\033[0m')
    while True:
        name = common.input_string('注册用户名')
        if name == 'q':
            break
        password = common.input_string('注册密码')
        if password == 'q':
            break
        password2 = common.input_string('确认密码')
        if password2 == 'q':
            break
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
def check_school(show=True):
    if show:
        print('\033[32m查看学校\033[0m')
    school_list = common.get_object_list('school')
    if not school_list:
        print('\033[31m学校列表为空！\033[0m')
        return
    print('-' * 30)
    for k,v in enumerate(school_list):
        print('%s %s' % (k, v))
    return school_list

@common.auth(ROLE)
def check_teacher():
    print('\033[32m查看老师\033[0m')
    teacher_list = common.get_object_list('teacher')
    if not teacher_list:
        print('\033[31m老师列表为空！\033[0m')
        return
    print('-' * 30)
    for k, v in enumerate(teacher_list):
        print('%s %s' % (k, v))

@common.auth(ROLE)
def check_course():
    print('\033[32m查看课程\033[0m')
    course_list = common.get_object_list('course')
    if not course_list:
        print('\033[31m课程列表为空！\033[0m')
        return
    print('-' * 30)
    for k, v in enumerate(course_list):
        print('%s %s' % (k, v))

@common.auth(ROLE)
def create_school():
    print('\033[32m创建学校\033[0m')
    while True:
        name = common.input_string('学校名称')
        if name == 'q':
            break
        address = common.input_string('学校地址')
        if address == 'q':
            break
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
        name = common.input_string('老师名字')
        if name == 'q':
            break
        flag, msg = admin_api.create_teacher(CURRENT_USER, name)
        if flag:
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

def choose_school():
    while True:
        school_list = check_school(False)
        if not school_list:
            return
        choice = common.input_integer('请为课程选择学校')
        if choice == 'q':
            return choice
        if choice < 0 or choice > len(school_list):
            print('\033[31m学校编号非法！\033[0m')
            continue
        choice = int(choice)
        return school_list[choice]

@common.auth(ROLE)
def create_course():
    print('\033[32m创建课程\033[0m')
    while True:
        school_name = choose_school()
        if not school_name:
            return
        name = common.input_string('课程名称')
        if name == 'q':
            break
        price = common.input_string('课程价格')
        if price == 'q':
            break
        cycle = common.input_string('课程周期')
        if cycle == 'q':
            break
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
        for k, v in menu.items():
            print('%-4s %-10s' % (k, v[1]))
        print('=' * 30)
        choice = common.input_string('请选择操作编号')
        if choice == 'q':
            if CURRENT_USER:
                logout()
            return
        if choice not in menu:
            print('\033[31m选择编号非法！\033[0m')
            continue
        menu[choice][0]()