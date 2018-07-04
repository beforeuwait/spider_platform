# coding=utf8

__author__ = 'wangjiawei'

"""
2018-02-24
"""

class RequestBaseError(Exception):
    """作为请求模块错误的提示"""

    def __init__(self, err):
        Exception.__init__(err)

