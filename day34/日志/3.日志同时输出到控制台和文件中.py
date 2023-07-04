#!/usr/bin/python3
# author ekubo
# 2023年07月03日
"""
用对象处理
"""
import logging

# 1.创建logger对象
logger = logging.getLogger()
logger.setLevel(logging.INFO)       # log等级总开关

# 2.创建一个handler，用于写入日志文件
fh = logging.FileHandler('log1.txt', encoding='utf8', mode='a')        # 'a'模式：打开进行写入，如果存在，则附加到文件末尾
fh.setLevel(logging.DEBUG)          # 输出到日志文件的log等级的开关

# 3.再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)        # 输出到控制台的log等级的开关

# 4.定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - &(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 5.将logger添加到handler中
logger.addHandler(fh)
logger.addHandler(ch)

logger.debug('这是logging debug message')
logger.info('这是logging info message')
logger.warning('这是logging warning message')
logger.error('这是logging error message')
logger.critical('这是logging critical message')