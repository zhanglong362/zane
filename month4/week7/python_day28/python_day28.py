# -*- encoding: utf-8 -*-
# 1. 多进程
import time
from multiprocessing import Process

def task(name):
    print('%s is running ...' % name)
    time.sleep(3)
    print('%s is done.' % name)


if __name__ == '__main__':
    # Windows系统之上，开启子进程的操作，一定要放到 __name__ == '__main__' 下面，
    # 因为会会涉及到重新导一遍上面的文件
    p1 = Process(target=task, args=('egon',))
    p2 = Process(target=task, kwargs={'name':'alex'})
    p1.start()
    print('===>')
    p2.start()
    print('--->')

# 2. 自定义多进程类
import time
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s is running ...' % self.name)
        time.sleep(3)
        print('%s is done.' % self.name)

if __name__ == '__main__':
    p = MyProcess('egon')
    p.start()
    print('===>')

# 3. 进程间隔离
import time
from multiprocessing import Process

x = 1000

def task():
    global x
    time.sleep(3)
    x = 0
    print('task: x = %s' % x)

if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    time.sleep(5)
    print('parent: x = %s' % x)

# 4. 父进程等待子进程结束  p.join
import time
from multiprocessing import Process

x = 1000

def task():
    global x
    time.sleep(3)
    x = 0
    print('task: x = %s' % x)

if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.join()
    print('parent: x = %s' % x)

# 5. 多进程
import time
import random
from multiprocessing import Process

def task(name):
    print('%s is running ...' % name)
    # time.sleep(name)
    time.sleep(random.randint(1,3))

if __name__ == '__main__':
    start_time = time.time()
    process = []
    for i in range(10):
        p = Process(target=task, args=('task-%s' % i,))
        process.append(p)
        p.start()
    for p in process:
        p.join()
    p.terminate()
    print('Process %s is %s.' % (p.pid, p.is_alive()))
    print('==>')
    print(time.time() - start_time)

# 6. 获取 pid 和 ppid
import os
import time
from multiprocessing import Process

x = 1000

def task():
    print('Pid: %s PPid: %s' % (os.getpid(), os.getppid()))
    time.sleep(3)

if __name__ == '__main__':
    p1 = Process(target=task,)
    p1.start()
    p1.join()
    print('===>')

# 7. 僵尸进程和孤儿进程
import os
import time
from multiprocessing import Process

def task(name):
    print('%s is running ...' % name)
    time.sleep(50)
    print('%s is done.' % name)

if __name__ == '__main__':
    process = []
    for i in range(1, 4):
        p = Process(target=task, args=(i,))
        process.append(p)
        p.start()
    for p in process:
        p.join()
    print('===>')
    print('ppid = %s' % os.getppid())


