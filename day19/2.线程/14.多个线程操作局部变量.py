#!/usr/bin/python3
# author ekubo
# 2023年05月22日
import time
from threading import Thread

"""
同属于一个进程的多个线程共享一套资源，局部变量也是一样
"""

def work1(nums):
    nums.append(44)
    print("---in work1", nums)


def work2(nums):
    time.sleep(1)
    print("---in work2", nums)


def main():
    g_nums = [11, 22]
    t1 = Thread(target=work1, args=(g_nums,))
    t2 = Thread(target=work2, args=(g_nums,))
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()