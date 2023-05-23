#!/usr/bin/python3
# author ekubo
# 2023年05月21日
import time
from multiprocessing import Queue, Process


def writer(q:Queue):
    for value in ['A', 'B', 'C']:
        print('Put %s to queue'% value)
        q.put(value)
        time.sleep(1)


def reader(q:Queue):
    while True:
        if not q.empty():
            print('Get %s from queue' % q.get())
            time.sleep(1)
        else:
            break


if __name__ == '__main__':
    q = Queue()         # 父进程创建Queue，并传递给子进程
    pw = Process(target=writer, args=(q,))          # 因为args里必须传元组，所有得加","不加的传进去是个整型
    pr = Process(target=reader, args=(q,))
    pw.start()
    time.sleep(1)
    pr.start()
    pw.join()
    pr.join()
