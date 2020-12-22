#! usr/bin/python
# -*- coding: utf-8 -*-
import logging
import os

from my_utils.get_dir import get_root_dir
from my_utils.get_time import get_now_time
from my_utils.get_logger import MyLogger

# 项目跟目录
BASEDIR = get_root_dir()

# case_data文件路径
yaml_add_remenber_path = os.path.join(BASEDIR,'data/case_data/add_remenber_data.yaml')

# 日志设置
logger_path = os.path.join(BASEDIR,f'logs/case_log/{get_now_time()}.log')
logger_level = logging.INFO
logger_format = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s-%(filename)s-%(lineno)d-%(funcName)s')
# 实例化一个logger
case_log = MyLogger(name='root',path=logger_path,level=logger_level,format=logger_format).get_logger()

# allure报告目录
result_path = os.path.join(BASEDIR,f'report/allure_result/{get_now_time()}')
report_path = os.path.join(BASEDIR,f'report/allure_report/{get_now_time()}')

# 失败截图目录
failed_img_dir = os.path.join(BASEDIR,'img/case_failed_img')





