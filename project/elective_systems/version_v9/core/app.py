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
        common.show_red('按"e"结束程序')
        common.show_menu(menu)
        choice = common.input_string('请选择平台编号')
        if choice == 'q':
            continue
        if choice == 'e':
            common.show_red('Goodbye!')
            return
        if choice not in menu:
            common.show_red('选择编号非法！')
            continue
        menu[choice][0].run()
