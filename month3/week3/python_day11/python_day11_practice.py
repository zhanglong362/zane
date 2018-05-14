# 3-29 作业
# 一：编写一个有参和一个无参函数，然后实现下列装饰器
# 二：编写装饰器，为函数加上统计时间的功能
# 三：编写装饰器，为函数加上认证的功能
#
# 四：编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
# 注意：从文件中读出字符串形式的字典，可以用eval('{"name":"egon","password":"123"}')转成字典格式
#
# 五：编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录
#
# 六：编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
#
# 七：为题目五编写装饰器，实现缓存网页内容的功能：
# 具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，否则，就去下载，然后存到文件中
#
# 扩展功能：用户可以选择缓存介质/缓存引擎，针对不同的url，缓存到不同的文件中
#
# 八：还记得我们用函数对象的概念，制作一个函数字典的操作吗，来来来，我们有更高大上的做法，在文件开头声明一个空字典，然后在每个函数前加上装饰器，完成自动添加到字典的操作
#
# 九 编写日志装饰器，实现功能如：一旦函数f1执行，则将消息2017-07-21 11:12:11 f1 run写入到日志文件中，日志文件路径可以指定
# 注意：时间格式的获取
# import time
# time.strftime('%Y-%m-%d %X')

import datetime
from urllib.request import urlopen

config = 'db.txt'
with open(r'%s' % config, 'a') as f:
    pass

def get_config():
    users = {}
    with open(r'%s' % config) as f:
        data = f.read().split('\n')
        for u in data:
            users.update(eval(u))
    return users

def auth(func):
    def wrapper(*args, **kwargs):
        if not name in users:
            print('用户不存在！')
            return
        if password != users[name]['password']:
            print('密码错误！')
            return
        if name in users and password == users[name]['password']:
            dt = users[name]['logintime']
            dt = datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
            alert_time = dt + datetime.timedelta(minutes=5)
            now = datetime.datetime.now()
            if now > alert_time:
                print('登陆已超时，请重新登陆！')
                return
            if users[name]['logintime']
            print('认证通过！')
            with open(r'config' % config) as f1, \
                    open(r'%s.swap' % config, 'w') as f2:
                for line in f1:
                    if name in line:
                        line = eval(line.strip('\n'))
                        line['logintime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        line = '%s\n' % line
                    f2.write(line)
            res = func(*args, **kwargs)
            return res
    return wrapper

def timmer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print('Run time is %s' % (stop_time - start_time))
        return res
    return wrapper

def cache(engine):
    def handler(func):
        def wrapper(*args, **kwargs):
            if engine == 'baidu':
                cache_file = 'baidu.txt'
            elif engine == 'google':
                cache_file = 'google.txt'
            with open(r'%s' % cache_file) as f:
                data = f.read()
                if data:
                    return data
            res = func(*args, **kwargs)
            with open(r'%s' % cache_file, 'w') as f
                f.write(res)
            return res
        return wrapper
    return handler

@auth
@timmer
def index():
    print('This is function index!')
    return 'function index!'

@auth
@timmer
def home(name):
    print('Hi, %s. This is function home!' % name)
    return 'function home!'

@auth
@cache(engine)
@timmer
def get_site_page(url):
    return urlopen(url).read()

def main():
    index = index()
    print('index: ' % index)
    home = home('egon')
    print('home: %s' % home)
    baidu = get_site_page(url)
    print('baidu: %s' % baidu)

if __name__ == "__main__":
    while True:
        engine = 'baidu'
        url = 'http://www.baidu.com'
        users = get_config()
        name = input('name >>: ').strip()
        password = input('password >>: ').strip()
        main()