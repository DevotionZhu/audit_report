from config.config_reader import configReader
from common.save_test_result import getTestResult
from common.get_sql_value import getSqlValue
from common.get_display_value import getDisplayValue


class check():
    def __init__(self):
        self.fields = ['workReportByOrg_ipt_zoneId',
                       'workReportByOrg_ipt_deptId',
                       'workReportByOrg_ipt_kfDocId',
                       'workReportByOrg_ipt_inWardId',
                       'workReportByOrg_opt_zoneId',
                       'workReportByOrg_opt_deptId',
                       'workReportByOrg_opt_kfDocId',
                       'workReportByPhar_ipt',
                       'workReportByPhar_opt',
                       'docDealReportByOrg_ipt_zoneId',
                       'docDealReportByOrg_ipt_deptId',
                       'docDealReportByOrg_ipt_kfDocId',
                       'docDealReportByOrg_ipt_inWardId',
                       'docDealReportByOrg_opt_zoneId',
                       'docDealReportByOrg_opt_deptId',
                       'docDealReportByOrg_opt_kfDocId',
                       'docDealReportByPhar_ipt',
                       'docDealReportByPhar_opt',
                       'issueReportByType_ipt',
                       'issueReportByType_opt']
        # 从配置文件中获取sql配置项
        self.confR = configReader()
        # 获取报表页面显示值的类
        self.getdisplay = getDisplayValue()
        # 获取sql值的类
        self.getsqlvalue = getSqlValue()
        # 从配置文件中获取sql中所需变量：zoneid、deptid、startT、endT和页面展示所需变量：startT、endT
        self.zoneid = self.confR.get("constant", "zoneid")
        self.zydeptid = self.confR.get("constant", "zydeptid")
        self.mdeptid = self.confR.get("constant", "mzdeptid")
        self.mzdeptid = self.zoneid + '_' + self.mdeptid
        self.kf_doc_id = self.confR.get('constant', 'kf_doc_id')
        self.in_ward_id = self.confR.get('constant', 'in_ward_id')
        self.audit_doctor_id = self.confR.get("constant", "audit_doctor_id")
        self.analysis_type = self.confR.get("constant", "analysis_type")
        self.analysis_result_type = self.confR.get("constant", "analysis_result_type")
        self.startT = self.confR.get("constant", "startT")
        self.endT = self.confR.get("constant", "endT")
        self.sql_dimension = {"workReportByOrg_ipt_zoneId": "zone",
                              "workReportByOrg_ipt_deptId": "zydept",
                              "workReportByOrg_ipt_kfDocId": "kfdoc",
                              "workReportByOrg_ipt_inWardId": "ward",
                              "workReportByOrg_opt_zoneId": "zone",
                              "workReportByOrg_opt_deptId": "mzdept",
                              "workReportByOrg_opt_kfDocId": "kfdoc",
                              "workReportByPhar_ipt": "phar",
                              "workReportByPhar_opt": "phar",
                              "docDealReportByOrg_ipt_zoneId":"zone",
                              "docDealReportByOrg_ipt_deptId":"zydept",
                              "docDealReportByOrg_ipt_kfDocId":"kfdoc",
                              "docDealReportByOrg_ipt_inWardId":"ward",
                              "docDealReportByOrg_opt_zoneId":"zone",
                              "docDealReportByOrg_opt_deptId":"mzdept",
                              "docDealReportByOrg_opt_kfDocId":"kfdoc",
                              "docDealReportByPhar_ipt":"phar",
                              "docDealReportByPhar_opt":"phar",
                              "issueReportByType_ipt":"issue",
                              "issueReportByType_opt": "issue"
                              }
        self.dis_dimension = {"workReportByOrg_ipt_zoneId": "dis_zone",
                              "workReportByOrg_ipt_deptId": "dis_dept",
                              "workReportByOrg_ipt_kfDocId": "dis_kfdoc",
                              "workReportByOrg_ipt_inWardId": "dis_ward",
                              "workReportByOrg_opt_zoneId": "dis_zone",
                              "workReportByOrg_opt_deptId": "dis_dept",
                              "workReportByOrg_opt_kfDocId": "dis_kfdoc",
                              "workReportByPhar_ipt": "dis_phar",
                              "workReportByPhar_opt": "dis_phar",
                              "docDealReportByOrg_ipt_zoneId": "dis_zone",
                              "docDealReportByOrg_ipt_deptId":"dis_dept",
                              "docDealReportByOrg_ipt_kfDocId": "dis_kfdoc",
                              "docDealReportByOrg_ipt_inWardId": "dis_ward",
                              "docDealReportByOrg_opt_zoneId": "dis_zone",
                              "docDealReportByOrg_opt_deptId": "dis_dept",
                              "docDealReportByOrg_opt_kfDocId": "dis_kfdoc",
                              "docDealReportByPhar_ipt": "dis_phar",
                              "docDealReportByPhar_opt": "dis_phar",
                              "issueReportByType_ipt": "dis_issue",
                              "issueReportByType_opt": "dis_issue"
                              }

    # 判断页面展示值与sql值是否相等
    def isEqual(self, displayvalue, sqlvalue):
        if displayvalue == sqlvalue:
            return "pass"
        else:
            return "fail"

    def zone(self, field, itemname):
        return self.getsqlvalue.getValue_zoneId(field, itemname, self.zoneid, self.startT, self.endT)

    def zydept(self, field, itemname):
        return self.getsqlvalue.getValue_zydeptId(field, itemname, self.zoneid, self.zydeptid, self.startT, self.endT)

    def mzdept(self, field, itemname):
        return self.getsqlvalue.getValue_mzdeptId(field, itemname, self.zoneid, self.mzdeptid, self.startT, self.endT)

    def kfdoc(self, field, itemname):
        return self.getsqlvalue.getValue_kfDocId(field, itemname, self.zoneid, self.kf_doc_id, self.startT, self.endT)

    def ward(self, field, itemname):
        return self.getsqlvalue.getValue_inWardId(field, itemname, self.zoneid, self.in_ward_id, self.startT, self.endT)

    def phar(self, field, itemname):
        return self.getsqlvalue.getValue_phar(field, itemname, self.audit_doctor_id, self.startT, self.endT)

    def issue(self, field, itemname):
        return self.getsqlvalue.getValue_issue(field, itemname, self.analysis_result_type, self.startT, self.endT)

    def dis_zone(self, field):
        return self.getdisplay.getvalue_zoneId(field)

    def dis_dept(self, field):
        return self.getdisplay.getvalue_deptId(field)

    def dis_kfdoc(self, field):
        return self.getdisplay.getvalue_kfDocId(field)

    def dis_ward(self, field):
        return self.getdisplay.getvalue_inWardId(field)

    def dis_phar(self, field):
        return self.getdisplay.getvalue_auditDoctorId(field)

    def dis_issue(self, field):
        return self.getdisplay.getvalue_issue(field)

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
            print("The SQL's result is None")
            self.sqlvalue_new = 0

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
                    if self.getItemsSql('disCount', self.fields[i]) == 0:
                        self.sqlvalue_f = 0
                    else:
                        self.sqlvalue_f = self.getItemsSql('autoPassCount', self.fields[i]) / self.getItemsSql(
                            'disCount',
                            self.fields[
                                i])
                    self.rlt = self.isEqual(self.disvalue_f, self.sqlvalue_f)
                    self.saveTR.writeData('autoPassCountRatio', self.disvalue_f, self.sqlvalue_f, self.rlt, count)
                    count += 1
                elif ratio == 'timeoutPassCountRatio':
                    self.disvalue_f = self.getDisValue(ratio, self.fields[i])
                    if self.getItemsSql('disCount', self.fields[i]) == 0:
                        self.sqlvalue_f = 0
                    else:
                        self.sqlvalue_f = self.getItemsSql('timeoutPassCount', self.fields[i]) / self.getItemsSql(
                            'disCount', self.fields[i])
                    self.rlt = self.isEqual(self.disvalue_f, self.sqlvalue_f)
                    self.saveTR.writeData('timeoutPassCountRatio', self.disvalue_f, self.sqlvalue_f, self.rlt, count)
                    count += 1
                elif ratio == 'disAuditCountRatio':
                    self.disvalue_f = self.getDisValue(ratio, self.fields[i])
                    if self.getItemsSql('disCount', self.fields[i]) == 0:
                        self.sqlvalue_f = 0
                    else:
                        self.sqlvalue_f = self.getItemsSql('disAuditCount', self.fields[i]) / self.getItemsSql(
                            'disCount', self.fields[i])
                    self.rlt = self.isEqual(self.disvalue_f, self.sqlvalue_f)
                    self.saveTR.writeData('disAuditCountRatio', self.disvalue_f, self.sqlvalue_f, self.rlt, count)
                    count += 1
                elif ratio == 'disAuditPassCountRatio':
                    self.disvalue_f = self.getDisValue(ratio, self.fields[i])
                    if self.getItemsSql('disAuditCount', self.fields[i]) == 0:
                        self.sqlvalue_f = 0
                    else:
                        self.sqlvalue_f = self.getItemsSql('disAuditPassCount', self.fields[i]) / self.getItemsSql(
                            'disAuditCount', self.fields[i])
                    self.rlt = self.isEqual(self.disvalue_f, self.sqlvalue_f)
                    self.saveTR.writeData('disAuditPassCountRatio', self.disvalue_f, self.sqlvalue_f, self.rlt, count)
                    count += 1
                elif ratio == 'disAuditRejecCountRatio':
                    self.disvalue_f = self.getDisValue(ratio, self.fields[i])
                    if self.getItemsSql('disAuditCount', self.fields[i]) == 0:
                        self.sqlvalue_f = 0
                    else:
                        self.sqlvalue_f = self.getItemsSql('disAuditRejecCount', self.fields[i]) / self.getItemsSql(
                            'disAuditCount', self.fields[i])
                    self.rlt = self.isEqual(self.disvalue_f, self.sqlvalue_f)
                    self.saveTR.writeData('disAuditRejecCountRatio', self.disvalue_f, self.sqlvalue_f, self.rlt, count)
                    count += 1
                elif ratio == 'auditPassCountRatio':
                    self.disvalue_f = self.getDisValue(ratio, self.fields[i])
                    if self.getItemsSql('auditCount', self.fields[i]) == 0:
                        self.sqlvalue_f = 0
                    else:
                        self.sqlvalue_f = self.getItemsSql('auditPassCount', self.fields[i]) / self.getItemsSql(
                            'auditCount', self.fields[i])

                    self.rlt = self.isEqual(self.disvalue_f, self.sqlvalue_f)
                    self.saveTR.writeData('auditPassCountRatio', self.disvalue_f, self.sqlvalue_f, self.rlt, count)
                    count += 1
                elif ratio == 'auditRejectCountRatio':
                    self.disvalue_f = self.getDisValue(ratio, self.fields[i])
                    if self.getItemsSql('auditCount', self.fields[i]) == 0:
                        self.sqlvalue_f = 0
                    else:
                        self.sqlvalue_f = self.getItemsSql('auditRejectCount', self.fields[i]) / self.getItemsSql(
                            'auditCount', self.fields[i])
                    self.rlt = self.isEqual(self.disvalue_f, self.sqlvalue_f)
                    self.saveTR.writeData('auditRejectCountRatio', self.disvalue_f, self.sqlvalue_f, self.rlt, count)
                    count += 1
                elif ratio == 'rejectSignCountRatio':
                    self.disvalue_f = self.getDisValue(ratio, self.fields[i])
                    if self.getItemsSql('rejectCount', self.fields[i]) == 0:
                        self.sqlvalue_f = 0
                    else:
                        self.sqlvalue_f = self.getItemsSql('rejectSignCount', self.fields[i]) / self.getItemsSql(
                            'rejectCount', self.fields[i])
                    self.rlt = self.isEqual(self.disvalue_f, self.sqlvalue_f)
                    self.saveTR.writeData('rejectSignCountRatio', self.disvalue_f, self.sqlvalue_f, self.rlt, count)
                    count += 1
                elif ratio == 'rejectAlterCountRatio':
                    self.disvalue_f = self.getDisValue(ratio, self.fields[i])
                    if self.getItemsSql('rejectCount', self.fields[i]) == 0:
                        self.sqlvalue_f = 0
                    else:
                        self.sqlvalue_f = self.getItemsSql('rejectAlterCount', self.fields[i]) / self.getItemsSql(
                            'rejectCount', self.fields[i])
                    self.rlt = self.isEqual(self.disvalue_f, self.sqlvalue_f)
                    self.saveTR.writeData('rejectAlterCountRatio', self.disvalue_f, self.sqlvalue_f, self.rlt, count)
                    count += 1
                elif ratio == 'docDealCountRatio':
                    self.disvalue_f = self.getDisValue(ratio, self.fields[i])
                    if self.getItemsSql('rejectCount', self.fields[i]) == 0:
                        self.sqlvalue_f = 0
                    else:
                        self.sqlvalue_f = self.getItemsSql('docDealCount', self.fields[i]) / self.getItemsSql(
                            'rejectCount', self.fields[i])
                    self.rlt = self.isEqual(self.disvalue_f, self.sqlvalue_f)
                    self.saveTR.writeData('docDealCountRatio', self.disvalue_f, self.sqlvalue_f, self.rlt, count)
                    count += 1
                elif ratio == 'docSignCountRatio':
                    self.disvalue_f = self.getDisValue(ratio, self.fields[i])
                    if self.getItemsSql('rejectCount', self.fields[i]) == 0:
                        self.sqlvalue_f = 0
                    else:
                        self.sqlvalue_f = self.getItemsSql('docSignCount', self.fields[i]) / self.getItemsSql(
                            'rejectCount', self.fields[i])
                    self.rlt = self.isEqual(self.disvalue_f, self.sqlvalue_f)
                    self.saveTR.writeData('docSignCountRatio', self.disvalue_f, self.sqlvalue_f, self.rlt, count)
                    count += 1
                elif ratio == 'docAlterCountRatio':
                    self.disvalue_f = self.getDisValue(ratio, self.fields[i])
                    if self.getItemsSql('rejectCount', self.fields[i]) == 0:
                        self.sqlvalue_f = 0
                    else:
                        self.sqlvalue_f = self.getItemsSql('docAlterCount', self.fields[i]) / self.getItemsSql(
                            'rejectCount', self.fields[i])
                    self.rlt = self.isEqual(self.disvalue_f, self.sqlvalue_f)
                    self.saveTR.writeData('docAlterCountRatio', self.disvalue_f, self.sqlvalue_f, self.rlt, count)
                    count += 1
                elif ratio == 'docCancelCountRatio':
                    self.disvalue_f = self.getDisValue(ratio, self.fields[i])
                    if self.getItemsSql('rejectCount', self.fields[i]) == 0:
                        self.sqlvalue_f = 0
                    else:
                        self.sqlvalue_f = self.getItemsSql('docCancelCount', self.fields[i]) / self.getItemsSql(
                            'rejectCount', self.fields[i])
                    self.rlt = self.isEqual(self.disvalue_f, self.sqlvalue_f)
                    self.saveTR.writeData('docCancelCountRatio', self.disvalue_f, self.sqlvalue_f, self.rlt, count)
                    count += 1

        self.saveTR.closexlsx()


if __name__ == '__main__':
    c = check()
