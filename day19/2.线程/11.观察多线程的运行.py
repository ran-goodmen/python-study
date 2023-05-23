#!/usr/bin/python3
# author ekubo
# 2023年05月22日
import time
from threading import Thread


def sing():
    for i in range(3):
        print("i am singing %d" % i)
        time.sleep(1)


def dance():
    for i in range(3):
        print("i am dancing %d" % i)
        time.sleep(1)


if __name__ == '__main__':
    print('---开始---%s'%time.ctime())
    t1 = Thread(target=sing)
    t2 = Thread(target=dance)
    t1.start()
    t2.start()
    print('---结束---%s'%time.ctime())