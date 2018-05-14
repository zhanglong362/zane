# 1. 多态性：可以在不用考虑对象具体类型的前提下，而直接使用对象下的方法；
# 动物的多种形态：猫、狗、猪
# 动物技能的派生：喵喵喵、汪汪汪、哼哼哼
class Animal:
    def eat(self):
        pass

    def drink(self):
        pass

    def run(self):
        pass

    def bark(self):
        pass

class Cat(Animal):
    def bark(self):
        print('喵喵喵')

class Dog(Animal):
    def bark(self):
        print('汪汪汪')

class Pig(Animal):
    def bark(self):
        print('哼哼哼')

2. 抽象方法：抽象方法只需声明，而不需实现，抽象方法由抽象类的子类去具体实现；
import abc

class Animal(metaclass=abc.ABCMeta):
    def eat(self):
        pass

    def drink(self):
        pass

    def run(self):
        pass

    @abc.abstractmethod
    def bark(self):
        pass

class Cat(Animal):
    def bark(self):
        print('喵喵喵')


class Dog(Animal):
    def bark(self):
        print('汪汪汪')


class Pig(Animal):
    def bark(self):
        print('哼哼哼')

c = Cat()
c.bark()

# 3. 鸭子类型
class Foo:
    def f1(self):
        print('from Foo.f1 ...')

    def f2(self):
        print('from Foo.f2 ...')

class Bar(Foo):
    def f1(self):
        print('from Bar.f1 ...')

    def f2(self):
        print('from Bar.f2 ...')

# 4. 类内部方法分类
# 绑定给对象：self
# 绑定给类：@classmethod cls
# 非绑定方法：既不和类绑定，也不和类绑定，谁来用都是一个普通函数（没有自动传值的特征）；












