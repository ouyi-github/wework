#! /usr/bin/python
# -*- coding: utf-8 -*-
from page.add_remenber_page import AddRemenberPage
from page.address_page import AddressPage
from page.base_page import BasePage
from my_utils import get_data
from my_config import config
from conftest import func_logger



class MainPage(BasePage):
    def goto_add_remenber(self):
        """
        点击添加成员
        :return: AddRemenberPage
        """
        try:
            ele = get_data.get_data_from_ini('main','add_remenber')
            self._find_element(method=ele[0],message=ele[1]).click()
            config.case_log.info('首页》点击添加用户')
        except Exception as e:
            config.case_log.error('首页》点击添加用户：失败')
            raise e
        return AddRemenberPage(base_driver=self._driver)


    def goto_main(self):
        """
        点击首页
        :return: MainPage
        """
        try:
            ele = get_data.get_data_from_ini('main', 'main')
            self._find_element(method=ele[0], message=ele[1]).click()
            config.case_log.info('点击返回首页')
            try:
                ele = get_data.get_data_from_ini('add_remenber', 'leave_page')
                self._find_element(method=ele[0], message=ele[1]).click()
                config.case_log.info('确认离开此页面')
            except:
                pass
        except Exception as e:
            config.case_log.error('返回首页：失败')
            raise
        return MainPage(self._driver)

    def goto_address(self):
        """
        点击通讯录
        :return:
        """
        try:
            ele = get_data.get_data_from_ini(node='main',key='adress')
            self._find_element(method=ele[0],message=ele[1]).click()
            config.case_log.info('首页》点击通讯录')
            return AddressPage(self._driver)
        except Exception as e:
            config.case_log.error('首页》点击通讯录：失败')
            raise






