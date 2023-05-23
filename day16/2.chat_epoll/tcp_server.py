#!/usr/bin/python3
# author ekubo
# 2023年05月05日
import socket
import select
import sys


def tcpserver():
    if len(sys.argv) == 1:
        return
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = (sys.argv[1], 2000)
    server.bind(addr)           # 和udp通信不一样，bind的时候端口没有激活
    server.listen(128)          # listen的时候端口才激活
    new_client, client_addr = server.accept()       # 与client建立连接，之后不需要ip地址
    print(client_addr)
    # 创建epoll对象
    epoll = select.epoll()
    # 让epoll监听new_client, 标准输入流。参数：(文件描述符，事件)
    epoll.register(new_client.fileno(), select.EPOLLIN)
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)
    while True:
        # 哪个缓冲区有数据，就填写到events，返回给events的是一个列表,列表里面是元组(fd，事件)
        events = epoll.poll(-1)
        for fd, event in events:
            if fd == new_client.fileno():
                data = new_client.recv(100).decode('utf8')
                # 一端断开时，另外一端的recv不会阻塞，会返回空，内核会把client标记为可读，所以会一直打印空，因此这里
                # 加一个条件判断，防止无限打印空
                if data:
                    print(data)
                else:
                    print("对面断开了")
                    return
            elif fd == sys.stdin.fileno():
                try:
                    send_data = input()
                except EOFError:            # 按ctrl D把服务器/客户端断开
                    print("i want go")
                    return
                new_client.send(send_data.encode('utf8'))

    # new_client.close()
    # server.close()


if __name__ == '__main__':
    tcpserver()