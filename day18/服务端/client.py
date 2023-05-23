#!/usr/bin/python3
# author ekubo
# 2023年05月11日

from socket import *
import struct


class Client:
    def __init__(self, ip, port):
        self.client:socket = None
        self.ip = ip
        self.port = port

    def tcp_connect(self):
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect((self.ip, self.port))

    def send_train(self, send_info_bytes):
        train_head_btypes = struct.pack("I", len(send_info_bytes))
        self.client.send(train_head_btypes + send_info_bytes)

    def recv_train(self):
        train_head_btypes = self.client.recv(4)
        info_len = struct.unpack("I", train_head_btypes)
        return self.client.recv(info_len[0])

    def send_command(self):
        while True:
            command = input()
            self.send_train(command.encode("utf8"))
            if command[:2] == 'ls':
                self.do_ls()
            elif command[:2] == 'rm':
                self.do_rm(command)
            elif command[:2] == 'cd':
                self.do_cd()
            elif command[:3] == 'pwd':
                self.do_pwd()
            elif command[:4] == 'puts':
                self.do_puts()
            elif command[:4] == 'gets':
                self.do_gets(command)
            # mkdir时客户端不需要任何操作
            elif command[:5] == 'mkdir':
                pass
            else:
                print('wrong command')

    def do_ls(self):
        data = self.recv_train().decode('utf8')
        print(data)

    def do_cd(self):
        print(self.recv_train().decode('utf8'))

    def do_pwd(self):
        print(self.recv_train().decode('utf8'))

    def do_rm(self, command):
        filename = command.split()[1]
        print(filename + " has been removed")

    def do_gets(self, command):
        filename = command.split()[1]
        storage_path = command.split()[2]
        f = open(filename.decode("utf8"))
        file_content = self.recv_train()
        f.write(file_content)
        f.close()
        print(filename + " has been downloaded")

    def do_puts(self):
        pass

    # 客户端不需要mkdir函数，因为只在服务器上操作
    # def do_mkdir(self):
    #     pass


if __name__ == '__main__':
    client = Client("192.168.37.128", 2000)
    client.tcp_connect()
    client.send_command()