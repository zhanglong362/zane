# 1. 守护进程
# 主进程结束之后，守护进程会同步结束
import time
from multiprocessing import Process

def foo():
    print(123)
    time.sleep(1)
    print('end123')

def bar():
    print(456)
    time.sleep(3)
    print('end456')

if __name__ == '__main__':
    p1 = Process(target=foo)
    p2 = Process(target=bar)

    p1.daemon = True
    p1.start()
    p2.start()
    time.sleep(0.01)
    print('main')

# 2. 守护进程的使用
import time
import random
from multiprocessing import Process, JoinableQueue

def producer(name, q, food):
    for i in range(1, 6):
        res = '%s%s' % (food, i)
        q.put(res)
        print('\033[32m生产者 ==> %s 生产了 %s\033[0m' % (name, res))
        time.sleep(random.randint(1, 2))

def consumer(name, q):
    while True:
        res = q.get()
        if not res:
            break
        print('\033[31m消费者 ==> %s 吃了 %s\033[0m' % (name, res))
        time.sleep(random.randint(1, 3))
        q.task_done()

if __name__ == '__main__':
    # 共享的队列
    q = JoinableQueue()

    p1 = Process(target=producer, args=('egon', q, '包子'))
    p2 = Process(target=producer, args=('刘清政', q, '汉堡'))
    p3 = Process(target=producer, args=('杨军', q, '米饭'))

    c1 = Process(target=consumer, args=('alex', q))
    c2 = Process(target=consumer, args=('成俊华', q))
    c3 = Process(target=consumer, args=('吴晨钰', q))
    c1.daemon = True
    c2.daemon = True
    c3.daemon = True

    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()
    c3.start()

    p1.join()
    p2.join()
    p3.join()
    # 生产者生产完毕后，拿到队列中的总个数，然后直到元素总数为0，q.join()这一行代码才算运行完毕
    q.join()
    # q.join()一旦结束就意味着队列中队列确实被取空，消费者已经确确实实把数据都取干净了
    print('主进程结束！')

# 3. 多线程
import time
from multiprocessing import Process
from threading import Thread

def task(name):
    print('%s is running ...' % name)
    time.sleep(3)

if __name__ == '__main__':
    p = Process(target=task, args=('egon',))
    p.start()
    t = Thread(target=task, args=('lxx',))
    t.start()
    print('主线程结束！')

# 4. 自定义线程类
import time
from threading import Thread

class MyThread(Thread):
    def run(self):
        print('%s is running ...' % self.name)
        time.sleep(3)
        print('%s is end.' % self.name)

if __name__ == '__main__':
    t = MyThread()
    t.start()
    print('主线程结束！')
# 5. 查看线程PID，线程name，等其它方法
import time
from threading import Thread,current_thread,active_count,enumerate

x = 1000

def task():
    global x
    x = 0
    time.sleep(3)

if __name__ == '__main__':
    t1 = Thread(target=task, name='egon')
    t2 = Thread(target=task,)
    t3 = Thread(target=task,)
    t1.start()
    t2.start()
    t3.start()
    print(t1.is_alive())
    print(active_count())
    print(enumerate())
    print('主线程 %s 结束！' % current_thread().name)

# 6.1 守护线程
import time
from threading import Thread, current_thread

def task():
    print('%s is running ...' % current_thread().name)
    time.sleep(3)
    print('%s is end' % current_thread().name)

if __name__ == '__main__':
    t = Thread(target=task, name='第一个线程')
    t.daemon = True
    t.start()
    print('主线程结束！')

# 6.2 守护线程
import time
from threading import Thread

def foo():
    print(123)
    time.sleep(1)
    print('end123')

def bar():
    print(456)
    time.sleep(3)
    print('end456')

if __name__ == '__main__':
    t1 = Thread(target=foo)
    t2 = Thread(target=bar)

    t1.daemon = True
    t1.start()
    t2.start()
    time.sleep(0.01)
    print('main')

# 7. 线程互斥锁
import time
from threading import Thread, Lock

mutex = Lock()

x = 100

def task():
    global x
    mutex.acquire()
    temp = x
    time.sleep(0.01)
    x = temp - 1
    # print(x)
    mutex.release()

if __name__ == '__main__':
    start = time.time()
    threads = []
    for i in range(100):
        t = Thread(target=task,)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print('x = %s' % x)
    print('主线程！')
    print(time.time() - start)

# 8. 线程死锁
import time
from threading import Thread, Lock

mutexA = Lock()
mutexB = Lock()

class MyThread(Thread):
    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        mutexA.acquire()
        print('%s 拿到了A锁' % self.name)
        mutexB.acquire()
        print('%s 拿到了B锁' % self.name)
        mutexB.release()
        mutexA.release()

    def f2(self):
        mutexB.acquire()
        print('%s 拿到了B锁' % self.name)
        time.sleep(0.1)
        mutexA.acquire()
        print('%s 拿到了A锁' % self.name)
        mutexA.release()
        mutexB.release()

if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()
    print('主线程')

# 9. 递归锁
import time
from threading import Thread, RLock

mutexA = mutexB = RLock()

class MyThread(Thread):
    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        mutexA.acquire()
        print('%s 拿到了A锁' % self.name)
        mutexB.acquire()
        print('%s 拿到了B锁' % self.name)
        mutexB.release()
        mutexA.release()

    def f2(self):
        mutexB.acquire()
        print('%s 拿到了B锁' % self.name)
        time.sleep(0.1)
        mutexA.acquire()
        print('%s 拿到了A锁' % self.name)
        mutexA.release()
        mutexB.release()

if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()
    print('主线程')
# 10. 信号量
import time
import random
from threading import Thread,Semaphore,current_thread

sm = Semaphore(5)

def go_wc():
    sm.acquire()
    print('%s 上厕所ing' % current_thread().name)
    time.sleep(random.randint(1,3))
    sm.release()

if __name__ == '__main__':
    for i in range(23):
        t = Thread(target=go_wc)
        t.start()
    print('主线程结束！')

