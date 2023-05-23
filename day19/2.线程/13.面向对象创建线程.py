#!/usr/bin/python3
# author ekubo
# 2023年05月22日
import threading
import time


class MyThread(threading.Thread):
    def run(self) -> None:                      # 自定义线程类需要重写run方法，因为start会调用run方法
        for i in range(3):
            time.sleep(1)
            msg = "I am " + self.name + " @" + str(i)       # name属性中保存的是当前线程的名字
            print(msg)


def test():
    for i in range(5):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    test()