# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 0001 3:35:09
# @Author  : zll
# @File    : simple_form_page.py
from common.page_base import BasePage


class SimpleFormPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.url = "/basic-first-form-demo.html"

    def openBrowser(self):
        self.open(self.url)

    def run_case_single_input_field(self, text):
        userMessage = self.driver.findElement("id", "user-message")
        self.driver.sendKeys(userMessage, text)
        button = self.driver.findElement("xpath", "//*[@id='get-input']/button")
        self.driver.click(button)
        display = self.driver.findElement("id", "display")
        return self.driver.getText(display)

    def run_case_two_input_fields(self, sum1, sum2):
        # 网站代码好像改了，之后再说 :)
        inputSum1 = self.driver.findElement("id", "sum1")
        self.driver.sendKeys(inputSum1, sum1)
        inputSum2 = self.driver.findElement("id", "sum2")
        self.driver.sendKeys(inputSum2, sum2)
        button = self.driver.findElement("xpath", "//*[@id='gettotal']/button")
        self.driver.click(button)
        displayvalue = self.driver.findElement("id", "displayvalue")
        return int(self.driver.getText(displayvalue))

