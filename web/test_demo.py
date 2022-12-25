# -*- coding: utf-8 -*- 
# @Time : 2022/12/24 11:39 
# @Author : zhaosq 
# @File : test_demo.py
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # sleep(40)
        # print(self.driver.get_cookies())
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'secure': False,
             'value': 'true'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False,
             'value': ''},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688857217281666'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325103523675'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688857217281666'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a7373195'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '3833458474354371'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1674446354, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': '6WJjP1h9d7bPyUUmORJeahN82msvNo8N5rJjQX8fXksMy4YDX0n8g6yOefUxcfw0y2g2_dRmXCsXfPDRsatBHFi__UkkC-PbkFTWTbO3UqKoaodDi4brTpKM_D9vBrIHJrfT_jaS8Ssbso9rCAPi2ct3YJ01iuuu4Z9wpKBGFROfG-AM2PA6yMeDcWwQREXip8p9aawR6357OGo_7bAK_L0YbJCcoWsgv0sqFlq-BniBqjHjKmm3dw2CrtU-zDtcygU6McqPEluCT_JNKcchfg'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'P8GmEdQIL-9XuHJjI1egnA3j0JREHbo7S02iM6ZvZLgUXQZQvX9yNJJuu_9jAcsI'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1703390343, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'}]
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for cookie in cookies():
            if "expiry" in cookie.keys():
                cookies.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(5)
