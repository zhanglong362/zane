# -*- encoding: utf-8 -*-

from lib import common
from interface import admin_api


CURRENT_USER = None
ROLE = 'admin'


def login():
    global CURRENT_USER
    common.show_green('登陆')
    if CURRENT_USER:
        common.show_red('用户不能重复登录！')
        return
    while True:
        name = common.input_string('用户名')
        if name == 'q': break
        password = common.input_string('密码')
        if password == 'q': break
        flag, msg = admin_api.login(name, password)
        if not flag:
            common.show_red(msg)
            continue
        CURRENT_USER = name
        common.show_green(msg)
        return


def register():
    common.show_green('注册')
    if CURRENT_USER:
        common.show_red('已登录，不能注册！')
        return
    while True:
        name = common.input_string('注册用户名')
        if name == 'q': break
        password = common.input_string('注册密码')
        if password == 'q': break
        password2 = common.input_string('确认密码')
        if password2 == 'q': break
        if password != password2:
            common.show_red('两次密码出入不一致！')
            continue
        flag, msg = admin_api.register(name, password)
        if not flag:
            common.show_red(msg)
            continue
        common.show_green(msg)
        return

@common.login_auth(ROLE)
def check_all_school():
    common.show_green('查看所有学校')
    common.show_object_list(type_name='school')

@common.login_auth(ROLE)
def check_all_teacher():
    common.show_green('查看所有老师')
    common.show_object_list(type_name='teacher')

@common.login_auth(ROLE)
def check_all_course():
    common.show_green('查看所有课程')
    common.show_object_list(type_name='course')

@common.login_auth(ROLE)
def create_school():
    common.show_green('创建学校')
    while True:
        name = common.input_string('学校名称')
        if name == 'q': break
        address = common.input_string('学校地址')
        if address == 'q': break
        flag, msg = admin_api.create_school(CURRENT_USER, name, address)
        if not flag:
            common.show_red(msg)
            continue
        common.show_green(msg)
        return

@common.login_auth(ROLE)
def create_teacher():
    common.show_green('创建老师')
    while True:
        name = common.input_string('老师名字')
        if name == 'q': break
        flag, msg = admin_api.create_teacher(CURRENT_USER, name)
        if not flag:
            common.show_red(msg)
            continue
        common.show_green(msg)
        return

@common.login_auth(ROLE)
def create_course():
    common.show_green('创建课程')
    while True:
        school_name = common.get_object_name(type_name='school')
        if not school_name:
            return
        name = common.input_string('课程名称')
        if name == 'q': break
        price = common.input_string('课程价格')
        if price == 'q': break
        cycle = common.input_string('课程周期')
        if cycle == 'q': break
        flag, msg = admin_api.create_course(CURRENT_USER, name, price, cycle, school_name)
        if not flag:
            common.show_red(msg)
            continue
        common.show_green(msg)
        return

def logout():
    global CURRENT_USER
    common.show_green('登出')
    common.show_red('用户%s登出！' % CURRENT_USER)
    CURRENT_USER = None

def run():
    menu = {
        '1': [login, '登陆'],
        '2': [register, '注册'],
        '3': [check_all_school, '查看所有学校'],
        '4': [check_all_teacher, '查看所有老师'],
        '5': [check_all_course, '查看所有课程'],
        '6': [create_school, '创建学校'],
        '7': [create_teacher, '创建老师'],
        '8': [create_course, '创建课程']
    }
    while True:
        common.show_green('按"q"退出视图')
        common.show_menu(menu)
        choice = common.input_string('请选择操作编号')
        if choice == 'q':
            if CURRENT_USER:
                logout()
            return
        if choice not in menu:
            common.show_red('选择编号非法！')
            continue
        menu[choice][0]()




