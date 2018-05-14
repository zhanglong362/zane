# 递归限制 1000
# import sys
# print(sys.getrecursionlimit())

# def bar():
#     print('from bar')
#     foo()
#
# def foo():
#     print('from foo')
#     bar()
#
# foo()

# 递归返回一个值
# def age(n):
#     if n == 1:
#         return 18
#     return age(n-1)+2
#
# print(age(5))

# 递归打印所有数值
# items = [1,[2,[3,[4,[5,[6,[7,[8]]]]]]]]
#
# def tell(l):
#     for item in l:
#         if type(item) is not list:
#             print(item)
#         else:
#             tell(item)
#
# tell(items)

# 匿名函数
# def foo(x, n):
#     return x ** n
#
# print(foo(3, 2))
# print(foo(3, 2))

# func = lambda x, n: x ** n
# print(func(3, 2))

# reduce 方法
# from functools import reduce
# print(reduce(lambda x,y:x+y, range(1,101)))

# 斐波那契迭代器
# class Fibs:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#
#     def next(self):
#         self.a, self.b = self.b, self.a + self.b
#         return self.a
#
#     def __iter__(self):
#         return self
#
# f = Fibs()
#
# print(f.next())
# print(f.next())
# print(f.next())
# print(f.next())
# print(f.next())


# 斐波那契递归
# Filename : test.py
# author by : www.runoob.com

# def recur_fibo(n):
#     """递归函数
#     输出斐波那契数列"""
#     if n <= 1:
#         return n
#     else:
#         return (recur_fibo(n - 1) + recur_fibo(n - 2))
#
#
# 获取用户输入
# nterms = int(input("您要输出几项? "))
#
# 检查输入的数字是否正确
# if nterms <= 0:
#     print("输入正数")
# else:
# print("斐波那契数列:")
# for i in range(10):
#     print(recur_fibo(i))