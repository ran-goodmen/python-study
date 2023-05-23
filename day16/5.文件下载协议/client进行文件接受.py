#!/usr/bin/python3
# author ekubo
# 2023年05月10日
import struct
from socket import *

def recv_file():
    client = socket(AF_INET, SOCK_STREAM)
    dest_addr = ("192.168.147.1", 2001)
    client.connect(dest_addr)

    file_head_btypes = client.recv(4)
    filename_len = struct.unpack("I", file_head_btypes)
    filename = client.recv(filename_len[0])
    # 在相同目录下，做一个不重名的处理
    f = open(filename.decode("utf8").split(".")[0] + "1." + filename.decode("utf8").split(".")[1], "wb")

    filecontent_btypes = client.recv(4)
    filecontent_len = struct.unpack("I", filecontent_btypes)
    filecontent = client.recv(filecontent_len[0])
    f.write(filecontent)
    f.close()
    client.close()


if __name__ == '__main__':
    recv_file()
