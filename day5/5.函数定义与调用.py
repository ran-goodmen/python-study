def sum(num1, num2):
    """
    这是一个求和
    :param num1:
    :param num2:
    :return: result
    """
    result = num1 + num2
    print("%d+%d=%d" % (num1, num2, result))
    return result


if __name__ == '__main__':
    num1 = int(input("请输入num1"))
    num2 = int(input("请输入num2"))
    result = sum(num1, num2)
