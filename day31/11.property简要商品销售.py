#!/usr/bin/python3
# author ekubo
# 2023年06月20日

class Goods:
    """
    类Goods的描述信息
    """
    def __init__(self):
        self.original_price = 100
        self.discount = 0.8

    @property
    def price(self):
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price


class Goods1:
    """
    类Goods1的描述信息
    """
    def __init__(self):
        self.original_price = 100
        self.discount = 0.8

    def get_price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    def set_price(self, value):
        self.original_price = value

    def del_price(self):
        del self.original_price

    PRICE = property(get_price, set_price, del_price, 'description...')


def use_goods():
    print(Goods.price)  # property是对象属性
    obj = Goods()
    print(obj.price)  # 获取商品价格
    obj.price = 200  # 修改商品原价
    print(obj.price)
    del obj.price  # 删除商品原价，保证后面有人使用会报错


def use_goods1():
    g = Goods1()
    print(g.PRICE)
    g.PRICE = 500
    print(g.PRICE)
    del g.PRICE
    print(Goods1.PRICE.__doc__)
    print(g.__dict__)               # 使用dict方法查看对象的属性


if __name__ == '__main__':
    # use_goods()
    use_goods1()
    # print(Goods.__doc__)            # 使用doc方法查看类的描述信息
    # print(Goods1.__doc__)
    # print(Goods1.__dict__)           # 使用dict方法查看类的属性和方法，其中有些方法是类默认自带的
