# coding=utf-8

"""
请求模块

重写的目的是，增加灵活，减少引用时的重写

"""
import chardet
import config
import requests
from copy import deepcopy
from session_handler import SessionHandler

# type

_switcher = dict

class DealRequest:

    def __init__(self):
        self.session = requests.session()
        self.sh = SessionHandler(self.session)

    def do_GET(self, url, params, payloads) -> tuple:
        """完成get请求"""
        html = 'null_html'
        status_code = 0
        try:
            response = self.session.get(url=url, params=params, allow_redirects=False, timeout=30)
        except:
            pass
        else:
            # 请求成功
            status_code = response.status_code
            # 拿到编码
            page_code = chardet.detect(response.content).get('encoding')
            html = response.content.decode('utf-8') if page_code == 'utf-8' else response.content.decode('gbk')

        return html, status_code

    def do_POST(self, **kwargs):
        """完成POST请求"""
        pass

    def switcher(self) -> _switcher:
        """返回一个选择器"""
        return {'GET': self.do_GET,
                'POST': self.do_POST}

    def do_request(self, **kwargs):
        """接受参数，完成请求"""
        # RETRY
        retry = deepcopy(config.retry)
        html = 'null_html'
        status_code = 0

        method = kwargs.get('method')
        url = kwargs.get('url')
        headers = kwargs.get('headers')
        cookies = kwargs.get('cookies')
        params = kwargs.get('params')
        payloads = kwargs.get('payloads')
        # 请求放大写
        method = method.upper()
        # 组织部分
        # 更新请求头
        self.sh.update_cookie_headers_params(('headers', headers))
        # 更新cookie
        if cookies:
            self.sh.update_cookie_headers_params(('cookies', cookies))
        # 执行请求
        while retry > 0:
            html, status_code = self.switcher().get(method)(url=url, params=params, payloads=payloads)
            is_go_on = self.deal_response(status_code)
            if status_code != 0 and is_go_on:
                # 说明刚刚的请求失败
                break
            else:
                # 这里可以休息一下，再次访问
                continue
        return html, status_code

    def deal_response(self, status_code):
        """为了方便重写
        往后只需要重构此部分
        针对 302的情况
        针对 301的情况
        针对 400 + 的情况
        针对 500 + 的情况
        """
        is_go_on = False
        if status_code < 300:
            # 请求通过
            is_go_on = True
        return is_go_on