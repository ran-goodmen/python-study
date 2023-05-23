#!/usr/bin/python3
# author ekubo
# 2023年04月06日
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
des_address = ('192.168.37.128', 2000)     # ubuntu ip
# des_address = ('192.168.147.1', 2000)    # 本地ip
client.sendto('中国'.encode('utf8'), des_address)
data = client.recvfrom(100)[0].decode('utf8')
print(data)

client.close()