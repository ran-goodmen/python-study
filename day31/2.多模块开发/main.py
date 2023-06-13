# 作者: 王道 龙哥
# 2022年03月21日16时15分04秒
from recv_msg import *
from handle_msg import *

"""
如果用from xxx import xxx 的方式导入不可变数据类型的全局变量，在不同模块下的全局变量是不同的
用improt xxx的方式导入则不同模块下的不可变数据类型的全局变量是同一个
对于可变数据类型，不论怎么导入都是不同的
"""

def main():
    # 1. 接收数据,往列表中放了0,1,2,3,4
    recv_msg()
    # 2. 测试是否接收完毕
    test_recv_data()
    # 3. 判断如果处理完成，则接收其它数据
    recv_msg_next()
    # 4. 处理数据
    handle_data()
    # 5. 测试是否处理完毕
    test_handle_data()
    # 6. 判断如果处理完成，则接收其它数据
    recv_msg_next()


if __name__ == "__main__":
    main()