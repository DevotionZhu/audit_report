#coding:utf8
import requests
import json
from common.config_reader import configReader
from common.connect_db import connectDB
import os

path=os.path.abspath('./config/sysconfig.ini')


class getDisplayValue():
        def __init__(self):
            self.cfR=configReader(path)
            self.url=self.cfR.get('url','url')
            self.headers = {
                'Content-Type': "application/json",
            }


# 登录系统
        def login(self):
            self.session = requests.session()
            self.api =self.cfR.get('api','login')
            self.addr = "{}/{}".format(self.url, self.api)
            self.name=self.cfR.get('url','username')
            self.passwd = self.cfR.get('url', 'password')
            self.params = {"name": self.name, "password": self.passwd}
            self.session.post(self.addr, data=json.dumps(self.params), headers=self.headers)

#获取统计报表页面上的显示值
        def getvalue(self):

            self.login()
            self.url_auditcenter=self.cfR.get('url','auditcenter')
            self.api = self.cfR.get('api','审方工作统计按机构统计')
            self.addr = "{}/{}".format(self.url_auditcenter, self.api)
            self.params = """{"endTime": 1558713599000,
                            "groupField": "zoneId",
                            "order": "",
                            "orderField": "",
                            "page": 1,
                            "pageSize": 20,
                            "pharNameList": [],
                            "source": "住院",
                            "startTime": 1558627200000,
                            "zoneIdAndDoctorsList": [],
                            "zoneIdAndGroupsList": [],
                            "zoneIdList": [331],
                            "zonedIdAndDeptsList": [],
                            "zonedIdAndWardsList": []}"""
            # response = self.session.post(self.addr, params=json.dumps(self.params, ensure_ascii=False), headers=self.headers)
            response = self.session.post(self.addr, data=self.params.encode('utf-8'), headers=self.headers).json()
            workReportByOrg = response['data']['recordList'][0]
            return workReportByOrg


if __name__=="__main__":

    configV=getDisplayValue()
    test = configV.getvalue()
    print(test)
    print(type(test))