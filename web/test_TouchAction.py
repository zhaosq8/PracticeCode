# -*- coding: utf-8 -*- 
# @Time : 2022/12/23 13:37 
# @Author : zhaosq 
# @File : test_TouchAction.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class TestAction():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touch(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element(By.ID, 'kw').send_keys('selenium测试')
        self.driver.find_element(By.ID,'su').click()
        action = TouchActions()