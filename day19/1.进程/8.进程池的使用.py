#!/usr/bin/python3
# author ekubo
# 2023年05月21日
"""
3个进程完成10个任务(3个服务员对10个顾客)
"""
from multiprocessing.pool import Pool
import os, random, time


def worker(msg):
    t_start = time.time()
    print("%s 开始执行，进程id为：%d" % (msg, os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg, "执行完毕,耗时%0.2f"%(t_stop-t_start))


if __name__ == '__main__':
    po = Pool(3)             # 定义一个进程池，最大进程数为3
    for i in range(10):
        # Pool.apply_async(要调用的目标,(传递给目标的参数元组,))
        # 每次循环将会用空闲出来的子进程调用目标
        po.apply_async(worker, (i,))
    print("---start---")
    po.close()               # 关闭进程池，关闭后po不在接受新的请求
    po.join()                # 等待po中所有子进程执行完成，必须放在close之后
    print("---end---")
