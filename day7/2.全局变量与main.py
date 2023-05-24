import my_module


def demo1():
    print(a)


if __name__ == '__main__':
    a = 10  # 在main里面的是全局变量
    demo1()
    # print(my_module.name)             # 这里会报错
    print(my_module.__name__)
    my_module.print_line()
