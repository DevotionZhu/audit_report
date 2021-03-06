# coding:utf8
import requests
import json
from config.config_reader import configReader
import os, time


class getDisplayValue():
    def __init__(self):
        self.cfR = configReader()
        self.zoneid = self.cfR.get('constant', 'zoneid')
        self.inwardid = self.cfR.get('constant', 'inwardid')
        self.deptid = self.cfR.get('constant', 'deptid')
        self.audit_doctor_id = self.cfR.get('constant', 'audit_doctor_id')
        self.kf_doc_id = self.cfR.get('constant', 'kf_doc_id')
        self.in_ward_id = self.cfR.get('constant', 'in_ward_id')
        self.analysis_type = self.cfR.get('constant', 'analysis_type')
        self.analysis_result_type = self.cfR.get('constant', 'analysis_result_type')
        self.end = self.cfR.get('constant', 'endT')
        self.endT = int(time.mktime(time.strptime(self.end, "%Y-%m-%d %H:%M:%S"))) * 1000
        self.start = self.cfR.get('constant', 'startT')
        self.startT = int(time.mktime(time.strptime(self.start, "%Y-%m-%d %H:%M:%S"))) * 1000
        self.headers = {
            'Content-Type': "application/json",
        }

    # 登录系统
    def login(self):
        self.session = requests.session()
        self.addr = self.cfR.get('login', 'address') + '/api/v1/currentUser'
        self.name = self.cfR.get('login', 'username')
        self.passwd = self.cfR.get('login', 'password')
        self.params = {"name": self.name, "password": self.passwd}
        self.session.post(self.addr, data=json.dumps(self.params), headers=self.headers)

    # 获取统计报表页面上的显示值
    def getvalue_zoneId(self, field):
        self.login()
        self.url_auditcenter = self.cfR.get('url', 'auditcenter')
        self.api = self.cfR.get(field, 'api')
        self.groupField = self.cfR.get(field, 'groupField')
        self.source = self.cfR.get(field, 'source')
        self.addr = "{}/{}".format(self.url_auditcenter, self.api)
        self.param = {"endTime": self.endT,
                      "groupField": self.groupField,
                      "order": "",
                      "orderField": "",
                      "page": 1,
                      "pageSize": 20,
                      "pharNameList": [],
                      "source": self.source,
                      "startTime": self.startT,
                      "zoneIdAndDoctorsList": [],
                      "zoneIdAndGroupsList": [],
                      "zoneIdList": [self.zoneid],
                      "zonedIdAndDeptsList": [],
                      "zonedIdAndWardsList": []}
        self.params = json.dumps(self.param)  # 将json对象转化为字符串
        # response = self.session.post(self.addr, params=json.dumps(self.params, ensure_ascii=False), headers=self.headers)
        response = self.session.post(self.addr, data=self.params.encode('utf-8'), headers=self.headers).json()
        if response['data']['recordList'] == []:
            data_zoneId = "Nodata"
        else:
            data_zoneId = response['data']['recordList'][0]
        return data_zoneId

    def getvalue_deptId(self, field):
        self.login()
        self.url_auditcenter = self.cfR.get('url', 'auditcenter')
        self.api = self.cfR.get(field, 'api')
        self.groupField = self.cfR.get(field, 'groupField')
        self.source = self.cfR.get(field, 'source')
        self.addr = "{}/{}".format(self.url_auditcenter, self.api)
        self.param = {"endTime": self.endT,
                      "groupField": self.groupField,
                      "order": "",
                      "orderField": "",
                      "page": 1,
                      "pageSize": 20,
                      "pharNameList": [],
                      "source": self.source,
                      "startTime": self.startT,
                      "zoneIdAndDoctorsList": [],
                      "zoneIdAndGroupsList": [],
                      "zoneIdList": [self.zoneid],
                      "zonedIdAndDeptsList": [{"deptList": [self.deptid], "zoneId": self.zoneid}],
                      "zonedIdAndWardsList": []}
        self.params = json.dumps(self.param)  # 将json对象转化为字符串
        # response = self.session.post(self.addr, params=json.dumps(self.params, ensure_ascii=False), headers=self.headers)
        response = self.session.post(self.addr, data=self.params.encode('utf-8'), headers=self.headers).json()
        if response['data']['recordList'] == []:
            data_deptId = "Nodata"
        else:
            data_deptId = response['data']['recordList'][0]
        return data_deptId

    def getvalue_kfDocId(self, field):
        self.login()
        self.url_auditcenter = self.cfR.get('url', 'auditcenter')
        self.api = self.cfR.get(field, 'api')
        self.groupField = self.cfR.get(field, 'groupField')
        self.source = self.cfR.get(field, 'source')
        self.addr = "{}/{}".format(self.url_auditcenter, self.api)
        self.param = {"endTime": self.endT,
                      "groupField": self.groupField,
                      "order": "",
                      "orderField": "",
                      "page": 1,
                      "pageSize": 20,
                      "pharNameList": [],
                      "source": self.source,
                      "startTime": self.startT,
                      "zoneIdAndDoctorsList": [{"zoneId": self.zoneid, "doctorIdList": [self.kf_doc_id]}],
                      "zoneIdAndGroupsList": [],
                      "zoneIdList": [self.zoneid],
                      "zonedIdAndDeptsList": [],
                      "zonedIdAndWardsList": []}
        self.params = json.dumps(self.param)  # 将json对象转化为字符串
        # response = self.session.post(self.addr, params=json.dumps(self.params, ensure_ascii=False), headers=self.headers)
        response = self.session.post(self.addr, data=self.params.encode('utf-8'), headers=self.headers).json()
        if response['data']['recordList'] == []:
            data_kfDocId = "Nodata"
        else:
            data_kfDocId = response['data']['recordList'][0]
        return data_kfDocId

    def getvalue_inWardId(self, field):
        self.login()
        self.url_auditcenter = self.cfR.get('url', 'auditcenter')
        self.api = self.cfR.get(field, 'api')
        self.groupField = self.cfR.get(field, 'groupField')
        self.source = self.cfR.get(field, 'source')
        self.addr = "{}/{}".format(self.url_auditcenter, self.api)
        self.param = {"endTime": self.endT,
                      "groupField": self.groupField,
                      "order": "",
                      "orderField": "",
                      "page": 1,
                      "pageSize": 20,
                      "pharNameList": [],
                      "source": self.source,
                      "startTime": self.startT,
                      "zoneIdAndDoctorsList": [],
                      "zoneIdAndGroupsList": [],
                      "zoneIdList": [self.zoneid],
                      "zonedIdAndDeptsList": [],
                      "zonedIdAndWardsList": [{"wardList": [self.in_ward_id], "zoneId": self.zoneid}]}
        self.params = json.dumps(self.param)  # 将json对象转化为字符串
        # response = self.session.post(self.addr, params=json.dumps(self.params, ensure_ascii=False), headers=self.headers)
        response = self.session.post(self.addr, data=self.params.encode('utf-8'), headers=self.headers).json()
        if response['data']['recordList'] == []:
            data_inWardId = "Nodata"
        else:
            data_inWardId = response['data']['recordList'][0]
        return data_inWardId

    def getvalue_auditDoctorId(self, field):
        self.login()
        self.url_auditcenter = self.cfR.get('url', 'auditcenter')
        self.api = self.cfR.get(field, 'api')
        self.groupField = self.cfR.get(field, 'groupField')
        self.source = self.cfR.get(field, 'source')
        self.addr = "{}/{}".format(self.url_auditcenter, self.api)
        self.param = {"endTime": self.endT,
                      "groupField": self.groupField,
                      "order": "",
                      "orderField": "",
                      "page": 1,
                      "pageSize": 20,
                      "pharNameList": [self.audit_doctor_id],
                      "source": self.source,
                      "startTime": self.startT,
                      "zoneIdAndDoctorsList": [],
                      "zoneIdAndGroupsList": [],
                      "zoneIdList": [],
                      "zonedIdAndDeptsList": [],
                      "zonedIdAndWardsList": []}
        self.params = json.dumps(self.param)  # 将json对象转化为字符串
        # response = self.session.post(self.addr, params=json.dumps(self.params, ensure_ascii=False), headers=self.headers)
        response = self.session.post(self.addr, data=self.params.encode('utf-8'), headers=self.headers).json()
        if response['data']['recordList'] == []:
            data_auditDoctorId = "Nodata"
        else:
            data_auditDoctorId = response['data']['recordList'][0]
        return data_auditDoctorId

    def getvalue_issue(self, field):
        self.login()
        self.url_auditcenter = self.cfR.get('url', 'auditcenter')
        self.api = self.cfR.get(field, 'api')
        self.source = self.cfR.get(field, 'source')
        self.addr = "{}/{}".format(self.url_auditcenter, self.api)
        self.param = {"analysisResultType": self.analysis_result_type,
                      "analysisType": self.analysis_type,
                      "endTime": self.endT,
                      "page": 1,
                      "pageSize": 20,
                      "source": self.source,
                      "startTime": self.startT}
        self.params = json.dumps(self.param)  # 将json对象转化为字符串
        # response = self.session.post(self.addr, params=json.dumps(self.params, ensure_ascii=False), headers=self.headers)
        response = self.session.post(self.addr, data=self.params.encode('utf-8'), headers=self.headers).json()
        if response['data']['recordList'] == []:
            data_issue = "Nodata"
        else:
            data_issue = response['data']['recordList'][0]
        return data_issue

if __name__ == "__main__":
    configV = getDisplayValue()
    test = configV.getvalue_deptId('workReportByOrg_ipt_deptId')
    print(test)
    # print(type(test))
