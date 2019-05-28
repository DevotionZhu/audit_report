import pymysql
from common.connect_db import connectDB
from common.config_reader import configReader
from common.log import mylog_except,mylog
from configparser import ConfigParser
import os

path=os.path.abspath('./config/index.ini')

class getSqlValue():
    def __init__(self):
        # 连接审方数据库
        self.conndb = connectDB()
        self.conn =self.conndb.connect(self.conndb.dbname_auditcenter)
        self.cur = self.conndb.getCursor(self.conn)

        # 从配置文件中获取sql配置项
        self.confR = configReader(path)
        self.ipt_work = self.confR.conf.items('ipt_workReportByOrg')

    # def getValue(self):
    #     Key=[key for key,value in dvalue]
    def getValue(self, itemname, zoneid, startT, endT):
        self.sql = self.confR.get("ipt_workReportByOrg", itemname)
        print(self.sql)
        sqlvalue = self.conndb.executeSQL_zoneid_one(self.cur, self.sql, zoneid, startT, endT)
        print(sqlvalue)
        return sqlvalue




    # def getValue(self):
    #     #     # python循环字典
    #     #     for i in self.ipt_work:
    #     #         print(self.ipt_work[i])

if __name__ == '__main__':
    vs = getSqlValue()
    vs.getValue()




    # # 从配置文件中获取sql配置项
    # cofR = configReader(path)
    # sql1 = cr.get('projectsql','disAuditCount')
    # v1 = conndb.execute_sql(cur,sql1)
    # print(v1)










