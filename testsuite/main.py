# -*- coding:utf-8 -*-
# @Time   : 2019/6/01 0026 03:21
# @Author : zll
# @File   : main.py
from common import HTMLTestRunner
import unittest
import time

from common.page_email import EmailPage
from common.page_read import ReadConfig


def get_test_cases(dirpath):
    # dirpath是存放测试用例的文件路径
    test_cases = unittest.TestSuite()
    # 测试用例均使用"test_"开头命名
    suites = unittest.defaultTestLoader.discover(dirpath, 'test_*.py', top_level_dir=dirpath)
    for suite in suites:
        test_cases.addTests(suite)
    return test_cases


if __name__ == '__main__':
    casePath = ReadConfig().getValue(section='located', name='testcase')
    cases = get_test_cases(casePath)
    now = time.strftime("%Y-%m-%d %H_%M_%S")  # 报告生成时间
    reportPath = ReadConfig().getValue(section='located', name='report')
    test_reports_address = reportPath      # 测试报告存放位置
    filename = reportPath + now + 'report.html'  # 设置报告文件名
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'Web自动化测试', description=u'详细测试结果如下:')
    runner.run(cases)
    fp.close()

    # 查找最新生成的测试报告地址
    new_report_addr = EmailPage().acquire_report_address(test_reports_address)
    # 自动发送邮件
    EmailPage().send_email(new_report_addr)