# 子类可以继承父类的属性和方法；
class OldboyPeople:
    school = 'Oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class OldboyTeacher(OldboyPeople):
    def change_student_score(self, score):
        print('Teacher %s is changeing score. %s' % (self.name, score))

class OldboyStudent(OldboyPeople):
    def choose_course(self, course):
        print('Student %s is choosing course. %s' % (self.name, course))


t1 = OldboyTeacher('Egon', 18, 'male')
stu1 = OldboyStudent('Zane', 20, 'male')

t1.change_student_score(90)
stu1.choose_course('Python全栈')

# 子类定义了和父类相同的属性或方法，会覆盖父类中的属性或方法；
class Foo:
    def f1(self):
        print('Foo.f1 ...')

    def f2(self):
        print('Foo.f2 ...')
        self.f1()

class Bar(Foo):
    def f1(self):
        print('Bar.f1 ...')

obj = Bar()
obj.f2()

# 类的派生
class OldboyPeople:
    school = 'Oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def f1(self):
        print('OldboyPeople.f1 ...')

class OldboyTeacher(OldboyPeople):
    def __init__(self, name, age, sex, grade, salary):
        self.name = name
        self.age = age
        self.sex = sex

        self.grade = grade
        self.salary = salary

    def get_teacher_info(self):
        print('''=======Teacher info=======
        
        name: %s
        age: %s
        sex: %s
        grade: %s
        salary: %s\n==========================
        ''' % (self.name, self.age, self.sex, self.grade, self.salary))

    def change_student_score(self, score):
        print('Teacher %s is changeing score. %s' % (self.name, score))

    def f1(self):
        print('OldboyTeacher.f1 ...')

class OldboyStudent(OldboyPeople):
    def choose_course(self, course):
        print('Student %s is choosing course. %s' % (self.name, course))

t1 = OldboyTeacher('Egon', 18, 'male', '特级教师', '5w')
t1.get_teacher_info()
t1.f1()

# 在子类派生中的新方法中，重用父类的功能：
# 1. 指名道姓的调用；（和继承无关）
# class OldboyPeople:
#     school = 'Oldboy'
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def f1(self):
#         print('OldboyPeople.f1 ...')
#
#     def get_teacher_info(self):
#         print('''=======Teacher info=======
#         name: %s
#         age: %s
#         sex: %s
#         ''' % (self.name, self.age, self.sex))
#
#
# class OldboyTeacher(OldboyPeople):
#     def __init__(self, name, age, sex, grade, salary):
#         OldboyPeople.__init__(self, name, age, sex)
#         self.grade = grade
#         self.salary = salary
#
#     def get_teacher_info(self):
#         OldboyPeople.get_teacher_info(self)
#         print('''
#         grade: %s
#         salary: %s
#         ''' % (self.grade, self.salary))
#
#     def change_student_score(self, score):
#         print('Teacher %s is changeing score. %s' % (self.name, score))
#
#     def f1(self):
#         print('OldboyTeacher.f1 ...')
#
#
# class OldboyStudent(OldboyPeople):
#     def choose_course(self, course):
#         print('Student %s is choosing course. %s' % (self.name, course))
#
#
# t1 = OldboyTeacher('Egon', 18, 'male', '特级教师', '5w')
# t1.get_teacher_info()
# t1.f1()
# 2. 使用 super 调用:（严格依赖于继承）
#     super() 的返回值是一个特殊的对象，该对象专门用来调用父类中的属性；
#     python2 中调用方式：super(, self)
class OldboyPeople:
    school = 'Oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def f1(self):
        print('OldboyPeople.f1 ...')

    def get_teacher_info(self):
        print('''
        name: %s
        age: %s
        sex: %s''' % (self.name, self.age, self.sex))


class OldboyTeacher(OldboyPeople):
    def __init__(self, name, age, sex, grade, salary):
        super().__init__(name, age, sex)
        self.grade = grade
        self.salary = salary

    def get_teacher_info(self):
        super().get_teacher_info()
        print('''
        grade: %s
        salary: %s
        ''' % (self.grade, self.salary))

    def change_student_score(self, score):
        print('Teacher %s is changeing score. %s' % (self.name, score))

    def f1(self):
        print('OldboyTeacher.f1 ...')


class OldboyStudent(OldboyPeople):
    def choose_course(self, course):
        print('Student %s is choosing course. %s' % (self.name, course))


t1 = OldboyTeacher('Egon', 18, 'male', '特级教师', '5w')
t1.get_teacher_info()
t1.f1()

# 打印属性查找顺序
print(OldboyTeacher.mro())

# super() 方法的继承，严格按照继承关系查找；
class A:
    def test(self):
        print('from A ...')
        super().test()
    pass

class B:
    def test(self):
        print('from B ...')
    pass

class C(A, B):
    pass

c = C()
c.test()
print(C.mro())


