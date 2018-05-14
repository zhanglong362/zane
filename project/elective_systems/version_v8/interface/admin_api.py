# -*- encoding: utf-8 -*-

from db import modules

def register(name, password):
    admin = modules.Admin.get_obj_by_name(name)
    if admin:
        return False, '用户%s不能重复注册！' % name
    if modules.Admin.register(name, password):
        return True, '用户%s注册成功！' % name
    else:
        return False, '用户%s注册失败！' % name

def create_school(admin_name, name, address):
    school = modules.School.get_obj_by_name(name)
    if school:
        return False, '学校%s已存在！' % name
    admin = modules.Admin.get_obj_by_name(admin_name)
    if admin.create_school(name, address):
        return True, '学校%s创建成功！' % name
    else:
        return False, '学校%s创建失败！' % name

def create_teacher(admin_name, name, password='123'):
    teacher = modules.Teacher.get_obj_by_name(name)
    if teacher:
        return False, '老师%s已存在！' % name
    admin = modules.Admin.get_obj_by_name(admin_name)
    if admin.create_teacher(name, password):
        return True, '老师%s创建成功！' % name
    else:
        return False, '老师%s创建失败！' % name

def create_course(admin_name, name, price, cycle, school_name):
    course = modules.School.get_obj_by_name(name)
    if course:
        return False, '课程%s已存在！' % name
    admin = modules.Admin.get_obj_by_name(admin_name)
    if admin.create_course(name, price, cycle, school_name):
        return True, '课程%s创建成功！' % name
    else:
        return False, '课程%s创建失败！' % name


