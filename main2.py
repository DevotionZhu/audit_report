from common.saveTestResult import getTestResult
import pymysql
from common.connect_db import connectDB
from common.config_reader import configReader
from common.log import mylog_except,mylog
from common.getSqlValue import getSqlValue
from common.getdisplay import configValue
import os

path=os.path.abspath('./config/index.ini')
field = 'ipt_workReportByOrg'
def run():

    # 连接审方数据库
    conndb = connectDB()
    conn = conndb.connect(conndb.dbname_auditcenter)
    cur = conndb.getCursor(conn)
    # 从配置文件中获取sql配置项
    cr = configReader(path)
    item = cr.getitems_new(field)
    test = []
    for i in item:
        sql = cr.get(field, i)
        v = conndb.execute_sql(cur,sql)
        print(v)
        test.append(v)
    print(test)
    sTR = getTestResult(field)
    sTR.createXlsx()
    sTR.writeColName()
    sTR.writeData(test[0], test[1], test[2])
    sTR.closexlsx()
run()
dis = configValue()
dis.getvalue()












