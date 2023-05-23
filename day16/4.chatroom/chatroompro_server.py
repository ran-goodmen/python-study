#!/usr/bin/python3
# author ekubo
# 2023年05月09日
"""
聊天室代码--服务端
服务端不发数据，只进行转发
客户端们之间进行通信，打印消息时显示自身标识

1. 改成字典，用哈希查找                    √
2. 添加标识信息（这个是在客户端改进）         √
3. 一个客户端断开，其他客户端显示            √
"""
import socket
import select


def chatServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 防止程序被异常终止后不能立即重启（因为程序被异常终止后端口不会立即释放）
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 不写就是0.0.0.0
    addr = ('', 2000)
    server.bind(addr)
    server.listen(128)
    # 构建epoll对象
    epoll = select.epoll()
    epoll.register(server.fileno(), select.EPOLLIN)
    # 因为服务器端不写数据，所以不用监听stdin.fileno()
    # epoll.register(sys.stdin.fileno(), select.EPOLLIN)
    # 连上服务端的客户端字典,用客户端文件标识符client.fileno() 作为键，用客户端对象 client 作为值
    client_dic = {}
    while True:
        # 返回给events的是一个列表，列表里面是元组(文件标识符，事件)
        events = epoll.poll(-1)
        for fd, event in events:
            if fd == server.fileno():
                new_client, client_addr = server.accept()
                print(client_addr)
                # 当有客户端连入时，添加新客户端对象到字典里
                client_dic[new_client.fileno()] = new_client
                # 并监听客户端
                epoll.register(new_client.fileno(), select.EPOLLIN)
            # 其他情况为fd是客户端的fileno的情况
            else:
                # 获取client对象
                client = client_dic[fd]
                # 获取数据
                client_data = client.recv(1000)
                # 如果不是空数据，就发给其他客户端
                if client_data:
                    for other_clientfd in client_dic:
                        if other_clientfd == fd:
                            pass
                        else:
                            other_client = client_dic[other_clientfd]
                            other_client.send(client_data)
                # 如果是空数据，则有人断开了
                else:
                    for other_clientfd in client_dic:
                        if other_clientfd == fd:
                            pass
                        else:
                            other_client = client_dic[other_clientfd]
                            # 像其他客户端发送断开信息，使用getpeername()可以从new_client对象中获取客户端的ip,port
                            str = "{}:{}".format(client.getpeername()[0], client.getpeername()()[1]) +' has unconnected'
                            other_client.send(str.encode("utf8"))
                    remove_client = client_dic.pop(fd)
                    epoll.unregister(fd)
                    remove_client.close()


if __name__ == '__main__':
    chatServer()
