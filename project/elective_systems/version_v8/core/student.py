# -*- encoding: utf-8 -*-

from lib import common
from interface import common_api, student_api

CURRENT_USER = None
ROLE = 'student'

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
        flag, msg = student_api.register(name, password)
        if flag:
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

@common.auth(ROLE)
def check_score():
    print('\033[32m查看成绩\033[0m')
    score = student_api.get_score(CURRENT_USER)
    if not score:
        print('\033[31m学生%s没有成绩信息！\033[0m' % CURRENT_USER)
        return
    print('-' * 30)
    for k,v in score.items():
        print('课程：%s 成绩：%s' % (k, v))
    print('-' * 30)

@common.auth(ROLE)
def check_learn_course(show=True):
    if show:
        print('\033[32m查看个人课程\033[0m')
    course = student_api.get_learn_course(CURRENT_USER)
    if not course:
        print('\033[31m学生%s没有课程信息！\033[0m' % CURRENT_USER)
        return
    print('-' * 30)
    for k, name in enumerate(course):
        print('%-4s %-10s' % (k, name))
    print('-' * 30)
    return course

@common.auth(ROLE)
def check_course(show=True):
    if show:
        print('\033[32m查看所有课程\033[0m')
    course_list = common.get_object_list('course')
    if not course_list:
        print('\033[31m课程列表为空！\033[0m')
        return
    print('-' * 30)
    for k, v in enumerate(course_list):
        print('%s %s' % (k, v))
    return course_list

@common.auth(ROLE)
def choose_course():
    print('\033[32m选择课程\033[0m')
    while True:
        course = check_course(False)
        if not course:
            return
        choice = common.input_integer('请选择课程编号')
        if choice == 'q':
            break
        if choice < 0 or choice > len(course):
            print('\033[31m课程编号非法！\033[0m')
            continue
        flag, msg = student_api.choose_course(CURRENT_USER, course[choice])
        if flag:
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

def run():
    menu = {
        '1': [login, '登陆'],
        '2': [register, '注册'],
        '3': [check_course, '查看所有课程'],
        '4': [check_learn_course, '查看个人课程'],
        '5': [choose_course, '选择课程'],
        '6': [check_score, '查看成绩']
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