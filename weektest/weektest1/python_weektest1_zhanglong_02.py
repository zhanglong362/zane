# 2. 编写拷贝文件的程序，要求(10分)
# 可以拷贝任意类型的文件
# 在命令行中执行，命令的格式为：python3 copy.py src_file dst_file

import sys

if len(sys.argv) == 3:
    src_file = sys.argv[1]
    dst_file = sys.argv[2]
else:
    print('请按样例正确输入参数：python3 copy.py src_file dst_file')
    sys.exit()

with open(r'%s' % src_file, 'rb') as f1, \
        open(r'%s' % dst_file, 'wb') as f2:
    for line in f1:
        f2.write(line)