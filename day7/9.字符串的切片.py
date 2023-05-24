#!/usr/bin/python3
# author ekubo
# 2022年09月26日

str1 = "python"
print(str1[2:5])
print(str1[2:])
print(str1[:5])
print(str1[:])
print(str1[::2])            # 隔一个字符截取一个
print(str1[1::2])           # 从第一个索引开始每隔一个字符截取一个
print(str1[2:-1])           # 截取从2到末尾-1的字符串
print(str1[-2::])           # 截取字符串末尾两个字符
print(str1[::-1])           # 逆序
