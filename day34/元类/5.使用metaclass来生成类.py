#!/usr/bin/python3
# author ekubo
# 2023年07月03日
"""
使用metaclass生成类，入参是函数
"""


def upper_attr(class_name, class_parents, class_attr):
    # 遍历属性字典，把不是__开头的属性名字和值都变为大写
    new_attr = {}
    for name, value in class_attr.items():
        if not name.startswith("__"):
            new_attr[name.upper()] = value.upper()
    return type(class_name, class_parents, new_attr)


class Foo(metaclass=upper_attr):
    bar = 'bip'


print(Foo.BAR)
print(help(Foo))
