#!/usr/bin/python3
# author ekubo
# 2023年05月23日
import re


def example1():
    ret = re.match(".", "M")
    print(ret.group())


def example2():
    ret = re.match("h", "hello python")
    print(ret.group())


def example3():
    ret = re.match("[hH]", "hello python")
    ret1 = re.match("[hH]", "Hello python")
    print(ret.group(), ret1.group())


def example4():
    ret = re.match("[0-35-9]hello", "3hello python")
    print(ret.group())


if __name__ == '__main__':
    example1()
    example2()
    example3()
    example4()