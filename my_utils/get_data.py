#! /usr/bin/python
# -*- coding: utf-8 -*-
import os
from configparser import ConfigParser

import yaml


def get_data_from_ini(node,key):
    """
    二次封装：读取element.ini文件内容
    :param node: 节点。例如：main
    :param key: 键。例如：add_remenber
    :return: 返回包含element中method和message的列表
    """
    from my_config import config
    path = os.path.join(config.BASEDIR, 'data/element.ini')
    target = ConfigParser()
    target.read(filenames=path,encoding='utf-8')
    result = target.get(node,key)
    result = result.split('|')
    return result

def get_data_from_yaml(path):
    """
    二次封装：读取yaml文件内容
    :param path:
    :return:
    """
    with open(path,'r',encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data



if __name__ == "__main__":
    from my_config import  config
    path = os.path.join(config.BASEDIR,'data/case_data/add_remenber_data.yaml')
    s = get_data_from_yaml(path=path)
    print(s)
