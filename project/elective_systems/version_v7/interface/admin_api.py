# -*- encoding: utf-8 -*-

from lib import common
from db import modules

logger = common.get_logger('admin_api')

def login(name, password):
    admin = modules.Admin.get_obj_by_name(name)
    if not admin:
        return False, '管理员%s不存在！' % name
    if password == admin.password:
        logger.info('管理员%s登陆成功！' % name)
        return True, '管理员%s登陆成功！' % name
    else:
        logger.warning('管理员%s登陆失败！' % name)
        return False, '管理员%s登陆失败！' % name

def register(name, password):
    admin = modules.Admin.get_obj_by_name(name)
    if admin:
        return False, '管理员%s不能重复注册！' % name
    if modules.Admin.register(name, password):
        logger.info('管理员%s注册成功！' % name)
        return True, '管理员%s注册成功！' % name
    else:
        logger.warning('管理员%s注册失败！' % name)
        return False, '管理员%s注册失败！' % name

def get_school_info(admin_name, name):
    logger.info('管理员%s获取学校%s信息！' % (admin_name, name))
    return modules.School.get_obj_by_name(name)

def get_teacher_info(admin_name, name):
    logger.info('管理员%s获取老师%s信息！' % (admin_name, name))
    return modules.Teacher.get_obj_by_name(name)

def get_course_info(admin_name, name):
    logger.info('管理员%s获取课程%s信息！' % (admin_name, name))
    return modules.Course.get_obj_by_name(name)

def create_school(admin_name, name, address):
    school = modules.School.get_obj_by_name(name)
    if school:
        return False, '学校%s已存在！' % name
    admin = modules.Admin.get_obj_by_name(admin_name)
    if admin.create_school(name, address):
        logger.info('管理员%s创建学校%s成功！' % (admin_name, name))
        return True, '管理员%s创建学校%s成功！' % (admin_name, name)
    else:
        logger.warning('管理员%s创建学校%s失败！' % (admin_name, name))
        return False, '管理员%s创建学校%s失败！' % (admin_name, name)

def create_teacher(admin_name, name, password='123'):
    teacher = modules.Teacher.get_obj_by_name(name)
    if teacher:
        return False, '老师%s已存在！' % name
    admin = modules.Admin.get_obj_by_name(admin_name)
    if admin.create_teacher(name, password):
        logger.info('管理员%s创建老师%s成功！' % (admin_name, name))
        return True, '管理员%s创建老师%s成功！' % (admin_name, name)
    else:
        logger.warning('管理员%s创建老师%s失败！' % (admin_name, name))
        return False, '管理员%s创建老师%s失败！' % (admin_name, name)

def create_course(admin_name, name, price, cycle, school_name):
    course = modules.Course.get_obj_by_name(name)
    if course:
        return False, '课程%s已存在！' % name
    admin = modules.Admin.get_obj_by_name(admin_name)
    if admin.create_course(name, price, cycle, school_name):
        logger.info('管理员%s创建课程%s成功！' % (admin_name, name))
        return True, '管理员%s创建课程%s成功！' % (admin_name, name)
    else:
        logger.warning('管理员%s创建课程%s失败！' % (admin_name, name))
        return False, '管理员%s创建课程%s失败！' % (admin_name, name)

