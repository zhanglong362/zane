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
        admin = cls(name, password)
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
        self.password = address
        self.course_list = []

    def set_up_course(self, course):
        self.course_list.append(course)
        return self.save()

class Teacher(Base):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.course_list = []

    def get_course_list(self):
        return self.course_list

    def choose_course(self, name):
        self.course_list.append(name)
        return self.save()

class Course(Base):
    def __init__(self, name, price, cycle, school_name):
        self.name = name
        self.price = price
        self.cycle = cycle
        self.school_name = school_name
        self.student_list = []

    def get_student_list(self):
        return self.student_list

class Student(Base):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.course_list = []
        self.score = {}
        self.school_list = []

    @classmethod
    def register(cls, name, password):
        student = cls(name, password)
        return student.save()

    def choose_course(self, course):
        self.course_list.append(course)
        course_info = Course.get_obj_by_name(course)
        self.school_list.append(course_info.school_name)
        return self.save()

    def change_score(self, course, score):
        self.score[course] = score
        return self.save()





