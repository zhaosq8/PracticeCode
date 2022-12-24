# -*- coding: utf-8 -*- 
# @Time : 2022/12/23 14:39 
# @Author : zhaosq 
# @File : test_window.py
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWindow():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID, 's-top-loginbtn').click()
        print(self.driver.current_window_handle)
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__regLink').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        sleep(3)


if __name__ == '__main__':
    pytest.main()