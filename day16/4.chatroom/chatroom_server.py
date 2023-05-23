#!/usr/bin/python3
# author ekubo
# 2023年05月09日
"""
聊天室代码--服务端
服务端不发数据，只进行转发
客户端们之间进行通信，打印消息时显示自身标识
"""
import socket
import sys
import select


def chatServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 防止程序被异常终止后不能立即重启（因为程序被异常终止后端口不会立即释放）
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 不写就是0.0.0.0
    addr = ('', 2000)
    server.bind(addr)
    server.listen(128)
    epoll = select.epoll()
    epoll.register(server.fileno(), select.EPOLLIN)
    # 因为服务器端不写数据，所以不用监听stdin.fileno()
    # epoll.register(sys.stdin.fileno(), select.EPOLLIN)
    # 连上服务端的客户端列表
    client_list = []
    while True:
        # 返回给events的是一个列表，列表里面是元组(文件标识符，事件)
        events = epoll.poll(-1)
        for fd, event in events:
            if fd == server.fileno():
                new_client, client_addr = server.accept()
                print(client_addr)
                # 当有客户端连入时，添加新客户端对象到列表里
                client_list.append(new_client)
                # 并监听客户端
                epoll.register(new_client.fileno(), select.EPOLLIN)
            # 其他情况为fd是客户端的fileno的情况
            else:
                # remove_client记录要断开的客户端
                remove_client = None
                for c in client_list:
                    if fd == c.fileno():
                        client_data = c.recv(100)
                        # 如果不是空数据（即没人断开）
                        if client_data:
                            for other_c in client_list:
                                if other_c is c:
                                    pass
                                else:
                                    # 拿到数据，将信息发给其他客户端
                                    other_c.send(client_data)
                        # 如果是空数据，即有人断开
                        else:
                            remove_client = c
                # 如果remove_client不为空，从客户端列表中移除，并解除监听和关闭
                if remove_client:
                    client_list.remove(remove_client)
                    epoll.unregister(remove_client.fileno())
                    remove_client.close()


if __name__ == '__main__':
    chatServer()
