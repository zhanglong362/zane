# 4.8号作业
# 1、复习常用模块time、datetime、random、os、sys、shutil、json、pickle、logging编写博客
# 2、编写认证功能装饰器，同一用户输错三次密码则锁定5分钟，5分钟内无法再次登录
import sys
import datetime

LOCK_USER = {}
USER_INFO = {
    'name': 'egon',
    'password': '123'
}

def auth(func):
    def wrapper(*args, **kwargs):
        name = func(*args, **kwargs)
        if name in LOCK_USER:
            if datetime.datetime.now() < LOCK_USER[name]:
                print('用户%s在%s内锁定，禁止登陆！' % (name, LOCK_USER[name]))
                sys.exit()
        print('用户%s登陆成功！' % CURRENT_USER)
    return wrapper

@auth
def login():
    i = 0
    while True:
        name = input('name >>: ').strip()
        password = input('password >>: ')
        if name != USER_INFO['name']:
            print('用户%s不存在！' % name)
            continue
        if password != USER_INFO['password']:
            print('用户%s密码错误！' % name)
            i += 1
            if i == 3:
                LOCK_USER[name] = datetime.datetime.now() + datetime.timedelta(seconds=30)
            continue
        return name

login()

# 3、编写注册功能，用户输入用户名、性别、年龄、密码。。。还需要输入一个随机验证码，若用户在60秒内输入验证码错误
# 则产生新的验证码要求用户重新输入，直至输入正确，则将用户输入的信息以json的形式存入文件
import json
import random
import datetime

RANDOM_CODE = {}

def make_code(n):
    res = ''
    for i in range(n):
        s1 = chr(random.randint(65, 90))
        s2 = str(random.randint(0,9))
        res += random.choice([s1, s2])
    return res

def register():
    global RANDOM_CODE
    name = input('name >>: ').strip()
    pwd = input('password >>: ')
    sex = input('sex >>: ').strip()
    age = input('age >>: ').strip()
    user_info = {
        'name': name,
        'password': pwd,
        'sex': sex,
        'age': age
    }
    random_code = None
    while True:
        if random_code in RANDOM_CODE:
            if datetime.datetime.now() > RANDOM_CODE[random_code]:
                random_code = make_code(4)
                RANDOM_CODE[random_code] = datetime.datetime.now() + datetime.timedelta(seconds=10)
        else:
            random_code = make_code(4)
            RANDOM_CODE[random_code] = datetime.datetime.now() + datetime.timedelta(seconds=10)
        print('identifying code: %s' % random_code)
        code = input('Please input identifying code >>: ').strip()
        if code == random_code:
            with open(r'user.json', 'w', encoding='utf-8') as f:
                json.dump(user_info, f)
            print('user %s register successful!' % name)
            return True

register()

# 4、编写进度条功能
import time

def progress(percent, width=100):
    if percent > 1:
        percent = 1
    show = ('[%%-%ds]' % width) % (int(width*percent)*'#')
    print('%s %s%%' % (show, int(100*percent)), end='\r')

def download():
    recv_size = 0
    file_size = 10000
    while recv_size < file_size:
        recv_size += 10
        percent = recv_size / file_size
        progress(percent)
        time.sleep(0.1)

download()

# 5、明日默写：生成随机验证码功能、打印进度条功能