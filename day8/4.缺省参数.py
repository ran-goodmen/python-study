#!/usr/bin/python3
# author ekubo
# 2022年10月18日

# 缺省参数指传参时可以不传对应参数
def print_info(name, gender = True):
    gender_text = "boy"
    if not gender:
        gender_text = "girl"
    print("%s 是 %s" % (name, gender_text))


if __name__ == '__main__':
    print_info("xiongda")