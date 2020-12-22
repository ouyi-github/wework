#! /usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
import pytest
from page.main_page import MainPage
from my_config import config
from my_utils.get_data import get_data_from_yaml
from my_utils.get_time import get_now_time
from conftest import func_logger
import allure
import inspect

@allure.story('添加用户')
class TestMain_AddRemenber:
    case_data = get_data_from_yaml(config.yaml_add_remenber_path)
    def setup_class(self):
        self.mainpage = MainPage()

    def teardown(self):
        self.mainpage.goto_main()

    def teardown_class(self):
        s = self.mainpage.goto_address()
        for i in ['13118175982','13118172239','11111113211']:
            s.delete_remenber_from_phone(phone=i)
            time.sleep(1)
        self.mainpage._driver.quit()

    @allure.title('添加用户成功')
    @func_logger
    @pytest.mark.parametrize('username,acctid,phone',case_data['add_remenber_success'])
    def test_main_add_remenber_success(self,username,acctid,phone):
        try:
            with allure.step('首页》点击添加用户'):
                res = self.mainpage.goto_add_remenber()
            with allure.step('添加用户操作'):
                res = res.add_remenber_success(username=username,acctid=acctid,phone=phone)
            assert username in res.get_name()
            assert str(phone) in res.get_phone()
            config.case_log.info(f'用例：{inspect.stack()[0][3]} success')
        except Exception as e:
            config.case_log.error(f'用例：{inspect.stack()[0][3]} failed')
            failed_imgs = os.path.join(config.failed_img_dir,f'{inspect.stack()[0][3]}-{get_now_time()}.PNG') # 失败截图路径
            self.mainpage.get_img_for_failedcase(failed_img=failed_imgs)
            raise e


    @allure.title('添加用户失败')
    @func_logger
    @pytest.mark.parametrize('username,acctid,phone,error_message',case_data['add_remenber_failed'])
    def test_main_add_remenber_failed(self,username,acctid,phone,error_message):
        try:
            with allure.step('首页》点击添加用户'):
                res = self.mainpage.goto_add_remenber()
            with allure.step('添加用户操作'):
                res = res.add_remenber_failed(username=username,acctid=acctid,phone=phone)
            assert error_message in res
            config.case_log.info(f'用例：{inspect.stack()[0][3]} success')
        except Exception as e:
            config.case_log.error(f'用例：{inspect.stack()[0][3]} failed')
            failed_imgs = os.path.join(config.failed_img_dir,f'{inspect.stack()[0][3]}-{get_now_time()}.PNG')  # 失败截图路径
            self.mainpage.get_img_for_failedcase(failed_img=failed_imgs)
            raise e


@allure.story('添加部门')
class TestAddDepartment:
    casedata = get_data_from_yaml(path=os.path.join(config.BASEDIR,'data/case_data/add_department_data.yaml'))
    def setup_class(self):
        self.mainpage = MainPage()




    @allure.title('添加部门成功')
    @func_logger
    @pytest.mark.parametrize('department_name,belong_to_department',casedata['success'])
    def test_add_department_success(self,department_name,belong_to_department):
        try:
            with allure.step('首页》点击通讯录'):
                res = self.mainpage.goto_address()
            with allure.step('通讯录》点击添加部门'):
                res = res.goto_add_department()
            with allure.step('添加部门'):
                res = res.add_partment_page_success(department_name,belong_to_department)
                time.sleep(1)
                assert department_name in res.get_department_text()
                config.case_log.info(f'用例：{inspect.stack()[0][3]} success')
        except Exception as e:
            failed_dir = os.path.join(config.failed_img_dir,f'{inspect.stack()[0][3]}-{get_now_time()}.PNG')
            self.mainpage.get_img_for_failedcase(failed_dir)
            config.case_log.error(f'用例：{inspect.stack()[0][3]} failed')
            raise e


if __name__ == "__main__":
    result = config.result_path
    report = config.report_path
    pytest.main(['-vs','test_wework_main.py',f'--alluredir={result}'])
    os.system(f'allure generate {result} -o {report}')