# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 0011 3:31:33
# @Author  : zll
# @File    : select_dropdown_page.py
from common.page_base import BasePage


class SelectDropdown(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.url = "/basic-select-dropdown-demo.html"

    def openBrowser(self):
        self.open(self.url)

    def run_case_select_list_demo(self, text):
        select = self.driver.findElement("id", "select-demo")
        self.driver.select("text", select, text)
        selected = self.driver.findElement("class", "selected-value")
        return self.driver.getText(selected)

    def run_case_multi_select_list_demo(self, type, value=""):
        if type == "single" and value != "":
            select = self.driver.findElement("id", "multi-select")
            self.driver.deselect("all", select)
            self.driver.select("value", select, value)
            printMe = self.driver.findElement("id", "printMe")
            self.driver.click(printMe)
            selected = self.driver.findElement("class", "getall-selected")
            return self.driver.getText(selected)
        elif type == "many":
            select = self.driver.findElement("id", "multi-select")
            '''
                长按Ctrl键不生效，暂时不知道怎么解决
            '''
            self.driver.actionsKeyDown()
            for i in value:
                self.driver.select("value", select, i)
            self.driver.actionsKeyUp()
            printAll = self.driver.findElement("id", "printAll")
            self.driver.click(printAll)
            selected = self.driver.findElement("class", "getall-selected")
            return self.driver.getText(selected)


