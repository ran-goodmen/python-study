"""
传送较大的文件时，因为缓冲区可能不够，一次接受不全，需要循环发送循环接受
"""


def cycle_recv(client, file, file_size):
    total = 0
    while total < file_size:
        data = client.recv(1000)
        file.write(data)
        total += len(data)