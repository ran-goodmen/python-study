#!/usr/bin/python3

xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 175}

# 1.新增，修改
xiaoming["408"] = 120
xiaoming["age"] = 22
xiaoming.setdefault("408", 130)         # 若key存在，则不修改；若key不存在，则新建键值对
print(xiaoming)
print("*" * 50)

# 2.更新
xiaoming.update({"math": 120, "english": 80})
print(xiaoming)
print("*" * 50)

# 3.查询
print(xiaoming["math"])                 # 用这个若没有个这个键值对，则会直接报错
print(xiaoming.get("math"))             # 用这个不会报错，会返回一个none继续执行
for key in xiaoming:                    # 默认情况是打印key
    print(key)

for values in xiaoming.values():         # 打印values
    print(values)

for i in xiaoming.items():               # 打印键值对，返回的是元组
    print(i)                             # 元组是有序的，可以使用i[0]，i[1]只打印键或值
print("*" * 50)

# 4.删除
del xiaoming["math"]
print(xiaoming)
xiaoming.pop("english")
print(xiaoming)
xiaoming.popitem()                       # 随记删除
print(xiaoming)
xiaoming.clear()                         # 清空字典
