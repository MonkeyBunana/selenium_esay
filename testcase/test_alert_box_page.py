# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 0012 17:27:45
# @Author  : zll
# @File    : test_alert_box_page.py
import unittest

from common.page_object import ObjectPage
from testpage.alert_box_page import AlertBoxPage


class TestAlertBoxPage(unittest.TestCase):

    def setUp(self):
        self.driver = ObjectPage()
        self.abp = AlertBoxPage(self.driver)
        self.abp.openBrowser()

    def tearDown(self):
        self.driver.quitBrowser()

    def test_java_script_alert_box(self):
        result = self.abp.run_case_java_script_alert_box()
        self.assertEqual(result, "I am an alert box!")
        self.driver.getImage("script_alert_box_suc")

    def test_java_script_confirm_box(self):
        result = self.abp.run_case_java_script_confirm_box("ok")
        self.assertEqual(result, "You pressed OK!")
        self.driver.getImage("script_confirm_box_ok_suc")

        result = self.abp.run_case_java_script_confirm_box("no")
        self.assertEqual(result, "You pressed Cancel!")
        self.driver.getImage("script_confirm_box_no_suc")

    def test_java_script_alertinput_box(self):
        result = self.abp.run_case_java_script_alertinput_box()
        self.assertEqual(result, "You have entered 'hello selenium' !")
        self.driver.getImage("script_alertinput_box_suc")
