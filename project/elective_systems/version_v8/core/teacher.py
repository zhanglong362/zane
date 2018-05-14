# -*- encoding: utf-8 -*-

from lib import common
from interface import common_api, teacher_api

CURRENT_USER = None
ROLE = 'teacher'

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
def check_teach_course(show=True):
    if show:
        print('\033[32m查看教授课程\033[0m')
    course = teacher_api.get_teach_course(CURRENT_USER)
    if not course:
        print('\033[31m老师教授课程列表为空！\033[0m')
        return
    print('-' * 30)
    for i, name in enumerate(course):
        print('%-4s %-10s' % (i, name))
    print('-' * 30)
    return course

@common.auth(ROLE)
def choose_teach_course():
    print('\033[32m选择教授课程\033[0m')
    while True:
        course = check_course(False)
        choice = common.input_integer('请选择课程编号')
        if choice < 0 or choice > len(course):
            print('\033[31m课程编号非法！\033[0m')
            continue
        flag, msg = teacher_api.choose_teach_course(CURRENT_USER, course[choice])
        if flag:
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

@common.auth(ROLE)
def check_course_student():
    print('\033[32m查看课程学员\033[0m')
    while True:
        course = check_teach_course(False)
        if not course:
            return
        print('-' * 30)
        choice = common.input_integer('请选择课程编号')
        if choice < 0 or choice > len(course):
            print('\033[31m课程编号非法！\033[0m')
            continue
        student_list = teacher_api.get_course_student(course[choice])
        if not student_list:
            print('\033[31m课程学员列表为空！\033[0m')
            return
        print('-' * 30)
        for i, name in enumerate(student_list):
            print('%-4s %-10s' % (i, name))
        print('-' * 30)
        return

def choose_student_course(name):
    while True:
        flag, course_list = teacher_api.get_student_course(name)
        if not flag:
            print('\033[31m%s\033[0m' % course_list)
            return
        print('-' * 30)
        for i, name in enumerate(course_list):
            print('%-4s %-10s' % (i, name))
        print('-' * 30)
        choice = common.input_integer('请选择课程编号')
        if choice < 0 or choice > len(course):
            print('\033[31m课程编号非法！\033[0m')
            continue
        return course_list[choice]

@common.auth(ROLE)
def change_student_score():
    print('\033[32m修改学员成绩\033[0m')
    while True:
        name = common.input_string('请输入学生名字')
        course = choose_student_course(name)
        if not course:
            continue
        score = common.input_string('请输入学生分数')
        flag, msg = teacher_api.change_student_score(CURRENT_USER, name, course, score)
        if flag:
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

def run():
    menu = {
        '1': [login, '登陆'],
        '2': [check_course, '查看所有课程'],
        '3': [check_teach_course, '查看教授课程'],
        '4': [choose_teach_course, '选择教授课程'],
        '5': [check_course_student, '查看课程学员'],
        '6': [change_student_score, '修改学生成绩'],
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