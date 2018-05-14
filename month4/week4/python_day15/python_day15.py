# # -*- encoding: utf-8 -*-
#
# import logging
# #
# # logging.basicConfig(
# #     filename='access.log',
# #     format='%(asctime)s  %(filename)s [line:%(lineno)d]: %(levelname)s: %(message)s',
# #     datefmt='%Y-%b-%d %H:%M:%S',
# #     level=10,
# #     filemode='w'
# # )
# #
# # logging.debug('检测有没有着火 ...')    # 10
# # logging.info('没有着火 ...')          # 20
# # logging.warning('可能着火 ...')       # 30
# # logging.error('着火啦快跑 ...')       # 40
# # logging.critical('火越烧越大 ...')    # 50
#
#
# # logger()    负责生产日志
# logger1 = logging.getLogger('mylogger')
#
# # filter()    过滤日志（不常用）
# # handler()   控制日志打印到文件或终端
# fh1 = logging.FileHandler(filename='a1.log',encoding='utf-8')
# fh2 = logging.FileHandler(filename='a2.log',encoding='utf-8')
# sh = logging.StreamHandler()
#
# # 为 logger 对象绑定 handler
# logger1.addHandler(fh1)
# logger1.addHandler(fh2)
# logger1.addHandler(sh)
#
# # formatter() 控制日志的格式
# format1 = logging.Formatter(fmt='%(asctime)s  %(filename)s [line:%(lineno)d]: %(levelname)s: %(message)s', datefmt='%Y-%b-%d %H:%M:%S')
# format2 = logging.Formatter(fmt='%(asctime)s - %(message)s',)
# # 为 handler 对象绑定日志格式
# fh1.setFormatter(format1)
# fh2.setFormatter(format1)
# sh.setFormatter(format2)
#
# # 日志级别
# logger1.setLevel(10)
# fh1.setLevel(10)
# fh2.setLevel(10)
# sh.setLevel(10)
#
# logger1.debug('调试 ...')

# 1. json.dumps 和 json.loads
# import json
#
# user = {'name': 'egon', 'age': 18, 'sex': 'male'}
# print(type(user), user)
#
# with open(r'a.txt', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(user))
#
# with open(r'a.txt') as f:
#     user = json.loads(f.read())
#     print(type(user), user)

# 2. json.dump 和 json.load
# import json
# user = {'name': 'egon', 'age': 18, 'sex': 'male'}
# print(type(user), user)
# with open(r'b.txt', 'w') as f:
#     json.dump(user, f)
#
# with open(r'b.txt', 'r') as f:
#     user = json.load(f)
#     print(type(user), user)

# 3. pickle.dumps 和 pickle.loads
# import pickle
# s = {1, 2, 3, 4}
# print(type(s), s)
# s = pickle.dumps(s)
# with open(r'b.txt', 'wb') as f:
#     f.write(s)
#
# with open(r'b.txt', 'rb') as f:
#     s = f.read()
#     s = pickle.loads(s)
#     print(type(s), s)

# 4. pickle.dump 和 pickle.load
# import pickle
# s = {1, 2, 3, 4}
# print(type(s), s)
# with open(r'b.txt', 'wb') as f:
#     pickle.dump(s, f)
#
# with open(r'b.txt', 'rb') as f:
#     s = pickle.load(f)
#     print(type(s), s)

# 增删改查小程序
# 1. 增加
# def add():
#     with open('db.txt', 'ab') as f: