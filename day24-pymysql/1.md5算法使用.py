#!/usr/bin/python3
# author ekubo
# 2023年05月31日
import hashlib

f = open('./test.log', 'rb')
f_md5 = hashlib.md5()
f_md5.update(f.read())

# 打印f的MD5值
print(f_md5.hexdigest())