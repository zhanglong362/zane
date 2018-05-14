#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

user_info = {
    'egon1': {'password': '123'},
    'egon2': {'password': '123'},
    'egon3': {'password': '123'}
}
i = 0
dbfile = "db.txt"
while 1:
    name = input('username>>: ')
    pwd = input('password>>: ')
    if not os.path.exists(dbfile):
        os.mknod(dbfile)
    with open(dbfile, 'r') as f:
        lock_users = f.read().split('|')
        if name in lock_users:
            print('用户 %s 已经被锁定' % name)
            break
    if name not in user_info:
        print('用户 %s 不存在！' % name)
        i += 1
    if name in user_info and pwd != user_info[name]['password']:
        print('用户 %s 密码错误！' % name)
        i += 1
    if i == 3:
        print('尝试次数过多，锁定!')
        with open(dbfile, 'a') as f:
            f.write('%s|' % name)
        break
    if name in user_info and pwd == user_info[name]['password']:
        print('Welcome %s, you are login successful!' % name)
        break



