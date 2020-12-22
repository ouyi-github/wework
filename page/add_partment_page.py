#! /usr/bin/python
# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By
from page.base_page import BasePage
from my_utils.get_data import get_data_from_ini
from my_config import config


class AddPartmentPage(BasePage):

    def add_partment_page_success(self,department_name,belong_to_department):
        """
        添加部门
        :return:
        """
        try:
            ele = get_data_from_ini(node='add_department',key='department_name')
            self._find_element(method=ele[0],message=ele[1]).send_keys(department_name)
            ele = get_data_from_ini(node='add_department', key='belong_to_department')
            self._find_element(method=ele[0], message=ele[1]).click()
            time.sleep(0.5)
            self._driver.find_element(By.XPATH, f'//form[@class="form"]//a[text()="{belong_to_department}"]').click()
            # ele = self._driver.find_element(By.XPATH,f'//form[@class="form"]//a[text()="{belong_to_department}"]').click()
            # self._driver.execute_script("arguments[0].click();", ele)
            ele = get_data_from_ini(node='add_department', key='add_save')
            self._find_element(method=ele[0], message=ele[1]).click()
            config.case_log.info('添加部门')
            from page.address_page import AddressPage
            return AddressPage(self._driver)
        except Exception as e:
            config.case_log.error('添加部门：失败')
            raise e

