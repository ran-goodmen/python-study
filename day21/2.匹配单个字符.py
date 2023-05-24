#!/usr/bin/python3
# author ekubo
# 2023年05月23日
import re


def example1():
    ret = re.match("嫦娥1号", "嫦娥1号发射成功")
    print(ret.group())


def example2():
    ret = re.match("嫦娥\d号", "嫦娥1号发射成功")
    print(ret.group())


def example3():
    ret = re.match("嫦娥\d号", "嫦娥2号发射成功")
    print(ret.group())


if __name__ == '__main__':
    example1()
    example2()
    example3()