# -*- encoding: utf-8 -*-

from db import modules

def login(name, password):
    student = modules.Student.get_obj_by_name(name)
    if not student:
        return False, '用户%s不存在！' % name
    if password != student.password:
        return False, '密码错误！'
    return True, '用户%s登陆成功！' % name

def register(name, password):
    student = modules.Student.get_obj_by_name(name)
    if student:
        return False, '不能重复注册！'
    if not modules.Student.register(name, password):
        return False, '用户%s注册失败！' % name
    return True, '用户%s注册成功！' % name


def get_student_course(name):
    student = modules.Student.get_obj_by_name(name)
    return student.course_list

def get_student_score(name):
    student = modules.Student.get_obj_by_name(name)
    return student.score

def get_school_name(course_name):
    course = modules.Course.get_obj_by_name(course_name)
    return course.school_name

def add_course_student(student_name, course_name):
    course = modules.Course.get_obj_by_name(course_name)
    if not course.add_course_student(student_name):
        return False, '学生%s加入课程班级%s失败！' % (student_name, course_name)
    return True, '学生%s加入课程班级%s成功！' % (student_name, course_name)

def choose_student_course(student_name, course_name, school_name):
    student = modules.Student.get_obj_by_name(student_name)
    if not student.set_student_course(course_name, school_name):
        return False, '学生%s选择课程失败！' % student_name
    return True, '学生%s选择课程成功！' % student_name



