#! /usr/bin/python
# -*- coding: utf-8 -*-
from page.address_page import AddressPage
from page.base_page import BasePage
from my_utils import get_data
from my_config import config
from conftest import func_logger

class AddRemenberPage(BasePage):

    def add_remenber_success(self,username,acctid,phone):
        """
        添加成员操作成功
        :return:
        """
        try:
            ele = get_data.get_data_from_ini(node='add_remenber',key='username')
            self._find_element(method=ele[0],message=ele[1]).send_keys(username)
            config.case_log.info('添加用户页面》输入用户名')
            ele = get_data.get_data_from_ini(node='add_remenber', key='acctid')
            self._find_element(method=ele[0],message=ele[1]).send_keys(acctid)
            config.case_log.info('添加用户页面》输入账号')
            ele = get_data.get_data_from_ini(node='add_remenber', key='phone')
            self._find_element(method=ele[0], message=ele[1]).send_keys(phone)
            config.case_log.info('添加用户页面》输入手机号')
            ele = get_data.get_data_from_ini(node='add_remenber', key='save_btn')
            self._find_element(method=ele[0], message=ele[1]).click()
            config.case_log.info('添加用户页面》点击保存')
        except Exception as e:
            config.case_log.error('添加用户页面》添加用户：失败')
            raise e
        return AddressPage(self._driver)



    def add_remenber_failed(self,username,acctid,phone):
        """
        添加成员失败
        :return: assert 数据
        """
        try:
            ele = get_data.get_data_from_ini(node='add_remenber', key='username')
            self._find_element(method=ele[0], message=ele[1]).send_keys(username)
            config.case_log.info('添加用户页面》输入用户名')
            ele = get_data.get_data_from_ini(node='add_remenber', key='acctid')
            self._find_element(method=ele[0], message=ele[1]).send_keys(acctid)
            config.case_log.info('添加用户页面》输入账号')
            ele = get_data.get_data_from_ini(node='add_remenber', key='phone')
            self._find_element(method=ele[0], message=ele[1]).send_keys(phone)
            config.case_log.info('添加用户页面》输入手机号')
            ele = get_data.get_data_from_ini(node='add_remenber', key='save_btn')
            self._find_element(method=ele[0], message=ele[1]).click()
            config.case_log.info('添加用户页面》点击保存')
            ele = get_data.get_data_from_ini(node='add_remenber', key='error_message')
            eles = self._find_elements(method=ele[0], message=ele[1])
            error_message_list = []
            for i in eles:
                i_text = i.text
                error_message_list.append(i_text)
            return error_message_list
        except Exception as e:
            config.case_log.error('添加用户页面》添加用户：失败')
            raise e



