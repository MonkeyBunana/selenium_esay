# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 0002 19:39:58
# @Author  : zll
# @File    : page_base.py
from common.page_read import ReadConfig


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        baseUrl = ReadConfig().getValue(section='testServer', name='baseUrl')
        self.driver.getUrl(baseUrl + url)
        self.driver.hideWait(3)
        self.driver.maximizeWindow()
        self.driver.clearCookies()

