#!/usr/bin/python3
# author ekubo
# 2023年05月26日
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#为了确保端口复用
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 2. 绑定
server_socket.bind(("", 7890))
# 3. 变为监听套接字
server_socket.listen(128)

new_client, client_addr = server_socket.accept()

# 通过浏览器访问，服务器端接受到的是http请求
data = new_client.recv(1000)
print(data.decode('utf8'))
response = "HTTP/1.1 200 OK\r\n"
response += "\r\n"
response += '<html><h1>nihao</h1></html>'
new_client.send(response.encode('utf8'))
