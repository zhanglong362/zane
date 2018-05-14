# -*- coding: utf-8 -*-

from interface import education


CURRENT_USER = None

def login():
    global CURRENT_USER
    while True:
        name = input('用户名 >>: ').strip()
        teachers = education.Teacher.get_object('teachers')
        if name not in teachers:
            print('老师%s未注册！' % name)
            return
        password = input('密码 >>: ')
        if password != teachers[name].password:
            print('密码错误！')
            continue
        CURRENT_USER = name
        print('老师%s登陆成功！' % name)
        return

def list_students():
    teachers = education.Teacher.get_object('teachers')
    classes = education.Teacher.get_object('classes')
    if classes[teachers[CURRENT_USER].classes]:
        student_list = []
        for name in classes[teachers[CURRENT_USER].classes].students:
            student_list.append(name)
        print('学生：%s' % student_list)
    else:
        print('班级%s没有学生！' % teachers[CURRENT_USER].classes)

def modify_student_score():
    while True:
        name = input('请输入学生的名字 >>: ').strip()
        students = education.Teacher.get_object('students')
        if name not in students:
            print('学生%s不存在！' % name)
            continue
        score = input('请输入学生的成绩 >>: ').strip()
        if not score.isdigit():
            print('成绩必须是数字！')
            continue
        score = float(score)
        students[name].score = score
        education.Manager.update_object('students', '学生', students[name])
        return

def run():
    while True:
        menu = {
            '1': [login, '登陆'],
            '2': [list_students, '查看学员列表'],
            '3': [modify_student_score, '修改学员成绩']
        }
        for k, v in menu.items():
            print('%-4s %-10s' % (k, v[1]))
        choice = input('请选择操作编号 >>: ').strip()
        if choice == 'quit':
            break
        if choice not in menu:
            print('选择编号非法！')
            continue
        menu[choice][0]()


