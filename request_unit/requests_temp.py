# coding=utf8

__author__ = 'wangjiawei'

"""
2018-02-24 开始开发请求模块，配合错误处理
2018-02-26 各模块编写
"""

import requests
from faker import Faker
# from request_unit.deal_error import

class RequestMainModel(object):
    """作为请求模块的的父类"""
    def __init__(self):
        pass

class HeadersAPI(object):
    """
    作为请求头处理的模块
    同时提供api，针对不同的请求拿出不同的headers
    从基础headers中提封装供相应的headers
    """

    def headers_api(self, **kwargs):
        """
        作为外部接口，知道调用谁的headers
        然后并封装返回
        :return:
        """
        headers = {}
        headers = self._headers_engine(kwargs.get('domain'), kwargs.get('data_type'))
        # 也可以先返回一个dict再去封装，减少内存的利用
        return headers

    def _headers_engine(self, domain, data_type):
        """
        headers引擎，作用是封装好一个可提供给爬虫执行的headers
        :param domain:
        :return:
        """
        headers = self._base_headers()
        # 搭建好基类的headers，（也可以设计到定制），然后按照定制化请求头
        if data_type == 'str':
            """字符串类型的数据定制的头"""
            pass
        elif data_type == 'json':
            """json类型定制的头"""
            pass
        elif data_type == 'xml':
            """xml类型的定制头"""
            pass
        # 2.拼接一个host字段
        headers['host'] = self._headers_host(domain)
        # 3. 定制请求头,针对不同的网站，定制不同的头

        # 4. 是否需要多个UA
        headers['User-Agent'] = self._ua_maker()
        return headers

    def _base_headers(self):
        """
        把headers基类返回给headers
        :return:
        """
        base = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        }
        return base

    def _headers_host(self, domain):
        """
        这里返回一个 host字段
        ** 具体怎么实现，有的website需要的host字段有变化
        :param domain:
        :return:
        """
        host = 'www.{}.com'.format(domain)
        return host

    def _ua_maker(self):
        return Faker().user_agent()

    def _xx_maker(self):
        """
        针对不同的网站或者网页，定制请求头
        与其是定制，其实是把提前设置好的请求头找到，并放进去
        :return:
        """
        pass

class RequestsAPI(object):
    """
    执行请求的模块
    提供api，完成请求这个动作
    """

    def request_api(self, data):
        """
        外部接口
        接受请求，同时调用引擎，最后返回结果
        :return:
        """

        # 1. 接口被调用，找到引擎，告诉引擎执行类型
        # 2. 接受返回结果，该接口调用结束

        # 传入的数据结构也要确定
        result = self._request_engine(data)
        return result

    def _request_engine(self, data):
        """
        request引擎
        负责从request_api那获取请求任务，并解析，执行任务
        :return:
        """
        # 1.先解析是GET任务还是POST任务
        method = data.get('method')
        if method == 'GET':
            # get请求的处理逻辑
            data = self._get_method(data)
        elif method == 'POST':
            # post请求的处理逻辑
            pass
        else:
            # 针对 option/put/delete的处理逻辑
            pass
        return data

    def _deal_request_method(self):
        """
        选择器，调用不同的方法

        这个模块暂时不需要，取消掉， 通过 engine就可以完成，后续需要封装，再启用
        :return:
        """
        pass

    def _get_method(self, data):
        """
        GET请求模块
        :return:
        """
        if not data.get('params', '') == '':
            response = requests.get(data.get('url'), headers=data.get('headers'), params=data.get('params'))
        else:
            response = requests.get(data.get('url'), headers=data.get('headers'))
        data['html'] = response.content.decode('utf8')
        data['status_code'] = response.status_code
        data['cookies'] = response.cookies
        return data

    def _post_method(self):
        """
        POST请求模块
        :return:
        """
        pass

class CookieAPI(object):
    """
    执行cookie处理的模块
    提供api，完成cookie处理/加载的动作
    """
    pass

class ProxyPoolAPI(object):
    """
    代理池开关
    针对请求中是否需要代理，从而机动的判断
    """
    pass

class StatusCodeHandle(object):
    """
    作为一个控制模块，通过处理状态码，告诉主模块流程执行状态
    code：200 则进行下一步
    code：300 相应处理
    code：4xx 相应处理
    """
    pass

class ErrorHandlerAPI(object):
    """
    错误处理的
    集合可能出现的错误，并提供相应的API
    """
    pass

class RequestModelAPI(object):
    """
    向外部提供的一个api,作为对这个模块的条用，接收参数，预处理
    1. 判断是什么请求
    2. 处理参数 不仅是 params和payloads

    """
    pass

if __name__ == '__main__':
    test_data1 = {
        'method': 'GET',
        'domain': 'baidu',
        'data_type': 'str',
        'multi_ua': 'yes',
        'headers': '',
        'referer': '',
        'url': 'http://www.baidu.com',
        'params': '',
        'payloads': '',
        'html': '',
        'status_code': '',
        'error_info': '',
        'cookies': '',
    }
    test_data2 = {
        'method': 'POST',
        'headers': '',
        'domain': 'baidu',
        'data_type': 'str',
        'multi_ua': 'yes',
        'referer': '',
        'params': '',
        'payloads': '',
        'url': 'http://www.baidu.com',
        'html': '',
        'status_code': '',
        'cookies': ''
    }
    baidu_headers = {}
    h_api = HeadersAPI()
    r_api = RequestsAPI()
    headers = h_api.headers_api(domain=test_data1.get('domain'), data_type=test_data1.get('data_type'))
    test_data1['headers'] = headers
    result = r_api.request_api(test_data1)
    print(result)