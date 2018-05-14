# -*- encoding: utf-8 -*-

from lib import common
from core import admin, user


def run():
    menu = {
        '1': [admin, '管理端'],
        '2': [user, '用户端']
    }
    while True:
        common.show_red('按"e"结束程序')
        common.show_menu(menu)
        choice = common.input_string('请输入平台编号')
        if choice == 'e':
            common.show_red('Goodbye!')
            return
        if choice not in menu:
            common.show_red('选择编号非法！')
            continue
        menu[choice][0].run()


