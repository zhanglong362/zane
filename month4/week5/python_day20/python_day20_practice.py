# 4月12日作业
# 1、类的属性和对象的属性有什么区别?
# 区别：
# 1. 类的属性可以给不同对象共享；
# 2. 对象的属性，是对象独有的；

# 2、面向过程编程与面向对象编程的区别与应用场景?
# 区别：
# 1. 面向过程是流水线式的，一步一步的；
# 2. 面向对象是通过类实例化对象，对象之间交互；
# 应用场景：
# 1. 面向过程适合扩展性低的场景；
# 2. 面向对象适合扩展性高的场景；

# 3、类和对象在内存中是如何保存的。
# 1. 类在内存中是一系列的变量名字和方法名字；
# 2. 对象在内存中是一系列的变量名字；

# 4、什么是绑定到对象的方法，、如何定义，如何调用，给谁用？有什么特性
# 1. 绑定到对象的方法，其实是对象所属类的方法，但可以被对象调用；
# 2. 定义对象的绑定方法，就是定义对象所属类的方法；
# 3. 调用对象的绑定方法，以 object.function() 的方式调用；
# 4. 对象的绑定方法，给对象自己用；
# 5. 绑定方法的特性是，绑定给谁，就应该由谁来调用。谁来调用，就把谁当做第一个参数传入__init__方法；

# 5、如下示例, 请用面向对象的形式优化以下代码
# 在没有学习类这个概念时，数据与功能是分离的, 如下
#
# def exc1(host, port, db, charset, sql):
#     conn = connect(host, port, db, charset)
#     conn.execute(sql)
#     return xxx
#
# def exc2(host, port, db, charset, proc_name)
#     conn = connect(host, port, db, charset)
#     conn.call_proc(sql)
#     return xxx
# 每次调用都需要重复传入一堆参数
# exc1('127.0.0.1', 3306, 'db1', 'utf8', 'select * from tb1;')
# exc2('127.0.0.1', 3306, 'db1', 'utf8', '存储过程的名字')
class Database:
    def __init__(self, host, port, db, charset):
        self.host = host
        self.port = port
        self.db = db
        self.charset = charset

    def exc1(self, sql):
        conn = connect(host, port, db, charset)
        return conn.execute(sql)

    def exc2(self, proc_name):
        conn = connect(host, port, db, charset)
        return conn.call_proc(proc_name)

conn =  Database('127.0.0.1', 3306, 'db1', 'utf8')
conn.exc1('select * from tb1;')
conn.exc2('proc_name')

# 6、下面这段代码的输出结果将是什么？请解释。
# class Parent(object):
#     x = 1
#
# class Child1(Parent):
#     pass
#
# class Child2(Parent):
#     pass

# print(Parent.x, Child1.x, Child2.x)
# 结果：1 1 1
# 解释：
#     1. Parent.x是类自己的属性x，直接打印x=1；
#     2. Child1.x 和 Child2.x 是子类找不到属性x，打印的父类 Parent 的属性x=1；

# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)
# 结果：1 2 1
# 解释：
#     1. Parent.x是类自己的属性x，直接打印x=1；
#     2. Child1.x 增加了自己的属性x，打印了自己的属性x=2；
#     3. Child2.x 是子类找不到属性x，打印的父类 Parent 的属性x；

# Parent.x = 3
# print(Parent.x, Child1.x, Child2.x)
# 结果：1 2 3
# 解释：
#     1. Parent.x是类自己的属性x，直接打印x=1；
#     2. Child1.x 增加了自己的属性x，打印了自己的属性x=2；
#     3. Child2.x 增加了自己的属性x，打印了自己的属性x=3；

# 7、多重继承的执行顺序，请解答以下输出结果是什么？并解释。
# class A(object):
#     def __init__(self):
#         print('A')
#         super(A, self).__init__()
#
# class B(object):
#     def __init__(self):
#         print('B')
#         super(B, self).__init__()
#
# class C(A):
#     def __init__(self):
#         print('C')
#         super(C, self).__init__()
#
# class D(A):
#     def __init__(self):
#         print('D')
#         super(D, self).__init__()
#
# class E(B, C):
#     def __init__(self):
#         print('E')
#         super(E, self).__init__()
#
# class F(C, B, D):
#     def __init__(self):
#         print('F')
#         super(F, self).__init__()
#
# class G(D, B):
#     def __init__(self):
#         print('G')
#         super(G, self).__init__()
#
#
# if __name__ == '__main__':
#     g = G()
#     f = F()
# 结果：
#     G
#     D
#     A
#     B
#     F
#     C
#     B
#     D
#     A
# 解释：
#     先调用 G() 类：
#         1. G            G类本身打印；
#         2. -> D -> A    第一个独立分支结束；
#         3. -> B         第二个独立分支结束；
#     再调用 F() 类：
#         1. F            F类本身打印；
#         2. -> C         第一个分支到C类结束，因为D类和C类都是基于A的子类，而A类是object的子类，根据新式类算法到C结束；
#         3. -> B         第二个分支结束，因为B类是独立分支的object的子类；
#         4. -> D -> A    第三个分支结束，因为没有其它基于A类的分支了，所以打印A；

# 8、什么是新式类，什么是经典类，二者有什么区别？什么是深度优先，什么是广度优先？
# 1. 新式类是指继承了object类的类，及其子类；
# 2. 经典类是指 python2 中不继承 object类的类，及其子类；
# 3. 经典类和新式类的区别，只有当多个子类继承于一个父类时，经典类基于深度优先的顺序查找属性，而新式类基于广度优先的顺序查找属性；
# 4. 深度优先，就是当多个子类继承于一个父类时，查找属性先按一条分支一直查找到顶层的父类，然后再查询其它分支且不再查找顶层的父类；
# 5. 广度优先，就是当多个子类继承于一个父类时，查找属性先查找每一条分支查找除了顶层的父类之外的所有子类，顶层的父类最后查找；

# 9、用面向对象的形式编写一个老师类, 老师有特征：编号、姓名、性别、年龄、等级、工资，老师类中有功能
# 1、生成老师唯一编号的功能，可以用hashlib对当前时间加上老师的所有信息进行校验得到一个hash值来作为老师的编号
# def create_id(self):
#     pass
# 2、获取老师所有信息
# def tell_info(self):
#     pass
# 3、将老师对象序列化保存到文件里，文件名即老师的编号，提示功能如下
# def save(self):
#     with open('老师的编号', 'wb') as f:
#         pickle.dump(self, f)
# 4、从文件夹中取出存储老师对象的文件，然后反序列化出老师对象, 提示功能如下
# def get_obj_by_id(self, id):
#     return pickle.load(open(id, 'rb'))
# import time
# import pickle
# import hashlib
#
# class Teacher:
#     def __init__(self, name, sex, age, grade, salary):
#         self.number = None
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.grade = grade
#         self.salary = salary
#         self.create_id()
#
#     def _make_md5_code(self, string):
#         string = (str(time.time()) + string).encode('utf-8')
#         m = hashlib.md5()
#         m.update(string)
#         return m.hexdigest()
#
#     def _get_user_info(self):
#         user_info = {
#             'number': self.number,
#             'name': self.name,
#             'sex': self.sex,
#             'age': self.age,
#             'grade': self.grade,
#             'salary': self.salary,
#         }
#         return user_info
#
#     def create_id(self):
#         user_info = str(self._get_user_info().pop('number'))
#         self.number = self._make_md5_code(user_info)
#
#     def tell_info(self):
#         print('''
#         number: %s
#         name: %s
#         sex: %s
#         age: %s
#         grade: %s
#         salary: %s
#         ''' % (self.number,
#               self.name,
#               self.sex,
#               self.age,
#               self.grade,
#               self.salary))
#
#     def save(self):
#         user_info = self._get_user_info()
#         with open(r'%s' % self.number, 'wb') as f:
#             pickle.dump(user_info, f)
#
#     def get_obj_by_id(self):
#         with open(r'%s' % self.number, 'rb') as f:
#             data = pickle.load(f)
#             print(data)
#             return data
#
# t = Teacher('Egon', 'male', 18, '特级教师', 50000)
# t.tell_info()
# t.save()
# t.get_obj_by_id()

# 10、按照定义老师的方式，再定义一个学生类
# import time
# import pickle
# import hashlib
# class Student:
#     def __init__(self, name, sex, age, classes, course):
#         self.number = None
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.classes = classes
#         self.course = course
#         self.create_id()
#
#     def _make_md5_code(self, string):
#         string = (str(time.time()) + string).encode('utf-8')
#         m = hashlib.md5()
#         m.update(string)
#         return m.hexdigest()
#
#     def _get_user_info(self):
#         user_info = {
#             'number': self.number,
#             'name': self.name,
#             'sex': self.sex,
#             'age': self.age
#         }
#         return user_info
#
#     def create_id(self):
#         user_info = str(self._get_user_info().pop('number'))
#         self.number = self._make_md5_code(user_info)
#
#     def tell_info(self):
#         print('''
#             number: %s
#             name: %s
#             sex: %s
#             age: %s
#             classes: %s
#             course: %s
#             ''' % (self.number,
#                    self.name,
#                    self.sex,
#                    self.age,
#                    self.classes,
#                    self.course))
#
#     def save(self):
#         user_info = self._get_user_info()
#         with open(r'%s' % self.number, 'wb') as f:
#             pickle.dump(user_info, f)
#
#     def get_obj_by_id(self):
#         with open(r'%s' % self.number, 'rb') as f:
#             data = pickle.load(f)
#             print(data)
#             return data
#
#
# stu = Student('Zane', 'male', 20, '上海一期班', 'Python全栈课程')
# stu.tell_info()
# stu.save()
# stu.get_obj_by_id()

# 11、抽象老师类与学生类得到父类，用继承的方式减少代码冗余
import time
import pickle
import hashlib

class OldboyPeople:
    def __init__(self, name, sex, age):
        self.number = None
        self.name = name
        self.sex = sex
        self.age = age
        self.create_id()

    def _make_md5_code(self, string):
        string = (str(time.time()) + string).encode('utf-8')
        m = hashlib.md5()
        m.update(string)
        return m.hexdigest()

    def _get_user_info(self):
        user_info = {
            'number': self.number,
            'name': self.name,
            'sex': self.sex,
            'age': self.age
        }
        return user_info

    def create_id(self):
        user_info = str(self._get_user_info().pop('number'))
        self.number = self._make_md5_code(user_info)

    def tell_info(self):
        print('''
            number: %s
            name: %s
            sex: %s
            age: %s
            classes: %s
            course: %s
            ''' % (self.number,
                   self.name,
                   self.sex,
                   self.age,
                   self.classes,
                   self.course))

    def save(self):
        user_info = self._get_user_info()
        with open(r'%s' % self.number, 'wb') as f:
            pickle.dump(user_info, f)

    def get_obj_by_id(self):
        with open(r'%s' % self.number, 'rb') as f:
            data = pickle.load(f)
            print(data)
            return data

class Teacher(OldboyPeople):
    def __init__(self, grade, salary):
        self.grade = grade
        self.salary = salary

class Student(OldboyPeople):
    def __init__(self, classes, course):
        self.classes = classes
        self.course = course

# stu = Student('Zane', 'male', 20, '上海一期班', 'Python全栈课程')
# stu.tell_info()
# stu.save()
# stu.get_obj_by_id()
#
# stu = Student('Zane', 'male', 20, '上海一期班', 'Python全栈课程')
# stu.tell_info()
# stu.save()
# stu.get_obj_by_id()

# 12、基于面向对象设计一个对战游戏并使用继承优化代码，参考博客
# http: // www.cnblogs.com / linhaifeng / articles / 7340497.
# html  # _label1
#
