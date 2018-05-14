# # 切片对象
# # sc = slice(1,5,2)
# # print(type(sc))
#
# # # 1. 列表推导式
# # list = ['egg%s' % x for x in range(1,101) if x <= 10]
# # print(list)
# #
# # # 2. 生成器表达式
# # genrator = ['egg%s' % x for x in range(1,101) if x <= 10]
# # print(list)
#
# # 练习
# # 1、将names=['egon','alex_sb','wupeiqi','yuanhao']中的名字全部变大写
# names = ['egon','alex_sb','wupeiqi','yuanhao']
# names = [x.upper() for x in names]
# print(names)
#
# # 2、将names=['egon','alex_sb','wupeiqi','yuanhao']中以sb结尾的名字过滤掉，然后保存剩下的名字长度
# names = ['egon','alex_sb','wupeiqi','yuanhao']
# names = [(x, len(x)) for x in names if not x.endswith('sb')]
# print(names)
#
# # 3、求文件a.txt中最长的行的长度（长度按字符个数算，需要使用max函数）
# with open(r'a.txt') as f:
#     print(max([(len(x), x) for x in f]))
#
# # 4、求文件a.txt中总共包含的字符个数？思考为何在第一次之后的n次sum求和得到的结果为0？（需要使用sum函数）
#
#
# # 5、思考题
# #
# # with open('a.txt') as f:
# #     g=(len(line) for line in f)
# # print(sum(g)) #为何报错？
# # 6、文件shopping.txt内容如下
# #
# # mac,20000,3
# # lenovo,3000,10
# # tesla,1000000,10
# # chicken,200,1
# # 求总共花了多少钱？
# #
# # 打印出所有商品的信息，格式为[{'name':'xxx','price':333,'count':3},...]
# #
# # 求单价大于10000的商品信息,格式同上


