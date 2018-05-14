# -*- encoding: utf-8 -*-

USER = {'name': None}
ROLE = 'admin'


def login():
    print('\033[32m\033[0m')


def register():
    print('\033[32m\033[0m')


def create_school():
    print('\033[32m\033[0m')


def create_teacher():
    print('\033[32m\033[0m')


def create_course():
    print('\033[32m\033[0m')


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
        if choice == 'q':
            break
        if choice not in menu:
            print('\033[31m选择编号非法！\033[0m')
            continue
        menu[choice][0]()
