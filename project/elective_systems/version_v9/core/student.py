# -*- encoding: utf-8 -*-

from lib import common
from interface import student_api

CURRENT_USER = None
ROLE = 'student'


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
        flag, msg = student_api.login(name, password)
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
        flag, msg = student_api.register(name, password)
        if not flag:
            common.show_red(msg)
            continue
        common.show_green(msg)
        return

@common.login_auth(ROLE)
def check_student_course():
    common.show_green('查看学生课程')
    student_course = student_api.get_student_course(CURRENT_USER)
    if not student_course:
        common.show_red('学生课程列表为空！')
        return
    common.show_info(*student_course)

@common.login_auth(ROLE)
def check_student_score():
    common.show_green('查看学生成绩')
    student_score = student_api.get_student_score(CURRENT_USER)
    if not student_score:
        common.show_red('学生成绩为空！')
        return
    common.show_info(**student_score)

def add_course_student(course_name):
    flag, msg = student_api.add_course_student(CURRENT_USER, course_name)
    if not flag:
        common.show_red(msg)
    common.show_green(msg)
    return flag

@common.login_auth(ROLE)
def choose_student_course():
    common.show_green('选择课程')
    while True:
        course_name = common.get_object_name(type_name='course')
        school_name = student_api.get_school_name(course_name)
        if not add_course_student(course_name):
            return
        flag, msg = student_api.choose_student_course(CURRENT_USER, course_name, school_name)
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
        '3': [check_student_course, '查看学生课程'],
        '4': [check_student_score, '查看学生成绩'],
        '5': [choose_student_course, '选择学生课程']
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
