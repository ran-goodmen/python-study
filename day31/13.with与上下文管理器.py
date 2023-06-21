#!/usr/bin/python3
# author ekubo
# 2023年06月20日
def m3():
    with open('test.txt', 'w') as f:
        f.write('python')


class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):  # 进入with时执行enter，返回值给as后面的
        print("entering")
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, *args):  # with结束时执行exit
        print("will exit")
        self.f.close()


# 另一种方式实现with(一要加上contextmanager装饰器，二要用yield分割函数，yield之前是enter部分，yield之后是exit部分)
def method_use_with():
    from contextlib import contextmanager

    @contextmanager
    def my_open(path, mode):
        try:
            f = open(path, mode)
            yield f
        except Exception as result:
            print(result)
        finally:
            f.close()  # 一旦发生异常，不会走到这里的close

    with my_open('output.txt', 'r') as f:
        f.write("hello , the simplest context manager")


def class_use_with():
    with File('test.txt', 'w') as f:
        print('I will write')
        f.write('python better')


if __name__ == '__main__':
    # m3()
    class_use_with()
    method_use_with()
