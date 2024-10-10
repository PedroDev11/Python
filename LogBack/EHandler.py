'''
Module for sending SMS message
'''
import requests
from urllib.error import HTTPError
import logging

class SmsConnectivityException(Exception):
    '''
    Custom exception for SMS service provider connectivity issues
    '''
    severity = 'warning'
    pass

def sms_send(*args, **kwargs) -> bool:
    '''
    Method to send SMS message
    '''
    try:
        result = requests.post(...)
        result.raise_for_status()
        return True
    except HTTPError as exception:
        # Propagate trace from HTTPError exception
        raise SmsConnectivityException() from exception
    
def exception_handler(exc):
    '''
    Custom exception handler to log exception with its defined severity
    '''
    getattr(logging, exc.severity)(exc)