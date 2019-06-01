# coding:utf8
import requests
import json
from config.config_reader import configReader
import os, time


class getDisplayValue():
    def __init__(self):
        self.cfR = configReader()
        self.url = self.cfR.get('url', 'url')
        self.zoneid = self.cfR.get('constant', 'zoneid')
        self.inwardid = self.cfR.get('constant', 'inwardid')
        self.deptid = self.cfR.get('constant', 'deptid')
        self.audit_doctor_id = self.cfR.get('constant', 'audit_doctor_id')
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
        self.api = self.cfR.get('api', 'login')
        self.addr = "{}/{}".format(self.url, self.api)
        self.name = self.cfR.get('url', 'username')
        self.passwd = self.cfR.get('url', 'password')
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


if __name__ == "__main__":
    configV = getDisplayValue()
    test = configV.getvalue_deptId('审方工作统计按机构统计', 'deptId', '住院')
    print(test)
    print(type(test))
