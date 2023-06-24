import logging
import math

class Loggerclient():
    count = 0
    def __init__(self,object):
        self.logger = logging.getLogger(type(object).__name__)
        self.count=1

    def info(self,msg):
        self.logger.info(msg)

    def error(self,msg):
        self.logger.error(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def warning(self,msg):
        self.logger.warning(msg)

    def exception(self,msg):
        self.logger.exception(msg)
        math.pow()

    @staticmethod
    def getLogger(self):
        if self.count ==1:

            return Loggerclient()
