#!/usr/bin/python3
# author ekubo
# 2022年10月18日

def measure():
    print("开始测量")
    temp = 39
    wetness = 10
    print("测量结束")
    return (temp, wetness)                  # 可以不加括号，仍然返回元组

if __name__ == '__main__':
    weather = measure()
    print(weather)