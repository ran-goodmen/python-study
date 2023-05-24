num = 10


def demo1():
    global num
    num = num + 10
    print(num)


def demo2():
    print(num)


# 针对全局变量，读的时候可以不加global，若要修改全局变量，要加上global
demo1()
demo2()
