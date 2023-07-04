#!/usr/bin/python3
# author ekubo
# 2023年07月03日
"""
type除了查看对象类型外还有一种完全不同的功能：动态创建类
type(类名, 由父类名称组成的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
"""
from test import ObjectCreator

print(ObjectCreator)  # 打印类：class 模块.类名
print('-' * 50)

# 使用type创建不带属性的类
Test = type('Test', (), {})
print(Test())
print(Test)
print(help(Test))
print('-' * 50)

# 使用type创建带属性的类
Foo = type('Foo', (), {'bar': True})
print(Foo.bar)


def echo_bar(self):
    print('echo bar:', end=' ')
    print(self.bar)


# 让FooChild类中的echo_bar属性，指向了上面定义的函数
FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
print(hasattr(FooChild, 'echo_bar'))
my_foo = FooChild()
my_foo.echo_bar()