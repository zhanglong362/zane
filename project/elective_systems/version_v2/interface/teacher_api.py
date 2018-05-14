# -*- encoding: utf-8 -*-

from lib import common

logger = common.get_logger('teacher')

def login():
    print('\033[32m登陆\033[0m')

def register():
    print('\033[32m注册\033[0m')

def check_course():
    print('\033[32m查看教授课程\033[0m')

def choose_course():
    print('\033[32m选择教授课程\033[0m')

def check_students():
    print('\033[32m查看课程学员\033[0m')

def modify_score():
    print('\033[32m修改学员成绩\033[0m')