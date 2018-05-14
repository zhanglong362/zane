#-*- encoding: utf-8 -*-

from lib import common
from db import modules

logger = common.get_logger('admin_api')


def login(name, password):
    admin = modules.Admin.get_obj_by_name(name)
    if not admin:
        return False, '管理员%s登陆失败！' % name
    if password == admin.password:
        logger.info('管理员%s登陆成功！' % name)
        return True, '管理员%s登陆成功！' % name
    else:
        logger.warning('管理员%s密码错误！' % name)
        return False, '管理员%s密码错误！' % name

def register(name, password):
    admin = modules.Admin.get_obj_by_name(name)
    if admin:
        return False, '管理员%s不能重复注册！' % name
    admin = modules.Admin.register(name, password)
    if admin:
        logger.info('管理员%s注册成功！' % name)
        return True, '管理员%s注册成功！' % name
    else:
        logger.warning('管理员%s注册失败！' % name)
        return False, '管理员%s注册失败！' % name

def create_school(admin_name, name, address):
    if modules.School.get_obj_by_name(name):
        return False, '学校%s已存在！' % name
    admin = modules.Admin.get_obj_by_name(admin_name)
    if admin.create_school(name, address):
        logger.info('管理员 %s 创建学校%s成功！' % (admin_name, name))
        return True, '管理员 %s 创建学校%s成功！' % (admin_name, name)
    else:
        logger.warning('管理员 %s 创建学校%s失败！' % (admin_name, name))
        return False, '管理员 %s 创建学校%s失败！' % (admin_name, name)

def create_teacher(admin_name, name, password='123'):
    if modules.Teacher.get_obj_by_name(name):
        return False, '老师%s已存在！' % name
    admin = modules.Admin.get_obj_by_name(admin_name)
    if admin.create_teacher(name, password):
        logger.info('管理员 %s 创建老师 %s 成功！' % (admin_name, name))
        return True, '管理员 %s 创建老师 %s 成功！' % (admin_name, name)
    else:
        logger.warning('管理员 %s 创建老师 %s 失败！' % (admin_name, name))
        return False, '管理员 %s 创建老师 %s 失败！' % (admin_name, name)

def create_course(admin_name, name, price, cycle, school_name):
    if modules.Course.get_obj_by_name(name):
        return False, '课程%s已存在！' % name
    admin = modules.Admin.get_obj_by_name(admin_name)
    if admin.create_course(name, price, cycle, school_name):
        logger.info('管理员%s 创建课程%s成功！' % (admin_name, name))
        return True, '管理员%s 创建课程%s成功！' % (admin_name, name)
    else:
        logger.warning('管理员%s 创建课程%s失败！' % (admin_name, name))
        return False, '管理员%s 创建课程%s失败！' % (admin_name, name)

def get_school_info(admin_name, obj_name):
    logger.info('管理员 %s 获取学校%s信息！' % (admin_name, obj_name))
    return modules.School.get_obj_by_name(obj_name)

def get_teacher_info(admin_name, obj_name):
    logger.info('管理员 %s 获取老师%s信息！' % (admin_name, obj_name))
    return modules.Teacher.get_obj_by_name(obj_name)

def get_course_info(admin_name, obj_name):
    logger.info('管理员 %s 获取课程%s信息！' % (admin_name, obj_name))
    return modules.Course.get_obj_by_name(obj_name)

