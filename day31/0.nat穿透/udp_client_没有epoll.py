#!/usr/bin/python
# coding=utf-8
"""
需要用云，因为要在不同外网网段
"""
from socket import *
import select
import sys

#男生

# 1. 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
# 注意 是元组，ip是字符串，端口是数字

# 2.这里是服务器的IP地址和端口
dest_addr = ('118.89.86.117', 8000)

# 3. 从键盘获取数据
send_data = input("请输入要发送的数据:")

# 4. 发送数据到指定的电脑上的指定程序中
udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

#从百度服务器接数据
recv_data = udp_socket.recvfrom(1000)
print(recv_data[0].decode('utf-8'))
# 5. 关闭套接字
#收到ip和端口后，进行分割
ip_port = recv_data[0].decode('utf-8').split()
ip_port[1] = int(ip_port[1])
ip_port=tuple(ip_port)
print(ip_port)
#给女方发一个world
udp_socket.sendto('I am boy'.encode('utf-8'), ip_port)
recv_data=udp_socket.recvfrom(1024)
print(recv_data[0].decode('utf-8'))

#男方先说话
while True:
    input_data = input('请输入数据')
    udp_socket.sendto(input_data.encode('utf-8'), ip_port)
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data[0].decode('utf-8'))
udp_socket.close()
