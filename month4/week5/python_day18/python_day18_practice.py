# 4月10号作业
# 1、编写用户认证功能，要求如下
#     1.1、对用户密码加盐处理
#     1.2、用户名与密文密码存成字典，是以json格式存到文件中的
#     1.3、要求密用户输入明文密码，但程序中验证的是密文
import json
import hmac

def file_handle_read(name):
    try:
        with open(r'%s.json' % name, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print('\033[31merror: %s\033[0m' % e)
        return
    else:
        return data

def file_handle_write(**kwargs):
    try:
        with open(r'%s.json' % kwargs['name'], 'w', encoding='utf-8') as f:
            json.dump(kwargs, f)
    except Exception as e:
        print('\033[31merror: %s\033[0m' % e)
        return
    else:
        return True


def get_user_info_api(name):
    return file_handle_read(name)

def user_register_api(name, pwd):
    user_info = {
        'name': name,
        'pwd': pwd,
        'balance': 0
    }
    file_handle_write(**user_info)

def get_hmac_api(string, salt=b'bingo'):
    h = hmac.new(salt)
    h.update(string.encode('utf-8'))
    return h.hexdigest()

def register():
    while True:
        print('\033[32m请输入注册信息:\033[0m')
        name = input('用户名 >>: ').strip()
        pwd = input('密码 >>: ')
        pwd2 = input('确认密码 >>: ')
        if pwd != pwd2:
            print('两次密码输入不一致！')
            continue
        user_register_api(name, get_hmac_api(pwd))
        print('用户注册成功！')
        return True

def login():
    while True:
        print('\033[32m请输入登陆信息:\033[0m')
        name = input('用户名 >>: ').strip()
        user_info = get_user_info_api(name)
        if not user_info:
            print('用户不存在！')
            continue
        pwd = input('密码 >>: ')
        if get_hmac_api(pwd) != user_info['pwd']:
            print('密码错误！')
            continue
        print('登陆成功！')
        return True

# register()
# login()

# 2、编写功能，传入文件路径，得到文件的hash值
import hashlib

def get_hashlib_md5_api(file_path):
    m = hashlib.md5()
    try:
        with open(r'%s' % file_path) as f:
            for line in f:
                m.update(line.encode('utf-8'))
    except Exception as e:
        print('\033[31merror: %s\0m' % e)
        return
    else:
        return m.hexdigest()

md5_code = get_hashlib_md5_api('egon.json')
print('md5: %s' % md5_code)

# 3、编写类cmd的程序，要求
#     1、先验证用户身份
#     2、认证通过后，用户输入命令，则将命令保存到文件中
import time
import subprocess

CURRENT_USER = None
USER_INFO = {
    'egon': {
        'pwd': '123'
    }
}

def file_handle_write(file_path, command_dic):
    try:
        with open(r'%s' % file_path, 'w', encoding='utf-8') as f:
            json.dump(command_dic, f)
    except Exception as e:
        print('error: %s' % e)
        return
    else:
        return True

def excute_command_api(cmd):
    res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, \
                           stderr=subprocess.PIPE)
    stdout = res.stdout.read()
    stderr = res.stderr.read()
    # print('stdout: %s' % stdout)
    # print('stderr: %s' % stderr)
    command_info = {
        'command': cmd,
        'runtime': time.time(),
        'stdout': stdout.decode('utf-8'),
        'stderr': stderr.decode('utf-8')
    }
    data = file_handle_read('command.json')
    print('data: %s' % data)
    if data and CURRENT_USER in data:
        data[CURRENT_USER].append(command_info)
    else:
        data[CURRENT_USER] = [command_info]
    file_handle_write('command.json', data)

def commandline():
    while True:
        cmd = input('请输入命令 >>: ').strip()
        if cmd == 'quit':
            print('Goodbye!')
            return
        excute_command_api(cmd)

def login():
    global CURRENT_USER
    while True:
        print('登陆cmd程序！')
        name = input('name >>: ').strip()
        pwd = input('passwrod >>: ')
        if name not in USER_INFO:
            print('user not exist!')
            continue
        if pwd != USER_INFO[name]['pwd']:
            print('password not valid!')
            continue
        print('login successful!')
        CURRENT_USER = name
        commandline()
        return

# login()

# 4、如果我让你编写一个选课系统，那么有如下对象，请抽象成类，然后在程序中定义出来
#     4.1 老男孩有两所学校：北京校区和上海校区
#     4.2 老男孩学校有两们课程：python和linux
#     4.3 老男孩有老师：egon，alex，lxx，wxx，yxx
#     4.3 老男孩有学生：。。。
#     4.4 老男孩有班级：python全栈开发1班，linux高级架构师2班

class Teacher:
    school = 'OldBoy'

    def __init__(self, name, team, school_zone='上海', course='python'):
        self.name = name
        self.team = team
        self.school_zone = school_zone
        self.course = course

    def teach(self):
        print('%s teach %s ...' % (self. name.capitalize(), self.course))

class Student:
    school = 'OldBoy'

    def __init__(self, name, team, school_zone='上海', course='python'):
        self.name = name
        self.team = team
        self.school_zone = school_zone
        self.course = course

    def learn(self):
        print('%s learn %s ...' % (self. name.capitalize(), self.course))

print('='*30)
egon = Teacher(name='egon', team='全栈开发1班')
print(egon.school)
print(egon.name)
print(egon.school_zone)
print(egon.team)
print(egon.course)
egon.teach()

print('-'*30)
alex = Teacher(name='alex', team='全栈开发1班', school_zone='北京')
print(alex.school)
print(alex.name)
print(alex.school_zone)
print(alex.team)
print(alex.course)
alex.teach()

print('-'*30)
zane = Student(name='zane', team='全栈开发1班')
print(zane.school)
print(zane.name)
print(zane.school_zone)
print(zane.team)
print(zane.course)
zane.learn()
print('='*30)


