# coding=utf8

"""
    author: wangjiawei
    date: 2018/07/09

    TODO LIST:
    1. RequestServer
    2. APIServer
    3. Util
    4. execute
"""
import requests
import requests_server_config as scf


class RequestServer():
    """请求模块
    负责 GET、POST、PUT、DELETE等请求
    session 应该传入，此处负责请求，不应该在此处创建session
    """

    def __init__(self, session, method, payloads):
        """
        session: Session
        url: 请求url
        method: 请求方式
        payloads: 请求参数
        """
        self.s = session
        self.m = method
        self.p = payloads

    def GET_request(self):
        """负责GET请求"""
        pass

    def POST_request(self):
        """负责POST请求"""
        pass
    
    def PUT_request(self):
        """负责PUT请求"""
        pass
    
    def DELETE_request(self):
        """负责DELETE请求"""
        pass
    
    def request_main(self):
        """执行请求的主体
        重试次数
        返回响应
        """
        pass
