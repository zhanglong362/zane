#!/usr/bin/env python3
# -*- coding:utf-8 -*-


user_info = {
    'username': 'egon',
    'password': '123'
}
i = 0
while 1:
    name = input('username>>: ')
    pwd = input('password>>: ')
    if name != user_info['username']:
        print('用户 %s 不存在！' % name)
        i += 1
    if name == user_info['username'] and pwd != user_info['password']:
        print('用户 %s 密码错误！' % name)
        i += 1
    if i == 3:
        print('尝试次数过多，锁定!')
        break
    if name == user_info['username'] and pwd == user_info['password']:
        print('Welcome %s, you are login successful!' % name)
        break





