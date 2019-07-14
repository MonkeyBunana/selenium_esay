# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 0001 4:00:21
# @Author  : zll
# @File    : test_simple_form_page.py
import unittest

from common.page_excel import ExcelPage
from common.page_object import ObjectPage
from testpage.simple_form_page import SimpleFormPage


class TestSimpleFromPage(unittest.TestCase):

    def setUp(self):
        self.driver = ObjectPage()
        self.sfp = SimpleFormPage(self.driver)
        self.sfp.openBrowser()

    def tearDown(self):
        self.driver.quitBrowser()

    def test_single_input_field(self):
        datas = ExcelPage().read_excel(0, 0)
        for i in datas:
            value = self.sfp.run_case_single_input_field(i['input'])
            self.assertEqual(value, i['output'])
            self.driver.getImage("single_input_field_suc("+i['input']+")")

    def test_two_input_fields(self):
        datas = ExcelPage().read_excel(0, 1)
        print(datas)
        for i in datas:
            value = self.sfp.run_case_two_input_fields(int(i['num1']), int(i['num2']))
            self.assertEqual(value, int(i['sum']))
            self.driver.getImage("two_input_fields_suc("+str(i['num1'])+"+"+str(i['num2'])+"+"+str(i['sum'])+")")
