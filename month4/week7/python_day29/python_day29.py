# 1. 守护进程
import time
import random
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s is MyProcess' % self.name)
        time.sleep(random.randrange(1, 3))
        print('%s is MyProcess end' % self.name)


p = MyProcess('egon')
p.daemon = True  # 一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
p.start()
print('主')

# 2. 进程同步，互斥锁
# 互斥锁，只能acquire一次，release一次的使用，不能连续acquire
# 互斥锁 vs join：
# 前提：两者的原理都是一样，都是将并发变成串行，从而保证有序；
# 区别：join 是按照认为指定的顺序执行，而互斥锁是所有进程平等地竞争，谁先抢到谁执行；

import time
import random
from multiprocessing import Process, Lock

mutex = Lock()

def task1(lock):
    lock.acquire()
    print('task1: 名字是 egon')
    time.sleep(random.randint(1, 3))
    print('task1: 性别是 male')
    time.sleep(random.randint(1, 3))
    print('task1: 年龄是 18')
    time.sleep(random.randint(1, 3))
    lock.release()

def task2(lock):
    lock.acquire()
    print('task2: 名字是 lxx')
    time.sleep(random.randint(1, 3))
    print('task2: 性别是 male')
    time.sleep(random.randint(1, 3))
    print('task2: 年龄是 30')
    time.sleep(random.randint(1, 3))
    lock.release()

def task3(lock):
    lock.acquire()
    print('task3: 名字是 alex')
    time.sleep(random.randint(1, 3))
    print('task3: 性别是 male')
    time.sleep(random.randint(1, 3))
    print('task3: 年龄是 78')
    time.sleep(random.randint(1, 3))
    lock.release()

if __name__ == '__main__':
    p1 = Process(target=task1, args=(mutex,))
    p2 = Process(target=task2, args=(mutex,))
    p3 = Process(target=task3, args=(mutex,))

    p1.start()
    print('--->')
    # p1.join()
    p2.start()
    # p2.join()
    p3.start()
    # p3.join()
    print('===>')

# 3. 模拟抢票
import os
import json
import time
import random
from multiprocessing import Process, Lock

mutex = Lock()

def search():
    time.sleep(0.5)
    with open(r'data.json', 'r', encoding='utf-8') as f:
        dic = json.load(f)
        print('%s 剩余票数: %s' % (os.getpid(), dic['count']))

def get():
    with open(r'data.json', 'r', encoding='utf-8') as f:
        dic = json.load(f)
    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(random.randint(0, 1))
        with open(r'data.json', 'w', encoding='utf-8') as f:
            json.dump(dic, f)
        print('%s 购票成功！' % os.getpid())

def task(lock):
    search()
    lock.acquire()
    get()
    lock.release()

if __name__ == '__main__':
    process = []
    for p in range(10):
        p = Process(target=task, args=(mutex,))
        process.append(p)
        p.start()
    print('===>')

# 4. 互斥锁
import os
import time
from multiprocessing import Process, Lock, Manager

mutex = Lock()

def task(dic, lock):
    lock.acquire()
    dic['num'] -= 1
    print('%s return: %s' % (os.getpid(), dic['num']))
    lock.release()

if __name__ == '__main__':
    m = Manager()
    dic = m.dict({'num': 10})

    for i in range(10):
        p = Process(target=task, args=(dic, mutex))
        p.start()

    time.sleep(0.1)
    print(dic['num'])
    print('===>')

# 5. 队列
# 1）共享的空间
# 2）是内存空间
# 3）自动帮我们处理好锁问题
from multiprocessing import Process, Queue

q = Queue(3)
try:
    q.put('first', block=False)
    q.put({'second': None}, block=False)
    q.put('三', block=False)
    q.put(4, block=False)
except Exception as e:
    print('error: %s' % e)

for i in range(10):
    print(q.get(timeout=3))

# 6. 生产者消费者模型
# 该模型中包含两类重要的角色：
# 1）生产者：将负责造数据的任务比喻为生产者；
# 2）消费者：接收生产者造出的数据来做进一步的处理，该类任务被比喻成消费者；
# 实现生产者消费者模型的三要素：
#     生产者；
#     消费者；
#     队列；
# 什么时候用该模型？
# 程序中出现明显的两类任务，一类任务是负责生产，另外一类任务是负责处理生产的数据的时候；
# 该模型的好处？
# 1）实现了生产者与消费者的解耦合；
# 2）平衡了生产力与与消费力，即生产者可以一直不停地生产，消费者可以不停的处理，
# 因为二者不再直接沟通，而是跟队列沟通；

import time
import random
from multiprocessing import Process, Queue

def producer(name, q, food):
    for i in range(1, 6):
        time.sleep(random.randint(1,2))
        res = '%s%s' % (food, i)
        q.put(res)
        print('\033[32m生产者 ==> %s 生产了 %s\033[0m' % (name, res))


def consumer(name, q):
    while True:
        res = q.get()
        time.sleep(random.randint(1, 3))
        print('\033[31m消费者 ==> %s 吃了 %s\033[0m' % (name, res))

if __name__ == '__main__':
    # 共享的队列
    q = Queue()

    p1 = Process(target=producer, args=('egon', q, '包子'))
    p2 = Process(target=producer, args=('刘清政', q, '汉堡'))
    p3 = Process(target=producer, args=('杨军', q, '米饭'))

    c1 = Process(target=consumer, args=('alex', q))
    c2 = Process(target=consumer, args=('成俊华', q))
    c3 = Process(target=consumer, args=('吴晨钰', q))

    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()
    c3.start()
    print('===>')



