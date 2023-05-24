#!/usr/bin/python3
# author ekubo
# 2022年10月19日

# 可变参数也叫多值参数
def demo1(*args, **kwargs):
    print(args)
    print(kwargs)

# 在元组前加*是解包(unpack)，效果是(1,2,3,4)会变成1,2,3,4
# 在字典前加**是解包字典，效果是将{'name': 'ekubo', 'age': 18, 'gender': True}变成'name': 'ekubo', 'age': 18, 'gender': True
def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)
    print('-' * 50)
    demo1(args,kwargs)              # 这样参数，会将args和kwargs识别成未知参数
    print('-' * 50)
    demo1(*args,**kwargs)           # 正确做法


demo(1, 2, 3, 4, 5, name="ekubo", age=18, gender=True)
