#!/usr/bin/python3
# author ekubo
# 2023年06月20日
class Foo:
    def func(self):
        print('实例方法')

    @property
    def prop(self):
        print('property属性')


f = Foo()
f.func()
f.prop
