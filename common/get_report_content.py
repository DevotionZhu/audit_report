# coding:utf8
"""
Created on 2018年5月4日
@author: changl
"""

from config.config_reader import configReader
from common.connect_db import connectDB
from common.log import mylog, mylog_except
import os


class getReportContent():
    def __init__(self):
        # 连接报表数据库
        self.conndb = connectDB()
        self.conn = self.conndb.connect(self.conndb.dbname_auditcenter)
        self.cur = self.conndb.getCursor(self.conn)

        # 从配置文件中获取SQL配置项
        self.confR = configReader()

    # 获取数据库中报表的report_id及data_dimension_value（数据维度的值）
    def getProjectID(self, projectName):

        try:

            self.sql = self.confR.get("projectsql", "projectID")

            self.cur.execute(self.sql, (projectName,))
            projectID = self.cur.fetchone()

            if projectID:
                return projectID
            else:
                mylog("项目名称不存在")

        except Exception as error:
            mylog("SQL执行错误")
            mylog_except(error)

    # 获取报表存放ES数据的表名
    def getReportDataName(self, reportID):
        reportDataName = "report_{}_data".format(reportID)
        return reportDataName

    # 获取报表中所有指标的ID
    def getReportItem(self, reportID):
        self.sql = self.confR.get("reportsql", "reportItemid")
        self.cur.execute(self.sql, (reportID,))
        return self.cur.fetchall()

    # 获取数据库中所有指标的ID与对应的指标名称
    def getAllItems(self):
        self.sql = self.confR.get("reportsql", "allItems")
        self.cur.execute(self.sql)
        return dict(self.cur.fetchall())

    # 获取数据库报表中指标的值
    def getESvalue(self, reportDataName):

        try:
            self.sql = self.confR.get("reportsql", "esValue")
            self.cur.execute(self.sql.format(reportDataName))  # 参见获取报表存放ES数据的表名
            result = self.cur.fetchall()[-1]
            return result

        except Exception as error:
            print("未生成报表数据", error)
            mylog("SQL执行错误")
            mylog_except(error)

    # 获取报表的数据维度
    def getDataDimensionName(self, reportDataName):
        self.sql = self.confR.get("reportsql", "dimension_name")
        self.cur.execute(self.sql, (reportDataName,))
        return self.cur.fetchone()[0]

    # 获取报表的数据维度
    def getBusinessDimensionName(self, reportDataName):
        self.sql = self.confR.get("reportsql", "business_dimension")
        self.cur.execute(self.sql, (reportDataName,))
        return self.cur.fetchone()[0]

    # 获取机构，科室，医生，医疗组的信息
    def getHospitalInfor(self, reportDataName):
        self.sql = self.confR.get("reportsql", "hospital")
        self.cur.execute(self.sql.format(reportDataName))
        return self.cur.fetchall()[-1]

    # 根据docid获取医生的username
    def getDocName(self, docid):
        self.sql = self.confR.get("reportsql", "docname")
        self.cur.execute(self.sql, (docid,))
        return self.cur.fetchone()[0]

    # 根据deptid获取科室的code
    def getDeptName(self, deptid):
        self.sql = self.confR.get("reportsql", "deptid")
        self.cur.execute(self.sql, (deptid,))
        return self.cur.fetchone()[0]

    # 获取报表的时间范围
    def getReportTime(self, record_id, reportDataName):

        try:
            self.sql = self.confR.get("reportsql", "reportDate")
            self.cur.execute(self.sql.format(record_id, reportDataName))
            return self.cur.fetchone()

        except Exception as error:
            mylog("SQL执行错误")
            mylog_except(error)

    # 获取数据库里面所有报表的名称
    def getAllReportNames(self):

        self.sql = self.confR.get('reportsql', 'allReportNames')
        self.cur.execute(self.sql)
        allNames = self.cur.fetchall()

        newAllNames = []

        for name in allNames:
            newAllNames.append(name[0].encode('utf8'))
        return newAllNames

    # 获取手术名称对应的手术编码
    def getOperationCode(self, operationName):
        self.sql = self.confR.get('reportsql', 'operation_code')
        self.cur.execute(self.sql, (operationName,))
        self.operationCode = self.cur.fetchall()[0]
        self.operationCode_convert = self.operationCode[0].decode('utf8')
        self.operationCode_str = '|'.join(self.operationCode_convert.split(','))
        return self.operationCode_str


if __name__ == "__main__":
    pass
