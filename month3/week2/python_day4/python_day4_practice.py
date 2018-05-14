一、字符串练习
# 写代码,有如下变量,请按照要求实现每个功能 （共6分，每小题各0.5分）
name = " aleX"
# 1)    移除 name 变量对应的值两边的空格,并输出处理结果
# 2)    判断 name 变量对应的值是否以 "al" 开头,并输出结果 
# 3)    判断 name 变量对应的值是否以 "X" 结尾,并输出结果 
# 4)    将 name 变量对应的值中的 “l” 替换为 “p”,并输出结果
# 5)    将 name 变量对应的值根据 “l” 分割,并输出结果。
# 6)    将 name 变量对应的值变大写,并输出结果 
# 7)    将 name 变量对应的值变小写,并输出结果 
# 8)    请输出 name 变量对应的值的第 2 个字符?
# 9)    请输出 name 变量对应的值的前 3 个字符?
# 10)    请输出 name 变量对应的值的后 2 个字符? 
# 11)    请输出 name 变量对应的值中 “e” 所在索引位置? 
# 12)    获取子序列,去掉最后一个字符。如: oldboy 则获取 oldbo

1
name = " aleX"
name = name.strip()
print(name)

2
name = " aleX"
if name[:2] == 'al':
    print('变量 name = %s, 是以 "al" 开头' % name)
else:
    print('变量 name = %s, 不是以 "al" 开头' % name)

3
name = " aleX"
if name[-1] == 'X':
    print('变量 name = %s, 是以 "X" 结尾' % name)
else:
    print('变量 name = %s, 不是以 "X" 结尾' % name)

4
name = " aleX"
if 'l' in name:
    name = name.replace('l', 'p')
    print(name)

5
name = " aleX"
name = name.split('l')
print(name)

6
name = " aleX"
name = name.upper()
print(name)

7
name = " aleX"
name = name.lower()
print(name)

8
name = " aleX"
print(name[1])

9
name = " aleX"
print(name[:3])

10
name = " aleX"
print(name[-2:])

11
name = " aleX"
index = name.find('e')
print(index)

12
name = " aleX"
name = name[:-1]
print(name)

二、列表练习
1. 有列表data=['alex',49,[1900,3,18]]，分别取出列表中的名字，年龄，出生的年，月，日赋值给不同的变量
name = data[0]
age = data[1]
year = data[2][0]
month = data[2][1]
day = data[2][2]

2. 用列表模拟队列
l = []
入站
l.append(1)
print(l)
l.append(2)
print(l)
l.append(3)
print(l)
出站
l.pop(0)
print(l)
l.pop(0)
print(l)
l.pop(0)
print(l)

3. 用列表模拟堆栈
l = []
入站
l.append(1)
print(l)
l.append(2)
print(l)
l.append(3)
print(l)
出站
l.pop()
print(l)
l.pop()
print(l)
l.pop()
print(l)

三、for循环练习
1、使用嵌套for循环打印99乘法表(补充：不换行打印的方法为print('xxxx',end=''))
   提示：
    for i in range(...):
        for j in range(...):
            ...

for i in range(1, 10):
    for j in range(1, i+1):
        p = i * j
        print('%s*%s=%s ' % (i, j, p), end='')
    print()

2、使用嵌套for循环打印金字塔，金字塔层数为5层，要求每一个空格、每一个*都必须单独打印
        *
       ***
      *****
     *******
    *********

    提示：
        一个for循环套两个小的for循环，两个小的for一循环，一个控制打印空格，一个控制打印*

    思路参考：http://www.cnblogs.com/linhaifeng/articles/7133167.html#_label14


l = 5
for i in range(1, 6):
    for j in range(l-i):
        print(' ', end='')
    for k in range(2*i-1):
        print('*', end='')
    print()

四：购物车程序
		#需求:
		启动程序后，先认证用户名与密码，认证成功则让用户输入工资,然后打印商品列表的详细信息，商品信息的数据结构可以像下面这种格式，也可以自己定制
		goods=[
		{'name':'mac','price':20000},
		{'name':'lenovo','price':10000},
		{'name':'apple','price':200},
		{'name':'tesla','price':1000000},

		]

		失败则重新登录，超过三次则退出程序
		允许用户根据商品编号购买商品
		用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
		可随时退出，退出时，打印已购买商品和余额


users = {
    'egon': {
        'password': '123',
        'money': 0,
        'goods': {}
    },
    'alex': {
        'password': '123',
        'money': 0,
        'goods': {}
    }
}
goods = {
    'mac': {
        'price': 20000
    },
    'lenovo': {
        'price': 10000
    },
    'apple': {
        'price': 200
    },
    'tesla': {
        'price': 1000000
    }
}
i = 0
line = '='*25
tag = True
while tag:
    inp_name = input('name>>: ').strip()
    inp_pwd = input('password>>: ')
    if inp_name not in users:
        print('用户名错误！')
        i += 1
    else:
        if inp_pwd != users[inp_name]['password']:
            print('密码错误！')
            i += 1
        else:
            print('登陆成功!')
            i = 0
    if i > 0 and i < 3:
        continue
    if i == 3:
        print('尝试次数过多，锁定用户')
        tag = False
        continue
    while tag:
        salary = input('请输入工资 >>: ')
        if salary == 'quit':
            tag = False
            continue
        if not salary.isdigit():
            print('工资无效，请输入整数')
            continue
        else:
            salary = int(salary)
        users[inp_name]['money'] = salary
        gd = {}
        while tag:
            print(line)
            for k,v in enumerate(goods):
                print('%-6s %-10s %-10s' % (k, v, goods[v]))
                gd[k] = v
            print(line)
            code = input('请选择要购买的商品编号 >>: ')
            if code == 'quit':
                tag = False
                continue
            if code not in gd:
                print('商品编码错误！')
                continue
            good = gd[code]
            if users[inp_name]['money'] >= goods[good]['price']:
                if good not in users[inp_name]['goods']:
                    users[inp_name]['goods'][good] = 1
                else:
                    users[inp_name]['goods'][good] = users[inp_name]['goods'][good] + 1
                users[inp_name]['money'] = users[inp_name]['money'] - goods[good]['price']
                print('商品 %s 已加入购物车，输入list命令查看购物车' % good)
                cmd = input('继续购物输入Y，结账输入N >>: ').lower()
                if cmd ==  'list':
                    print('已经购买的商品：\n%s' % users[inp_name]['goods'])
                if cmd == 'y':
                    continue
                if cmd == 'n' or cmd == 'quit':
                    print('用户名: %s\n购买商品: %s\n账户余额: %s' % (inp_name, users[inp_name]['goods'], users[inp_name]['money']))
                    tag = False
            else:
                print('账户余额不足')
