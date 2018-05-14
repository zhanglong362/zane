'''
name='egon'
age=78
'''

# 数字类型：
# 整型：int
# 等级、年龄、身份证号、学号、id号
level=10    # level=int(10)
level=int(10)
#print(id(level), type(level), level)
age=18
empid=123

# 浮点数：float
# 身高、体重、薪资
salary=3.1
height=1.83

# 字符串: str 包含在引号（单引号、双引号、三引号）内的一串字符
# 用来表示：名字、家庭住址、描述性的数据
s1='egon'
s2="egon"
s3='''
egon
'''
s4="""
egon
"""
#print(s1, s2, s3, s4)

msg='hello "egon"'
msg="hello 'egon'"
#print(msg)

# 字符串拼接：+ *
s1='hello'
s2='world'
#print(s1+s2)
#print(s1*10)

# 列表：定义在[]中括号内用逗号分隔多个值，值可以是任意类型
# 用来存放多个值：多个爱好、多个人名
stu_names=['asb', 'egon', 'wsb']  # stu_names=list(['asb', 'egon', 'wsb'])
#print(id(stu_names), type(stu_names), stu_names)
#print(stu_names[0], stu_names[1])

user_info=['egon',18,['read', 'music', 'dancing', 'play']]
#print(user_info[1], user_info[2][1])

# 字典：定义在{}花括号内用逗号隔开，每一个元素都是key,value的形式，其中value可以是任意类型
user_info={'name': 'egon', 'age': 18, 'hobby': ['read', 'music', 'dancing', 'play']}
#print(id(user_info), type(user_info), user_info)

#print(user_info['age'])
#print(user_info['hobby'][3])

info={
    'name':'egon',
    'hobbies':['play','sleep'],
    'company_info':{
        'name':'Oldboy',
        'type':'education',
        'emp_num':40,
    }
}
#print(info['company_info']['name']) #取公司名


students=[
    {'name':'alex','age':38,'hobbies':['play','sleep']},
    {'name':'egon','age':18,'hobbies':['read','sleep']},
    {'name':'wupeiqi','age':58,'hobbies':['music','read','sleep']},
]
#print(students[1]['hobbies'][1]) #取第二个学生的第二个爱好

# 布尔类型：bool: True False
# 用途：判断
age_of_oldboy=18
#print(age>18)

#inp_age=input('your age: ')
#inp_age=int(inp_age)

#if inp_age > age_of_oldboy:
#    print('猜大了')
#elif inp_age < age_of_oldboy:
#    print('猜小了')
#else:
#    print('猜对了')

# 布尔值的重点知识，所有自带数据类型布尔值
# 1 只有三种类型的值为False: 0, None, 空
# 2 其余全为True

#if ['',]:
#    print('===>')


# 可变类型与不可变类型
# 可变：在id不变的情况，值可以改变，则称为可变类型，如列表、字典
# 不可变类型：值一旦改变，id也改变，则称为不可变类型（id变，意味着创建了新的内存空间），如数字、字符串
x=[1,2,3]
#print(id(x), type(x), x)
x[2]=6
#print(id(x), type(x), x)

dic={'x':'1', 'y':'2'}
#print(id(dic), type(dic), dic)
dic['x']=6
#print(id(dic), type(dic), dic)

line='-'*10
#name=input('名字： ')
#age=input('年龄： ')
#sex=input('性别： ')
#job=input('工作： ')
msg='''
%s info of %s %s
Name: %s
Age: %s
Sex: %s
Job: %s
%s end %s
'''
#print('My name is %s, age is %s' % ('John', 18))
#print(msg % (line, name, line, name, age, sex, job, line, line))

#print(10/3)
#print(10//3)
#print(10%3)
#print(3**3)

# 增量赋值
age=18
#age=age+1
age+=2    #age=age+2
age-=10
#print(age)


# 逻辑运算
# and：逻辑与，用于连接左右两个条件都为True的情况下，and运算的最终结果才是 True
#print(1>2 and 3>4)
#print(2>3 and 3>4)
#print(True and True and True and False)
#print(True or False and False)


sex='female'
age=20
is_beutiful=True
is_successful=True

#if sex == 'female' and age>18 and age<26 and is_beutiful:
#    print('表白...')
#    if is_successful:
#        print('在一起')
#    else:
#        print('表白失败')
#else:
#    print('阿姨好')

username='egon'
password='123'
name=input('name>>: ')
pwd=input('password>>: ')

tag=True
while tag:
    if name == username and pwd == password:
        print('login successful!')
        while tag:
            cmd=input('cmd>>: ')
            if cmd == 'quit':
                tag=False
                continue
                #break
            print('%s 命令在执行...' % cmd)
        #break
    else:
        print('name or password not valid')
    #print('====>')

'''
如果成绩>=90，那么：优秀
如果成绩>=80,那么：良好
如果成绩>=70,那么：普通
否则,那么：很差
'''

# score=input('score>>: ')
# score=int(score)
# if score >= 90:
#     print('优秀')
# elif score >= 80 and score < 90:
#     print('良好')
# elif score >= 70 and score < 80:
#     print('普通')
# elif score < 70:
#     print('很差')

# while：条件循环
# import time
# count=1
# while count <= 3:
#     print('====>', count)
#     count+=1
#     time.sleep(0.1)

# break: 跳出本层循环
# age_of_oldboy=18
# count=1
# while 1:
#     if count > 3:
#         print('try too many times')
#         break
#     inp_age=input('your age: ')
#     inp_age=int(inp_age)
#     if inp_age > age_of_oldboy:
#         print('猜大了')
#     elif inp_age < age_of_oldboy:
#         print('猜小了')
#     else:
#         print('猜对了')
#         break
#     print('猜的次数： ', count)
#     count+=1


# continue：跳过本次循环，进入下次循环
# count=1
# while count<5:
#     if count == 3:
#         count+=1
#         continue
#     print(count)
#     count+=1

# while True:
#     print('====>')
#     continue
#     print('====>')
#     print('====>')
#     print('====>')