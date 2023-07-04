#!/usr/bin/python3
# author ekubo
# 2023年07月03日
import logging

logging.basicConfig(
    level=logging.WARNING,              # 级别比高于等于WARNING的才会输出
    filename='log.txt',
    filemode='a',                       # 'a'模式：打开进行写入，如果存在，则附加到文件末尾
    # encoding='utf8',                    # 默认是GBK编码
    format='%(asctime)s - &(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s'
)

logging.info('这是logging info message')
logging.debug('这是logging debug message')
logging.warning('这是logging warning message')
logging.error('这是logging error message')
logging.critical('这是logging critical message')