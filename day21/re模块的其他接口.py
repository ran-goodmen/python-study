#!/usr/bin/python3
# author ekubo
# 2023年05月26日
import re

# search 的用法, search只能匹配第一个
ret = re.search("\d+", '阅读次数是 9999')
print(ret.group())
ret = re.search("\d+", 'python = 9999, c = 7890, c++ = 12345')
print(ret.group())

# findall能找到所有匹配的，返回的是一个列表
ret = re.findall('\d+', 'python = 9999, c = 7890, c++ = 12345')
print(ret)

# sub可以对字符串进行替换处理
s = 'hello world, now is 2023/5/25 15:15, 现在是2023年5月25日15时15分'
ret_s = re.sub("年|月", '/', s)
ret_s = re.sub("日|分", ' ', ret_s)
ret_s = re.sub("时", ':', ret_s)
print(ret_s)

# re.split对字符串进行分割，可以用多个符号分割
ret = re.split(":| ", "info:xiaozhang 33 shandong")
print(ret)