#!/usr/bin/python3
# author ekubo
# 2023年05月31日
from pymysql import *


# 查询一行
# fetchone()查询结果集的第一行数据，返回一个元组
def main1():
    conn = connect(host='192.168.37.128', port=3306, database='day23_1', user='root', password='123', charset='utf8')
    cs1 = conn.cursor()


    count = cs1.execute(
        'select id, name from goods where id  >= 4'
    )
    print("查询到%d条数据"%count)
    for i in range(count):
        result = cs1.fetchone()
        print(result)
    cs1.close()
    conn.close()


# 查询全部
# fetchall()获取结果集的所有行，一行构成一个元组，再将这些元组装入一个元组返回
def main2():
    conn = connect(host='192.168.37.128', port=3306, database='day23_1', user='root', password='123', charset='utf8')
    cs1 = conn.cursor()

    # 查询一行
    count = cs1.execute(
        'select id, name from goods where id  >= 4'
    )
    print("查询到%d条数据" % count)
    print(cs1.fetchall())
    cs1.close()
    conn.close()


if __name__ == '__main__':
    # main1()
    main2()