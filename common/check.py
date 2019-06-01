from config.config_reader import configReader
from common.save_test_result import getTestResult
from common.get_sql_value import getSqlValue
from common.get_display_value import getDisplayValue


class check():
    def __init__(self):
        self.fields = ['workReportByOrg_ipt_zoneId', 'workReportByOrg_ipt_deptId']
        # 从配置文件中获取sql配置项
        self.confR = configReader()
        # 获取报表页面显示值的类
        self.getdisplay = getDisplayValue()
        # 获取sql值的类
        self.getsqlvalue = getSqlValue()
        # 从配置文件中获取sql中所需变量：zoneid、deptid、startT、endT和页面展示所需变量：startT、endT
        self.zoneid = self.confR.getint("constant", "zoneid")
        self.deptid = self.confR.get("constant", "deptid")
        self.audit_doctor_id = self.confR.get("constant", "audit_doctor_id")
        self.startT = self.confR.get("constant", "startT")
        self.endT = self.confR.get("constant", "endT")
        self.sql_dimension = {"workReportByOrg_ipt_zoneId": "zone", "workReportByOrg_ipt_deptId": "dept"}
        self.dis_dimension = {"workReportByOrg_ipt_zoneId": "dis_zone",
                              "workReportByOrg_ipt_deptId": "dis_dept"
                              }

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

    def phar(self, field, itemname):
        return self.getsqlvalue.getValue_phar(field, itemname, self.audit_doctor_id, self.startT, self.endT)

    def dis_zone(self, field):
        return self.getdisplay.getvalue_zoneId(field)

    def dis_dept(self, field):
        return self.getdisplay.getvalue_deptId(field)

    def dis_phar(self, field):
        return self.getdisplay.getvalue_auditDoctorId(field)

    # 获取报表页面display值
    def getDisValue(self, itemKey, field):

        name = 'self.{}'.format(self.dis_dimension[field])
        functionName = eval(name)
        self.disvalue = functionName(field)
        s = self.confR.getitems_new(field)
        t = self.confR.get(field, 'ratio').split(",")
        if self.disvalue == "Nodata":
            disvalue_new = 0
        else:
            # 局部变量需要先定义再赋值
            disvalue_new = ''
            if itemKey not in s + t:
                disvalue_new = "Nodata"

            elif itemKey in s + t:
                disvalue_new = self.disvalue[itemKey]
        return disvalue_new

    # 获取报表sql统计值
    def getItemsSql(self, itemname, field):

        name = 'self.{}'.format(self.sql_dimension[field])
        functionName = eval(name)
        self.sqlvalue = functionName(field, itemname)
        if self.sqlvalue == None:  # 当SQL查询结果为None时
            self.sqlvalue_new = "The SQL's result is None"

        else:
            self.sqlvalue_new = self.sqlvalue

        return self.sqlvalue_new

    # 执行报表中统计的验证并输出测试结果
    def executeCheck(self):
        # 保存测试结果
        self.saveTR = getTestResult('统计报表')
        # 创建excel文件
        self.saveTR.createXlsx()
        # 需要创建len(self.fields)个worksheet
        for i in range(len(self.fields)):
            # 创建第i个worksheet
            self.saveTR.createSheet(self.fields[i])
            count = 1
            # for itemkey in self.confR.getitems_new(self.fields[i]):
            items = self.confR.getitems_new(self.fields[i])
            for j in range(len(items) - 4):
                self.disvalue_f = self.getDisValue(items[j], self.fields[i])
                self.sqlvalue_f = self.getItemsSql(items[j], self.fields[i])
                self.itemname = items[j]
                self.rlt = self.isEqual(self.disvalue_f, self.sqlvalue_f)
                self.saveTR.writeData(self.itemname, self.disvalue_f, self.sqlvalue_f, self.rlt, count)
                count += 1
            for ratio in self.confR.get(self.fields[i], 'ratio').split(","):
                if ratio == 'autoPassCountRatio':
                    self.disvalue_f = self.getDisValue(ratio, self.fields[i])
                    self.sqlvalue_f = self.getItemsSql('autoPassCount', self.fields[i]) / self.getItemsSql('disCount',
                                                                                                           self.fields[
                                                                                                               i])
                    self.rlt = self.isEqual(self.disvalue_f, self.sqlvalue_f)
                    self.saveTR.writeData('autoPassCountRatio', self.disvalue_f, self.sqlvalue_f, self.rlt, count)
                    count += 1
                elif ratio == 'timeoutPassCountRatio':
                    self.disvalue_f = self.getDisValue(ratio, self.fields[i])
                    self.sqlvalue_f = self.getItemsSql('timeoutPassCount', self.fields[i]) / self.getItemsSql(
                        'disCount', self.fields[i])
                    self.rlt = self.isEqual(self.disvalue_f, self.sqlvalue_f)
                    self.saveTR.writeData('timeoutPassCountRatio', self.disvalue_f, self.sqlvalue_f, self.rlt, count)
                    count += 1
        self.saveTR.closexlsx()


if __name__ == '__main__':
    c = check()
