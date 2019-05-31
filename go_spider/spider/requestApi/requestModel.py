# coding=utf-8


import time
import random
import requests
from copy import deepcopy
from .config import retry
from .config import sleep_w
from .loggerHandler import logger, filter_dict


class RequestModel:

    def __init__(self):
        self.session = requests.Session()

    def run(self, url, headers, is_proxy, method, is_byte, is_verify, params=None, payloads=None, cookies=None,
            code=None):
        # receive parameters
        # then choose func to execute
        rty = deepcopy(retry)
        html = 'null_html'
        while rty > 0:
            try:
                response = self.sub_switch().get(is_proxy).get(method)(url=url, headers=headers, params=params,
                                                                       payloads=payloads, is_verify=is_verify,
                                                                       cookies=cookies)
                status_code = response.status_code
                if self.deal_state_code(status_code):
                    if code and not is_byte:
                        html = response.content.decode(code)
                    elif not (is_byte, code):
                        html = response.text
                    else:
                        html = response.content
                    break
            except Exception as e:
                logger.warning('请求过程中出错:\t{0}'.format(e), extra=filter_dict)
                time.sleep(random.choice(sleep_w))
            rty -= 1
        return html

    def get_request_proxy(self, *args, **kwargs):
        # do get request with proxy in request way
        pass

    def post_request_proxy(self, *args, **kwargs):
        # do post request with proxy in request way
        pass

    def get_request_no_proxy(self, *args, **kwargs):
        # do get request without proxy in request way
        pass

    def post_request_no_proxy(self, *args, **kwargs):
        # do post request without proxy in request way
        pass

    def get_session_proxy(self, *args, **kwargs):
        # do get request with proxy in session way
        pass

    def post_session_proxy(self, *args, **kwargs):
        # do post request with proxy in session way
        pass

    def get_session_no_proxy(self, *args, **kwargs):
        # do get request without proxy in session way
        pass

    def post_session_no_proxy(self, *args, **kwargs):
        # do post request without proxy in session
        pass

    def get_session_cookie(self):
        # return cookie
        return self.session.cookies.items()

    @staticmethod
    def deal_state_code(state_code):
        # 特殊情况
        # 自行重构
        if state_code < 300:
            return True
        else:
            return False

    def switcher(self):
        return {
            # request with session
            'yes': {
                # request with proxy
                'yes': {
                    'get': self.get_session_proxy,
                    'post': self.post_session_proxy,
                },
                # request without proxy
                'no': {
                    'get': self.get_session_no_proxy,
                    'post': self.post_session_no_proxy
                }
            },
            # request with out session
            'no': {
                # with proxy
                'yes': {
                    'get': self.get_request_proxy,
                    'post': self.post_request_proxy
                },
                # without proxy
                'no': {
                    'get': self.get_request_no_proxy,
                    'post': self.post_session_no_proxy
                }
            }
        }

    def sub_switch(self):
        # choose func to execute
        pass

    def cookies_handler(self, cookies):
        # deal cookie
        pass

    def headers_handler(self, session):
        # deal headers
        # like change the referer
        # like change the user_agent
        # even add/delete parameter
        # user define it
        pass
