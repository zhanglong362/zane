# -*- encoding: utf-8 -*-

from interface import education

CURRENT_USER = None

def register():
    print('注册')
    while True:
        name = input('用户名 >>: ').strip()
        admins = education.Manager.get_object('admin')
        if name in admins:
            print('管理员%s已经注册！' % name)
            return
        password = input('密码 >>: ')
        password2 = input('确认密码 >>: ')
        if password != password2:
            print('两次密码输入不一致！')
            continue
        obj = education.Manager(name, password)
        education.Manager.update_object('admin', '管理员', obj)
        print('管理员%s注册成功！' % name)
        return

def login():
    global CURRENT_USER
    while True:
        name = input('用户名 >>: ').strip()
        admins = education.Manager.get_object('admin')
        if name not in admins:
            print('管理员%s未注册！' % name)
            return
        password = input('密码 >>: ')
        if password != admins[name].password:
            print('密码错误！')
            continue
        CURRENT_USER = name
        print('管理员%s登陆成功！' % name)
        return

def create_teacher():
    print('创建老师')
    while True:
        name = input('用户名 >>: ').strip()
        password = input('密码 >>: ')
        password2 = input('确认密码 >>: ')
        if password != password2:
            print('两次密码输入不一致！')
            continue
        obj = education.Teacher(name, password)
        schools = education.Manager.get_object('schools')
        while True:
            for name in schools:
                print('学校: %s' % name)
            choice = input('请为老师选择学校 >>: ').strip()
            if choice not in schools:
                print('学校不存在！')
                continue
            obj.school = schools[choice]
            break
        education.Manager.update_object('teachers', '老师', obj)
        return

def create_course():
    print('创建课程')
    name = input('课程名称 >>: ').strip()
    price = input('课程价格 >>: ').strip()
    cycle = input('课程周期 >>: ').strip()
    obj = education.Course(name, price, cycle)
    education.Manager.update_object('course', '课程', obj)

def create_classes():
    print('创建班级')
    name = input('班级名称 >>: ').strip()
    obj = education.Classes(name)
    schools = education.Manager.get_object('schools')
    while True:
        for name in schools:
            print('学校：%s' % name)
        choice = input('请为班级选择学校 >>: ').strip()
        if choice not in schools:
            print('学校不存在！')
            continue
        obj.school = schools[choice]
        break
    course = education.Manager.get_object('course')
    while True:
        for name in course:
            print('课程：%s' % name)
        choice = input('请为班级选择课程 >>: ').strip()
        if choice not in course:
            print('课程不存在！')
            continue
        obj.course = course[choice]
        break
    teachers = education.Manager.get_object('teachers')
    while True:
        for name in teachers:
            print('老师：%s' % name)
        choice = input('请为班级选择老师 >>: ').strip()
        if choice not in teachers:
            print('老师不存在！')
            continue
        obj.teacher = teachers[choice]
        teachers[choice].classes = name
        education.Manager.update_object('teachers', '老师', teachers[choice])
        break
    education.Manager.update_object('classes', '班级', obj)
    return

def check_object(type_name, desc):
    print('查看%s' % desc)
    objects = education.Manager.get_object(type_name)
    if not objects:
        print('目前还没有%s！' % desc)
        return
    for name in objects:
        print('%s: %s' % (desc, name))

def check_school():
    check_object('schools', '学校')

def check_course():
    check_object('course', '课程')

def check_teacher():
    check_object('teachers', '老师')

def check_classes():
    check_object('classes', '班级')

def create_school():
    print('创建学校')
    name = input('学校名称 >>: ').strip()
    address = input('地址 >>: ').strip()
    obj = education.School(name, address)
    education.Manager.update_object('schools', '学校', obj)

def initialize_db():
    confirm = input('确定要初始化数据库吗?(y/n)').strip()
    if confirm == 'y':
        education.Manager.initialize_db()
        print('管理%s初始化数据库成功！' % CURRENT_USER)
    else:
        print('管理%s已取消初始化数据库！' % CURRENT_USER)

def run():
    while True:
        menu = {
            '0': [login, '登陆'],
            '1': [register, '注册'],
            '2': [check_school, '查看学校'],
            '3': [check_course, '课程'],
            '4': [check_teacher, '老师'],
            '5': [check_classes, '班级'],
            '6': [create_school, '创建学校'],
            '7': [create_course, '创建课程'],
            '8': [create_teacher, '创建老师'],
            '9': [create_classes, '创建班级'],
            '10': [initialize_db, '初始化数据库'],
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
