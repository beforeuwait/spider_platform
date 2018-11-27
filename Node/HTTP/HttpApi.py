# coding=utf8

"""
外部引用的api
"""


from request_model import DealRequest


class HttpApi(DealRequest):

    def __init__(self) -> None:
        super(HttpApi).__init__()

    # def receive_and_request_old(self, **kwargs):
    #     """接收参数
    #     处理参数
    #     选择请求方式
    #     默认是带代理的
    #     """
    #
    #     # 先获取参数， 目前就想了这么多
    #     url = kwargs.get('url')
    #     headers = kwargs.get('headers')
    #     method = kwargs.get('method')
    #     cookie = kwargs.get('cookie')
    #     params = kwargs.get('params')
    #     payloads = kwargs.get('payloads')
    #
    #     # 构建请求头
    #     self.update_headers(headers)
    #     if cookie is not None:
    #         self.update_cookie_with_outer(cookie)
    #
    #     # 开始请求
    #     html = self.do_request(url=url,
    #                            params=params,
    #                            method=method,
    #                            payloads=payloads)
    #     # 在通用的一次性请求里，到这里是要关闭session的
    #     # 清理cookie
    #     self.discard_cookies()
    #     self.close_session()
    #
    #     return html

    def receive_and_request(self, **kwargs):
        """
        接受参数，这里要检查method
        :param kwargs:
        :return:
        """

        method = kwargs.get('method')

        self.do_request(kwargs)

    def user_define_request(self, **kwargs):
        """这个方法的意义在于用户自己去设计请求过程
        一般登录啊
        绕过js啊
        。。。
        都这这里自己定义
        """
        pass


if __name__ == '__main__':
    api = HttpApi()
    api.receive_and_request(url='a', headers='b', method='get', cookies='c', params='d')