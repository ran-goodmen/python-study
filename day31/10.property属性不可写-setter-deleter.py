#!/usr/bin/python3
# author ekubo
# 2023年06月20日
class Goods:

    @property
    def price(self):
        print('@property')

    @price.setter
    def price(self, value):
        print(value)
        print('@price.setter')

    @price.deleter
    def price(self):
        print('price.deleter')


g = Goods()
g.price                 # 自动执行 @property 修饰的 price 方法，并获取方法的返回值
g.price = 123           # 赋值操作执行@price.setter修饰的 price 方法，并将123赋值给方法的参数
del g.price             # 删除操作执行 @price.deleter 修饰的 price 方法
