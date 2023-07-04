#!/usr/bin/python3
# author ekubo
# 2023年07月03日
class ObjectCreator:
    pass


my_object = ObjectCreator()
print(my_object)  # 打印对象：模块.类名 内存中的地址
print(ObjectCreator)  # 打印类：class 模块.类名


def echo(obj):
    print(obj)


echo(my_object)
echo(ObjectCreator)
print('-' * 50)

# hasattr用来判断一个对象是否有某个属性，有就是True，没有就是false
print(hasattr(ObjectCreator, 'new_attribute'))
ObjectCreator.new_attribute = 'foo'  # 可以这样为类增加类属性
print(hasattr(ObjectCreator, 'new_attribute'))
print('-' * 50)

# 可以把类赋值给一个变量
val = ObjectCreator
print(val)

print(type(1))
print(type(my_object))
print(type(ObjectCreator))      # 创建类出来的那个类，叫元类
