#! /usr/bin/python
# -*- coding: utf-8 -*-

from my_config import config
import functools


def pytest_collection_modifyitems(session, config, items):
    """
    钩子函数
    :param session:
    :param config:
    :param items:
    :return:
    """
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape') # 设置用例名字的编码方式
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')  # 设置用例ID的编码方式



# 自定义公共装饰器

def func_logger(func):
    """
    自定义函数执行日志记录装饰器
    :param func:
    :return:
    """
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        config.case_log.info(f'执行函数：{func.__name__}')
        return func(*args,**kwargs)
    return wrapper

