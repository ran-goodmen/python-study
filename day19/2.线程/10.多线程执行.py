#!/usr/bin/python3
# author ekubo
# 2023年05月22日
import time
from threading import Thread


def work():
    print("i am working")
    time.sleep(1)


# 多线程执行的情况下，不会打印一条等1秒，而是打印和睡眠并发执行，表现出的效果是一瞬间全部打印完然后等待
if __name__ == '__main__':
    for i in range(5):
        t = Thread(target=work)
        t.start()
