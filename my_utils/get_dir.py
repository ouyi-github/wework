#! /usr/bin/python
# -*- coding: utf-8 -*-

import os


def get_root_dir():
    """
    封装获取当前项目目录的方法
    :return:
    """
    now_dir = os.getcwd()
    while True:
        now_dir = os.path.split(now_dir)
        if now_dir[1] == 'wework':
            now_dir = os.path.join(now_dir[0],'wework')
            break
        now_dir = now_dir[0]
    return now_dir








if __name__ == "__main__":
    print(get_root_dir())