#!/usr/bin/python3
# author ekubo
# 2023年05月21日
import os
import time
from multiprocessing import Process


def work():
    print("我是子进程{}".format(os.getpid()))


if __name__ == '__main__':
    p = Process(target=work)
    p.start()
    while True:
        print("---1---")
        time.sleep(1)

# 子进程结束了，父进程还在忙碌没有回收子进程，子进程变成僵尸态（Z），即占着PCB但是不干活
