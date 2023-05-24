# 在函数中去改变函数外某个变量的值
def use_list():
    demo_list = [1, 2, 3]  # demo_list是一个列表

    print(demo_list)
    print("定义列表后的内存地址 %d" % id(demo_list))

    print(demo_list[0])
    print(demo_list[1])
    print(demo_list[2])

    demo_list[0] = 10  # 这时候demo_list的地址不会发生改变，这就是可变数据类型
    print(id(demo_list))
    print(type(demo_list))


# 可变数据类型可以在子函数中通过其接口修改数据空间中的值
def change(my_list):
    my_list[0] = 20


if __name__ == '__main__':
    demo_list1 = [1, 2, 3]
    change(demo_list1)
    print(demo_list1)
