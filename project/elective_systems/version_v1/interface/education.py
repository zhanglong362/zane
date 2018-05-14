# -*- coding: utf-8-*-

from db.handler import Db
from lib.common import Common

logger = Common.get_logger('education')


class Base(Db, Common):
    @classmethod
    def get_object(cls, type_name=None):
        data = cls.read()
        if type_name:
            return data[type_name]
        return data

    @classmethod
    def update_object(cls, type_name, desc, obj):
        data = cls.read()
        data[type_name][obj.name] = obj
        cls.write(data)
        logger.info('更新%s %s 信息成功！ ' % (desc, obj.name))

class Manager(Base):
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @classmethod
    def initialize_db(cls):
        data = {
            'schools': {},
            'classes': {},
            'course': {},
            'teachers': {},
            'admin': {},
            'students': {}
        }
        cls.write(data)

    @classmethod
    def remove_object(cls, type_name, desc, obj):
        data = cls.read()
        data[type_name].pop(obj.name)
        cls.write(data)
        logger.info('删除%s %s 信息成功！ ' % (desc, obj.name))

class School(Base):
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.classes = []
        self.course = []
        self.teacher = []
        self.student = []

class Teacher(Base):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.school = None
        self.classes = None

class Course(Base):
    def __init__(self, name, price, cycle):
        self.name = name
        self.price = price
        self.cycle = cycle

class Classes(Base):
    def __init__(self, name):
        self.name = name
        self.teacher = None
        self.course = None
        self.school = None
        self.students = {}

class Student(Base):
    def __init__(self, name, password):
       self.name = name
       self.password = password
       self.school = None
       self.classes = None
       self.tuition = 0
       self.score = 0
