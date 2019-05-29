import pymysql
from common.connect_db import connectDB
from common.config_reader import configReader
from common.log import mylog_except, mylog
from configparser import ConfigParser
import os

path = os.path.abspath('./config/index.ini')


class getSqlValue():
    def __init__(self):
        # 连接审方数据库
        self.conndb = connectDB()
        self.conn = self.conndb.connect(self.conndb.dbname_auditcenter)
        self.cur = self.conndb.getCursor(self.conn)

        # 从配置文件中获取sql配置项
        self.confR = configReader(path)
        # self.ipt_work = self.confR.conf.items('workReportByOrg_ipt_zoneId')

    def getValue_zoneId(self, field,itemname, zoneid, startT, endT):
        self.sql = self.confR.get(field, itemname)
        sqlvalue = self.conndb.executeSQL_zoneid_one(self.cur, self.sql, zoneid, startT, endT)
        return sqlvalue

    def getValue_deptId(self, field,itemname, zoneid, deptid, startT, endT):
        self.sql = self.confR.get(field, itemname)
        sqlvalue = self.conndb.executeSQL_deptid_one(self.cur, self.sql, zoneid, deptid, startT, endT)
        return sqlvalue


if __name__ == '__main__':
    vs = getSqlValue()

