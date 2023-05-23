#!/usr/bin/python3
# author ekubo
# 2023年05月22日
from collections.abc import Iterable


class FibIterator:
    def __init__(self, num):
        self.n = num
        self.current = 0        # current保存当前生成到数列中的第几个数
        self.num0 = 0           # 用于保存前前一个数，初始值为数列的第一个数0
        self.num1 = 1           # 用于保存前一个数，初始值为数列的第二个数1

    def __next__(self):
        # 被next调用来获取下一个数
        if self.current < self.n:
            num = self.num0
            self.num0, self.num1 = self.num1, self.num0 + self.num1
            self.current += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    fb = FibIterator(10)
    for i in fb:
        print(i, end=' ')
