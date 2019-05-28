#coding:utf-8
'''
@Created on 2018年5月12日
@author:changl
'''

import xlsxwriter
import os,datetime

curdate=datetime.datetime.now().strftime("%Y-%m-%d")
class getTestResult():

    def __init__(self,reportName):
        self.reportName=reportName
        self.date = curdate

    def createXlsx(self):
        self.xlsxname = './result/{}-{}.xlsx'.format(self.reportName,curdate)
        self.workbook = xlsxwriter.Workbook(self.xlsxname) #创建工作簿
        self.worksheet_workReportByOrg = self.workbook.add_worksheet('审方工作统计按机构统计') #创建工作表
        self.worksheet_workReportByOrg.set_column('A:A',50)#设置第一列宽度为50像素
        self.worksheet_workReportByOrg.set_column('B:D', 30)
    #添加固定的表头
    def writeColName(self):
        self.worksheet_workReportByOrg.write(0, 0,"统计名称")
        self.worksheet_workReportByOrg.write(0, 1, "页面展示值")
        self.worksheet_workReportByOrg.write(0, 2, "SQL统计值")
        self.worksheet_workReportByOrg.write(0, 3, "测试结果")


    def writeData(self,itemname,displayvalue,sqlvalue,result,count):
            self.worksheet_workReportByOrg.write(count,0,itemname)
            self.worksheet_workReportByOrg.write(count,1,displayvalue)
            self.worksheet_workReportByOrg.write(count,2,sqlvalue)
            self.worksheet_workReportByOrg.write(count,3,result)


    def closexlsx(self):
            self.workbook.close()

if __name__=="__main__":
    getTR=getTestResult('中文名称')
    getTR.createXlsx()
    getTR.writeColName()
    getTR.writeData("门诊患者就诊总人次","es","sql","pass",1)
    getTR.closexlsx()

