#!/usr/bin/python3
# author ekubo
# 2023年05月21日
"""
Process之间优势需要通信，可以使用Queue实现进程之间的数据传递
"""

from multiprocessing import Queue

q = Queue(3)  # 初始化一个Queue对象，缓冲区为3，即最多可接受3条信息

q.put(1)
q.put(2)
print(q.full())
q.put(3)
print(q.full())
print(q.get())
print(q.get())
print(q.get())
