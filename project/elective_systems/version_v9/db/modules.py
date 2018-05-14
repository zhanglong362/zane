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
        school = School.get_obj_by_name(school_name)
        school.set_up_course(name)
        course = Course(name, price, cycle, school_name)
        if school.save() and course.save():
            return True

class School(Base):
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.course_list = []

    def get_school_course(self):
        return self.course_list

    def set_up_course(self, name):
        self.course_list.append(name)
        return self.save()

class Teacher(Base):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.course_list = []

    def get_teacher_course(self):
        return self.course_list

    def set_up_course(self, course_name):
        self.course_list.append(course_name)
        return self.save()

class Course(Base):
    def __init__(self, name, price, cycle, school_name):
        self.name = name
        self.price = price
        self.cycle = cycle
        self.student_list = []
        self.school_name = school_name

    def get_course_student_list(self):
        return self.student_list

    def add_course_student(self, student_name):
        self.student_list.append(student_name)
        return self.save()

class Student(Base):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.school_list = []
        self.course_list = []
        self.score = {}

    @classmethod
    def register(cls, name, password):
        student = cls(name, password)
        return student.save()

    def get_student_course(self):
        return self.course

    def get_student_score(self):
        return self.score

    def set_student_score(self, course, score):
        self.score[course] = score
        return self.save()

    def choose_student_school(self, school_name):
        self.school_list.append(school_name)
        return self.save()

    def set_student_course(self, course_name, school_name):
        self.course_list.append(course_name)
        self.school_list.append(school_name)
        self.score[course_name] = 0
        return self.save()








