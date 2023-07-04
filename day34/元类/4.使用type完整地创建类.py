#!/usr/bin/python3
# author ekubo
# 2023年07月03日
class A:
    num = 100


def print_b(self):
    print(self.num)


"""
静态方法，其实就是我们学过的函数，和函数唯一的区别是，静态方法定义在类这个空间（类命名空间）中，而函数则定义在程序所在的空间（全局命名空间）中。
静态方法没有类似 self、cls 这样的特殊参数，因此 Python 解释器不会对它包含的参数做任何类或对象的绑定。也正因为如此，类的静态方法中无法调用任何类属性和类方法。
"""


@staticmethod
def print_static():
    print('---haha---')


@classmethod
def print_class(cls):
    print(cls.num)


B = type("B", (A,), {"print_b": print_b, "print_static": print_static, "print_class": print_class})

b = B()
b.print_b()
b.print_static()
b.print_class()


a = A()
print(a.__class__)
print(a.__class__.__class__)
i = 1
print(i.__class__)
print(i.__class__.__class__)
