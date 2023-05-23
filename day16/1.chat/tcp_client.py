#!/usr/bin/python3
# author ekubo
# 2023年05月05日
import socket


def tcpclient():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest_addr = ('192.168.147.1', 2000)
    client.connect(dest_addr)  # 建立连接，完成三次握手
    while True:
        send_data = input()
        client.send(send_data.encode('utf8'))
        data = client.recv(1000)
        print(data.decode('utf8'))


#   client.close()                           #进行四次挥手


if __name__ == '__main__':
    tcpclient()
