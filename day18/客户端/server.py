#!/usr/bin/python3
# author ekubo
# 2023年05月11日
"""
注：客户端只是进行显示操作，真正的业务逻辑都在服务端完成

功能：1、
实现输入 ls 时，显示文件大小 文件名效果
输入 gets file 可以下载文件 file，输入 puts file可以上传 file文件
rm file 可以删除 file 文件（使用 os.remove 接口）
cd 可以切换路径(使用 chdir 接口)
pwd 可以显示当前在服务器上的路径（使用 getcwd）类似简洁版百度网盘
"""

import os
import socket
import struct
from socket import *

class Server:
    def __init__(self, ip, port):
        self.server:socket = None
        self.ip = ip
        self.port = port

    def tcp_init(self):
        self.server = socket(AF_INET, SOCK_STREAM)
        addr = (self.ip, self.port)
        self.server.bind(addr)
        self.server.listen(128)

    def task(self):
        new_client, client_addr = self.server.accept()
        user = User(new_client)
        user.deal_command()


class User:
    def __init__(self, new_client):
        self.new_client = new_client
        self.username = None
        self.path = os.getcwd()         # 存储连上用户的路径

    def send_train(self, send_info_bytes):
        train_head_btypes = struct.pack("I", len(send_info_bytes))
        self.new_client.send(train_head_btypes + send_info_bytes)

    def recv_train(self):
        train_head_btypes = self.new_client.recv(4)
        info_len = struct.unpack("I", train_head_btypes)
        return self.new_client.recv(info_len[0])

    def deal_command(self):
        while True:
            command = self.recv_train().decode("utf8")
            if command[:2] == "ls":
                self.do_ls()
            elif command[:2] == "cd":
                self.do_cd(command)
            elif command[:2] == "rm":
                self.do_rm(command)
            elif command[:3] == "pwd":
                self.do_pwd()
            # 客户端要gets，服务端就puts
            elif command[:4] == 'puts':
                self.do_gets()
            # 客户端要puts，服务端就gets
            elif command[:4] == 'gets':
                self.do_puts(command)
            elif command[:5] == 'mkdir':
                self.do_mkdir(command)

    def do_ls(self):
        data = ''
        for file in os.listdir(self.path):
            data += file + ' '*5 + str(os.stat(file).st_size) + '\n'
        data = data[:-2]            # 让最后一行不显示换行
        self.send_train(data.encode('utf8'))

    def do_cd(self, command):
        path = command.split()[1]
        os.chdir(path)
        self.path = os.getcwd()
        self.send_train(self.path.encode('utf8'))

    def do_pwd(self):
        self.send_train(self.path.encode('utf8'))

    def do_rm(self, command):
        path_file = command.split()[1]
        os.remove(path_file)

    def do_puts(self, command):
        # 不用发文件名，因为客户端知道文件名
        filename = command.split()[1]
        # 发文件内容
        file = open(filename, "rb")
        file_content = file.read()
        self.send_train(file_content)

    def do_gets(self):
        pass

    def do_mkdir(self, command):
        dir_name = command.split()[1]
        os.mkdir(dir_name)


if __name__ == '__main__':
    server = Server('', 2000)
    server.tcp_init()
    server.task()