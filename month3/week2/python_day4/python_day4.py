# 1. strip() lstrip() rstrip()
# msg = '***ssss***'
# print(msg.lstrip('*'))
# print(msg.rstrip('*'))

# 2. lower() upper()
# msg = 'Egon'
# print(msg.lower())
# print(msg.upper())

# 3. startswith endswith
# msg = 'alex is sb'
# print(msg.startswith('alex'))
# print(msg.endswith('sb'))

# 4. format 的三种使用方式
# 占位符方式
# s1 = 'my name is %s, my age is %s' % ('egon', 18)

# 第一种：
# s2 = 'my name is {}, my age is {}'.format('egon', 18)
# print(s1)
# print(s2)

# 第二种：
# s2 = 'my name is {0}, my age is {1} {1} {1} {0} {1}'.format('egon', 18)
# print(s2)

# 第三种：
# s2 = 'my name is {name}, my age is {age}'.format(name='egon', age=18)
# print(s2)

# 5. split() rsplit()
# cmd = 'get|C:\a.txt|3333'
# print(cmd.split('|'))
# print(cmd.rsplit('|', 1))

# 6. join()
# join 方法传入的列表必须只包含字符串类型的元素
# cmd = 'egon:123:admin:rwx'
# l = cmd.split(':')
# print(l)

# s = ':'.join(l)
# print(s)

# 7. replace()
# msg = 'wupeiqi say my name wupeiqi'
# print(msg.replace('wupeiqi', 'SB'))
# print(msg.replace('wupeiqi', 'SB', 1))

# 8. isdigit()
# print('10'.isdigit())
#
# age = 18
# i = 0
# while True:
#     inp_age = input('age >>: ').strip()
#     if not inp_age.isdigit():
#         print('输入数据非法')
#         continue
#     else:
#         inp_age = int(inp_age)
#     if inp_age > age:
#         print('猜大了')
#         i += 1
#     if inp_age < age:
#         print('猜小了')
#         i += 1
#     if i == 3:
#         print('Try too many times')
#         break
#     if inp_age == age:
#         print('恭喜你猜对了！')
#         break
#
# 其他操作
# 1）find() rfind() index() rindex() count()
# msg = 'my egon hegon 123'
# print(msg.find('sb'))
# print(msg.find('egon', 8, 20))
# print(msg.rfind('egon', 8, 20))
#
# print(msg.index('egon'))
# print(msg.index('sb'))
#
# 2) center() ljust() rjust() zfill()
# print('end')
# print('egon'.center(50, '*'))
# print('egon'.ljust(50, '*'))
# print('egon'.rjust(50, '*'))
# print('egon'.zfill(50))
#
# 3) expandtabs()
# msg = 'abc\tdef'
# print(msg.expandtabs(4))
#
# 4) capitalize() swapcase() title()
# print('abeCdEF'.capitalize())
# print('abeCdEF'.swapcase())
# print('my name is egon'.title())
#
# 5) is 数字系列
# num1 = b'4'    # bytes
# num2 = u'4'    # unicode，python3 中无需加 u 就是 Unicode
# num3 = '四'    # 中文数字
# num4 = 'IV'    # 罗马数字
#
# print(num1.isdigit())
# print(num2.isdigit())
# print(num3.isdigit())
# print(num4.isdigit())
#
# print(num2.isdecimal())
# print(num3.isdecimal())
# print(num4.isdecimal())
#
# print(num1.isalnum())
# print(num2.isalnum())
# print(num3.isalnum())
# print(num4.isalnum())
#
# 6) is 其他
#
# 字符串总结：
#     字符串只能存一个值；
#     有序；              # 可以按照索引取值，就是有序的
#     不可变数据类型；
#     可 hash；

# 列表类型
# 1. 按索引取值（正反向，既可以取也可以存）
l = ['a', 'b', 'c']
print(id(l))
print(l[-1])
l[0] = 'A'
print(id(l))
# l[3] = 'd'       # 不存在的索引，报错

# 2. 切片（顾头不顾尾，步长）
stus = ['alex', 'wxx', 'yxx', 'lxx']
print(stus[0:3:1])

# 3. 长度 len()
stus = ['alex', 'wxx', 'yxx', 'lxx']
print(len(stus))

# 4. 成员运算 in 和 not in
stus = ['alex', 'wxx', 'yxx', 'lxx']
print('alex' in stus)

# 5. 追加
stus = ['alex', 'wxx', 'yxx', 'lxx']
stus.append('wupeiqi')
stus.append('peiqi')
print(stus)

# 6. 插入
stus = ['alex', 'wxx', 'yxx', 'lxx']
stus.insert(1, '艾利克斯')  # 按照索引插入新元素
print(stus)

# 7. 删除
stus = ['alex', 'wxx', 'yxx', 'lxx']
# del stus[1]
stus.remove('alex')       # 按照成员方式删除
stus.pop(1)               # 按照索引方式删除
print(stus)

# 8. 循环
stus = ['alex', 'wxx', 'yxx', 'lxx']

i = 0
while i < len(stus):
    print(stus[i])
    i += 1

for i in range(len(stus)):
    print(stus[i])

for i in stus:
    print(i)

# 需要掌握的操作
stus = ['alex', 'wxx', 'yxx', 'lxx']
print(stus.count('alex'))
stus.extend(['a', 'b', 'c'])
print(stus)
# print(stus.index('alex', 1, 5))
stus.reverse()
print(stus)
l = [1, 10, 3, 12]
stus.sort(reverse=True)
print(l)
# stus.append('')

# 前提：只能同类型直接比较大小，对于有索引值直接的比较是按照位置一一对应进行对比的
# s1 = 'heelo'
# s2 = 'hf'
# print(s1 > s2)

# l1 = ['a', 'b', 'c']
# l2 = ['d']
# print(l1 > l2)

# l1 = [3, 'a', 'b', 'c']
# l2 = [xxx, 'd']
# print(l1 > l2)                    # 不通类型之间比较大小，报错

print('Z' > 'a')
print('a' > 'B')

# 练习
# 队列：先进先出
l1 = []
# 入队
l1.append('1')
l1.append('2')
l1.append('3')
# l1.insert(-1, '1')
# l1.insert(-1, '2')
# l1.insert(-1, '3')
# 出队
l1.pop(0)
l1.pop(0)
l1.pop(0)

# 堆栈：先进后出
l2 = []
# 入栈
l2.append('1')
l2.append('2')
l3.append('3')
# l2.insert(-1, '1')
# l2.insert(-1, '2')
# l2.insert(-1, '3')
# 出栈
l2.pop()
l2.pop()
l2.pop()

# 总结列表：
#     可以存多个值；
#     有序；
#     可变数据类型；
#     不可 hash；

a = 'lsl'