# -*- encoding: utf-8 -*-

from core import admin, teacher, student


def run():
    menu = {
        '1': [admin, '管理段'],
        '2': [teacher, '教师端'],
        '3': [student, '学生端'],
    }
    while 1:
        print('=' * 30)
        for k,v in menu.items():
            print('%-4s %-10s' % (k, v[1]))
        print('=' * 30)
        choice = input('请选择平台编号[q to exit] >>: ').strip()
        if choice == 'q': break
        if choice not in menu:
            print('\033[31m选择编号非法！\033[0m')
            continue
        menu[choice][0].run()