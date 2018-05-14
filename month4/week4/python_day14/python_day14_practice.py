# 4月3号作业：
# 1、求文件a.txt中总共包含的字符个数？思考为何在第一次之后的n次sum求和得到的结果为0？
with open(r'a.txt') as f:
    total_count = sum(len(line) for line in f)
    print(total_count)

# 2、思考题
#     with open('a.txt',encoding='utf-8') as f:
#         g=(len(line) for line in f)
#     print(sum(g))

#答：g 通过生成器表达式'len(line) for line in f'得到一个生成器，sum 循环生成器g里面的每个值相加得到总的字符个数。

# 3、文件shopping.txt内容如下
#     mac,2000,3
#     lenovo,3000,10
#     tesla,1000000,10
#     chicken,200,1
#
#     求总共花了多少钱？
#     打印出所有的商品信息，格式为
#     [{'name':'xxx','price':'3333','count':3},....]
#     求单价大于10000的商品信息，格式同上

with open(r'shopping.txt') as f:
    g = (line.strip('\n').split(',') for line in f)
    l = [{'name':name,'price':int(price),'count':int(count)} for name,price,count in g]

    cost = sum(map(lambda x:(x['price'] * x['count']), l))
    print('本次购物总共花费了 %s' % cost)
    print(l)

    good_above_10000 = list(filter(lambda x:x['price']>10000, l))
    print(good_above_10000)

# 4、改写ATM作业，将重复用到的功能放到模块中，然后通过导入的方式使用
