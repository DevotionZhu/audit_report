from common.config_reader import configReader
from common.saveTestResult import getTestResult
from common.getSqlValue import getSqlValue
from common.getdisplay import getDisplayValue
import json, os

path = os.path.abspath('./config/index.ini')


class check():
    def __init__(self,field):
        self.reportName = '审方工作统计'
        # 从配置文件中获取sql配置项
        self.confR = configReader(path)
        self.itemnames = self.confR.getitems_new(field)
        print(self.itemnames)
        # 获取报表页面显示值的类
        self.getdisplay = getDisplayValue()
        self.getdv = self.getdisplay.getvalue()
        print(self.getdv.keys)
        # 从配置文件中获取sql中所需变量：zoneid、startT、endT
        self.zoneid = self.confR.getint("constant", "zoneid")
        print(self.zoneid)
        self.startT = self.confR.get("constant", "startT")
        print(self.startT)
        self.endT = self.confR.get("constant", "endT")

        # 获取sql值的类
        self.getsqlvalue = getSqlValue()

        # 保存测试结果
        self.saveTR = getTestResult(self.reportName)

    # 判断页面展示值与sql值是否相等
    def isEqual(self, displayvalue, sqlvalue):
        if displayvalue == sqlvalue:
            return "pass"
        else:
            return "fail"

    # 获取报表中的sql值
    def getItemsSql(self, itemname):
        self.sqlvalue = self.getsqlvalue.getValue(itemname, self.zoneid, self.startT, self.endT)
        if self.sqlvalue == None:  # 当SQL查询结果为None时
            self.sqlvalue_new = "The SQL's result is None"
        else:
            self.sqlvalue_new = self.sqlvalue
        return self.sqlvalue_new

    # 获取报表页面display值
    def getDisValue(self, itemKey):
        # 局部变量需要先定义再赋值
        disvalue_new = ''
        if itemKey not in self.itemnames:
            disvalue_new = "Nodata"

        elif itemKey in self.itemnames:
                disvalue_new = self.getdv[itemKey]
        return disvalue_new, itemKey

    # 执行报表中统计的验证并输出测试结果
    def executeCheck(self):
        # 创建excel文件
        self.saveTR.createXlsx()
        self.saveTR.writeColName()
        count = 1

        for itemkey in self.itemnames:
            # self.disvalue_f = self.getDisValue(itemkey)
            self.disvalue_f = self.getdv[itemkey]
            self.sqlvalue_f = self.getItemsSql(itemkey)
            self.itemname = itemkey
            self.rlt = self.isEqual(self.disvalue_f, self.sqlvalue_f)
            # 将内容打印到日志里面
            # self.content=self.rlt+","+self.itemname+","+str(self.esvalue_f)+','+str(self.sqlvalue_f)
            # mylog(self.content)
            self.saveTR.writeData(self.itemname, self.disvalue_f, self.sqlvalue_f, self.rlt, count)
            count += 1
        self.saveTR.closexlsx()


if __name__ == '__main__':
    c = check()
    print(c.itemnames)
