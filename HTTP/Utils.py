# coding=utf8

"""
    定义一些常见的处理
    以及
    自定义异常
"""

import logging

def check_params(params):
    """检查参数是否为dict"""
    if not isinstance(params, dict):
        raise InputParamsError


class InputParamsError(Exception):
    
    def __str__(self):
        return '当前传入参数不是dict格式，请检查...'

# 定义个过滤器
class RequestFilter(logging.Filter):
    """这是一个过滤request_log的过滤器
    """

    def filter(self, record):
        result = False
        try:
            filter_key = record.isRequest
        except AttributeError:
            filter_key = 'error_record'

        if filter_key == 'notRequestLog':
            result = True
        return result

