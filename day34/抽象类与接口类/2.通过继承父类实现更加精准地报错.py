#!/usr/bin/python3
# author ekubo
# 2023年07月03日
"""
继承父类，父类添加错误提示
"""


class payment:
    def pay(self, money):
        e = Exception('缺少编写pay方法')
        raise e  # 手动抛异常


class Alipay(payment):
    def paying(self, money):  # 这里类的方法不是一致的pay,导致后面调用的时候找不到pay
        print('支付宝支付了')


def pay(payment, money):  # 支付函数，总体负责支付，对应支付的对象和要支付的金额
    payment.pay(money)


p = Alipay()  # 不报错
pay(p, 200)
