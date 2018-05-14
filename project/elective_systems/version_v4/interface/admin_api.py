# -*- encoding: utf-8 -*-

from lib import common
from db import modules

logger = common.get_logger('admin_api')

def login(name, password):
    admin = modules.Admin.get_obj_by_name(name)
    if not admin:
        return False, '管理员%s不存在！' % name
    if password == admin.password:
        return True, '管理员%s登陆成功！' % name
    else:
        return False, '管理员%s密码错误！' % name

def register(name, password):
    admin = modules.Admin.get_obj_by_name(name)
    if admin:
        return False, '管理员%s已存在！' % name
    modules.Admin(name, password)
    if modules.Admin.get_obj_by_name(name):
        return True, '管理员%s注册成功！' % name
    else:
        return False, '管理员%s注册失败！' % name

def create_school(admin_name, name, address):
    school = modules.School.get_obj_by_name(name)
    if school:
        return False, '学校%s已经存在！' % name
    admin = modules.Admin.get_obj_by_name(admin_name)
    if admin.create_school(name, address):
        return True, '管理员%s创建学校%s成功！' % (admin_name, name)
    else:
        return False, '管理员%s创建学校%s失败！' % (admin_name, name)

def get_school_info(obj_name):
    return modules.School.get_obj_by_name(obj_name)

def get_teacher_info(obj_name):
    return modules.Teacher.get_obj_by_name(obj_name)

def get_course_info(obj_name):
    return modules.Course.get_obj_by_name(obj_name)

def create_teacher(admin_name, name, password='123'):
    teacher = modules.Teacher.get_obj_by_name(name)
    if teacher:
        return False, '老师%s已经存在！' % name
    admin = modules.Admin.get_obj_by_name(admin_name)
    if admin.create_teacher(name, password):
        return True, '管理员%s创建老师%s成功！' % (admin_name, name)
    else:
        return False, '管理员%s创建老师%s失败！' % (admin_name, name)

def create_course(admin_name, name, price, cycle, school_name):
    course = modules.Course.get_obj_by_name(name)
    if course:
        return False, '课程%s已经存在！' % name
    admin = modules.Admin.get_obj_by_name(admin_name)
    if admin.create_course(name, price, cycle, school_name):
        return True, '管理员%s创建课程%s成功！' % (admin_name, name)
    else:
        return False, '管理员%s创建课程%s失败！' % (admin_name, name)








