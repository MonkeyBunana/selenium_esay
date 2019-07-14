# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 0011 4:00:15
# @Author  : zll
# @File    : test_select_dropdown_page.py
import random
import unittest

from common.page_excel import ExcelPage
from common.page_object import ObjectPage
from testpage.select_dropdown_page import SelectDropdown


class TestSelectDropdownPage(unittest.TestCase):

    def setUp(self):
        self.driver = ObjectPage()
        self.sd = SelectDropdown(self.driver)
        self.sd.openBrowser()

    def tearDown(self):
        self.driver.closeBrowser()

    def test_select_list_demo(self):
        datas = ExcelPage().read_excel(0, 4)
        for i in datas:
            select = self.sd.run_case_select_list_demo(i['select'])
            self.assertEqual(select, i['result'])
            self.driver.getImage("select_list_demo_suc("+i['select']+")")

    def test_multi_select_list_demo(self):
        datas = ExcelPage().read_excel(0, 5)
        for i in datas:
            select = self.sd.run_case_multi_select_list_demo("single", i['select'])
            self.assertEqual(select, i["result"])
            self.driver.getImage("multi_select_list_demo_suc(" + i['select'] + ")")

        # datas = ExcelPage().read_excel(0, 5)
        # value = []
        # for i in datas:
        #     value.append(i['select'])
        # b = random.sample(value, 3)
        # selects = self.sd.run_case_multi_select_list_demo("many", b)
        # self.assertEqual(selects, "Options selected are : "+','.join(b))
