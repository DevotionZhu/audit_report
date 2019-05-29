from common.config_reader import configReader
from common.save_test_result import getTestResult
from common.get_sql_value import getSqlValue
from common.get_display_value import getDisplayValue
import json, os

path = os.path.abspath('./config/index.ini')


class check():
    def __init__(self):
        self.fields = ['workReportByOrg_ipt_zoneId', 'workReportByOrg_ipt_deptId']
        # 从配置文件中获取sql配置项
        self.confR = configReader(path)
        # self.itemnames_ipt_zoneId = self.confR.getitems_new('workReportByOrg_ipt_zoneId')
        # print(self.itemnames_ipt_zoneId)
        # 获取报表页面显示值的类
        self.getdisplay = getDisplayValue()
        # 获取sql值的类
        self.getsqlvalue = getSqlValue()
        # 从配置文件中获取sql中所需变量：zoneid、deptid、startT、endT和页面展示所需变量：startT、endT
        self.zoneid = self.confR.getint("constant", "zoneid")
        self.deptid = self.confR.get("constant", "deptid")
        self.startT = self.confR.get("constant", "startT")
        self.endT = self.confR.get("constant", "endT")
        self.sql_dimension = {"workReportByOrg_ipt_zoneId": "zone", "workReportByOrg_ipt_deptId": "dept"}
        self.dis_dimension = {"workReportByOrg_ipt_zoneId": "dis_workReportByOrg_ipt_zoneId",
                              "workReportByOrg_ipt_deptId": "dis_workReportByOrg_ipt_deptId"}

    # 判断页面展示值与sql值是否相等
    def isEqual(self, displayvalue, sqlvalue):
        if displayvalue == sqlvalue:
            return "pass"
        else:
            return "fail"

    def zone(self, field, itemname):
        return self.getsqlvalue.getValue_zoneId(field, itemname, self.zoneid, self.startT, self.endT)

    def dept(self, field, itemname):
        return self.getsqlvalue.getValue_deptId(field, itemname, self.zoneid, self.deptid, self.startT, self.endT)

    def dis_workReportByOrg_ipt_zoneId(self):
        return self.getdisplay.getvalue_zoneId("审方工作统计按机构统计", "zoneId", "住院")

    def dis_workReportByOrg_ipt_deptId(self):
        return self.getdisplay.getvalue_deptId("审方工作统计按机构统计", "deptId", "住院")

    # 获取报表页面display值
    def getDisValue(self, itemKey, field):

        name = 'self.{}'.format(self.dis_dimension[field])
        functionName = eval(name)
        self.disvalue = functionName()
        if self.disvalue == "Nodata":
            disvalue_new = 0
        else:
        # 局部变量需要先定义再赋值
            disvalue_new = ''
            if itemKey not in self.confR.getitems_new(field):
                disvalue_new = "Nodata"

            elif itemKey in self.confR.getitems_new(field):
                disvalue_new = self.disvalue[itemKey]
        return disvalue_new

    # 获取报表sql统计值
    def getItemsSql(self, itemname, field):

        name = 'self.{}'.format(self.sql_dimension[field])
        functionName = eval(name)
        self.sqlvalue = functionName(field,itemname)
        if self.sqlvalue == None:  # 当SQL查询结果为None时
            self.sqlvalue_new = "The SQL's result is None"

        else:
            self.sqlvalue_new = self.sqlvalue

        return self.sqlvalue_new

    # 执行报表中统计的验证并输出测试结果
    def executeCheck(self):
        # 保存测试结果
        self.saveTR = getTestResult('审方工作统计')
        # 创建excel文件
        self.saveTR.createXlsx()
        for i in range(len(self.fields)):
            # 创建第一个worksheet
            self.saveTR.createSheet(self.fields[i])
            count = 1
            for itemkey in self.confR.getitems_new(self.fields[i]):
                self.disvalue_f = self.getDisValue(itemkey, self.fields[i])
                self.sqlvalue_f = self.getItemsSql(itemkey, self.fields[i])
                self.itemname = itemkey
                self.rlt = self.isEqual(self.disvalue_f, self.sqlvalue_f)
                self.saveTR.writeData(self.itemname, self.disvalue_f, self.sqlvalue_f, self.rlt, count)
                count += 1
        self.saveTR.closexlsx()


if __name__ == '__main__':
    c = check()
