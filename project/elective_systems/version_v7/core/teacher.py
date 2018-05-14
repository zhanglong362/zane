# -*- encoding: utf-8 -*-

from lib import common
from interface import teacher_api

CURRENT_USER = None
ROLE = 'teacher'

def login():
    global CURRENT_USER
    print('\033[32m登陆\033[0m')
    while True:
        name = input('请输入登陆用户名 >>: ').strip()
        if name == 'q': break
        password = input('请输入登陆密码 >>: ').strip()
        flag, msg = teacher_api.login(name, password)
        if flag:
            CURRENT_USER = name
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

@common.auth(ROLE)
def check_course():
    print('\033[32m查看教授课程\033[0m')
    teacher = teacher_api.get_teacher_info(CURRENT_USER)
    print('-' * 30)
    if not teacher.course:
        print('\033[31m教授课程列表为空！\033[0m')
        return
    for k, name in enumerate(teacher.course):
        print('%s %s' % (k, teacher_api.get_course_info(CURRENT_USER, name)))
    print('-' * 30)
    return teacher.course



@common.auth(ROLE)
def check_student():
    print('\033[32m创建课程\033[0m')
    while True:
        course = check_course()
        name = input('请输入课程名字 >>: ').strip()
        if name == 'q': break
        price = input('请输入课程价格 >>: ').strip()
        cycle = input('请输入课程周期 >>: ').strip()
        flag, msg = teacher_api.create_course(CURRENT_USER, name, price, cycle, school_name)
        if flag:
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

@common.auth(ROLE)
def choose_course():
    print('\033[32m选择教授课程\033[0m')
    while True:
        course = common.get_object_list('course')
        print('-' * 30)
        for k,v in enumerate(course):
            print('%s %s' % (k, v))
        print('-' * 30)
        choice = input('请选择教授课程编号 >>: ').strip()
        if choice == 'q':
            return choice
        if not choice.isdigit():
            print('\033[31m课程编号必须是数字！\033[0m')
            continue
        choice = int(choice)
        if choice < 0 or choice > len(course):
            print('\033[31m课程编号非法！\033[0m')
            continue
        flag, msg = teacher_api.choose_course(CURRENT_USER, course[choice])
        if flag:
            print('\033[32m%s\033[0m' % msg)
            return
        else:
            print('\033[31m%s\033[0m' % msg)

@common.auth(ROLE)
def modify_score():
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

def run():
    menu = {
        '1': [login, '查看'],
        '2': [check_course, '查看教授课程'],
        '3': [check_student, '查看学员列表'],
        '4': [choose_course, '选择教授课程'],
        '5': [modify_score, '修改学生成绩']
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

