# 1. 读文件
# f = open('a.txt', mode='r', encoding='utf-8')
# # for i in range(1, 5):
# #     f.write('哈哈哈%s\n' % i)
# print('=========>1')
# #print(f.readable())
# print(f.readline().strip('\n'))
# print('=========>2')
# #print(f.read())
# print('=========>3')
# print(f.readlines())
# print('=========>4')
# f.close()

# 循环
# with open('a.txt', encoding='utf-8') as f:
#     # 这种方式是最好的，内存只有一行数据
#     for line in f:
#         print(line, end='')
#     # 这种方式文件大的情况下，一次读取所有数据到内存，可能会耗尽内存
#     # for line in f.readlines():
#     #     print(line, end='')

# 2. 写文件
# l = ['lines1\n', 'lines2\n', 'lines3\n', 'lines4\n']
# with open('a.txt', 'w') as f:
#     for i in range(1, 5):
#         f.write('哈哈哈%s\n' % i)
#     f.writelines(l)


