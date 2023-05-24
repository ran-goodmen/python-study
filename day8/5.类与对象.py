#!/usr/bin/python3
# author ekubo
# 2022年10月19日

class Person():
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def run(self):              # self 是默认把对象传入，实际传参不用串self
        print("%s is running" %self.name)


xiaoming = Person('xiaoming', 19, 177)
xiaoming.run()
lili = xiaoming
print(id(lili))
print(id(xiaoming))
xiaoming.score_408 = 111
print(xiaoming.score_408)
