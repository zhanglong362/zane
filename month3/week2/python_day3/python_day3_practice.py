1. python test.py执行的三个阶段是什么？在哪个阶段识别文件内的python语法？
    第一阶段：启动 python 解释器；
    第二阶段：将 python 程序的代码读入内存；
    第三阶段：python 解释器，解释执行内存中读入的 python 程序代码；（在执行前先检查语法）

2. 将下述两个变量的值交换
    s1='alex'
    s2='SB'
    s1, s2 = s2, s1

3. 判断下述结果
    msg1='alex say my name is alex,my age is 73,my sex is female'
    msg2='alex say my name is alex,my age is 73,my sex is female'
    msg1 is msg2
    msg1 == msg2

    如果两个结果都是 True，则是 Python 做了优化；
    如果第一个结果是 False，则是 Python 没有优化；

4. 什么是常量？在python中如何定义常量？
    程序运行过程中不允许改变的量称为常量。Python 中用全部大写字母作为常量的名称，但 python 中没有真正的常量。

5. 有存放用户信息的列表如下，分别存放用户的名字、年龄、公司信息
    userinfo={
        'name':'egon',
        'age':18,
        'company_info':{
            'cname':'oldboy',
            'addr':{
                'country':'China',
                'city':'Shanghai',
            }
        }

    }
    a. 要求取出该用户公司所在的城市？
        city = userinfo['company_info']['addr']['city']

    students=[
        {'name':'alex','age':38,'hobbies':['play','sleep']},
        {'name':'egon','age':18,'hobbies':['read','sleep']},
        {'name':'wupeiqi','age':58,'hobbies':['music','read','sleep']},
    ]
    取第二个学生的第二个爱好？
        second_hobby = students[1]['hobbies'][1]

6. students=[
        {'name':'egon','age':18,'sex':'male'},
        {'name':'alex','age':38,'sex':'fmale'},
        {'name':'wxx','age':48,'sex':'male'},
        {'name':'yuanhao','age':58,'sex':'fmale'},
        {'name':'liwenzhou','age':68,'sex':'male'},
]
    要求循环打印所有学生的详细信息，格式如下
        <name:egon age:18 sex:male>
        <name:alex age:38 sex:fmale>
        <name:wxx age:48 sex:male>
        <name:yuanhao age:58 sex:fmale>
        <name:liwenzhou age:68 sex:male>


    students=[
        {'name':'egon','age':18,'sex':'male'},
        {'name':'alex','age':38,'sex':'fmale'},
        {'name':'wxx','age':48,'sex':'male'},
        {'name':'yuanhao','age':58,'sex':'fmale'},
        {'name':'liwenzhou','age':68,'sex':'male'},
    ]
    for std in students:
        s = '<name:%s age:%s sex:%s>'
        print(s % (std['name'], std['age'], std['sex']))

7. 编写程序，根据用户输入内容打印其权限:
    '''
    egon --> 超级管理员
    tom  --> 普通管理员
    jack,rain --> 业务主管
    其他 --> 普通用户
    '''

    user_info = {
        'egon': '超级管理员',
        'tom': '普通管理员',
        'jack': '业务主管',
        'rain': '业务主管'
    }
    while True:
        name = input('username>>: ')
        if name in user_info:
            print('用户 %s 权限：%s' % (name, user_info[name]))
        else:
            print('用户 %s 权限：普通用户' % name)

8. 编写程序，实现如下功能:
    如果:今天是Monday,那么:上班
    如果:今天是Tuesday,那么:上班
    如果:今天是Wednesday,那么:上班
    如果:今天是Thursday,那么:上班
    如果:今天是Friday,那么:上班
    如果:今天是Saturday,那么:出去浪
    如果:今天是Sunday,那么:出去浪

    plan = {
        '上班': [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
        '出去浪':['Saturday', 'Sunday']
    }
    while True:
        today = input('What day is today>>: ')
        for k,v in plan.items():
            if today in v:
                print('今天是 %s, %s。' % (today, k))

9. while循环练习:
    #1. 使用while循环输出1 2 3 4 5 6 8 9 10
    #2. 求1-100的所有数的和
    #3. 输出 1-100 内的所有奇数
    #4. 输出 1-100 内的所有偶数
    #5. 求1-2+3-4+5 ... 99的所有数的和
    #6. 用户登陆（三次机会重试）
    #7：猜年龄游戏
    要求：
        允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出
    #8：猜年龄游戏升级版
    要求：
        允许用户最多尝试3次
        每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，如果回答N或n，就退出程序
        如何猜对了，就直接退出

    1)
    i = 1
    while i <= 10:
        print(i)
        i += 1

    2)
    sum = 0
    i = 1
    while i <= 100:
        sum += i
        i += 1
    print('sum is %s' % sum)

    3)
    i = 1
    while i <= 100:
        n = i%2
        if n == 1:
            print('奇数 %s' % i)
        i += 1

    4)
    i = 1
    while i <= 100:
        n = i % 2
        if n == 0:
            print('偶数 %s' % i)
        i += 1

    5)
    sum = 0
    i = 1
    while i <= 100:
        n = i % 2
        if n == 1:
            sum += i
        if n == 0:
            sum -= i
        i += 1
    print('sum is %s' % sum)

    6)
    user_info = {
        'egon': '123'
    }
    i = 0
    while True:
        name = input('username>>: ')
        pwd = input('password>>: ')
        if name not in user_info:
            print('用户登录名错误！')
            i += 1
        else:
            if pwd != user_info[name]:
                print('用户密码错误')
                i += 1
        if i == 3:
            print('Try too many times!')
            break
        if name in user_info and pwd == user_info[name]:
            print('login successful!')
            break

    7)
    age = 18
    i = 0
    while True:
        inp_age = input("egon's age is ?>>: ")
        inp_age = int(inp_age)
        if inp_age > age:
            print('猜大了！')
            i += 1
        if inp_age < age:
            print('猜小了')
            i += 1
        if i == 3:
            print('Try too many times!')
            break
        if inp_age == age:
            print('恭喜你猜对了 egon 的年龄！')
            break

    8)
    age = 18
    i = 0
    while True:
        inp_age = input("egon's age is ?>>: ")
        inp_age = int(inp_age)
        if inp_age > age:
            print('猜大了！')
            i += 1
        if inp_age < age:
            print('猜小了')
            i += 1
        if i == 3:
            print('Do you want to continue playing？')
            action = input("Please input 'Y/y' or 'N/n'>>: ")
            if action == 'Y' or action == 'y':
                i = 0
            if action == 'N' or action == 'n':
                break
        if inp_age == age:
            print('恭喜你猜对了 egon 的年龄！')
            break
10. 编写计算器程序，要求
    #1、用户输入quit则退出程序
    #2、程序运行，让用户选择具体的计算操作是加法or乘法or除法。。。然后输入数字进行运算
    #3、简单示范如下，可以在这基础上进行改进
    while True:
        msg='''
        1 加法
        2 减法
        3 乘法
        4 除法
        '''
        print(msg)
        choice = input('>>: ').strip()
        num1 = input('输入第一个数字：').strip()
        num2 = input('输入第二个数字：').strip()
        if choice == '1':
            res=int(num1)+int(num2)
            print('%s+%s=%s' %(num1,num2,res))


    choose = '''1 加法 2 减法 3 乘法 4 除法 5 保留小数的除法 6 取余
    Please choose an opration >>: '''

    def check_number(n):
        if int(n):
            return (int(n))
        elif int(n):
            return (int(n))

    while True:
        o = input(choose)
        if o not in ['1', '2', '3', '4', '5', '6']:
            print('Please select the operation number correctly!')
            continue
        else:
            o = int(o)
        nums = input('Please enter two numbers >>: ')
        x, y = nums.split()
        x = check_number(x)
        y = check_number(y)
        if not x or not y:
            print('Please enter integers or floating-point numbers!')
            continue
        if o == 1:
            r = x + y
        if o == 2:
            r = x - y
        if o == 3:
            r = x * y
        if o == 4:
            r = x // y
        if o == 5:
            r = x / y
        if o == 6:
            r = x % y
        print('result: %s' %  r)
