# -*- coding: utf-8 -*-

from interface import education


CURRENT_USER = None

def register():
    print('注册')
    while True:
        name = input('用户名 >>: ').strip()
        students = education.Student.get_object('students')
        if name in students:
            print('学生%s已经注册！' % name)
            return
        password = input('密码 >>: ')
        password2 = input('确认密码 >>: ')
        if password != password2:
            print('两次密码输入不一致！')
            continue
        obj = education.Student(name, password)
        education.Student.update_object('students', '学生', obj)
        print('学生%s注册成功！' % name)
        return

def login():
    print('登陆')
    global CURRENT_USER
    while True:
        name = input('用户名 >>: ').strip()
        students = education.Student.get_object('students')
        if name not in students:
            print('学生%s未注册！' % name)
            return
        password = input('密码 >>: ')
        if password != students[name].password:
            print('密码错误！')
            continue
        CURRENT_USER = name
        print('学生%s登陆成功！' % name)
        return

def choose_classes():
    print('选择班级')
    students = education.Student.get_object('students')
    classes = education.Student.get_object('classes')
    teachers = education.Student.get_object('teachers')
    while True:
        for name in classes:
            print('班级：%s' % name)
        choice = input('请选择班级 >>: ').strip()
        if choice not in classes:
            print('班级不存在！')
            continue
        students[CURRENT_USER].school = classes[choice].school
        students[CURRENT_USER].classes = classes[choice].name
        students[CURRENT_USER].tuition = classes[choice].course.price
        classes[choice].students[students[CURRENT_USER].name] = students[CURRENT_USER]
        education.Student.update_object('classes', '班级', classes[choice])
        education.Student.update_object('students', '学生', students[CURRENT_USER])
        return

def pay_tuition():
    print('交费')
    while True:
        students = education.Student.get_object('students')
        print('学生%s应缴学费%s元！' % (CURRENT_USER, students[CURRENT_USER].tuition))
        amount = input('请输入缴费金额 >>:').strip()
        if not amount.isdigit():
            print('金额必须是数字！')
            continue
        students[CURRENT_USER].tuition -= amount
        education.Student.update_object('students', '学生', obj)
        return

def run():
    while True:
        menu = {
            '1': [login, '登陆'],
            '2': [register, '注册'],
            '3': [choose_classes, '选择班级'],
            '4': [pay_tuition, '交费']
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
