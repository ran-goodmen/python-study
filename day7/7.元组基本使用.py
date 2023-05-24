# i = (50)                        # i是整型
# print(type(i))

info_tuple = (50,)  # 加上逗号才是元组
print(type(info_tuple))

# 元组只有两个函数,index和count

# 将一个元组格式化为字符串
info_tuple1 = ("小明", 21, 1.85)
print("%s 年龄是 %d 身高是 %.2f" % info_tuple1)
info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple1
print(type(info_str))


# 元组列表互相转换
info = ("xiaomei", 18)
demo_list = list(info)
print(type(demo_list))
demo_tuple = tuple(demo_list)
print(type(demo_tuple))

demo = tuple(x for x in range(10))
print(demo)