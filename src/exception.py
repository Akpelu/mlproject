import sys
import logging
from pipeline import logger

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in Python script name {file_name} line number {exc_tb.tb_lineno}: {error}"
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        
    def __str__(self) -> str:
        return self.error_message
    
try:
    # code that may raise error
    x = 10 / 0 #Raising a zero division error
except ZeroDivisionError as e:
    try:
        raise CustomException("Division by zero error", sys.exc_info())
    except CustomException as ce:
        logging.error(ce)
        
if __name__ == '__main__':
    logging.info("ZeroDivisionError")