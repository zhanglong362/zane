# # == == == == == =*args == == == == == =
# print('*agrs')
# def foo(x, y, *args):
#     print(x, y)
#     print(args)
# foo(1, 2, 3, 4, 5)
#
# def foo(x, y, *args):
#     print(x, y)
#     print(args)
# foo(1, 2, *[3, 4, 5])
# foo(1, 2, *'hello')
# foo(1, 2, *(3, 4, 5))
#
# def foo(x, y, z):
#     print(x, y, z)
# foo(*[1, 2, 3])

# # == == == == == = ** kwargs == == == == == =
# print('**kwargs')
# def foo(x, y, **kwargs):
#     print(x, y)
#     print(kwargs)
# foo(1, y=2, a=1, b=2, c=3)
#
# def foo(x, y, **kwargs):
#     print(x, y)
#     print(kwargs)
# foo(1, y=2, **{'a': 1, 'b': 2, 'c': 3})
#
# def foo(x, y, z):
#     print(x, y, z)
# foo(**{'z': 1, 'x': 2, 'y': 3})


# def foo(x, y, *args):
#     print(x, y)
#     print(args)
#
# foo(1,2,3,4,5)
#
# def bar(x, y, **kwargs):
#     print(x, y)
#     print(kwargs)
#
# bar(1,2,a=1,b=2,c=3)
#
# def both(x, y, *args, **kwargs):
#     print(x, y)
#     print(args)
#     print(kwargs)
#
# both(1,2,3,4,5,a=1,b=2,c=3)


# # 组合使用
# def index(name, age, gender):
#     print('name: %s age: %s gender: %s' % (name, age, gender))
#
# def wrapper(*args, **kwargs):
#     index(*args, **kwargs)
#
# wrapper('egon',18,'male')
# wrapper('egon',age=18,gender='male')
# wrapper(name='egon',age=18,gender='male')





