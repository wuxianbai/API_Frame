import logging
from logging import handlers
import time, os

logLevel = {
        'info': logging.INFO,
        'debug': logging.DEBUG,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

class Log():

    def __init__(self):
        filepath = os.path.abspath('../Logs')
        if not os.path.exists(filepath):
            os.mkdir(filepath)

        localtime = time.localtime()
        today = time.strftime('%Y-%m-%d', localtime)
        self.filename = os.path.join(filepath, '{}.log'.format(today))

    def getHandler(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # self.logger.setLevel(logLevel.get(level, logging.DEBUG))
        self.th = handlers.TimedRotatingFileHandler(self.filename, when='D', backupCount=1, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        self.th.setFormatter(formatter)
        self.logger.addHandler(self.th)

    def print(self, infos):
        self.getHandler()
        self.logger.debug(infos)
        self.logger.removeHandler(self.th)

if __name__ == '__main__':
    # Log().print('你好')
    print(os.getcwd())