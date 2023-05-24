def change(num):
    print("%d 在函数中的地址是 %d" % (num, id(num)))
    num = 20
    print(id(num))


if __name__ == '__main__':
    a = 10
    print(id(a))
    change(a)
    print(a)  # a不会发生改变
