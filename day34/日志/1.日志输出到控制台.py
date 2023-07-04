#!/usr/bin/python3
# author ekubo
# 2023年07月03日
"""
日志等级：从低到高
DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL
"""
import logging

# basicConfig中格式有很多参数可用，这个format可以记一下，是工作中常用的格式
logging.basicConfig(
    level=logging.WARNING,              # 级别比高于等于WARNING的才会输出
    format='%(asctime)s - &(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s'
)

logging.info('这是logging info message')
logging.debug('这是logging debug message')
logging.warning('这是logging warning message')
logging.error('这是logging error message')
logging.critical('这是logging critical message')