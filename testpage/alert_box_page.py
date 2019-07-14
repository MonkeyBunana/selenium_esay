# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 0012 17:14:22
# @Author  : zll
# @File    : alert_box_page.py
from common.page_base import BasePage


class AlertBoxPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.url = "/javascript-alert-box-demo.html"

    def openBrowser(self):
        self.open(self.url)

    def run_case_java_script_alert_box(self):
        button = self.driver.findElement("xpath", "//*[@id='easycont']/div/div[2]/div[1]/div[2]/button")
        self.driver.click(button)
        return self.driver.textAlert()

    def run_case_java_script_confirm_box(self, type):
        button = self.driver.findElement("xpath", "//*[@id='easycont']/div/div[2]/div[2]/div[2]/button")
        self.driver.click(button)
        if type == "ok":
            self.driver.acceptAlert()
        elif type == "no":
            self.driver.dismissAlert()
        confirm = self.driver.findElement("id", "confirm-demo")
        return self.driver.getText(confirm)

    def run_case_java_script_alertinput_box(self):
        button = self.driver.findElement("xpath", "//*[@id='easycont']/div/div[2]/div[3]/div[2]/button")
        self.driver.click(button)
        self.driver.sendKeysAlert("hello selenium")
        t = self.driver.findElement("id", "prompt-demo")
        return self.driver.getText(t)
