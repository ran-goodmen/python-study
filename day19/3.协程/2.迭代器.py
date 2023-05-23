#!/usr/bin/python3
# author ekubo
# 2023年05月22日
from collections.abc import Iterable


# 自定义可迭代对象类
class Mylist:
    def __init__(self):
        self.container = []

    def add(self, item):
        self.container.append(item)

    def __iter__(self):  # __iter__()方法放回一个可迭代对象
        myiteratror = MyIterator(self)
        return myiteratror


# 自定义一个供上面可迭代对象使用的迭代器
class MyIterator:
    def __init__(self, mylist):
        self.mylist: Mylist = mylist
        # current用于记录当前访问到的位置
        self.current = 0

    # 被next调用来获取下一个数
    def __next__(self):
        if self.current < len(self.mylist.container):
            item = self.mylist.container[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration

    # 迭代器里的__iter__方法返回自身
    def __iter__(self):
        return self


if __name__ == '__main__':
    mylist = Mylist()
    print(isinstance(mylist, Iterable))
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.add(4)
    for i in mylist:
        print(i, end=' ')
    print()
    myiterator = MyIterator(mylist)
    for i in myiterator:
        print(i, end=' ')
    print(next(myiterator))  # 打印结果会报错,因为迭代器已经走到最后了
