class Foo:
    __x = 1

    def __init__(self, y=2):
        self.__y = y

    def __f1(self):
        print('Foo.f1 ...')

    def f2(self):
        print('Foo.f2 ...')
        self.__f1()

    def get_y(self):
        print('get y: %s' % self.__y)

# obj = Foo(2)

# print(obj.x)
# print(obj.y)
# obj.f1()
#
# print(obj._Foo__x)
# print(obj._Foo__y)
# obj._Foo__f1()
# print(Foo.__dict__)
#
# obj.get_y()

class Bar(Foo):
    def __f1(self):
        print('Bar.f1 ...')

# obj = Bar()
# obj.f2()

class People:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_user_info_api(self):
        # name = input('请输入用户名 >>: ').strip()
        # if name == self.__name:
        #     print('''
        #     用户名：%s
        #     年龄：%s
        #     ''' % (self.__name, self.__age))
        print('''
                    用户名：%s
                    年龄：%s
                    ''' % (self.__name, self.__age))

    def modify_user_info_api(self, name, age):
        if not isinstance(name, str):
            raise TypeError('用户名必须是字符串！')
        self.__name = name
        if not isinstance(age, int):
            raise TypeError('年龄必须是整型！')
        self.__age = age
        self.get_user_info_api()

p = People('egon', 18)
# print(p.name, p.age)
p.get_user_info_api()
p.modify_user_info_api('egon', 20)
p.get_user_info_api()












