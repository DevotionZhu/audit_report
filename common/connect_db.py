import os
import pymysql
from config.config_reader import configReader
from common.log import mylog, mylog_except


class connectDB():
    def __init__(self):

        self.dbconf = configReader()
        self.host = self.dbconf.get("db_auditcenter", "auditcenter_host")
        self.port = self.dbconf.getint("db_auditcenter", "auditcenter_port")
        self.username = self.dbconf.get("db_auditcenter", "auditcenter_username")
        self.passwd = self.dbconf.get("db_auditcenter", "auditcenter_passwd")
        self.dbname_auditcenter = self.dbconf.get("db_auditcenter", "auditcenter_db")

    def connect(self, dbname):
        try:
            return pymysql.Connect(host=self.host, port=self.port, user=self.username, passwd=self.passwd, db=dbname,
                                   charset='utf8')
        except Exception as error:
            mylog("数据库连接出错")
            mylog_except(error)

    def getCursor(self, conn):
        if conn is not None:
            return conn.cursor()

    def closeConn(self, conn):
        if conn is not None:
            conn.close()

    def closeCur(self, cur):
        if cur is not None:
            cur.closeCur()

    # 执行没有变量的sql
    def execute_sql(self, cur, sql):
        cur.execute(sql)
        return cur.fetchone()[0]

    # 执行的SQL语句传入的值是机构，开始时间，结束时间
    def executeSQL_zoneid_one(self, cur, sql, zoneid, startT, endT):
        cur.execute(sql, (zoneid, startT, endT))
        return cur.fetchone()[0]

    # 执行的SQL语句传入的值是机构，科室，开始时间，结束时间
    def executeSQL_deptid_one(self, cur, sql, zoneid, deptid, startT, endT):
        cur.execute(sql, (zoneid, deptid, startT, endT))
        return cur.fetchone()[0]

    # 执行的SQL语句传入的值是机构，开方医生，开始时间，结束时间
    def executeSQL_kfdocid_one(self, cur, sql, zoneid, kfdocid, startT, endT):
        cur.execute(sql, (zoneid, kfdocid, startT, endT))
        return cur.fetchone()[0]

    # 执行的SQL语句传入的值是机构，病区，开始时间，结束时间
    def executeSQL_inwardid_one(self, cur, sql, zoneid, inwardid, startT, endT):
        cur.execute(sql, (zoneid, inwardid, startT, endT))
        return cur.fetchone()[0]

    # 执行的SQL语句传入的值是提示类型，开始时间，结束时间
    def executeSQL_issue(self, cur, sql, analysis_result_type, startT, endT):
        cur.execute(sql, (analysis_result_type, startT, endT))
        return cur.fetchone()[0]

    # 执行的SQL语句传入的值是机构，开始时间，结束时间，机构，开始时间，结束时间（用于统计全院的指标数据）
    def executeSQL_zoneid_two(self, cur, sql, zoneid, startT, endT):
        cur.execute(sql, (zoneid, startT, endT, zoneid, startT, endT))
        return cur.fetchone()[0]

    # 执行的SQL语句传入的值是机构，开始时间，结束时间，配置项的值
    def executeSQL_zoneid_three(self, cur, sql, zoneid, startT, endT, configValue):
        try:
            cur.execute(sql, (zoneid, startT, endT, configValue))
            self.rlt = cur.fetchone()[0]
        except Exception as error:
            print(error)
            self.rlt = 'no data'
        return self.rlt

    # 药品维度下获取标准产品属性的SQL执行，传入的是一个标准产品的id
    def executeSQL_drug_productinfor(self, cur, sql, productid):
        try:
            cur.execute(sql, (productid,))
            self.rlt = cur.fetchone()[0]
        except Exception as error:
            print(error)
            self.rlt = 'no data'
        return self.rlt

    # 执行的SQL语句传入的值是机构，科室，开始时间，结束时间，机构，科室，开始时间，结束时间
    def executeSQL_deptid_two(self, cur, sql, zoneid, deptid, startT, endT):
        cur.execute(sql, (zoneid, deptid, startT, endT, zoneid, deptid, startT, endT))
        return cur.fetchone()[0]

    # 执行的SQL语句传入的值是机构，科室，开始时间，结束时间，配置项的值
    def executeSQL_deptid_three(self, cur, sql, zoneid, deptid, startT, endT, configValue):
        try:
            cur.execute(sql, (zoneid, deptid, startT, endT, configValue))
            self.rlt = cur.fetchone()[0]
        except Exception as error:
            print(error)
            self.rlt = 'no data'
        return self.rlt

    # 执行的SQL语句传入的值是机构，医生，开始时间，结束时间，配置项的值
    def executeSQL_docid_three(self, cur, sql, zoneid, docid, startT, endT, configValue):
        try:
            cur.execute(sql, (zoneid, docid, startT, endT, configValue))
            self.rlt = cur.fetchone()[0]
        except Exception as error:
            print(error)
            self.rlt = 'no data'
        return self.rlt

    # 执行的SQL语句传入的值是药师，开始时间，结束时间
    def executeSQL_phar(self, cur, sql, audit_doctor_id, startT, endT):
        cur.execute(sql, (audit_doctor_id, startT, endT))
        return cur.fetchone()[0]

    # 执行的SQL语句传入的值是机构，医生，开始时间，结束时间
    def executeSQL_docid_one(self, cur, sql, zoneid, docid, startT, endT):
        cur.execute(sql, (zoneid, docid, startT, endT))
        return cur.fetchone()[0]

    # 执行的SQL语句传入的值是机构，医生，开始时间，结束时间，机构，医生，开始时间，结束时间
    def executeSQL_docid_two(self, cur, sql, zoneid, docid, startT, endT):
        cur.execute(sql, (zoneid, docid, startT, endT, zoneid, docid, startT, endT))
        return cur.fetchone()[0]

    # 执行的SQL语句传入的值是机构，医疗组，开始时间，结束时间
    def executeSQL_groupone(self, cur, sql, zoneid, groupname, startT, endT):
        cur.execute(sql, (zoneid, groupname, startT, endT))
        return cur.fetchone()[0]

    # 执行的SQL语句传入的值是机构，医疗组，开始时间，结束时间，机构，医疗组，开始时间，结束时间
    def executeSQL_group_two(self, cur, sql, zoneid, groupname, startT, endT):
        cur.execute(sql, (zoneid, groupname, startT, endT, zoneid, groupname, startT, endT))
        return cur.fetchone()[0]

    # 执行的SQL语句传入的值是机构，开始时间，结束时间，产品，机构，开始时间，结束时间，产品
    def executeSQL_drug(self, cur, sql, zoneid, startT, endT, productId):
        cur.execute(sql, (zoneid, startT, endT, productId, zoneid, startT, endT, productId))
        return cur.fetchone()[0]


if __name__ == "__main__":
    # connectDB=connectDB()
    # conn=connectDB.connect(connectDB.dbname_report)
    # cur=connectDB.getCursor(conn)
    # confr=configReader(path)
    # sql=confr.get('zone',"急诊患者就诊总人次")
    # print(sql)
    # rlt=cur.execute(sql,(1,'2014-08-01','2014-08-01'))
    # print(cur.fetchone()[0])
    connectDB = connectDB()
    conn = connectDB.connect(connectDB.dbname_auditcenter)
    cur = connectDB.getCursor(conn)
