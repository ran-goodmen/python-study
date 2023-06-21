#!/usr/bin/python3
# author ekubo
# 2023年06月20日
class Province(object):
    """
    类描述
    """
    country = 'China'

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def func(self, *args, **kwargs):
        print('func')

print(Province.__dict__)
obj1 = Province('山东', 10000)
print(obj1.__dict__)