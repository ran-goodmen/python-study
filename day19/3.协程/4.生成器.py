def fblq(n):
    current = 0
    num0, num1 = 0, 1
    while current < n:
        num = num0
        num0, num1 = num1, num0 + num1
        current += 1
        yield num
    return "done"       # 正常用for循环调用生成器时拿不到这个返回值，看下面的操作


if __name__ == '__main__':
    fb = fblq(10)
    for i in fb:
        print(i, end=' ')
    print()
    try:
        print(next(fb))
    except StopIteration as e:
        print("生成器返回值: %s" % e.value)