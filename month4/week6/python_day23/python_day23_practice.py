# 4-17日作业
# 1、判断一个对象是否属于str类型，判断一个类是否是另外一个类的子类
# s = 'hello'
# if isinstance(s, str):
#     print('对象 "%s" 是 "str" 类型！' % s)
# else:
#     print('对象 "%s" 不是 "str" 类型！' % s)
#
# class Foo:
#     pass
#
# class Bar(Foo):
#     pass
#
# if issubclass(Bar, Foo):
#     print('类 "%s" 是 "%s" 的子类！' % ('Bar', 'Foo'))
# else:
#     print('类 "%s" 不是 "%s" 的子类！' % ('Bar', 'Foo'))

# 2、有俩程序员，一个lili，一个是egon，lili在写程序的时候需要用到egon所写的类(放到了另外一个文件中)，但是egon去跟女朋友度蜜月去了，还没有完成他写的类，
#     class FtpClient:
#         """
#         ftp客户端,但是还么有实现具体的功能
#         """
#         def __init__(self,addr):
#             print('正在连接服务器[%s]' %addr)
#             self.addr=addr
#
#         此处应该完成一个get功能
# lili想到了反射，使用了反射机制lili可以继续完成自己的代码，等egon度蜜月回来后再继续完成类的定义并且去实现lili想要的功能。


# 3、定义一个老师类，定制打印对象的格式为‘<name:egon age:18 sex:male>’
# class Teacher:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def __str__(self):
#         return '<name: %s age: %s sex: %s>' % (self.name, self.age, self.sex)
#
# t = Teacher('egon', 18, 'male')
# print(t)

# 4、定义一个自己的open类，控制文件的读或写，在对象被删除时自动回收系统资源
# class MyOpen:
#     def __init__(self, file_path, mode='r', encoding='utf-8'):
#         self.file_path = file_path
#         self.mode = mode
#         self.encoding = encoding
#         self.file = open(file_path, mode=mode, encoding=encoding)
#
#     def __del__(self):
#         self.file.close()
#
# f = MyOpen(r'settings.py')
# data = f.file.read()
# print(data)
# del f

# 5、自定义元类，把自定义类的数据属性都变成大写，必须有文档注释，类名的首字母必须大写
# class Mymeta(type):
#     def __init__(self, class_name, class_bases, class_dic):
#         if class_name[0].islower():
#             raise TypeError('类名的首字母必须是大写！')
#         if not class_dic.get('__doc__'):
#             raise TypeError('类必须有文档注释！')
#         d = {}
#         for k,v in class_dic.items():
#             if not hasattr(v, '__call__') and not (k.startswith('__') and k.endswith('__')):
#                 d[k] = v
#         for k in d:
#             class_dic.pop(k)
#             class_dic[k.upper()] = d[k]
#         self.class_name = class_name
#         self.class_bases = class_bases
#         self.class_dic = class_dic
#
# # class_dic = {'__doc__': 'Foo class'}
# # Foo = Mymeta('Foo', (object, ), class_dic)
#
# class Foo(object,metaclass=Mymeta):
#     '''
#     Foo class
#     '''
#     x = 1
#     def __init__(self):
#         pass
#
#     def __del__(self):
#         pass

# 6、用三种方法实现单例模式，参考答案:http://www.cnblogs.com/linhaifeng/articles/8029564.html#_label5
# 第一种方式：类方法
import settings

class Mysql:
    __instance = None

    def __init__(self, host, port):
        self.host = host
        self.port = port

    @classmethod
    def singleton(cls):
        if not cls.__instance:
            cls.__instance = cls(settings.HOST, settings.PORT)
        return cls.__instance

# 第二种方式：元类
import settings
class Mymeta(type):
    def __init__(self, class_name, class_bases, class_dict):
        self.__instance = object.__new__(self)
        self.__init__(self.__instance, settings.HOST, settings.PORT)
        super().__init__(class_name, class_bases, class_dict)

    def __call__(self, *args, **kwargs):
        if args or kwargs:
            obj = object.__new__(self)
            self.__init__(obj, settings.HOST, settings.PORT)
            return obj
        return self.__instance

class Mysql(metaclass=Mymeta):
    def __init__(self, host, port):
        self.host = host
        self.port = port

# 第三种方式：装饰器
import settings

def singleton(cls):
    __instance = cls(settings.HOST, settings.PORT)
    def wrapper(*args, **kwargs):
        if args or kwargs:
            return cls(settings.HOST, settings.PORT)
        return __instance
    return wrapper

@singleton
class Mysql:
    def __init__(self, host, port):
        self.host = host
        self.port = port







