# 1. 迭代器
# str1 = 'hello'
# list1 = [1,2,3]
# tup1 = (1,2,3)
# dic1 = {'x':1,'y':2,'z':3}
# set1 = {1,2,3}
# f = open(r'a.txt')
#
# for s in [str1, list1, tup1, dic1, set1, f]:
#     _iter = s.__iter__()
#     print(s, iter)
#     while True:
#         try:
#             r = _iter.__next__()
#         except StopIteration:
#             print('迭代结束！')
#             break
#         else:
#             print(r)
# f.close()
#
# 2. 生成器
# def chicken():
#     print('=====> first')
#     yield 1
#     print('=====> second')
#     yield 2
#     print('=====> third')
#     yield 3
#
# obj = chicken()
# # print('obj.__iter__() is obj')
# # res = obj.__next__()
# # print(res)
# # res1 = obj.__next__()
# # print(res1)
# # res2 = obj.__next__()
# # print(res2)
#
# for item in obj:
#     print(item)
#
# def my_range():
#     print('start...')
#     i = 0
#     while True:
#         yield i
#         i += 1
#
# obj = my_range()
#
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
#
# print(my_range().__next__())
# print(my_range().__next__())
#
# for i in obj:
#     print(i)
#
# def my_range(start, end, step=1):
#     i = start
#     while i < end:
#         yield i
#         i += step
#
# # obj = my_range(0, 10)
# # obj = obj.__iter__()
# # print(obj.__next__())
# # print(obj.__next__())
# # print(obj.__next__())
# # print(obj.__next__())
#
#
# for i in my_range(0,10):
#     print(i)
#
# # 3. 协程函数
# def eat(name):
#     print('%s ready to eat' % name)
#     food_list = []
#     while True:
#         food = yield food_list
#         print('%s start to eat %s' % (name, food))
#         food_list.append(food)
#
#
# dog1 = eat('John')
#
# # 1）函数必须初始化一次，就是先调用一次 next 方法，让函数停留在 yield 的位置；
# print(dog1.__next__())
#
# # 2）使用 send 方法给 yield 传值，其次和 next 方法一致；
# print(dog1.send('面包'))
# print(dog1.send('骨头'))
#
#
