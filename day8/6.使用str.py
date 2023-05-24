#!/usr/bin/python3
# author ekubo
# 2022年10月19日

class Cat:
    def __init__(self, name):
        self.name = name
        print("%s coming" %self.name)

    def __str__(self):
        return "i am a cat[%s]" %self.name

tom = Cat("tom")
print(tom)