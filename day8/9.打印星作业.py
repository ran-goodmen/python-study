#!/usr/bin/python3
# author ekubo
# 2022年10月20日

def print_diamond():
    i = 1
    j = 1
    while j <= 9:
        i = 1
        while i <= abs(5 - j):
            print(' ', end=' ')
            i += 1
        i = 1
        while i <= 9 - 2 * abs(5 - j):
            if i == 1 or i == 9 - 2 * abs(5 - j):
                print('*', end=' ')
            else:
                print(' ', end=' ')
            i += 1
        print()
        j += 1

# 从101个数找出只出现一次的那个数，其余数皆出现2次
def find_list_one():
    list1 = [8, 3, 2, 6, 2, 8, 3]
    result = 0
    for i in list1:
        result ^= i
    print(result)

# 从102个数找出只出现一次的那两个数，其余数皆出现2次
def find_list01_one():
    list1 = [8, 3, 2, 6, 2, 8, 3, 11]
    result = 0
    for i in list1:
        result ^= i
    split_flag = result & -result    # 任何数与其相反数与得到的是此数二进制最低位1的那个数
    result1 = 0
    result2 = 0
    for i in list1:
        if split_flag & i:
            result1 ^= i
        else:
            result2 ^= i
    print("%d %d"%(result1, result2))


if __name__ == '__main__':
    # print_diamond()
    # find_list_one()
    find_list01_one()
