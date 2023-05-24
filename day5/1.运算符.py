# 定义算术运算函数
def calc():
    print(5 / 2)  # 不是整除
    print(5 // 2)  # 整除
    print(2 ** 3)  # 幂运算，2的三次方


# 关系运算和逻辑运算
def relation():
    num = int(input('请输入一个数:'))
    print(3 < num < 10)  # python支持一些数运算符关系连写


def logic():
    # year = int(input('请输入年份:'))
    # print(year%400 == 0 or year&4 == 0 and year%100 != 0)
    print(5 and 3)
    print(5 or 3)


# 位运算（只能对整数做位运算）
def bit():
    i = 5;
    j = 7;
    print(i & j)
    print(i | j)
    print(i >> 1)  # 右移是整除，负数的右移是减1再整除2
    print(i << 1)


# 这是一个入口，代码从这里开始执行
if __name__ == '__main__':
    # calc()
    # relation()
    # logic()
    bit()

# 优先级 算术运算符 > 位移运算符 > 比较运算符 > 逻辑运算符
