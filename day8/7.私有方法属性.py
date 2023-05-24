#!/usr/bin/python3
# author ekubo
# 2022年10月19日

class Women:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

xiaomei = Women("xiaomei", 18)
print(xiaomei.__age)