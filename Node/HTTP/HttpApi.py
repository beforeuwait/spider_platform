# coding=utf8

"""
外部引用的api
"""


from request_model import DealRequest

# type
_html = str
_status_code = int

class HttpApi:

    def __init__(self) -> None:
        self.dr = DealRequest()

    def receive_and_request(self, **kwargs) -> _html:
        """
        接受参数，这里要检查method
        :param kwargs:
        :return:
        """

        method = kwargs.get('method')
        url = kwargs.get('url')
        headers = kwargs.get('headers')
        cookies = kwargs.get('cookies')
        params = kwargs.get('params')
        payloads = kwargs.get('payloads')
        html, statuscode = self.dr.do_request(method=method,
                                              url=url,
                                              headers=headers,
                                              cookies=cookies,
                                              params=params,
                                              payloads=payloads,
                                              redirect=False)
        return html

    def user_define_request(self, **kwargs):
        """这个方法的意义在于用户自己去设计请求过程
        一般登录啊
        绕过js啊
        。。。
        都这这里自己定义
        """
        pass
