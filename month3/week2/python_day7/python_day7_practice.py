# 一、改进用户注册、查看程序
line = '='*25
config = 'db.txt'
tag = True
while tag:
    users = {}
    with open(config, 'a') as f:
        pass
    with open(config, 'r') as f:
        for u in f:
            u = u.split()
            if u:
                n, p, i, x, a = u
                d = {n: {'password': p, 'phone': i, 'sex': x, 'age': a}}
                users.update(d)
    print(line)
    print('1  注册用户\n2  登陆查看')
    print(line)
    action = input('选择操作 >>: ').strip()
    if action == '1':
        while tag:
            register = False
            print('\033[31m输入注册信息！\033[0m')
            r_i = input('手机 >>: ')
            for p in users.values():
                if r_i == p['phone']:
                    print('手机号 %s 已经注册！' % r_i)
                    register = True
                    break
            if register:
                continue
            r_n = input('用户名 >>: ').strip()
            r_p = input('密码 >>: ')
            r_s = input('性别 >>: ')
            r_a = input('年龄 >>: ')
            user = '%s %s %s %s %s' % (r_n, r_p, r_i, r_s, r_a)
            with open(config, 'a') as f:
                f.write('%s\n' % user)
            print('%s 注册成功！' % r_n)
            break
    elif action == '2':
        while tag:
            print('请输入用户名和密码！')
            name = input('用户名 >>: ').strip()
            if name == 'quit':
                tag = False
                continue
            if name not in users:
                print('\033[31m用户名不存在，请先注册后登陆！\033[0m')
                break
            pwd = input('密码 >>: ')
            if pwd == 'quit':
                tag = False
                continue
            if pwd != users[name]['password']:
                print('密码错误！')
                continue
            if name in users and pwd == users[name]['password']:
                print('登陆成功！')
                phone = users[name]['phone']
                sex = users[name]['sex']
                age = users[name]['age']
                print('用户名: %s\n手机号: %s\n性别: %s\n年龄: %s' % (name, phone, sex, age))
                break
    else:
        print('输入编号非法！')

# 二、编写程序，实现下列功能
# 1、提供两种可选功能：
#     1 拷贝文件
#     2 修改文件
# 2、用户输入操作的编码，根据用户输入的编号，执行文件拷贝（让用户输入原文件路径和目标文件路径）或修改操作

# #!/usr/bin/env python3
# # -*- encoding: utf-8 -*-
#
# import os
#
# while 1:
#     print('\n1  拷贝文件\n2  修改文件\n')
#     action = input('选择操作 >>: ').strip()
#     if action == '1':
#         print('输入拷贝信息！')
#         src = input('源路径 >>: ').strip()
#         dst = input('目标路径 >>: ').strip()
#         with open(r'%s' % src, 'rb') as f1, open(r'%s' % dst, 'wb') as f2:
#             for line in f1:
#                 f2.write(line)
#         print('文件%s拷贝到%s完成！' % (src, dst))
#     elif action == '2':
#         print('输入修改信息！')
#         path = input('文件路径 >>: ').strip()
#         path_tmp = '%s.swap' % path
#         str_s = input('原字符串 >>: ').encode('utf-8')
#         str_r = input('替换字符串 >>: ').encode('utf-8')
#         with open(r'%s' % path, 'rb') as f1, open(r'%s' % path_tmp, 'wb') as f2:
#             for line in f1:
#                 if str_s in line:
#                     line = line.replace(str_s, str_r)
#                 f2.write(line)
#         os.remove(path)
#         os.rename(path_tmp, path)
#         print('文件%s修改完成！' % path)
#     else:
#         print('输入编号非法！')
