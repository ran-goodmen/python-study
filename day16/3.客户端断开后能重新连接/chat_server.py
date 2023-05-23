#!/usr/bin/python3
# author ekubo
# 2023年05月05日
import socket
import select
import sys
"""
一对一聊天--服务端代码
客户端可以断了再连
"""

def tcpserver():
    if len(sys.argv) == 1:
        return
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = (sys.argv[1], 2000)
    server.bind(addr)  # 和udp通信不一样，bind的时候端口没有激活
    server.listen(128)  # listen的时候端口才激活

    # 创建epoll对象
    epoll = select.epoll()
    # 让epoll监听server。参数：(文件描述符，事件)
    epoll.register(server.fileno(), select.EPOLLIN)
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)
    while True:
        # 哪个缓冲区有数据，就填写到events，返回给events的是一个列表,列表里面是元组(fd，事件)
        events = epoll.poll(-1)
        for fd, event in events:
            if fd == server.fileno():
                # 有客户端连接，就注册让epoll监听它
                new_client, client_addr = server.accept()
                print(client_addr)
                epoll.register(new_client.fileno(), select.EPOLLIN)
            if fd == new_client.fileno():
                data = new_client.recv(100).decode('utf8')
                # 一端断开时，另外一端的recv不会阻塞，会返回空，内核会把client标记为可读，所以会一直打印空，因此这里
                # 加一个条件判断，防止无限打印空
                if data:
                    print(data)
                else:
                    print("对面断开了")
                    # 对面断开连接后，不在监听new_client，在关闭new_client
                    epoll.unregister(new_client.fileno())
                    new_client.close()
                    break
            elif fd == sys.stdin.fileno():
                try:
                    send_data = input()
                except EOFError:  # 按ctrl D把服务器/客户端断开
                    print("i want go")
                    return
                new_client.send(send_data.encode('utf8'))


if __name__ == '__main__':
    tcpserver()
