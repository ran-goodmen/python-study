def cycle():
    result = 0
    i = 0
    j = 0
    while i <= 100:
        result += i
        i += 1
        while j <= 10:
            result += j
            j += 1
    print("结果是%d" % result)


if __name__ == '__main__':
    cycle()