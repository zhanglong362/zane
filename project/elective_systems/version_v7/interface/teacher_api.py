# -*- encoding: utf-8 -*-

from lib import common
from db import modules

logger = common.get_logger('teacher_api')

def login(name, password):
    teacher = modules.Teacher.get_obj_by_name(name)
    if not teacher:
        return False, '老师%s不存在！' % name
    if password == teacher.password:
        logger.info('老师%s登陆成功！' % name)
        return True, '老师%s登陆成功！' % name
    else:
        logger.warning('老师%s登陆失败！' % name)
        return False, '老师%s登陆失败！' % name

def get_teacher_info(name):
    logger.info('老师%s获取个人信息！' % name)
    return modules.Teacher.get_obj_by_name(name)

def get_course_info(name, course):
    logger.info('老师%s获取教授课程%s信息！' % (name, course))
    return modules.Course.get_obj_by_name(course)

