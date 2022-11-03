# x = input('请输入:')           # 这里的x是字符串，如果要进行运算需要转为整型或浮点型
# print(x)
# print(1+int(x))

name = '小王'
student_number = 1001
price = 10.2
weight = 6.25
money = price * weight

print("我的名字是%s" %name)
print("我的学号是%06d" %student_number)      #保留6位
print("苹果的单价是%.02f元/斤，购买%.02f斤，需要支付%.02f元" %(price, weight, money)) #保留小数点后面两位
# 若要输出百分号，则要用两个百分号
