# -*- coding: utf-8 -*- 
# @Time : 2022/12/22 11:02 
# @Author : zhaosq 
# @File : demo.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import pytest
import time


class TestWait:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_click(self):
        self.driver.get("https://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH, "//input[@value = 'click me']")
        element_doubleclick = self.driver.find_element(By.XPATH, "//input[@value = 'dbl click me']")
        element_rightclick = self.driver.find_element(By.XPATH, "//input[@value = 'right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        time.sleep(3)
        action.double_click(element_doubleclick)
        time.sleep(3)
        action.context_click(element_rightclick)
        action.perform()
        time.sleep(5)

    @pytest.mark.skip
    def test_move_to(self):
        self.driver.get("https://www.baidu.com/ ")
        element_test = self.driver.find_element(By.ID, 's-usersetting-top')
        action = ActionChains(self.driver)
        action.move_to_element(element_test)
        action.perform()
        time.sleep(5)

    def test_dragdrop(self):
        self.driver.get('https://sahitest.com/demo/dragDropMooTools.htm')
        drag_element = self.driver.find_element(By.ID, 'dragger')
        item_element = self.driver.find_element(By.XPATH, "//div[@class = 'item'][1]")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_element, item_element)
        action.perform()
        time.sleep(5)
if __name__ == '__main__':
    pytest.main()
