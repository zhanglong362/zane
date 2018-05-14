# -*- encoding: utf-8 -*-

from db import modules

def register(name, password):
    student = modules.Student.get_obj_by_name(name)
    if student:
        return False, '学生%s不能重复注册！' % name
    if modules.Student.register(name, password):
        return True, '学生%s注册成功！' % name
    else:
        return False, '学生%s注册失败！' % name

def get_score(name):
    student = modules.Student.get_obj_by_name(name)
    return student.score

def get_learn_course(name):
    student = modules.Student.get_obj_by_name(name)
    return student.course_list

def choose_course(name, course):
    student = modules.Student.get_obj_by_name(name)
    if course in student.course_list:
        return False, '学生%s不能选择已学习的课程！' % name
    if student.choose_course(course):
        return True, '学生%s选择课程%s成功！' % (name, course)
    else:
        return False, '学生%s选择课程%s失败！' % (name, course)



