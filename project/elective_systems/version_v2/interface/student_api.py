# -*- encoding: utf-8 -*-

from lib import common

logger = common.get_logger('student')

def login():
    print('\033[32m登陆\033[0m')

def register():
    print('\033[32m注册\033[0m')

def choose_school():
    print('\033[32m选择校区\033[0m')

def choose_course():
    print('\033[32m选择课程\033[0m')

def check_score():
    print('\033[32m查看成绩\033[0m')

