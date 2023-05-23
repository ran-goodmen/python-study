#!/usr/bin/python3
# author ekubo
# 2023年05月21日
import os
import time
from multiprocessing import Process


def work(name, age, **kwargs):
    print("我是子进程{}{}岁{}分".format(name, age, kwargs))


if __name__ == '__main__':
    p = Process(target=work, args=("ekubo", 23), kwargs={"408":111})
    p.start()
    print("我是父进程")

