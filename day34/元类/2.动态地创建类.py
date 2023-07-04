#!/usr/bin/python3
# author ekubo
# 2023年07月03日
def choose_class(name):
    if name == 'foo':
        class Foo:
            pass

        return Foo  # 返回的是类，而不是类的实例
    else:
        class Bar:
            pass

        return Bar


MyClass = choose_class('foo')
my_class = MyClass()
print(MyClass)
print(my_class)