# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 0003 8:29:59
# @Author  : zll
# @File    : radio_button_page.py
from common.page_base import BasePage
from common.page_log import log1


class RadioButtonPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.url = "/basic-radiobutton-demo.html"

    def openBrowser(self):
        self.open(self.url)

    def run_case_radio_button_demo(self, sex):
        optradio = self.driver.findElements("name", "optradio")
        try:
            for i in optradio:
                if self.driver.getAttribute(i, "value") == sex:
                    self.driver.click(i)
            button = self.driver.findElement("id", "buttoncheck")
            self.driver.click(button)
        except BaseException:
            log1.error("Not Found Element", exc_info=1)
        radiobutton = self.driver.findElement("class", "radiobutton")
        return self.driver.getText(radiobutton)

    def run_case_group_radio_buttons_demo(self, sex, age):
        gender = self.driver.findElements("name", "gender")
        ageGroup = self.driver.findElements("name", "ageGroup")
        try:
            for i in gender:
                if self.driver.getAttribute(i, "value") == sex:
                    self.driver.click(i)
            for j in ageGroup:
                if self.driver.getAttribute(j, "value") == age:
                    self.driver.click(j)
            button = self.driver.findElement("xpath", "//*[@id='easycont']/div/div[2]/div[2]/div[2]/button")
            self.driver.click(button)
        except BaseException:
            log1.error("Not Found Element", exc_info=1)
        groupradiobutton = self.driver.findElement("class", "groupradiobutton")
        return self.driver.getText(groupradiobutton)
