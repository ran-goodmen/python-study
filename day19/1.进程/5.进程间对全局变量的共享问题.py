#!/usr/bin/python3
# author ekubo
# 2023年05月21日
import os
import time
from multiprocessing import Process
nums = [11, 22]


def work1():
    print("我是子进程{}".format(os.getpid()))
    nums.append(33)
    print("work1: {}".format(nums))


def work2():
    print("我是子进程{}".format(os.getpid()))
    print(nums)


if __name__ == '__main__':
    p = Process(target=work1)
    p.start()
    p.join()

    p = Process(target=work2)
    p.start()



