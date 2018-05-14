# -*- encoding: utf-8 -*-

from lib import common

logger = common.get_logger('student')
USER = {'name': None}
ROLE = 'student'

def login():
    print('\033[32m登陆\033[0m')
    while True:
        name = input('用户名').strip()
        pwd = input('密码').strip()
        flag, msg = common_api.login(name, pwd, ROLE)
        print(msg)
        if flag:
            USER['name'] = name
            return


def register():
    print('\033[32m注册\033[0m')

@common.auth(USER['name'], ROLE)
def choose_school():
    print('\033[32m选择校区\033[0m')

@common.auth(USER['name'], ROLE)
def choose_course():
    print('\033[32m选择课程\033[0m')

@common.auth(USER['name'], ROLE)
def check_score():
    print('\033[32m查看成绩\033[0m')


def run():
    menu = {
        '1': [login, '登陆'],
        '2': [register, '注册'],
        '3': [choose_school, '选择校区'],
        '4': [choose_course, '选择课程'],
        '5': [check_score, '查看成绩'],
    }
    while True:
        print('=' * 30)
        for k, v in menu.items():
            print('%-4s %-10s' % (k, v[1]))
        print('=' * 30)
        choice = input('请选择操作编号[q to exit] >>: ').strip()
        if choice == 'q':
            print('\033[31mLogout Success! Goodbye!\033[0m')
            break
        if choice not in menu:
            print('\033[31m选择编号非法！\033[0m')
            continue
        try:
            menu[choice][0]()
        except Exception as e:
            print('\033[31merror from student: %s\033[0m' % e)