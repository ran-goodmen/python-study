#!/usr/bin/python3
# author ekubo
# 2023年05月26日
import re

# 匹配不是以4,7结尾的手机号码（11位）
tels = ['13100001234', '18912344321', '10086', '18800087777']
for tmp in tels:
    ret = re.match('1\d{9}[^(4|7)]$', tmp)
    # ret = re.match('1\d{9}[0-35-68-9]$', tmp)
    if ret:
        print(ret.group())
    else:
        print('%s 不是一个合适的号码'%tmp)

# 匹配出163、126、qq的邮箱
mails = ['test@163.com', 'test@126.com', 'test@qq.com', 'test@gmail.com','test@qq.com.']
for tmp in mails:
    ret = re.match('\w{4,20}@(163|126|qq).com$', tmp)
    if ret:
        print(ret.group())
    else:
        print('%s不是指定邮箱'%tmp)

# 匹配区号和电话号码
ret = re.match('([^-]+)-(\d+)', '010-12345678')
print(ret.group())

# 用r""这种格式可以引用分组中匹配到的数据，从而保证后面标签里的内容和前面标签里的内容一样
ret = re.match(r'<([a-zA-Z]*)>\w*</\1>', '<html>nihao</html>')
print(ret.group())


