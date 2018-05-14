# -*- encoding: utf-8 -*-

from db import modules

def get_teach_course(name):
    teacher = modules.Teacher.get_obj_by_name(name)
    return teacher.course_list

def choose_teach_course(name, course):
    teacher = modules.Teacher.get_obj_by_name(name)
    if course in teacher.course_list:
        return False, '老师%s不能选择已教授的课程！' % name
    if teacher.choose_course(course):
        return True, '老师%s选择教授课程%s成功！' % (name, course)
    else:
        return False, '老师%s选择教授课程%s失败！' % (name, course)

def get_course_student(course):
    course = modules.Course.get_obj_by_name(course)
    return course.student_list

def get_student_course(name):
    student = modules.Student.get_obj_by_name(name)
    if not student:
        return False, '学生%s不存在！' % name
    else:
        return True, student.course_list

def change_student_score(teacher, name, course, score):
    student = modules.Student.get_obj_by_name(name)
    if not student:
        return False, '学生%s不存在！' % name
    if student.change_score(course, score):
        return True, '老师%s修改学生%s课程%s分数为%s成功！' % (teacher, name, course, score)
    else:
        return False, '老师%s修改学生%s课程%s分数为%s失败！' % (teacher, name, course, score)





