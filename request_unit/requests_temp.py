# coding=utf8

__author__ = 'wangjiawei'

"""
2018-02-24 开始开发请求模块，配合错误处理

"""

import requests

from request_unit.deal_error import

class RequestMainModel():
    """作为请求模块的的父类"""
    def __init__(self):
        pass

class HeadersAPI():
    """
    作为请求头处理的模块
    同时提供api，针对不同的请求拿出不同的headers
    从基础headers中提封装供相应的headers
    """

    def __init__(self):
        pass

class RequestsAPI():
    """
    执行请求的模块
    提供api，完成请求这个动作
    """

    def request_api(self):
        """
        外部接口
        :return:
        """
        pass

    def request_engine(self):
        """
        request引擎
        负责从request_api那获取请求任务，并解析，执行任务
        :return:
        """
        pass

    def deal_request_method(self):
        """
        选择器，调用不同的方法
        :return:
        """
        pass

    def get_method(self):
        """
        GET请求模块
        :return:
        """
        pass

    def post_method(self):
        """
        POST请求模块
        :return:
        """
        pass

class CookieAPI():
    """
    执行cookie处理的模块
    提供api，完成cookie处理/加载的动作
    """
    pass

class ProxyPoolAPI():
    """
    代理池开关
    针对请求中是否需要代理，从而机动的判断
    """
    pass

class StatusCodeHandle():
    """
    作为一个控制模块，通过处理状态码，告诉主模块流程执行状态
    code：200 则进行下一步
    code：300 相应处理
    code：4xx 相应处理
    """
    pass

class ErrorHandlerAPI():
    """
    错误处理的
    集合可能出现的错误，并提供相应的API
    """
    pass

class RequestModelAPI():
    """
    向外部提供的一个api,作为对这个模块的条用，接收参数，预处理
    1. 判断是什么请求
    2. 处理参数 不仅是 params和payloads

    """
    pass