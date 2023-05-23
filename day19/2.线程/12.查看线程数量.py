#!/usr/bin/python3
# author ekubo
# 2023年05月22日
import threading
from time import sleep
from threading import Thread


def sing():
    for i in range(3):
        print("i am singing %d" % i)
        sleep(1)


def dance():
    for i in range(3):
        print("i am dancing %d" % i)
        sleep(1)


if __name__ == '__main__':
    t1 = Thread(target=sing)
    t2 = Thread(target=dance)
    t1.start()
    t2.start()
    while True:
        length = len(threading.enumerate())
        print("当前运行的线程数为%d"%length)
        if length <= 1:         # 因为有个主线程，所以是<=1
            break
        sleep(0.5)