#!/usr/bin/python3
# author ekubo
# 2023年05月23日
"""
匹配出163邮箱，且@符号钱有4到20位
"""
import re

email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@163.com", "comxw@qq.com"]
for i in email_list:
    ret = re.match("\w{4,20}@163.com$", i)
    if ret:
        print(ret.group())
    else:
        print("%s不合规" % i)
