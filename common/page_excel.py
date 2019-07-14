# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 0003 2:22:01
# @Author  : zll
# @File    : page_excel.py
import xlrd

from common.page_log import log1
from common.page_read import ReadConfig


class ExcelPage(object):

    @staticmethod
    def open_excel():
        try:
            excelPath = ReadConfig().getValue(section='located', name='excel')
            log1.info("Open Excel")
            return xlrd.open_workbook(excelPath)
        except BaseException:
            log1.error("Open Excel Error", exc_info=1)
            raise IOError("Open Excel Error")

    def read_excel(self, colindex=0, by_index=0):
        data = self.open_excel()
        tab = data.sheets()[by_index]  # 选择excel里面的Sheet
        nrows = tab.nrows  # 行数
        ncols = tab.ncols  # 列数
        colName = tab.row_values(colindex)  # 第0行的值
        list = []  # 创建一个空列表
        for x in range(1, nrows):  # 第一行为标题（第一行为0），所以从第二行开始
            row = tab.row_values(x)
            if row:
                app = {}  # 创建空字典
                for y in range(0, ncols):
                    app[colName[y]] = row[y]
                list.append(app)
        return list


if __name__ == '__main__':
    list = ExcelPage().read_excel(0, 1)
    print(list)
    for i in list:
        print(i)
        print(i['sum'])
