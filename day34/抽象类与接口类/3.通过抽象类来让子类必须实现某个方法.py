#!/usr/bin/python3
# author ekubo
# 2023年07月03日
"""
接口继承实质上是要求“做出一个良好的抽象，这个抽象规定了一个兼容接口，使得外部调用者无需关心具体细节，可一视同仁的处理实现了特定接口的所有对象”——这在程序设计上，叫做归一化
"""
from abc import abstractmethod, ABCMeta


# 使用了抽象方法的类，就是抽象类，Payment就是一个抽象类
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    # def pay(self, money):
    #     print('支付宝支付')
    pass


# 如果子类中没有实现抽象方法，实例化对象时，就会报错Can't instantiate abstract class Alipay with abstract method pay（没有抽象方法pay不能实例化抽象类Alipay）
p = Alipay()
