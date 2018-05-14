# -*- encoding: utf-8 -*-

from lib import common
from db import modules


def login(name, password):
    admin = modules.Admin.get_obj_by_name(name)
    if not admin:
        return False, '用户%s不存在！' % name
    if password != admin.password:
        return False, '密码错误！'
    return True, '用户%s登陆成功！' % name

def register(name, password):
    admin = modules.Admin.get_obj_by_name(name)
    if admin:
        return False, '不能重复注册！'
    if not modules.Admin.register(name, password):
        return False, '用户%s注册失败！' % name
    return True, '用户%s注册成功！' % name

def create_school(admin_name, name, address):
    school = modules.School.get_obj_by_name(name)
    if school:
        return False, '学校%s已经存在！' % name
    admin = modules.Admin.get_obj_by_name(admin_name)
    if not admin.create_school(name, address):
        return False, '%s创建学校%s失败！' % (admin_name, name)
    return True, '%s创建学校%s成功！' % (admin_name, name)

def create_teacher(admin_name, name, password='123'):
    teacher = modules.Teacher.get_obj_by_name(name)
    if teacher:
        return False, '老师%s已经存在！' % name
    admin = modules.Admin.get_obj_by_name(admin_name)
    if not admin.create_teacher(name, password):
        return False, '%s创建老师%s失败！' % (admin_name, name)
    return True, '%s创建老师%s成功！' % (admin_name, name)

def create_course(admin_name, name, price, cycle, school_name):
    course = modules.Course.get_obj_by_name(name)
    if course:
        return False, '课程%s已经存在！' % name
    admin = modules.Admin.get_obj_by_name(admin_name)
    if not admin.create_course(name, price, cycle, school_name):
        return False, '%s创建课程%s失败！' % (admin_name, name)
    return True, '%s创建课程%s成功！' % (admin_name, name)




