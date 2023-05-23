#!/usr/bin/python3
# author ekubo
# 2023年05月10日
import os
from socket import *
import struct

def tcp_init():
    server = socket(AF_INET, SOCK_STREAM)
    addr = ("", 2001)
    server.bind(addr)
    server.listen(128)
    return server


def send_file():
    server = tcp_init()
    new_client, client_addr = server.accept()
    print(client_addr)

    # 先发文件名(文件名长度+文件名)
    file_name = "file.mp4"
    b_file_name = file_name.encode("utf8")
    new_client.send(struct.pack("I", len(b_file_name)))
    new_client.send(b_file_name)
    # 字节流也可以用加号直接拼接，所以可以这样写：
    # head_btypes = struct.pack("I", len(b_file_name))
    # new_client.send(head_btypes + b_file_name)

    # 发文件大小
    file_size = os.stat(file_name).st_size
    text_head_btypes = struct.pack("I", file_size)
    new_client.send(text_head_btypes)
    # 再发文件内容（文件长度+文件内容）
    # rb是读字节流
    file = open(file_name, "rb")
    while True:
        file_content = file.read(10000)
        if file_content:
            new_client.send(file_content)
        else:
            break
    file.close()
    new_client.close()
    server.close()

if __name__ == '__main__':
    send_file()