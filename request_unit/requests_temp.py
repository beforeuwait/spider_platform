# coding=utf8
from __future__ import absolute_import
__author__ = 'wangjiawei'

"""
先开发，暂不优化
2018-02-24 开始开发请求模块，配合错误处理
2018-02-26 各模块编写
2018-03-05 继续编写模块
2018-03-06 编辑模块， 关于 headers中referer的带法是个难题
"""
import requests
from faker import Faker
# from request_unit.deal_error import


class RequestMainModel(object):
    """作为请求模块的的父类
    主逻辑模块，调度headers cookie等各模块的逻辑
    从request_api 获取任务，然后执行相应的逻辑
    """
    def __init__(self):
        pass

class HeadersAPI(object):
    """作为请求头处理的模块
    同时提供api，针对不同的请求拿出不同的headers
    从基础headers中提封装供相应的headers
    """

    def headers_api(self, **kwargs):
        """作为外部接口，知道调用谁的headers
        然后并封装返回
        * 针对，以后的可能出现 http/2.0 的headers，在api这里做分流，配置不同的engine来达到效果
        :return:
        """
        headers = {}
        headers = self._headers_engine(kwargs.get('domain'), kwargs.get('data_type'))
        # 也可以先返回一个dict再去封装，减少内存的利用
        return headers

    def _headers_engine(self, domain, data_type):
        """headers引擎，作用是封装好一个可提供给爬虫执行的headers
        :param domain:
        :return:
        """

        #获取最初的headers
        headers = self._base_headers()
        # 搭建好基类的 base headers，（也可以设计到定制），然后按照定制化请求头
        if data_type == 'str':
            """
            字符串类型的数据定制的头,通常没有需要额外添加的部分
            """
            pass
        elif data_type == 'json':
            """
            json类型定制的头
            * 调用字典的update方法，这样的好处就是，更新自己的数据
            """
            headers.update(self._json_headers())
        elif data_type == 'xml':
            """
            xml类型的定制头，
            现阶段暂时未遇到，单纯一个json格式可以满足需求
            """
            pass

        # 2.拼接一个host字段
        headers['host'] = self._headers_host(domain)
        # 3. 定制请求头,针对不同的网站，定制不同的头

        # 4. 是否需要多个UA
        headers['User-Agent'] = self._ua_maker()
        return headers

    def _base_headers(self):
        """把headers基类返回给headers
        :return:
        """
        base = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
        }
        return base

    def _headers_host(self, domain):
        """这里返回一个 host字段
        ** 具体怎么实现，有的website需要的host字段有变化

        ** 03.07更行此处逻辑,domain这里需要一个list，针对统一网站不同项目的host不同，需要定制
           domain_list = {
                'ctrip_hotel': 'hotels.ctrip.com',
                'ctrip_scenic': 'piao.ctrip.com',
                ........
           }
        ** 至于http/2.0 的请求头又如何定制
        :param domain:
        :return:
        """
        domain_list = {
            'ctrip_hotel': 'hotels.ctrip.com',
            'ctrip_scenic': 'piao.ctrip.com',
            'dianping_food': 'www.dianping.com',
            'dianping_shopping': 'www.dianping.com',
            'ly_hotel': 'www.ly.com',
            'baidu': 'www.baidu.com'
        }
        host = '{0}'.format(domain_list.get(domain))
        return host

    def _headers_referer(self):
        """添加 referer 这个字段
        针对有的网站的反爬虫认证有关于确认referer这个字段
        因此我们需要定制一个添加referer的方法

        * 至于referer的带法，
        :return:
        """
        pass

    def _ua_maker(self):
        return Faker().user_agent()

    def _json_headers(self):
        """请求头关于json格式数据请求

        :return:
        """
        json_headers = {
            'Accept': 'application/json, text/javascript',
            'X-Request': 'JSON',
            'X-Requested-With': 'XMLHttpRequest',
        }
        return json_headers

    def _xx_maker(self):
        """针对不同的网站或者网页，定制请求头
        与其是定制，其实是把提前设置好的请求头找到，并放进去
        :return:
        """
        pass

class CookieAPI(object):
    """执行cookie处理的模块
    提供api，完成cookie处理/加载的动作
    """

    def cookie_switch(self, cookie_info):
        """
        作为筛选器，就是为其装备各种所需的cookie
        :param cookie_info:
        :return:
        """
        if cookie_info == 'baidu_tieba':
            return self.baidu_tieba()
        elif cookie_info == 'dianping_cmt':
            return None
        elif cookie_info == 'dianping_info':
            return None

    def baidu_tieba(self):
        cookie = {'Cookie': ('BAIDUID=00FDDFB865205E569DFB828760CE2DDE:'
                             'FG=1;'
                             ' BIDUPSID=00FDDFB865205E569DFB828760CE2DDE;'
                             ' PSTM=1519116523;'
                             ' BDUSS=DBXLWdUUHBUV2pOc0RpdDlyOE83QkJtcjNRUXRkM3pu'
                             'QzU2SWYzT1RpMXhZcmhhQVFBQUFBJCQAAAAAAAAAAAEAAADzyq'
                             'AYsK6z1LzQyfq3uQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
                             'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHVkFpx1ZBaT;'
                             ' TIEBA_USERTYPE=59831fa6e4e4c0875d0a49ab;'
                             ' STOKEN=8243706d62f9ba145342902ddecef4783d20e15e8616590c1bc77d10b91497ca;'
                             ' TIEBAUID=69b534f8e3a2ecdf0c852a15;'
                             ' bdshare_firstime=1519450995355;'
                             ' BDORZ=B490B5EBF6F3CD402E515D22BCDA1598;'
                             ' H_PS_PSSID=1444_21094;'
                             ' Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1519896519,1519956045,1520211218,1520387111;'
                             ' BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0;'
                             ' PSINO=3;'
                             ' Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1520405011')
                  }
        return cookie

class ProxyPoolAPI(object):
    """代理池开关
    针对请求中是否需要代理，从而机动的判断
    """
    pass

class StatusCodeHandle(object):
    """作为一个控制模块，通过处理状态码，告诉主模块流程执行状态
    code：200 则进行下一步
    code：300 相应处理
    code：4xx 相应处理
    """
    pass

class ErrorHandlerAPI(object):
    """错误处理的
    集合可能出现的错误，并提供相应的API
    """
    pass

class RequestsAPI(CookieAPI, StatusCodeHandle, ErrorHandlerAPI):
    """执行请求的模块
    提供api，完成请求这个动作
    """

    def request_api(self, data):
        """外部接口
        接受请求，同时调用引擎，最后返回结果
        * 暂时叫 data，想好了新的名字再确认
        *
        :return:
        """

        # 1. 接口被调用，找到引擎，告诉引擎执行类型
        # 2. 接受返回结果，该接口调用结束

        # 传入的数据结构也要确定

        # for k, v in data.items():
        #     print(k, v)
        result = self._request_engine(data)
        # return result

    def _request_engine(self, data):
        """request引擎
        负责从request_api那获取请求任务，并解析，执行任务
        :return:
        """
        # 1.先解析是GET任务还是POST任务
        method = data.get('method')
        # 2.根据解析的任务结果选择相应的请求处理方式
        # 在处理get/post 请求时候，除了登录等个别的对post要求严格的请求方式中
        # get/post是互通的

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
        """选择器，调用不同的方法

        这个模块暂时不需要，取消掉， 通过 engine就可以完成，后续需要封装，再启用
        :return:
        """
        pass

    def _get_method(self, data):
        """GET请求模块
        因为继承自 cookie ，status， error模块，这里就要有相应的cookie处理，反馈机制的status处理机制
        :return:
        """
        # cookie 的 switch
        cookies = {}
        if not data.get('cookie_info', '') == '':
            # 需要装载cookie
            cookies = self.cookie_switch(data.get('cookie_info'))
        # 带参数和不带参数的处理方法
        if not data.get('params', '') == '' and cookies == {}:
            response = requests.get(data.get('url'), headers=data.get('headers'), params=data.get('params'))
        elif not data.get('params', '') == '' and cookies != {}:
            response = requests.get(data.get('url'), headers=data.get('headers'), cookies=cookies, params=data.get('params'))
        elif data.get('params', '') == '' and cookies == {}:
            response = requests.get(data.get('url'), headers=data.get('headers'))
        else:
            response = requests.get(data.get('url'), headers=data.get('headers'), cookies=cookies)
        try:
            data['html'] = response.content.decode('utf8')
        except:
            # 编码出错的情况下
            data['html'] = response.content.decode('gbk')
        # 开始对status_code 处理， 这里的原则就是，200 通过，300无视，400/500处理
        data['status_code'] = response.status_code
        data['cookies'] = response.cookies
        return data

    def _post_method(self):
        """POST请求模块
        :return:
        """
        pass


class RequestModelAPI(object):
    """向外部提供的一个api,作为对这个模块的条用，接收参数，预处理
    1. 判断是什么请求
    2. 处理参数 不仅是 params和payloads

    """
    pass

if __name__ == '__main__':
    test_data1 = {
        'method': 'GET',
        'domain': 'baidu',
        'data_type': 'json',
        'multi_ua': 'yes',
        'headers': '',
        'referer': '',
        'url': 'http://www.baidu.com',
        'params': '',
        'payloads': '',
        'html': '',
        'status_code': '',
        'error_info': '',
        'cookie_info': 'baidu_tieba',
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
        'cookie_info': 'baidu_tieba'
    }
    baidu_headers = {}
    h_api = HeadersAPI()
    r_api = RequestsAPI()
    headers = h_api.headers_api(domain=test_data1.get('domain'), data_type=test_data1.get('data_type'))
    test_data1['headers'] = headers
    result = r_api.request_api(test_data1)
    print(result)
    # print(test_data1)