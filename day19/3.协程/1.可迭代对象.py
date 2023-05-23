#!/usr/bin/python3
# author ekubo
# 2023年05月22日
from collections.abc import Iterable


class Mylist:
    def __init__(self):
        self.container = []

    def add(self, item):
        self.container.append(item)

    def __iter__(self):
        pass


if __name__ == '__main__':
    mylist = Mylist()
    print(isinstance(mylist, Iterable))