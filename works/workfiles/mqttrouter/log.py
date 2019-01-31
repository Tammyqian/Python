#coding=utf-8

import sys
import logging
import logging.handlers

#日志内容最大值
MAX_BYTES = 1024*1024*100

#最大日志保留数
B_COUNT = 8

#日志等级
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

class log:
    """
    封装logging类
    >>level 可以输出的最低级别
    >>type    0:输出到前台和文件 1:输出到文件
    """
    def __init__(self, name, level = logging.DEBUG, type = 1):
        log_file = name+".log"

        self._log = logging.getLogger(log_file)

        self._log.setLevel(level)

        lfh = logging.handlers.RotatingFileHandler(log_file, maxBytes=MAX_BYTES, backupCount = B_COUNT)

        #lfh = logging.handlers.TimedRotatingFileHandler(log_file, when = 'midnight', backupCount = B_COUNT)
        #lfh = logging.handlers.RotatingFileHandler(log_file, maxBytes=MAX_BYTES, backupCount = B_COUNT)

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        lfh.setFormatter(formatter)

        self._log.addHandler(lfh)

        if type == 0:
            ch = logging.StreamHandler()
            ch.setFormatter(formatter)
            self._log.addHandler(ch)

    def getLogger(self):
        return self._log

if __name__ == '__main__':
    l = log("/tmp/test").getLogger()
    while True:
        import time
        time.sleep(3)
        l.debug('a' * 1024)



