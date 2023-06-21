#!/usr/bin/python3
# author ekubo
# 2023年06月20日
"""
使用property属性的到第多少个
"""


class Pager:
    def __init__(self, current_page):
        # 记录当前页码
        self.current_page = current_page
        # 每页显示10条数据
        self.per_items = 10

    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    @property
    def end(self):
        val = self.current_page * self.per_items
        return val


p = Pager(5)
print(p.start)
print(p.end)
