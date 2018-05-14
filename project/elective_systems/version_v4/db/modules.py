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
        self.save()

    def create_school(self, school_name, address):
        school = School(school_name, address)
        return school.save()

    def create_teacher(self, teacher_name, teacher_password):
        teacher = Teacher(teacher_name, teacher_password)
        return teacher.save()

    def create_course(self, course_name, course_price, course_cycle, school_name):
        course = Course(course_name, course_price, course_cycle, school_name)
        return course.save()

class School(Base):
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return '学校名称：%s \n学校地址：%s' % (self.name, self.address)

class Teacher(Base):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.course = []

    def __str__(self):
        return '老师名字：%s \n老师教授的课程：%s' % (self.name, self.course)

class Course(Base):
    def __init__(self, name, price, cyle, school_name):
        self.name = name
        self.price = price
        self.cyle = cyle
        self.school_name = school_name

    def __str__(self):
        return '课程名称：%s\n课程价格：%s\n课程周期：%s\n学校校区：%s' % (
            self.name, self.price, self.cyle, self.school_name
        )







