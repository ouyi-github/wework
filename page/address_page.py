#! /usr/bin/python
# -*- coding: utf-8 -*-
from page.add_partment_page import AddPartmentPage
from page.base_page import BasePage
from my_utils.get_data import get_data_from_ini
from my_config import config


class AddressPage(BasePage):

    def get_name(self):
        """
        获取通讯录中，姓名列的值
        :return: 包含姓名的列表
        """
        ele = get_data_from_ini(node='address',key='username')
        eles = self._find_elements(method=ele[0],message=ele[1])
        assert_list= []
        for ele in eles:
            ele_text = ele.text
            assert_list.append(ele_text)
        return assert_list


    def get_phone(self):
        """
        获取通讯录中，手机号列的值
        :return: 包含手机号的列表
        """
        ele = get_data_from_ini(node='address', key='phone')
        eles = self._find_elements(method=ele[0], message=ele[1])
        assert_list = []
        for ele in eles:
            ele_text = ele.text
            assert_list.append(ele_text)
        return assert_list

    def delete_remenber_from_phone(self,phone):
        """
        根据电话号码，删除对应用户
        :return: AddressPage
        """
        try:
            ele = get_data_from_ini(node='address',key='delete')
            self._find_element(method='xpath',message=f'//span[text()="{phone}"]/../../td[1]').click()
            self._find_element(method=ele[0],message=ele[1]).click()
            ele = get_data_from_ini(node='address',key='delete_save')
            self._find_element(method=ele[0],message=ele[1]).click()
            return AddressPage(self._driver)
        except Exception as e:
            pass

    def goto_add_department(self):
        """
        通讯录页面》点击添加部门按钮
        :return:
        """
        try:
            ele = get_data_from_ini(node='address',key='goto_addpartment1')
            self._find_element(method=ele[0],message=ele[1]).click()
            ele = get_data_from_ini(node='address',key='goto_addpartment2')
            self._find_element(method=ele[0],message=ele[1]).click()
            config.case_log.info('通讯录页面》点击添加部门按钮')
            return AddPartmentPage(self._driver)

        except Exception as e:
            config.case_log.error('通讯录页面》点击添加部门按钮：失败')
            pass


    def get_department_text(self):
        """
        获取部门列名称
        :return:
        """
        try:
            ele = get_data_from_ini(node='address',key='get_partment_names')
            eles = self._find_elements(method=ele[0],message=ele[1])
            departnames_list = [i.text for i in eles]
            return departnames_list
        except Exception as e:
            raise e









