import my_module


def test():
    print("-" * 50)


if __name__ == '__main__':
    my_module.print_line('*')
    print(my_module.name)
    test()
