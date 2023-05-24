# 使用迭代遍历列表
"""
顺序地从列表中依次获取数据，每一次循环中，数据会保存在my_name变量中，在循环体内部可以访问到当前这一次获取到的数据
for my_name in 列表变量:
    print("我的名字是%s" % my_name)
"""

name_list = ["zhangsan", "lisi", "wangwu"]
for my_name in name_list:
    print("我的名字是%s" % my_name)