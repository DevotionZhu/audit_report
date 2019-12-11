# coding:utf-8
'''
@Created on 2019年5月28日
'''

import xlsxwriter
import os, datetime

curdate = datetime.datetime.now().strftime("%Y%m%d%H%M%S")


class getTestResult:
    # 获取创建excel标名所需参数
    def __init__(self, reportName):
        self.reportName = reportName
        self.date = curdate

    # 创建工作簿
    def createXlsx(self):
        self.xlsxname = './result/{}-{}.xlsx'.format(self.reportName, curdate)
        self.workbook = xlsxwriter.Workbook(self.xlsxname)

    # 创建工作表并添加固定表头
    def createSheet(self, worksheetname):
        self.worksheet = self.workbook.add_worksheet(worksheetname)
        self.worksheet.set_column('A:A', 50)  # 设置第一列宽度为50像素
        self.worksheet.set_column('B:D', 30)
        self.worksheet.write(0, 0, "统计名称")
        self.worksheet.write(0, 1, "页面展示值")
        self.worksheet.write(0, 2, "SQL统计值")
        self.worksheet.write(0, 3, "测试结果")

    # 写数据到worksheet里
    def writeData(self, itemname, displayvalue, sqlvalue, result, count):
        self.worksheet.write(count, 0, itemname)
        self.worksheet.write(count, 1, displayvalue)
        self.worksheet.write(count, 2, sqlvalue)
        self.worksheet.write(count, 3, result)

    def closexlsx(self):
        self.workbook.close()


if __name__ == "__main__":
    getTR = getTestResult('test')
    getTR.createXlsx()
    getTR.createSheet('按机构统计')
    getTR.writeData("机构患者就诊总人次", "es", "sql", "pass", 1)
    getTR.createSheet('按药师统计')
    getTR.writeData("药师患者就诊总人次", "es", "sql", "pass", 1)
    getTR.closexlsx()
