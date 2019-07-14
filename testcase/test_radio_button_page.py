# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 0003 8:38:11
# @Author  : zll
# @File    : test_radio_button_page.py
import unittest

from common.page_excel import ExcelPage
from common.page_object import ObjectPage
from testpage.radio_button_page import RadioButtonPage


class TestBaseRadioButtonPage(unittest.TestCase):

    def setUp(self):
        self.driver = ObjectPage()
        self.brp = RadioButtonPage(self.driver)
        self.brp.openBrowser()

    def tearDown(self):
        self.driver.quitBrowser()

    def test_radio_button_demo(self):
        datas = ExcelPage().read_excel(0, 2)
        for i in datas:
            result = self.brp.run_case_radio_button_demo(i['sex'])
            self.assertEqual(result, i['result'])
            self.driver.getImage("radio_button_demo_suc("+i['sex']+")")

    def test_group_radio_buttons_demo(self):
        datas = ExcelPage().read_excel(0, 3)
        for i in datas:
            result = self.brp.run_case_group_radio_buttons_demo(i['sex'], i['age'])
            self.assertEqual(result, i['result'])
            self.driver.getImage("group_radio_buttons_demo_suc("+i['sex']+"+"+i['age']+")")
