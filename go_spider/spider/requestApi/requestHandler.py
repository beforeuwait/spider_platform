# coding=utf-8


import requests
from .requestModel import RequestModel
from .real_config import proxy_dyn
from .config import timeout


class RequestRequest(RequestModel):

    def __init__(self):
        super(RequestRequest, self).__init__()

    def get_request_proxy(self, url, headers, is_verify, params=None, payloads=None, cookies=None):

        return requests.get(url=url, headers=headers, params=params, cookies=cookies, verify=is_verify, proxies=proxy_dyn, timeout=timeout)

    def post_request_proxy(self, url, headers, is_verify, params=None, payloads=None, cookies=None):

        return requests.post(url=url, headers=headers, data=payloads, cookies=cookies, verify=is_verify, proxies=proxy_dyn, timeout=timeout)

    def get_request_no_proxy(self, url, headers, is_verify, params=None, payloads=None, cookies=None):

        return requests.get(url=url, headers=headers, params=params, verify=is_verify, cookies=cookies, timeout=timeout)

    def post_request_no_proxy(self, url, headers, is_verify, params=None, payloads=None, cookies=None):
        return requests.post(url=url, headers=headers, data=payloads, verify=is_verify, cookies=cookies, timeout=timeout)

    def sub_switch(self):
        return self.switcher().get('no')


class SessionRequest(RequestModel):

    def __init__(self):
        super(SessionRequest, self).__init__()

    def get_session_proxy(self, url, headers, is_verify, params=None, payloads=None, cookies=None):

        return self.session.get(url=url, headers=headers, params=params, cookies=cookies, verify=is_verify, proxies=proxy_dyn, timeout=timeout)

    def post_session_proxy(self, url, headers, is_verify, params=None, payloads=None, cookies=None):

        return self.session.post(url=url, headers=headers, data=payloads, cookies=cookies, verify=is_verify, proxies=proxy_dyn, timeout=timeout)

    def get_session_no_proxy(self, url, headers, is_verify, params=None, payloads=None, cookies=None):

        return self.session.get(url=url, headers=headers, params=params, verify=is_verify, cookies=cookies, timeout=timeout)

    def post_session_no_proxy(self, url, headers, is_verify, params=None, payloads=None, cookies=None):
        return self.session.post(url=url, headers=headers, data=payloads, verify=is_verify, cookies=cookies, timeout=timeout)

    def sub_switch(self):
        return self.switcher().get('yes')
