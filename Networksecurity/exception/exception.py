import sys
from Networksecurity.logging.logger import logger
import logging
import os
from datetime import datetime

class NetworksecurityException(Exception):
    def __init__(self,error_message,error_detail:sys):
        self.error_message=error_message
        self.error_detail=error_detail
        _,_,exc_tb=self.error_detail.exc_info()

        self.lineno=exc_tb.tb_lineno
        self.filename=exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.filename,self.lineno,str(self.error_message)
        )
        

if __name__=="__main__":
    try:
        logger.logging.info("Attempting to divide by zero")
        a=1/0
        print(a)

    except Exception as e:
        raise NetworksecurityException(e,sys)