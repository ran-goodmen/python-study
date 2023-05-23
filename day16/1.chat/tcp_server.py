#!/usr/bin/python3
# author ekubo
# 2023年05月05日
import socket

def tcpserver():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('192.168.147.1', 2000)
    server.bind(addr)           # 和udp通信不一样，bind的时候端口没有激活
    server.listen(128)          # listen的时候端口才激活
    new_client, client_addr = server.accept()       # 与client建立连接，之后不需要ip地址
    # getsockname()可以获取socket对象的(ip,port)元组
    print(new_client)
    while True:
        data = new_client.recv(100).decode('utf8')
        print(data)
        send_data = input()
        new_client.send(send_data.encode('utf8'))

#   new_client.close()
#   server.close()


if __name__ == '__main__':
    tcpserver()