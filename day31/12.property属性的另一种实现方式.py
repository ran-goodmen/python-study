#!/usr/bin/python3
# author ekubo
# 2023年06月20日
class Foo(object):
    def get_bar(self):
        print("getter...")
        return 'laowang'

    def set_bar(self, value):
        """必须两个参数"""
        print("setter...")
        return 'set value' + value

    def del_bar(self):
        print("deleter...")
        return 'laowang'

    BAR = property(get_bar, set_bar, del_bar, 'description...')

def use_foo():
    f = Foo()
    f.BAR
    f.BAR = 'xixi'
    del f.BAR
    desc = Foo.BAR.__doc__        # 调用property属性的doc方法获取第四个参数中设置的值：description...(这里必须使用类名调用类属性)
    print(desc)

if __name__ == '__main__':
    use_foo()