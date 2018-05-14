# -*- encoding: utf-8 -*-

from db import db_handler


class Base:
    @classmethod
    def get_obj_by_name(cls, name):
        return db_handler.select(name, cls.__name__.lower())

    def save(self):
        db_handler.save(self)

class Admin(Base):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.save()

    def create_school(self, school_name, school_addr):
        school = School(school_name, school_addr)
        school.save()

    def create_teacher(self, teacher_name, teacher_pwd):
        teacher = Teacher(teacher_name, teacher_pwd)
        teacher.save()

    def create_course(self, course_name, course_price, course_cycle):
        course = Course(course_name, course_price, course_cycle)
        course.save()

class School(Base):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.course_name_list = []

class Teacher(Base):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.course_list = []

class Course(Base):
    def __init__(self, name, price, cycle):
        self.name = name
        self.price = price
        self.cycle = cycle
        self.student_name_list = []

class Student(Base):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.school = None
        self.course_list = []
        self.scores = {}
