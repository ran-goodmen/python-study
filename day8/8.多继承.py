#!/usr/bin/python3
# author ekubo
# 2022年10月19日

class A:
    def demo(self):
        print('A demo')
    def test(self):
        print('A test')

class B:
    def demo(self):
        print('B demo')
    def test(self):
        print('B test')

class C(A, B):
    pass

print(C.__mro__)