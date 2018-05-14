# 一、元组
# 1. 列表与元组的区别，是元组不可修改，而列表可以。
#
# 二、for 循环练习
# 1.
# 字符串
# goods = 'hello'
# for number, good in enumerate(goods):
#     print(number, good)
# 列表
# goods = ['mac', 'apple', 'iphone', 'tesla']
# for number, good in enumerate(goods):
#     print(number, good)
# 字典
# goods = {'mac': 10000, 'apple': 200, 'iphone': 8000, 'tesla': 20000}
# for number, good in enumerate(goods):
#     print(number, good)

# 2.
# 结果：程序打印了三个元组，元组内容是字典 {'name':'egon','age':18,'sex':'male'} 的索引和key：
# (0, 'name')
# (1, 'age')
# (2, 'sex')
# 解释：enumerate() 用于将一个可遍历的数据对象（字符串、列表、字典）组合为一个索引序列，同时列出索引和数据。

# 三、简单购物车
# msg_dic = {
#     'apple': 10,
#     'tesla': 100000,
#     'mac': 3000,
#     'lenovo': 30000,
#     'chicken': 10
# }
#
# goods = []
# while 1:
#     for name in msg_dic:
#         print('商品名: %-10s 价格: %-10s' % (name, msg_dic[name]))
#     good_name = input('商品名称 >>: ')
#     if good_name not in msg_dic:
#         continue
#     price = msg_dic[good_name]
#     while 1:
#         count = input('购买个数 >>: ')
#         if count.isdigit():
#             count = int(count)
#             break
#     info = {
#         'good_name': good_name,
#         'price': price,
#         'count': count
#     }
#     goods.append(info)
#     print(goods)

# 四、字典练习
# 1. 字典是无序的；
# 2. 三种方式取出字典中的key和value:
msg_dic = {
    'apple': 10,
    'tesla': 100000,
    'mac': 3000,
    'lenovo': 30000,
    'chicken': 10,
}
# 1）
# for k,v in msg_dic.items():
#     print('key: %s, value: %s' % (k, v))
# # 2)
# for k in msg_dic:
#     print('key: %s, value: %s' % (k, msg_dic[k]))
# 3)
# for k,v in enumerate(msg_dic):
#     print('key: %s, value: %s' % (v, msg_dic[v]))
# 3. 可以使用字典的 get() 方法取值，如果 key 不存在不会报错。
# 4. l = [11,22,33,44,55,66,77,88,99,90...]
# d = {
#     'k1': [],
#     'k2': []
# }
# for i in l:
#     if i > 66:
#         d['k1'].append(i)
#     if i < 66:
#         d['k2'].append(i)
# print(d)

# 5. 统计s='hello alex alex say hello sb sb'中每个单词的个数
# s='hello alex alex say hello sb sb'
# l = s.split()
# d = {}
# for i in l:
#     # d[i] = l.count(i)
#     d.setdefault(i, l.count(i))
# print(d)

# 五、集合练习
# 1. 关系运算
# pythons={'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}
# linuxs={'wupeiqi','oldboy','gangdan'}
# 1）求出即报名python又报名linux课程的学员名字集
# s = pythons & linuxs
# print(s)
# 2) 求出所有报名的学生名字集合
# s = pythons | linuxs
# print(s)
# 3) 求出只报名python课程的学员名字
# s = pythons - linuxs
# print(s)
# 4) 求出没有同时这两门课程的学员名字集合
# s = pythons ^ linuxs
# print(s)

# 2. 去重
# 1）有列表l=['a','b',1,'a','a']，列表元素均为可hash类型，去重，得到新列表,且新列表无需保持列表原来的顺序
# l = ['a','b',1,'a','a']
# new_l = list(set(l))
# print(new_l)

# 2) 在上题的基础上，保存列表原来的顺序
# l = ['a','b',1,'a','a']
# n = []
# for i in l:
#     if i not in n:
#         n.append(i)
# print(n)

# 3) 去除文件中重复的行，肯定要保持文件内容的顺序不变
# n = []
# with open('t.txt', 'r') as f:
#     msg = f.readlines()
#     for i in msg:
#         i = i.strip('\n')
#         print(i)
#         if i not in n:
#             n.append(i)
# with open('t.txt', 'w') as f:
#     for i in n:
#         f.write(i+'\n')

# 4) 有如下列表，列表元素为不可hash类型，去重，得到新列表，且新列表一定要保持列表原来的顺序
# l = [
#     {'name':'egon','age':18,'sex':'male'},
#     {'name':'alex','age':73,'sex':'male'},
#     {'name':'egon','age':20,'sex':'female'},
#     {'name':'egon','age':18,'sex':'male'},
#     {'name':'egon','age':18,'sex':'male'},
# ]
# n = []
# for i in l:
#     if i not in n:
#         n.append(i)
# print(n)








