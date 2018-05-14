# -*- encoding: utf-8 -*-

from db import db_handler


class Base:
    @classmethod
    def get_obj_by_name(cls, name):
        return db_handler.select(name, cls.__name__)

    def save(self):
        db_handler.save(self)

class Admin(Base):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.save()

    def create_school(self, name, addr):
        school = School(name, addr)
        school.save()

    def create_teacher(self, name, password):
        teacher = Teacher(name, password)
        teacher.save()

    def create_course(self, name, price, cycle, school):
        course = Course(name, price, cycle, school)
        course.save()

class School(Base):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr



