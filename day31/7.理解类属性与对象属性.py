#!/usr/bin/python3
# author ekubo
# 2023年06月20日
"""
类变量在内部是作为字典处理的。如果一个变量的名字没有在当前类的字典中发现，将搜索祖先类知道被引用的变量名被找到。
随后如果任意子类中重写了此变量，该值仅仅在子类中改变。若在父类中被修改，则会影响此父类的所有未重写此变量的子类
"""


class Parent:
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass


print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)  # 3 2 3
print('*' * 20)
c1 = Child1()
c2 = Child2()
p = Parent()
print(c1.x, c2.x, p.x)  # 2 3 3
c1.x = 4
print(c1.x, c2.x, p.x)  # 4 3 3
print(Child1.x, Child2.x, Parent.x)     # 2 3 3
p.x = 5
print(c1.x, c2.x, p.x)  # 4 3 5
