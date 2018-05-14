# 1、文件内容如下,标题为:姓名,性别,年纪,薪资
#
#     egon male 18 3000
#     alex male 38 30000
#     wupeiqi female 28 20000
#     yuanhao female 28 10000
#
# 	要求:
# 	从文件中取出每一条记录放入列表中,
# 	列表的每个元素都是{'name':'egon','sex':'male','age':18,'salary':3000}的形式

config = 'db.txt'
def get_user_info():
    with open(r'%s' % config) as f:
        line = (line.split() for line in f)
        user_info = [{'name': name, 'sex': sex, 'age': age, 'salary': salary} \
                     for name, sex, age, salary in line]
    print(user_info)
    return user_info

user_info = get_user_info()

# 2 根据1得到的列表,取出薪资最高的人的信息
salary_max = max(user_info, key=lambda x:x['salary'])
print(salary_max)

# 3 根据1得到的列表,取出最年轻的人的信息
age_min = min(user_info, key=lambda x:x['age'])
print(age_min)

# 4 根据1得到的列表,将每个人的信息中的名字映射成首字母大写的形式
user_info_map = map(lambda x:x['name'].capitalize(), user_info)
user_info_map = []
print(list(user_info_map))

# 5 根据1得到的列表,过滤掉名字以a开头的人的信息
user_info_filter = filter(lambda x:x['name'].startswith('a'), user_info)
print(list(user_info_filter))

# 6 使用递归打印斐波那契数列(前两个数的和得到第三个数，如：0 1 1 2 3 5 8...)

# # while 循环版本
# def fibo(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(a)
#         a, b = b, a + b
#         n += 1
#     return 'done'
#
# fibo(10)

# # 成生成器版本（print 换成 yield）
# def fibo(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield a
#         a, b = b, a + b
#         n += 1
#     return 'done'
#
# f = fibo(10)
# for i in f:
#     print(i)

# 函数递归版本
def fibo(a, b, n):
    if n == 0:
        return 'done'
    print(a)
    n -= 1
    return fibo(b, a + b, n)

fibo(0, 1, 10)

# 7 一个嵌套很多层的列表，如l=［1,2,[3,[4,5,6,[7,8,[9,10,[11,12,13,[14,15]]]]]]］，用递归取出所有的值

l = [1,2,[3,[4,5,6,[7,8,[9,10,[11,12,13,[14,15]]]]]]]

def tell(l):
    for i in l:
        if type(i) is not list:
            print(i)
        else:
            tell(i)

# tell(l)

