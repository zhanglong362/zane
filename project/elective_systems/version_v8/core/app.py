# -*- encoding: utf-8 -*-

from core import admin, teacher, student
from lib import common



def run():
    menu = {
        '1': [admin, '管理端'],
        '2': [teacher, '教师端'],
        '3': [student, '学生端'],
    }
    while True:
        print('=' * 30)
        for k, v in menu.items():
            print('%-4s %-10s' % (k, v[1]))
        print('=' * 30)
        choice = common.input_string('请选择操作编号')
        if choice == 'q':
            print('\033[31m输入"e"结束程序！\033[0m')
            continue
        if choice == 'e':
            break
        if choice not in menu:
            print('\033[31m选择编号非法！\033[0m')
            continue
        menu[choice][0].run()


