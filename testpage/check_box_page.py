# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 0001 9:31:02
# @Author  : zll
# @File    : check_box_page.py
import time

from common.page_base import BasePage


class CheckBoxPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.url = "/basic-checkbox-demo.html"

    def openBrowser(self):
        self.open(self.url)

    def run_case_single_checkbox_demo(self):
        ageSelected = self.driver.findElement("id", "isAgeSelected")
        self.driver.click(ageSelected)
        return self.driver.isSelect(ageSelected)

    def run_case_multiple_checkbox_demo(self):
        checkboxes = self.driver.findElements("css", "input[type=checkbox]")
        for checkbox in checkboxes:
            checkbox.click()
            time.sleep(1)
        return checkboxes
