# 1. 赋值方式：
# 1.1 链式赋值
# x = 1
# y = 1
# y = x = a = b = c = 1
# print(id(y), id(c))

# 1.2 交叉赋值
# m = 1
# n = 2
# tmp = 1
# m = n
# n = tmp
# print(m, n)

# m, n = n, m
# print(m, n)

# 1.3 变量的解压
salarys = [11, 12, 13, 14, 15]

# mon1_sal = salarys[0]
# mon2_sal = salarys[1]
# mon3_sal = salarys[2]
# mon4_sal = salarys[3]
# mon5_sal = salarys[4]
# print(mon1_sal, mon2_sal, mon3_sal, mon4_sal, mon5_sal)

# mon1_sal, mon2_sal, mon3_sal, mon4_sal, mon5_sal = salarys
# print(mon1_sal, mon2_sal, mon3_sal, mon4_sal, mon5_sal)

# mon1_sal, *_, mon5_sal = salarys
# print(mon1_sal, mon5_sal)

# *_, mon4_sal, mon5_sal = salarys
# print(mon4_sal, mon5_sal)

# count = 1
# while count < 6:
#     if count == 4:
#         break
#     print(count)
#     count += 1
#     # break
# else:
#     print('Loop 已经完整运行完， 中间没有被 break 中断的情况下，else 部分的代码才有作用')

# int 整型
# 进制转换
# print(bin(2))
# print(oct(8))
# print(10)
# print(hex(16))


# str 字符串
# 1. 按索引取值（只能取不能写）
# s = 'egon'
# x = s[0]
# print(x)
# x = s[-1]
# print(x)
# 2. 切片（取首不取尾，步长）
# msg = 'Alex say my name is alex.'
# 正向切片
# print(msg[0:6])
# print(msg[0:6:2])
# 反向切片
# print(msg[-1:-5:-1])
# 3. 字符串长度 len()
# name = 'egon'
# print(len(name))
# 4. 成员运算 in 和 not in
# name = 'egon'
# print('e' in name)

# 5. 移除空白 strip()
# name = ' egon '
# print(name.strip())
# name = '***egon***'
# print(name.strip('*'))

# 6. 拆分字符串 split()
# info = 'egon:123:admin'
# info = info.split(':')
# print(info)

# 7. 字符串循环取值
# msg = '123456'
# i = 0
# while i < len(msg):
#     print(msg[i])
#     i += 1

# for m in msg:
#     print(m)

# 函数的作用是 从十进制转为八进制
print('八进制：%s --> 十进制：%s' % ('20', oct(20)))
# 24(八进制)  -->  20(十进制)
# 2x8^1 + 4x8^0 = 20

# 函数的作用是 从十进制转为八进制
# print('八进制：%s' % oct(16))
# 20(八进制)  -->  16(十进制)
# 2x8^1 + 0x8^0 = 16

print('十进制：%s --> 八进制：%s' % ('24', int('24', 8)))
# print(int('20', 8))


msg1='alex say my name is alex,my age is 73,my sex is female'
msg2='alex say my name is alex,my age is 73,my sex is female'
print(msg1 is msg2)
print(msg1 == msg2)