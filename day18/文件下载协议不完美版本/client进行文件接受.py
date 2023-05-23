#!/usr/bin/python3
# author ekubo
# 2023年05月10日
"""
此版在发送时循环发送，每次发送1000字节，当读取为空时停止发送
存在的问题：发送较大的文件时，发送端和接收端的速度不匹配，会造成出错的情况
如：发送端发送1000B过去，但接受端那会只接收了600B（recv不是到1000才接收，而是缓冲区有就接收），导致接收端程序运行到后面再接收4个字节的头部时，接收到的
是那剩下的400B里的内容，而不是真实的下一个头部
"""

import struct
from socket import *

def recv_file():
    client = socket(AF_INET, SOCK_STREAM)
    dest_addr = ("192.168.147.1", 2001)
    client.connect(dest_addr)

    # 接收文件名
    file_head_btypes = client.recv(4)
    filename_len = struct.unpack("I", file_head_btypes)
    filename = client.recv(filename_len[0])
    # 在相同目录下，做一个不重名的处理
    f = open(filename.decode("utf8").split(".")[0] + "1." + filename.decode("utf8").split(".")[1], "wb")

    # 接收文件内容
    while True:
        filecontent_btypes = client.recv(4)
        filecontent_len = struct.unpack("I", filecontent_btypes)
        if filecontent_len[0]>0:
            filecontent = client.recv(filecontent_len[0])
            f.write(filecontent)
        else:
            break
    f.close()
    client.close()


if __name__ == '__main__':
    recv_file()
