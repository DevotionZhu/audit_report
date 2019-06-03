from common.connect_db import connectDB
from config.config_reader import configReader
import os


class getSqlValue():
    def __init__(self):
        # 连接审方数据库
        self.conndb = connectDB()
        self.conn = self.conndb.connect(self.conndb.dbname_auditcenter)
        self.cur = self.conndb.getCursor(self.conn)

        # 从配置文件中获取sql配置项
        self.confR = configReader()
        # self.ipt_work = self.confR.conf.items('workReportByOrg_ipt_zoneId')

    def getValue_zoneId(self, field, itemname, zoneid, startT, endT):
        self.sql = self.confR.get(field, itemname)
        sqlvalue = self.conndb.executeSQL_zoneid_one(self.cur, self.sql, zoneid, startT, endT)
        return sqlvalue

    def getValue_zydeptId(self, field, itemname, zoneid, zydeptid, startT, endT):
        self.sql = self.confR.get(field, itemname)
        sqlvalue = self.conndb.executeSQL_deptid_one(self.cur, self.sql, zoneid, zydeptid, startT, endT)
        return sqlvalue

    def getValue_mzdeptId(self, field, itemname, zoneid, mzdeptid, startT, endT):
        self.sql = self.confR.get(field, itemname)
        sqlvalue = self.conndb.executeSQL_deptid_one(self.cur, self.sql, zoneid, mzdeptid, startT, endT)
        return sqlvalue

    def getValue_kfDocId(self, field, itemname, zoneid, kfdocid, startT, endT):
        self.sql = self.confR.get(field, itemname)
        sqlvalue = self.conndb.executeSQL_kfdocid_one(self.cur, self.sql, zoneid, kfdocid, startT, endT)
        return sqlvalue

    def getValue_inWardId(self, field, itemname, zoneid, inwardid, startT, endT):
        self.sql = self.confR.get(field, itemname)
        sqlvalue = self.conndb.executeSQL_inwardid_one(self.cur, self.sql, zoneid, inwardid, startT, endT)
        return sqlvalue

    def getValue_phar(self, field, itemname, audit_doctor_id, startT, endT):
        self.sql = self.confR.get(field, itemname)
        sqlvalue = self.conndb.executeSQL_phar(self.cur, self.sql, audit_doctor_id, startT, endT)
        return sqlvalue


if __name__ == '__main__':
    vs = getSqlValue()
