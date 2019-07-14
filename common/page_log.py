# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 0001 21:23:24
# @Author  : zll
# @File    : page_log.py
import logging
import os

from common.page_read import ReadConfig


def LogPage(logger_name):

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # 设置所有日志和错误日志的存放路径
    path = os.getcwd()
    # 通过getcwd.py文件的绝对路径来拼接日志存放路径
    logPath = ReadConfig().getValue(section='located', name='log')
    all_log_path = os.path.join(path, logPath)
    # 设置日志文件名
    all_log_name = all_log_path + logger_name + '.log'

    # 创建一个handler写入所有日志
    fh = logging.FileHandler(all_log_name)
    fh.setLevel(logging.INFO)
    # 创建一个handler写入错误日志
    eh = logging.FileHandler(all_log_name)
    eh.setLevel(logging.ERROR)
    # 创建一个handler输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # 定义日志输出格式
    # 以时间-日志器名称-日志级别-日志内容的形式展示
    all_log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 以时间-日志器名称-日志级别-文件名-函数行号-错误内容
    error_log_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(module)s  - %(lineno)s - %(message)s')
    # 将定义好的输出形式添加到handler
    fh.setFormatter(all_log_formatter)
    ch.setFormatter(all_log_formatter)
    eh.setFormatter(error_log_formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(eh)
    logger.addHandler(ch)
    return logger


log1 = LogPage("selenium")
