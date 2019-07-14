# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 0001 13:00:48
# @Author  : zll
# @File    : test_check_box_page.py
import unittest
from common.page_object import ObjectPage
from testpage.check_box_page import CheckBoxPage


class TestCheckBoxPage(unittest.TestCase):

    def setUp(self):
        self.driver = ObjectPage()
        self.cbp = CheckBoxPage(self.driver)
        self.cbp.openBrowser()

    def tearDown(self):
        self.driver.quitBrowser()

    def test_single_checkbox_demo(self):
        bool = self.cbp.run_case_single_checkbox_demo()
        self.assertTrue(bool)
        self.driver.getImage("single_checkbox_demo_suc")

    def test_multiple_checkbox_demo(self):
        checkboxes = self.cbp.run_case_multiple_checkbox_demo()
        for checkbox in checkboxes:
            self.assertTrue(checkbox.is_selected())
        self.driver.getImage("multiple_checkbox_demo_suc")
