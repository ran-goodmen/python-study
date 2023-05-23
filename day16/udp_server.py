#!/usr/bin/python3
# author ekubo
# 2023年04月06日
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)       # AF_INET指ipv4，SOCK_DGRAM指UDP
address = ('192.168.147.1', 2000)                               # 服务器端ip地址和端口
server.bind(address)
data, client_addr = server.recvfrom(100)                        # 100代表接受的长度
print(data.decode('utf8'))
server.sendto('很牛'.encode('utf8'), client_addr)
server.close()