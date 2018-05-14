# -*- encoding: utf-8 -*-
# 1、定义学校类，实例化出：北京校区、上海校区两个对象
#     校区独有的特征有：
#         校区名 = 'xxx'
#         校区地址 = {'city': "所在市", 'district': '所在的区'}
#         多们课程名 = ['xxx', 'yyy', 'zzz']
#         多个班级名 = ['xxx', 'yyy', 'zzz']
#
#     校区可以：
#         1、创建班级
#         2、查看本校区开设的所有班级名
#         3、创建课程
#         4、查看本校区开设的所有课程名
class School:
    def __init__(self, name, city, district):
        self.name = name
        self.city = city
        self.district = district
        self.classes = []
        self.course = []

    def get_school_info(self):
        print('''
        校区：%s
        城市：%s
        分区：%s
        ''' % (self.name, self.city, self.district))

    def get_classes_info(self):
        print('%s 校区的所有班级 %s' % (self.name, self.classes))

    def get_course_info(self):
        print('%s 校区的所有班级 %s' % (self.name, self.course))

    def add_classes_api(self, classes):
        self.classes.append(classes)
        print('增加新班级 "%s" 成功！' % classes)

    def add_course_api(self, course):
        self.course.append(course)
        print('增加新课程 "%s" 成功！' % course)

print('-'*50)
print('\n\033[31m第一题:\033[0m')
s = School('老男孩上海', '上海市', '浦东新区')
s.get_school_info()
s.add_classes_api('上海一期班')
s.add_course_api('Python全栈课程')
s.get_classes_info()
s.get_course_info()

s = School('老男孩北京', '北京市', '朝阳区')
s.get_school_info()
s.add_classes_api('北京二十一期班')
s.add_course_api('Python全栈课程')
s.get_classes_info()
s.get_course_info()
print('-'*50)

# 2、定义出班级类，实例化出两个班级对象
#     班级对象独有的特征：
#         班级名 ='xxx'
#         所属校区名 ='xxx'
#         多门课程名 = ['xxx', 'yyy', 'zzz']
#         多个讲师名 = ['xxx', 'xxx', 'xxx']
#
#     班级可以：
#         1、查看本班所有的课程
#         2、查看本班的任课老师姓名
class Classes:
    def __init__(self, school, name, course, teacher):
        self.school = school
        self.name = name
        self.course = course
        self.teacher = teacher

    def get_course(self):
        print('%s 的所有课程 %s' % (self.name, self.course))

    def get_teacher(self):
        print('%s 的所有老师 %s' % (self.name, self.teacher))

print('\n\033[31m第二题:\033[0m')
c1 = Classes('老男孩上海', '上海一期班', ['Python全栈课程', 'Linux运维'], ['Egon'])
c1.get_course()
c1.get_teacher()
print('-'*50)

# 3、定义课程类，实例化出python、linux、go三门课程对象
#     课程对象独有的特征：
#         课程名 =‘xxx’
#         周期 =‘3months’
#         价格 = 3000
#
#     课程对象可以：
#         1、查看课程的详细信息
class Course:
    def __init__(self, name, cycle, price):
        self.name = name
        self.cycle = cycle
        self.price = price

    def get_course_info(self):
        print('%s 课程的周期是 %s，费用是 %s 元。' % (self.name, self.cycle, self.price))

print('\n\033[31m第三题:\033[0m')
course = Course('Python全栈', '5 months', 19800)
course.get_course_info()
print('-'*50)

# 4、定义学生类，实例化出张铁蛋、王三炮两名学生对象
#     学生对象独有的特征：
#         学号 = 10
#         名字 =”xxx“
#         班级名 = ['xxx', 'yyy']
#         分数 = 33
#
#     学生可以：
#         1、选择班级
#         3、注册，将对象序列化到文件
print('\n\033[31m第四题:\033[0m')
import json

class Student:
    def __init__(self, school, name, student_id, classes, course, score):
        self.school = school
        self.name = name
        self.student_id = student_id
        self.classes = classes
        self.course = course
        self.score = score

    def get_student_info(self):
        print('''
        学校：%s
        名字：%s
        学号：%s
        班级：%s
        课程：%s
        成绩：%s
        ''' % (self.school,
               self.name,
               self.student_id,
               self.classes,
               self.course,
               self.score
        ))

    def choose_classes(self, classes):
        self.classes = classes
        print('学生"%s"转班到"%s"成功！' % (self.name, self.classes))

    def register_student(self):
        student_info = {
            'school': self.school,
            'name': self.name,
            'student_id': self.student_id,
            'classes': self.classes,
            'score': self.score
        }
        self._file_handler_write(student_info)
        print('学生%s注册成功！' % self.name)

    def _file_handler_write(self, student_info):
        with open(r'%s.json' % student_info['name'], 'w') as f:
            json.dump(student_info, f)

stu1 = Student('老男孩上海', 'zane', '0521', '一期班', 'Python全栈周末', '90')
stu1.get_student_info()
stu1.choose_classes('Python全栈脱产')
stu1.register_student()
print('-'*50)

# 5、定义讲师类，实例化出egon，lqz，alex，wxx四名老师对象
#     老师对象独有的特征：
#         名字 =“xxx”
#         等级 =“xxx”
#
#     老师可以：
#         1、修改学生的成绩
print('\n\033[31m第五题:\033[0m')
import json

class Teacher:
    def __init__(self, school, name, classes, course, grade):
        self.school = school
        self.name = name
        self.classes = classes
        self.course = course
        self.grade = grade

    def get_teacher_info(self):
        print('''
        校区：%s
        名字：%s
        班级：%s
        课程：%s
        职级：%s
        ''' % (self.school,
               self.name,
               self.classes,
               self.course,
               self.grade))

    def modify_student_score(self, student, score):
        student_info = self._file_handler_read(student.name)
        student_info['score'] = score
        self._file_handler_write(student_info)
        print('"%s"老师修改学生"%s"的成绩"%s"成功！' % (self.name, student.name, score))

    def _file_handler_read(self, name):
        with open(r'%s.json' % name) as f:
            return json.load(f)

    def _file_handler_write(self, student_info):
        with open(r'%s.json' % student_info['name'], 'w') as f:
            json.dump(student_info, f)

t = Teacher('老男孩上海', 'Egon', '一期班', 'Python全栈', '特级教师')
t.get_teacher_info()
t.modify_student_score(stu1, 95)
print('-'*50)


