# 3-21作业：
#  1、什么是字符编码？
# 字符编码，也称字集码，是把字符集中的字符编码为指定集合中某一对象（例如：比特模式），以便文本在计算机中存储和通过通信网络的传递。

#  2、保证不乱码的核心法则是？
# 保证不乱码的核心法则，就是字符按什么标准编码的，就必须按照什么标准解码；

#  3、循环读取文件内容
# 第一种:
# with open('a.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line)
# 第二种：
# with open('a.txt', 'r', encoding='utf-8') as f:
#     for line in f.readlines():
#         print(line)

#  4、编写用户注册程序，
#   用户选择注册功能则：
#    将用户输入用户名、性别、年龄等信息存放于文件中
#   用户选择查看功能：
#    则将用户的详细信息打印出来

# config = 'db.txt'
# while 1:
#     print('\n1  注册\n2  查看\n')
#     action = input('选择操作 >>: ').strip()
#     if action == '1':
#         print('输入注册信息！')
#         r_n = input('用户名 >>: ').strip()
#         r_p = input('密码 >>: ')
#         r_i = input('手机 >>: ')
#         r_s = input('性别 >>: ')
#         r_a = input('年龄 >>: ')
#         user = '%s %s %s %s %s' % (r_n, r_p, r_i, r_s, r_a)
#         with open(config, 'a') as f:
#             f.write('%s\n' % user)
#             print('%s 注册成功！' % r_n)
#     elif action == '2':
#         phone = input('请输入手机号查询 >>: ').strip()
#         with open(config, 'r') as f:
#             for u in f:
#                 u = u.split()
#                 if phone in u:
#                     n, p, i, x, a = u
#                     print('用户名: %s\n手机号: %s\n性别: %s\n年龄: %s' % (n, i, x, a))
#     else:
#         print('输入编号非法！')

#  5、编写用户认证接口，其中用户的账号密码是存放文件中的。

# config = 'db.txt'
# while 1:
#     users = {}
#     with open(config, 'r') as f:
#         for u in f:
#             u = u.split()
#             if u:
#                 n, p, i, x, a = u
#                 d = {n: {'password': p, 'phone': i, 'sex': x, 'age': a}}
#                 users.update(d)
#     name = input('用户名 >>: ').strip()
#     pwd = input('密码 >>: ')
#     if name not in users:
#         print('用户名错误！')
#         continue
#     if pwd != users[name]['password']:
#         print('密码错误！')
#         continue
#     if name in users and pwd == users[name]['password']:
#         print('登陆成功！')


