#!/usr/bin/python3
# author ekubo
# 2023年07月03日
class Alipay:
    def pay(self, money):
        print('支付宝支付了')


class Apppay:
    def pay(self, money):
        print('苹果支付了')


class Weicht:
    def pay(self, money):
        print('微信支付了')
    # def paying(self, money):
    #     print('微信支付了')


def pay(payment, money):  # 支付函数，总体负责支付，对应支付的对象和要支付的金额
    payment.pay(money)


p = Weicht()
pay(p, 200)  # 支付宝支付了
