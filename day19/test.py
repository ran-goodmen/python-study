#!/usr/bin/python3
# author ekubo
# 2023年05月22日
from collections.abc import Iterator
g = (i for i in range(10))
print(type(g))
# 生成器属于迭代器
print(isinstance(g, Iterator))