#!/usr/bin/python3
# author ekubo
# 2023年05月10日
import socket
import struct

file_name = 'file.txt'
b_file_name = file_name.encode('utf8')
# 变成4个字节的字节流
head = struct.pack("I", len(b_file_name))
print(head)
# 解包
source_head = struct.unpack("I", head)
print(source_head[0])
