#! /usr/bin/python
# -*- coding: utf-8 -*-

import logging


class MyLogger:
    """
    二次封装日志生成器
    """
    def __init__(self,name,path,level,format):
        self.logger = logging.getLogger(name=name)
        self.logger.setLevel(logging.DEBUG)
        self.path = path
        self.level = level
        self.format = format

    def get_logger(self):
        """
        获取一个用于文件写入的logger
        :return:
        """
        if not self.logger.hasHandlers():
            handler_file = logging.FileHandler(self.path,encoding='utf-8')
            handler_file.setLevel(self.level)
            handler_file.setFormatter(self.format)
            self.logger.addHandler(handler_file)
        else:
            self.logger = self.logger
        return self.logger


if __name__ == "__main__":
    format = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s-%(filename)s-%(lineno)d-%(funcName)s')
    s = MyLogger(name='root',path='case.log',level=logging.INFO,format=format).get_logger()
    s.info('666')
    s.info('777')
    s.error('888')