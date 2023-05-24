name_list = ["zhangsan", "lisi", "wangwu"]
print(name_list[0])
print(name_list.index("lisi"))          # 知道数据的内容，想知道数据的位置使用index，若有多个内容，则返回第一次出现的位置
name_list[1] = "李四"

# 1.增加
# 使用append向列表尾追加数据
name_list.append("wangmazi")
print(len(name_list))

# 使用insert在列表的指定索引位置插入数据
name_list.insert(2, "xiaomei")
name_list.insert(2, 10)                 # 在python中列表内可存放不同的数据类型

# 使用extend把其他列表的完整内容追加到当前了列表的末尾
temp_list = ["wukong", "bajie"]
name_list.extend(temp_list)
print(name_list)


# 2.删除
# 使用remove删除指定数据(仅移除第一次出现的)
name_list.remove("wangwu")

# 使用pop默认吧列表最后一个元素删除
name_list.pop()
name_list.pop(3)                        # 还可以指定删除元素的索引，即指哪删哪
# del name_list[3]                      可实现同样的功能
print(name_list)
# 使用clear清空列表
# name_list.clear()


# 3.统计
list_len = len(name_list)
print("列表中包含%d个元素" % list_len)

# 使用count统计列表中一个数据出现的次数
print(name_list.count("zhangsan"))


# 销毁列表
del name_list
