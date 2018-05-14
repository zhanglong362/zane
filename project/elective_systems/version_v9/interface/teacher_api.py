
from db import modules


def login(name, password):
    teacher = modules.Teacher.get_obj_by_name(name)
    if not teacher:
        return False, '用户%s不存在！' % name
    if password != teacher.password:
        return False, '密码错误！'
    return True, '用户%s登陆成功！' % name

def get_teach_course(teacher_name):
    teacher = modules.Teacher.get_obj_by_name(teacher_name)
    return teacher.course_list


def get_teach_course_student(course_name):
    course = modules.Course.get_obj_by_name(course_name)
    return course.student_list


def choose_teach_course(teacher_name, course_name):
    teacher = modules.Teacher.get_obj_by_name(teacher_name)
    if not teacher.set_up_course(course_name):
        return False, '%s选择教授课程%s失败！' % (teacher_name, course_name)
    return True, '%s选择教授课程%s成功！' % (teacher_name, course_name)


def set_student_score(teacher_name, student_name, course, score):
    student = modules.Student.get_obj_by_name(student_name)
    if not student:
        return False, '学生%s不存在！' % student_name
    if not student.set_student_score(course, score):
        return False, '%s修改学生课程%s成绩失败！' % (teacher_name, student_name)
    return True, '%s修改学生课程%s成绩成功！' % (teacher_name, student_name)