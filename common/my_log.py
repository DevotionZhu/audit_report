# coding:utf8
import logging
from logging import handlers
import os


class Logger():

    def __init__(self):
        self.logger_obj = logging.getLogger()
        self.fh = logging.FileHandler("fail_log.txt", mode='w')  # 创建一个文件输出流
        self.fh.setLevel(logging.ERROR)  # 定义文件输出流的告警级别
        formater = logging.Formatter(
            '%(asctime)s - %(levelname)s %(pathname)s[line:%(lineno)d]: %(message)s')  # 定义日志输出格式
        self.fh.setFormatter(formater)  # 给Handler选择一个格式
        self.logger_obj.addHandler(self.fh)

    def mylog(self, content):
        return self.logger_obj.error(content)


if __name__ == '__main__':
    log = Logger()
    log.mylog('ceshi')
