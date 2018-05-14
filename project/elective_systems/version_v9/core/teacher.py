# -*- encoding: utf-8 -*-

from lib import common
from interface import teacher_api


CURRENT_USER = None
ROLE = 'teacher'

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
        flag, msg = teacher_api.login(name, password)
        if not flag:
            common.show_red(msg)
            continue
        CURRENT_USER = name
        common.show_green(msg)
        return

@common.login_auth(ROLE)
def check_teach_course():
    common.show_green('查看教授课程')
    teach_course = teacher_api.get_teach_course(CURRENT_USER)
    if not teach_course:
        common.show_red('老师教授课程列表为空！')
        return
    common.show_info(*teach_course)

@common.login_auth(ROLE)
def check_teach_course_student():
    common.show_green('查看教授课程学生')
    teach_course = teacher_api.get_teach_course(CURRENT_USER)
    if not teach_course:
        common.show_red('老师教授课程列表为空！')
        return
    common.show_info(*teach_course)
    course_name = common.get_object_name(object_list=teach_course)
    teach_course_student = teacher_api.get_teach_course_student(course_name)
    if not teach_course_student:
        common.show_red('教授课程%s学生列表为空！' % course_name)
        return
    common.show_info(*teach_course_student)

@common.login_auth(ROLE)
def choose_teach_course():
    common.show_green('选择教授课程')
    while True:
        teach_course = common.get_object_name(type_name='course')
        flag, msg = teacher_api.choose_teach_course(CURRENT_USER, teach_course)
        if not flag:
            common.show_red(msg)
            continue
        common.show_green(msg)
        return

@common.login_auth(ROLE)
def set_student_score():
    common.show_green('修改学生成绩')
    while True:
        name = common.input_string('学生名字')
        if name == 'q': break
        course = common.input_string('学习课程')
        if course == 'q': break
        score = common.input_integer('课程成绩', is_float=True)
        if score == 'q': break
        flag, msg = teacher_api.set_student_score(CURRENT_USER, name, course, score)
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
        '2': [check_teach_course, '查看教授课程'],
        '3': [check_teach_course_student, '查看教授课程学生'],
        '4': [choose_teach_course, '选择教授课程'],
        '5': [set_student_score, '修改学生成绩']
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








