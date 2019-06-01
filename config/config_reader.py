# coding:utf8
from configparser import ConfigParser
from common.log import mylog, mylog_except
import os


class configReader():
    # 实例化ConfigParser 并加载配置文件
    def __init__(self):
        path = os.path.dirname(os.path.abspath(__file__))
        self.configfile = os.path.join(path, 'index.ini')
        self.conf = ConfigParser()
        self.conf.read(self.configfile, encoding='utf8')

    # 读取指定的配置信息，如print 'host of db:', cp.get('db', 'host')     # host of db: 127.0.0.1
    def get(self, field, key):

        try:
            return self.conf.get(field, key)

        except Exception as error:
            logcontent = "读取配置项发生了错误" + "," + field + "," + key
            mylog(logcontent)
            mylog_except(error)

    # 按类型读取配置信息：getint、 getfloat
    def getint(self, field, key):
        try:
            return self.conf.getint(field, key)
        except Exception as error:
            logcontent = "读取配置项发生了错误" + "," + field + "," + key
            mylog(logcontent)
            mylog_except(error)

    def geti(self, field):
        return self.conf.items(field)

    # 获取option 键值元组列表，如print 'items of [ssh]:', cp.items('ssh')    # items of [ssh]: [('host', '192.168.1.101'), ('user', 'huey'), ('pass', 'huey')]
    def getitems(self, field):
        try:
            defaultvalue = self.conf.items('zone')
            defaultKey = [key for key, value in defaultvalue]
            result = self.conf.items(field)
            hospitalItemnames = []
            for key, value in result:
                if key not in defaultKey or key.startswith('i'):
                    hospitalItemnames.append(key.upper())
                else:
                    hospitalItemnames.append(key)
            return hospitalItemnames

        except Exception as error:
            # print "读取配置项发生了错误",field
            logcontent = "读取配置项发生了错误" + "," + field
            mylog(logcontent)
            mylog_except(error)

    def getitems_new(self, field):
        try:
            dvalue = self.conf.items(field)
            sqlItemnames = []
            for key, value in dvalue:
                sqlItemnames.append(key)
            return sqlItemnames

        except Exception as error:
            # print "读取配置项发生了错误",field
            logcontent = "读取配置项发生了错误" + "," + field
            mylog(logcontent)
            mylog_except(error)
