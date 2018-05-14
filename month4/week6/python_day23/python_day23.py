# 1. 反射
# class Foo:
#     def run(self):
#         while True:
#             cmd = input('cmd >>: ').strip()
#             if hasattr(self, cmd):
#                 print('%s run ...' % cmd)
#                 func = getattr(self, cmd)
#                 func()
#             else:
#                 print('命令无效！')
#
#     def download(self):
#         print('download ...')
#
#     def upload(self):
#         print('upload ...')
#
#
# obj = Foo()
# obj.run()

# 2. __str__() 方法
# import time
#
# class People:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def __str__(self):
#         return '<名字: %s 年龄: %s 性别: %s>' % (self.name, self.age, self.sex)
#
#     def __del__(self):
#         print('obj deleted ..')
#
#
# obj = People('egon', 18, 'male')
# print(obj)
# del obj
# time.sleep(5)
# print('server stoped ..')

# 3. __del__() 方法：回收系统资源
# class Mysql:
#     def __init__(self):
#         self.ip = ip
#         self.port = port
#         self.conn = connect(ip, port)
#
#     def __del__(self):
#         self.conn.close()
#
# obj = Mysql('1.1.1.1', 3306)
#
# class MyOpen:
#     def __init__(self, filepath, mode='r', encoding='utf-8'):
#         self.filepath = filepath
#         self.mode = mode
#         self.encoding = encoding
#         self.fobj = open(filepath, mode=mode, encoding=encoding)
#
#     def __str__(self):
#         msg = '''
#         filepath: %s
#         mode: %s
#         encoding: %s
#         '''
#         return msg
#
#     def __del__(self):
#         self.fobj.close()
#
# f = MyOpen('a.txt', mode='r', encoding='utf-8')
# print(f)
#
# res = f.fobj.read()
# print(res)

# 4. 元类 类的类就是元类
# 我们用class定义的类使用来产生我们自己的对象；
# 内置元类type是用来专门产生class定义的类的；

# exec 函数知识储备
# exec(str, {}, {}) 把函数名放入名称空间内
# code = '''
# global x
# x = 0
# y = 2
# '''
# global_dic = {'x': 10000}
# local_dic = {}
#
# exec(code, global_dic, local_dic)
# print(global_dic)
# print(local_dic)

# class Chinese:
#     country = 'China'
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def speak(self):
#         print('%s speak Chinese' % self.name)
#
# p = Chinese('egon', 18, 'male')
# print(type(p))
#
# print(type(Chinese))

# 4. __call__() 方法储备知识
# class Foo:
#     def __init__(self):
#         print('__init__')
#
#     def __str__(self):
#         return '__str__'
#
#     def __del__(self):
#         print('__del__')
#
#     def __call__(self, *args, **kwargs):
#         print('__call__', args, kwargs)
#
# obj = Foo()
# print(obj)
#
# obj(1,2,3,a=1,b=2,c=3)

# 5. 自定义元类
# class Mymeta(type):
#     # 控制类Foo的创建
#     def __init__(self, class_name, class_bases, class_dic):
#         if class_name.isdigit():
#             raise TypeError('类名称不能是数字！')
#         # print('class_name: %s' % class_name)
#         if not class_dic.get('__doc__'):
#             raise TypeError('类内必须写好文档注释！')
#         # print('__doc__: %s' % class_dic['__doc__'])
#         self.class_name = class_name
#         self.obj = class_bases
#         self.class_dic = class_dic
#
#     # 控制类Foo的调用过程，即控制实例化Foo的过程
#     def __call__(cls, *args, **kwargs):
#         obj = object.__new__(cls)
#         cls.__init__(obj, *args, ** kwargs)
#         return obj
#
# # class_dic = {'__doc__':'\033[32mFoo class\033[0m'}
# # Foo = Mymeta('Foo', (object,), class_dic)
#
# class Foo(object, metaclass=Mymeta):
#     x = 1
#     __doc__ = '''
#     \033[32mFoo class\033[0m
#     '''
#     def __init__(self, y):
#         self.y = y
#
#     def __str__(self):
#         return 'y: %s' % self.y
#
#     def f1(self):
#         print('from f1')
#
# obj = Foo('2')
# print(obj)
# print(obj.x)
# print(obj.y)
# print(obj.f1)
# 6. 单例模式
# import settings
#
# class MySQL:
#     __conn = None
#     def __init__(self, ip, port):
#         self.ip = ip
#         self.port = port
#
#     @classmethod
#     def singleton(cls):
#         if not cls.__conn:
#             cls.__conn = cls(settings.IP, settings.PORT)
#         return cls.__conn
#
#     def __call__(self, *args, **kwargs):
#         pass
#
# obj1 = MySQL('1.1.1.2', 3306)
# obj2 = MySQL('1.1.1.3', 3306)
# obj3 = MySQL('1.1.1.4', 3306)
#
# obj4 = MySQL.singleton()
# obj5 = MySQL.singleton()
# obj6 = MySQL.singleton()
# print(obj4)
# print(obj5)
# print(obj6)

