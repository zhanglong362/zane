# -*- encoding: utf-8 -*-

# import random
# print(random.random())

# 1. 随机生成验证码
import random
def make_code(n):
    res = ''
    for i in range(n):
        s1 = chr(random.randint(65, 90))
        s2 = str(random.randint(0, 9))
        res += random.choice([s1, s2])
    return res

code = make_code(9)
print(code)

# 2. 打印进度条
def progress(percent, width=50):
    show = ('[%%-%ds]' % width) % (int(width*percent) * '#')
    print('%s %d%%' % (show, int(100*percent)), end='\r')

import time
recv_size = 0
total_size = 100
while recv_size < total_size:
    time.sleep(0.1)
    recv_size += 1
    percent = recv_size/total_size
    progress(percent)


