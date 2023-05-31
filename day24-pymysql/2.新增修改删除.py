#!/usr/bin/python3
# author ekubo
# 2023年05月31日
from pymysql import *


def main():
    # 1.创建connect对象
    conn = connect(host='192.168.37.128', port=3306, database='day23_1', user='root', password='123', charset='utf8')

    # 2.创建cursor（光标，游标）对象
    cs1 = conn.cursor()

    # 3.执行sql语句,execute()放回的是影响的行数
    # 插入数据
    count = cs1.execute(
        'insert into goods_cates(cname) value ("硬盘")'
    )
    print(count)

    # 更新数据
    count = cs1.execute(
        'update goods_cates set cname="机械硬盘" where cname = "硬盘"'
    )
    print(count)

    # 删除数据
    count = cs1.execute(
        'delete from goods_cates where id = "11"'
    )
    print(count)

    # 4.提交之前的操作
    conn.commit()

    # 关闭cursor对象
    cs1.close()
    # 关闭conn对象
    conn.close()


if __name__ == '__main__':
    main()