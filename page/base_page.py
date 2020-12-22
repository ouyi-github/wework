#! /usr/bin/python
# -*- coding: utf-8 -*-
import os
import time

import allure
import yaml
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from my_config import config


class BasePage:
    """
    页面类基类，用于其他页面类继承
    """
    def __init__(self,base_driver:WebDriver=None):
        if base_driver is None:
            self._driver = webdriver.Chrome()
            self._driver.maximize_window()
            self._driver.implicitly_wait(3)
            self._driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
            self._cookie_login()
        else:
            self._driver = base_driver



    def _cookie_login(self):
        """
        添加cookie后，登录企业微信
        :return:
        """
        with open(os.path.join(config.BASEDIR,'data/cookie.yaml'), 'r', encoding='utf-8') as f:
            cookies = yaml.safe_load(f)
            print(cookies)
        for cookie in cookies:
            self._driver.add_cookie(cookie)
        self._driver.get('https://work.weixin.qq.com/wework_admin/frame')

    def _find_element(self,method,message):
        """
        二次封装元素查找方法
        :param method: 定位元素的方法。例如：By.ID
        :param message: 元素信息。例如："kw"
        :return:
        """
        try:
            if method == "id":
                return self._driver.find_element(By.ID,message)
            elif method == "name":
                return self._driver.find_element(By.NAME,message)
            elif method == "xpath":
                return self._driver.find_element(By.XPATH,message)
            elif method == "css":
                return self._driver.find_element(By.CSS_SELECTOR,message)
            elif method == 'class':
                return self._driver.find_element(By.CLASS_NAME,message)
            elif method == 'link_text':
                return self._driver.find_element(By.LINK_TEXT,message)
            elif method == 'partial_link_text':
                return self._driver.find_element(By.PARTIAL_LINK_TEXT,message)
            elif method == 'tag_name':
                return self._driver.find_element(By.TAG_NAME,message)
        except:
            raise NoSuchElementException(f'not find element：method={method},message={message}')

    def _find_elements(self, method, message):
        """
        二次封装元素查找方法
        :param method: 定位元素的方法。例如：By.ID
        :param message: 元素信息。例如："kw"
        :return:
        """
        try:
            if method == "id":
                return self._driver.find_elements(By.ID, message)
            elif method == "name":
                return self._driver.find_elements(By.NAME, message)
            elif method == "xpath":
                return self._driver.find_elements(By.XPATH, message)
            elif method == "css":
                return self._driver.find_elements(By.CSS_SELECTOR, message)
            elif method == 'class':
                return self._driver.find_elements(By.CLASS_NAME, message)
            elif method == 'link_text':
                return self._driver.find_elements(By.LINK_TEXT, message)
            elif method == 'partial_link_text':
                return self._driver.find_elements(By.PARTIAL_LINK_TEXT, message)
            elif method == 'tag_name':
                return self._driver.find_elements(By.TAG_NAME, message)
        except:
            raise NoSuchElementException(f'not find elements：method={method},message={message}')

    def get_img_for_failedcase(self,failed_img):
        """
        二次封装：case失败截图
        :param failed_img:
        :return:
        """
        self._driver.get_screenshot_as_file(filename=failed_img)
        allure.attach.file(source=failed_img, name='失败截图', attachment_type=allure.attachment_type.PNG)











def get_cookie():
    """
    复用chrome浏览器，获取登录后cookie,写入cookie.yaml文件
    :return:
    """
    option = Options()
    option.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=option)
    cookies = driver.get_cookies()
    print(os.getcwd())
    with open(os.path.join(config.BASEDIR,'data/cookie.yaml'),'w',encoding='utf-8') as f:
        yaml.safe_dump(data=cookies,stream=f)





if __name__ == "__main__":
        get_cookie()









