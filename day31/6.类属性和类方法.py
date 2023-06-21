#!/usr/bin/python3
# author ekubo
# 2023年06月20日
class Foo:
    def __init__(self, name):
        self.name = name

    def ord_func(self):             # 定义实例方法，至少有一个self参数
        print('实例方法')

    @classmethod
    def class_func(cls):             # 定义类方法，类方法至少有一个cls参数
        print('类方法')

    @staticmethod
    def static_func():
        print('静态方法')


f = Foo("中国")
# 调用实例方法
f.ord_func()

# 调用类方法
Foo.class_func()

# 调用静态方法
Foo.static_func()