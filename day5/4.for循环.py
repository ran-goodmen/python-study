def use_for():
    a = [1, 2, 3]
    for i in a:
        print(i, end=' ')

# range左闭又开，写10则是打印到9
def use_range():
    for i in range(10):
        print(i, end=' ')


if __name__ == '__main__':
    # use_for()
    use_range()