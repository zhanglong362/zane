# 扩展：文件的光标移动 seek()
# with open(r'users.txt', 'r+') as f:
#     f.seek(9)
#     print(f.tell())

# 1. 复制文件小程序
# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# import sys
#
# l = sys.argv
# if len(l) == 3:
#     src_path = l[1]
#     dst_path = l[2]
#     copy(src_path, dst_path)
# else:
#     print('参数错误！请输入文件的源地址和目标地址！')
#     sys.exit()
# with open(r'%s' % src_path, 'rb') as f1, open(r'%s' % dst_path, 'wb') as f2:
#     for line in f1:
#         f2.write(line)

# 2. 修改文件小程序
# 第一种方式：
# 第一步：先把文件内容全部读入内存；
# 第二部：然后再内存中完成修改；
# 第三部：再把修改后的结果，覆盖写入原文件；
# 缺点：会在文件内容过大的情况下，占用很多内存

# with open(r'user.txt', 'r') as f:
#     data = f.read()
#     data = data.replace('吴佩琪', '吴佩琪[老男孩老师]')
# with open(r'user.txt', 'w') as f:
#     f.(data)

# # 第二种方式：

# import os
#
# with open(r'user.txt', 'rb') as f1, open(r'user.txt.swap', 'wb') as f2:
#     for line in f1:
#         if '吴佩琪' in line:
#             line = line.replace('吴佩琪', '吴佩琪[老男孩老师]')
#         f2.write(line)
# os.remove('user.txt')
# os.rename('user.txt.swap', 'user.txt')


