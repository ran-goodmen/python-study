#!/usr/bin/python3
# author ekubo
# 2023年05月05日
import socket
import select
import sys


def chatclient():
    if len(sys.argv) == 1:
        ip='192.168.37.128'
    else:
        ip=sys.argv[1]
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest_addr = ('192.168.37.128', 2000)
    client.connect(dest_addr)  # 建立连接，完成三次握手
    # 创建epoll对象
    epoll = select.epoll()
    # 让epoll监听new_client, 标准输入流。参数：(文件描述符，事件)
    epoll.register(client.fileno(), select.EPOLLIN)
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)
    while True:
        # 哪个缓冲区有数据，就填写到events
        events = epoll.poll(-1)
        for fd, event in events:
            if fd == client.fileno():
                # 添加客户端的标识信息，getsockname()返回一个元组(ip, port)
                recv_data = client.recv(100)
                str = "{}:{}".format(client.getsockname()[0], client.getsockname()[1])
                data = str + " : " + recv_data.decode('utf8')
                print(data)
            elif fd == sys.stdin.fileno():
                try:
                    send_data = input()
                except EOFError:        # 按ctrl D把服务器/客户端断开
                    print("我断开了")
                    return
                client.send(send_data.encode('utf8'))


if __name__ == '__main__':
    chatclient()
