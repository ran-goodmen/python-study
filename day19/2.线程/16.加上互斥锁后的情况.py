#!/usr/bin/python3
# author ekubo
# 2023年05月22日
import threading
from threading import Thread


def work1(nums):
    global g_nums
    for i in range(nums):
        mutex.acquire()
        g_nums += 1
        mutex.release()
    print("---in work1, g_nums is %d" % g_nums)


def work2(nums):
    global g_nums
    for i in range(nums):
        mutex.acquire()
        g_nums += 1
        mutex.release()
    print("---in work2, g_nums is %d" % g_nums)


g_nums = 0
print("线程创建前g_nums的值是%d" % g_nums)
mutex = threading.Lock()
t1 = Thread(target=work1, args=(1000000,))
t2 = Thread(target=work2, args=(1000000,))
t1.start()
t2.start()
t1.join()
t2.join()
print("多个线程操作同一变量的结果g_nums的值是%d" % g_nums)
