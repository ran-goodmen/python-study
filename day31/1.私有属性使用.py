#!/usr/bin/python3
# author ekubo
# 2023年06月13日
class Person():
    def __init__(self, name, age, taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def showperson(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    def dowork(self):
        self._work()
        self.__away()

    def _work(self):
        print('my _work')

    def __away(self):
        print('my __away')


class Student(Person):
    def construction(self, name, age, taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def showstudent(self):
        print(self.name)
        print(self._age)
        print(self.__taste)


s1 = Student('ekubo', 23, 'basketball')
s1.showperson()
s1.construction('naruto', 16, 'lamian')         # 调用construction后才能调用showstudent函数
s1.showstudent()