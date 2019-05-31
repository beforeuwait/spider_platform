# coding=utf-8

"""define some exception"""
from .loggerHandler import logger, filter_dict

class MethodError(Exception):
    

    def __str__(self):
        logger.warning('none Method input', extra=filter_dict)
        return 'none Method, send a method'

class MethodChoiceError(Exception):
    

    def __str__(self):
        logger.warning('wrong Method Choice input', extra=filter_dict)
        return 'wrong Method, only accept get post'


class IsProxyError(Exception):
    

    def __str__(self):
        logger.warning('wrong Proxy express input', extra=filter_dict)
        return 'wrong Proxy express, only accept yes/no'

class IsSessionError(Exception):
    

    def __str__(self):
        logger.warning('wrong Session express input', extra=filter_dict)
        return 'wrong Session express, on accept yes/no'


class ParametersError(Exception):


    def __str__(self):
        logger.warning('wrong parameters input', extra=filter_dict)
        return 'wrong parameters, check it that accept Dict type params'