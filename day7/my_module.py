def print_line():
    print("*" * 50)


# if __name__ == '__main__':是为了实现一切皆模块，
if __name__ == '__main__':
    name = "xiongda"  # 虽然是全局变量，但是对外不可见
    print(__name__)
