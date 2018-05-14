#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import manager
from core import teacher
from core import student

def main():
    while True:
        menu = {
            '1': [student, '学生端'],
            '2': [teacher, '老师端'],
            '3': [manager, '管理端']
        }
        for k,v in menu.items():
            print('%-4s %-10s' % (k, v[1]))
        choice = input('请选择平台编号 >>: ').strip()
        if choice not in menu:
            print('选择编号非法！')
            continue
        menu[choice][0].run()


if __name__ == '__main__':
    main()
