# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 0001 21:04:10
# @Author  : zll
# @File    : page_email.py
"""
使用一个邮箱向另一个邮箱发送测试报告的html文件，这里需要对发送邮件的邮箱进行设置，获取邮箱授权码。
username=“发送邮件的邮箱”， password=“邮箱授权码”
这里要特别注意password不是邮箱密码而是邮箱授权码。
mail_server = "发送邮箱的服务器地址"
这里常用的有 qq邮箱——"stmp.qq.com", 163邮箱——"stmp.163.com"
其他邮箱服务器地址可自行百度
"""
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
from common.page_log import log1
from common.page_read import ReadConfig


class EmailPage(object):

    @staticmethod
    def send_email(new_report):
        # 读取测试报告中的内容作为邮件的内容
        with open(new_report, 'r', encoding='utf8') as f:
            mail_body = f.read()

        log1.info("-------------------- Found Send Email Content --------------------")
        addrPath = ReadConfig().getValue(section='email', name='username')
        serverPath = ReadConfig().getValue(section='email', name='server')
        passwordPath = ReadConfig().getValue(section='email', name='password')
        send_addr = addrPath
        reciver_addr = addrPath
        mail_server = serverPath
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        # 邮件标题
        subject = 'web自动化测试报告测试报告' + now
        username = addrPath
        password = passwordPath
        # 邮箱的内容和标题
        message = MIMEText(mail_body, 'html', 'utf8')
        message['Subject'] = Header(subject, charset='utf8')
        log1.info("-------------------- Get Send Email Content --------------------")
        # 发送邮件，使用的使smtp协议
        smtp = smtplib.SMTP()
        smtp.connect(mail_server)
        smtp.login(username, password)
        smtp.sendmail(send_addr, reciver_addr.split(','), message.as_string())
        smtp.quit()
        log1.info("-------------------- Send Email End --------------------")

    # 获取最新的测试报告地址
    @staticmethod
    def acquire_report_address(reports_address):
        log1.info("-------------------- Send Email Start --------------------")
        log1.info("-------------------- Found New Report --------------------")
        # 测试报告文件夹中的所有文件加入到列表
        test_reports_list = os.listdir(reports_address)
        # 按照升序排序生成新的列表
        new_test_reports_list = sorted(test_reports_list)
        # 获取最新的测试报告
        the_last_report = new_test_reports_list[-1]
        # 最新的测试报告地址
        the_last_report_address = os.path.join(reports_address, the_last_report)
        log1.info("-------------------- Get New Report --------------------")
        return the_last_report_address
