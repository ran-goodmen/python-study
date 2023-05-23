#!/usr/bin/python3
# author ekubo
# 2023年05月21日
from multiprocessing import Manager, Pool
import os, time, random


def reader(q):
    print("reader启动(%s), 父进程是(%s)" % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到信息：%s" % q.get())


def writer(q):
    print("writer启动(%s), 父进程是(%s)" % (os.getpid(), os.getppid()))
    for i in "wangdao":
        q.put(i)


if __name__ == '__main__':
    print("父进程%s start" % os.getpid())
    q = Manager().Queue()
    po = Pool()
    po.apply_async(writer, (q,))
    time.sleep(1)
    po.apply_async(reader, (q,))
    po.close()
    po.join()
    print("父进程%s end" % os.getpid())