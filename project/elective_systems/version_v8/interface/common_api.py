# -*- encoding: utf-8 -*-

from db import modules

def login(name, password, role):
    if role == 'admin':
        obj = modules.Admin.get_obj_by_name(name)
    elif role == 'teacher':
        obj = modules.Teacher.get_obj_by_name(name)
    elif role == 'student':
        obj = modules.Student.get_obj_by_name(name)
    else:
        return False, '用户角色%s非法！' % role
    if not obj:
        return False, '用户%s不存在！' % name
    if password == obj.password:
        return True, '用户%s登陆成功！！' % name
    else:
        return False, '用户%s登陆失败！！' % name

def get_school_info(type_name):
    return modules.School.get_obj_by_name(type_name)

def get_teacher_info(type_name):
    return modules.Teacher.get_obj_by_name(type_name)

def get_course_info(type_name):
    return modules.Course.get_obj_by_name(type_name)






