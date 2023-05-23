#!/usr/bin/python3
# author ekubo
# 2023年05月19日

from multiprocessing import Process
import time


def fun():
    while True:
        print("---2---")
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=fun)
    p.start()
    while True:
        print("---1---")
        time.sleep(1)
