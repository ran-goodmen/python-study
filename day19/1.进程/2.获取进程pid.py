#!/usr/bin/python3
# author ekubo
# 2023年05月21日
import os
from multiprocessing import Process


def work():
    print("我是子进程{}".format(os.getpid()))


if __name__ == '__main__':
    p = Process(target=work)
    p.start()
    # 在linux下父子进程的pid一般是连着的
    print("我是父进程{}".format(os.getpid()))
