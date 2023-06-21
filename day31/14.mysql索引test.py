#!/usr/bin/python3
# author ekubo
# 2023年06月21日
from pymysql import connect


def main():
    conn = connect(host='192.168.37.128', port=3306, user='root', password='123', database='jing_dong', charset='utf8')
    cursor = conn.cursor()
    for i in range(100000):
        cursor.execute("insert into test_index values('ha-%d')" % i)
    conn.commit()


if __name__ == '__main__':
    main()
