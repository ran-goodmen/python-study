import random


def use_if():
    age = 18
    if age >= 18:
        print("you can ent in netbar")
    else:
        print("you are too young, go home")


# 随机数
def use_if_two():
    player = int(input("请出拳 石头1 剪刀2 布3："))
    computer = random.randint(1, 3)
    print("computer: %d" % computer)

    if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        print("computer loss")
    elif player == computer:
        print("A draw")
    else:
        print("you lose")


if __name__ == '__main__':
    # use_if()
    use_if_two()
