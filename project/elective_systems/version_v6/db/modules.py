# -*- encoding: utf-8 -*-

from db import db_handler

class Base:
    @classmethod
    def get_obj_by_name(cls, name):
        return db_handler.select(name, cls.__name__.lower())

    def save(self):
        return db_handler.save(self)

class Admin(Base):
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @classmethod
    def register(cls, name, password):
        admin = Admin(name, password)
        return admin.save()

    def create_school(self, name, address):
        school = School(name, address)
        return school.save()

    def create_teacher(self, name, password):
        teacher = Teacher(name, password)
        return teacher.save()

    def create_course(self, name, price, cycle, school_name):
        course = Course(name, price, cycle, school_name)
        return course.save()

class School(Base):
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return '校区：%s 地址：%s' % (self.name, self.address)

class Teacher(Base):
    def __init__(self, name, password):
        self.name = name
        self.address = password
        self.course = []

    def __str__(self):
        return '名字：%s 课程：%s' % (self.name, self.course)

class Course(Base):
    def __init__(self, name, price, cycle, school_name):
        self.name = name
        self.price = price
        self.cycle = cycle
        self.school_name = school_name

    def __str__(self):
        return '课程：%s 价格：%s 周期：%s 校区：%s' % (self.name, self.price, self.cycle, self.school_name)

class Student(Base):
    def __init__(self, name):
        self.name = name










