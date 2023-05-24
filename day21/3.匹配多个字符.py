#!/usr/bin/python3
# author ekubo
# 2023年05月23日
import re


# *匹配前一个字符出现任意次（包括0次）
def use_start():
    ret = re.match("[A-X][a-z]*", "M")
    print(ret.group())

    ret = re.match("[A-X][a-z]*", "MnnM")
    print(ret.group())

    ret = re.match("[A-X][a-z]*", "Aabcdef")
    print(ret.group())


# +前面的至少要出现1次，所以2-name不合法
def use_plus():
    name = ['name1', '_name', '2_name', '_name_']
    for i in name:
        ret = re.match("[a-zA-Z_]+[\w]*", i)
        if ret:
            print(ret.group())
        else:
            print("%s不合规" % i)


# ?匹配前一个字符不出现或出现1次
def use_Questionmark():
    ret = re.match("[1-9]?[0-9]", "7")
    print(ret.group())

    ret = re.match("[1-9]?\d", "33")
    print(ret.group())

    str = "09"
    ret = re.match("[1-9]?\d$", str)            # 匹配0到99的数
    if ret:
        print(ret.group())
    else:
        print("%s不合规" % str)


# {m}匹配前一个字符出现m次
def use_m():
    ret = re.match("[a-zA-Z0-9_]{6}", "312a3g45678")
    print(ret.group())
    ret = re.match("[a-zA-Z0-9_]{8,17}", "1ad12f23s34455ff66")
    print(ret.group())


if __name__ == '__main__':
    use_start()
    print('-' * 20)
    use_plus()
    print('-' * 20)
    use_Questionmark()
    print('-'*20)
    use_m()