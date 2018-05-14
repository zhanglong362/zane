#
# x = 1
#
# def outter(name):
#     def inner():
#         print(name)
#     return inner
#
# foo = outter('egon')
# bar = outter('alex')
# foo()
# bar()
#
import time
#
# def index():
#     time.sleep(2)
#     print('welcome to index page!')
#
# def home(name):
#     time.sleep(3)
#     print('welcome %s to home page!' % name)
#
# def wrapper(func):
#     start_time = time.time()
#     func()
#     stop_time = time.time()
#     print('run time is %s' % (stop_time - start_time))
#
# wrapper(index)                   # 修改了原函数的调用方式

import time

user_info = {
    'egon': {
        'password': '123'
    }
}

login_list = []
# name = input('name >>: ').strip()
# password = input('password >>: ').strip()
name = 'egon'
password = '123'

def auth(name, password):
    def wrapper(func):
        def wrapper(*args, **kwargs):
            if len(login_list) > 0:
                print('用户%s认证通过！' % name)
                res = func(*args, **kwargs)
                return res
            if name not in user_info:
                print('用户名不存在！')
                return
            if password != user_info[name]['password']:
                print('密码错误！')
                return
            print('用户%s认证通过！' % name)
            login_list.append(name)
            res = func(*args, **kwargs)
            return res
        return wrapper
    return wrapper

def timmer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print('Run time is %s' % (stop_time - start_time))
        return res
    return wrapper

@auth(name, password)
@timmer
def index():
    time.sleep(1)
    print('Welcome to Index Page!')
    return 123
@auth(name, password)
@timmer
def home(name):
    time.sleep(2)
    print('Welcome %s to Home Page!' % name)
    return 'home'

index()
print(home('alex'))











