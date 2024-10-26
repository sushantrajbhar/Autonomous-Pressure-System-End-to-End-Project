import sys
import os 
"""
We create a class named SensorException which is inherited by a class Exception.
Now, as class is created, next step is to create a constructor.
We Initialize two variables and sys is used to capture the error details
As we have inherited a class. To use it we use the super function.
Exception class will give you the error_message. To use that variable, we will pass it as function 
The exception will not be directly seen as string. Hence we create a new function

We also create a new function which will show the error details. THe expected details are file in which there is error
Line number and what is the error.
"""

def error_message_detail(error,error_details:sys):
     _,_,exc_tb=error_details.exc_info()  #when the command runs, a tuple is received. We only want details hence we discard other two.
     filename=exc_tb.tb_frame.f_code.co_filename  #store the filename in variable
     error_message="error occured! File name is [{0}] and line number is [{1}], error is [{2}]".format(
     filename,exc_tb.tb_lineno,str(error))

     return error_message



class SensorException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)

        self.error_message=error_message_detail(error_message,error_details=error_details)

    def __str__(self):
        return self.error_message

