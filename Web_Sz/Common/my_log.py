import logging
from Web_Sz.Common.project_path import *


class My_Log:
    def my_log(self,msg,level):
        #定义日志收集器
        my_logger = logging.getLogger('python11')
        #设置级别
        my_logger.setLevel('DEBUG')
        #设置日志输出格式
        foematter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #穿件我们自己的输出渠道
        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')
        ch.setFormatter(foematter)

        fh = logging.FileHandler(Log_path,'a',encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(foematter)
        #两者对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)
        #收集日志
        if level=='DEBUG':
            my_logger.debug(msg)
        elif level=='INFO':
            my_logger.info(msg)
        elif level=='WARNING':
            my_logger.warning(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        elif level=='CRITICAL':
            my_logger.critical(msg)
        #关闭日志收集器
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)


    def debug(self,msg):
        self.my_log(msg,'DEBUF')

    def info(self,msg):
        self.my_log(msg,'INFO')

    def warning(self,msg):
        self.my_log(msg,'WARNING')

    def error(self,msg):
        self.my_log(msg,'ERROR')

    def critical(self,msg):
        self.my_log(msg,'CRITICAL')


if __name__ == '__main__':
    My_Log().my_log('hdahdhahdadadadadada','INFO')

