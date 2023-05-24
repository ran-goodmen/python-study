# 使用列表生成式可以减少代码量
# 列表表达式里面第一个数据就是其列表的成员
a = [x for x in range(10)]
print(a)

# 不使用的普通做法：
b = []
for x in range(10):
    b.append(x)
print(b)


# 两个for循环
a = [j for i in range(10) for j in range(i)]
print(a)
a = [[col * row for col in range(5)] for row in range(5)]
# 里面嵌套一个列表，后面循环5次，则为5个列表
print(a)


# 2维列表转1维列表,a为2维则x拿到的是1维，x为1维则j拿到的是单个元素
a = [j for x in a for j in x]
print(a)

# 使用if即有一个过滤条件，筛选偶数
a = [x for x in range(10) if x % 2 == 0]
print(a)

# if-else 三元表达式,必须把if-else写在for循环前面
a = [x if x%2==0 else x ** 2 for x in range(10)]
print(a)