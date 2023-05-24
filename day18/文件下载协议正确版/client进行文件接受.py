#!/usr/bin/python3
# author ekubo
# 2023年05月10日
import struct
from socket import *
import os

def cycle_recv(client, file, file_size):
    total = 0
    while total < file_size:
        data = client.recv(10000)
        file.write(data)
        total += len(data)
        # 显示下载进度
        print("\r %5.2f%s" % (total/file_size*100, "%"), end="")


def recv_file():
    client = socket(AF_INET, SOCK_STREAM)
    dest_addr = ("192.168.147.1", 2001)
    client.connect(dest_addr)

    file_head_btypes = client.recv(4)
    filename_len = struct.unpack("I", file_head_btypes)
    filename = client.recv(filename_len[0])
    # 在相同目录下，做一个不重名的处理
    f = open(filename.decode("utf8").split(".")[0] + "1." + filename.decode("utf8").split(".")[1], "wb")

    # 接一个文件大小
    train_head = client.recv(4)
    train_head_len = struct.unpack("I",  train_head)
    file_size = train_head_len[0]

    cycle_recv(client, f, file_size)
    f.close()
    client.close()


if __name__ == '__main__':
    recv_file()
