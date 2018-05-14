# 扩展：
# enumerate() 函数
# goods = 'hello'
# goods = ['mac', 'apple', 'iphone', 'tesla']
# goods = {'mac': 10000, 'apple': 200, 'iphone': 8000, 'tesla': 20000}
#
# for number, good in enumerate(goods):
#     print(number, good)

# 字典类型
# 1. 购物车小程序
# msg_dic = {
#     'apple': 10,
#     'tesla': 100000,
#     'mac': 3000,
#     'lenovo': 30000,
#     'chicken': 10
# }
# users = {
#     'egon': {
#         'password': '123',
#         'goods': {}
#     }
# }
# line = '='*25
# tag = True
# while tag:
#     inp_name = input('name >>: ').strip()
#     inp_pwd = input('password >>: ')
#     if inp_name in users and inp_pwd == users[inp_name]['password']:
#         print('login successful!')
#         while tag:
#             print(line)
#             for k,v in msg_dic.items():
#                 print('%-10s %-10s' % (k, v))
#             print(line)
#             good = input('please choose your good >>: ')
#             count = input('please choose your count >>: ')
#             if not count.isdigit():
#                 print('count not valid')
#                 continue
#             else:
#                 count = int(count)
#             if good in msg_dic:
#                 d[good] = count
#                 if good not in users[inp_name]['goods']:
#                     users[inp_name]['goods'][good] = count
#                 else:
#                     users[inp_name]['goods'][good] = users[inp_name]['goods'][good] + count
#                 print('%s %s has joined the shopping cart: \n%s' % (count, good, users[inp_name]['goods']))
#             else:
#                 print('good not valid')
#     else:
#         print('name or password not valid')

# 2.按索引取值，可取可存
# dic = {'name': 'egon'}

# 3.增加和修改
# dic['age'] = 10
# print(dic)
# dic['name'] = 'EGON'
# print(dic)
# dic['name'] = dic['name'].upper()
# print(dic)

# 4.长度 len()
# dic = {'name': 'egon', 'age': 18}
# print(len(dic))

# 5.删除
# dic = {'name': 'egon', 'age': 18}
# dic.pop('name')
# dic.pop('name', None)  # 如果不存在 key，则返回 None

# 6.获取字典内的所有元素
# 获取所有键 dict.keys()  # 默认的是获取键
# dic = {'name': 'egon', 'age': 18}
# dict_keys = dic.keys()
# print(dict_keys)

# 获取所有值 dict.values()
# dict_values = dic.values()
# print(dict_values)

# 获取所有键值对 dict.items()
# dict_items = dic.items()
# print(dict_items)

# 7. get()
# dic = {'name': 'egon', 'age': 18}
# print(dic.get('name'))
# print(dic.get('lala'))

# l = ['name', 'age', 'sex']
# print({}.fromkeys(l))

# s1 = {1, 2, 3, 4, 5}
# s2 = {1, 2, 3}

# s1.isdisjoint()

# print(set(l))
