# 3. 请用两种方式实现，将文件中的alex全部替换成SB的操作（20分）

str1 = 'alex'
str2 = 'SB'

# 第一种方式：
with open(r'a.txt') as f:
    data = f.read()
    data = data.replace(str1, str2)
with open(r'a.txt', 'w') as f:
    f.write(data)

# 第二种方式：
import os

with open(r'a.txt') as f1, \
        open(r'a.txt.swap', 'w') as f2:
    for line in f1:
        if str1 in line:
            line = line.replace(str1, str2)
        f2.write(line)
os.remove('a.txt')
os.rename('a.txt.swap', 'a.txt')