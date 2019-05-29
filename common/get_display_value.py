# coding:utf8
import requests
import json
from common.config_reader import configReader
from common.connect_db import connectDB
import os, time

path = os.path.abspath('./config/index.ini')


class getDisplayValue():
    def __init__(self):
        self.cfR = configReader(path)
        self.url = self.cfR.get('url', 'url')
        self.zoneid = self.cfR.get('constant', 'zoneid')
        self.inwardid = self.cfR.get('constant', 'inwardid')
        self.deptid = self.cfR.get('constant', 'deptid')
        self.end = self.cfR.get('constant', 'endT')
        self.endT = int(time.mktime(time.strptime(self.end, "%Y-%m-%d %H:%M:%S"))) * 1000
        print(self.endT)
        self.start = self.cfR.get('constant', 'startT')
        self.startT = int(time.mktime(time.strptime(self.start, "%Y-%m-%d %H:%M:%S"))) * 1000
        print(self.startT)
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
    def getvalue_zoneId(self, apiname, groupField, source):
        self.login()
        self.url_auditcenter = self.cfR.get('url', 'auditcenter')
        self.api = self.cfR.get('api', apiname)
        self.addr = "{}/{}".format(self.url_auditcenter, self.api)
        self.param = {"endTime": self.endT,
                      "groupField": groupField,
                      "order": "",
                      "orderField": "",
                      "page": 1,
                      "pageSize": 20,
                      "pharNameList": [],
                      "source": source,
                      "startTime": self.startT,
                      "zoneIdAndDoctorsList": [],
                      "zoneIdAndGroupsList": [],
                      "zoneIdList": [self.zoneid],
                      "zonedIdAndDeptsList": [],
                      "zonedIdAndWardsList": []}
        self.params = json.dumps(self.param)  # 将json对象转化为字符串
        # response = self.session.post(self.addr, params=json.dumps(self.params, ensure_ascii=False), headers=self.headers)
        response = self.session.post(self.addr, data=self.params.encode('utf-8'), headers=self.headers).json()
        data_zoneId = response['data']['recordList'][0]
        return data_zoneId

    def getvalue_deptId(self, apiname, groupField, source):
        self.login()
        self.url_auditcenter = self.cfR.get('url', 'auditcenter')
        self.api = self.cfR.get('api', apiname)
        self.addr = "{}/{}".format(self.url_auditcenter, self.api)
        self.param = {"endTime": self.endT,
                      "groupField": groupField,
                      "order": "",
                      "orderField": "",
                      "page": 1,
                      "pageSize": 20,
                      "pharNameList": [],
                      "source": source,
                      "startTime": self.startT,
                      "zoneIdAndDoctorsList": [],
                      "zoneIdAndGroupsList": [],
                      "zoneIdList": [self.zoneid],
                      "zonedIdAndDeptsList": [{"deptList": [self.deptid], "zoneId": self.zoneid}],
                      "zonedIdAndWardsList": []}
        self.params = json.dumps(self.param)  # 将json对象转化为字符串
        # response = self.session.post(self.addr, params=json.dumps(self.params, ensure_ascii=False), headers=self.headers)
        response = self.session.post(self.addr, data=self.params.encode('utf-8'), headers=self.headers).json()
        data_deptId = response['data']['recordList'][0]
        return data_deptId


if __name__ == "__main__":
    configV = getDisplayValue()
    test = configV.getvalue_deptId('审方工作统计按机构统计', 'deptId', '住院')
    print(test)
    print(type(test))