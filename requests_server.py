# coding=utf8

"""
    author = wangjiawei
    start_date = 2018/07/04

    change log:
    2018/07/04: 开始造轮子，开始构思
"""

import requests
import time
import requests_server_config as cf

class GeneralRequestServer():
    """正经的请求模块

    作为通用的请求模块，将请求服务转换为提供api

    满足通常来说的 GET/POST/PUT/DELETE 请求外
    针对不同的协议比如 http/1.1 http/1.0 以及 http/2 都有良好的支撑
    """

    def __init__(self):
        self.__session = requests.session()
        self.__response = None

    def __GET_request(self, url, params):
        """get请求的发起者
        因为存在状态码的处理，请求是不允许跳转的
        """
        response = self.__session.get(url, 
                                    params=params, 
                                    proxies=cf.proxy,
                                    allow_redirects=False, 
                                    timeout=30) \
            if params != {} \
            else self.__session.get(url, 
                                    proxies=cf.proxy, 
                                    allow_redirects=False, 
                                    timeout=30)
        return response

    def __status_code_handler(self):
        """用来处理返回状态码

        200-300 正常请求，如何处理
        300-400 跳转，如何处理
        400-500 客户端的错误，如何处理
        >500    服务端的错误，如何处理
        """
        status_code = self.__response.status_code
        if status_code < 300:
            return True
        else:
            return False

    def __circle_request(self, url, params):
        """循环模块"""
        retry = cf.retry
        html = 'none_page'
        while retry > 0:
            try:
                self.__response = self.__GET_request(url, params)

            except Exception as e:
                cf.logger.info('http error, url: {0}, info:{1}'.format(url, e))
            else:
                right_code = self.__status_code_handler()
                if right_code:

                    html = self.__response.content.decode(cf.ec_u)

                    break
                else:
                    time.sleep(cf.r_sleep)
                    continue
            retry -= 1
        return html

    def request_api(self, **kwargs):
        """获取外部调用，解析出url，headers，params等等

        **目前是简版**
        """
        url = kwargs.get('url')
        headers = kwargs.get('headers')
        method = kwargs.get('method')
        payloads = kwargs.get('payloads', {})
        params = kwargs.get('params', {})
        payloads_type = kwargs.get('payloads_type', 'dict')
        if method == 'GET':
            # 这是个get请求
            html = self.__circle_request(url, params)
        elif method == 'POST':
            # 这是个post请求
            html = ''
        else:
            # 别的请求
            html = ''
        return html

    def __update_headers(self, headers):

        self.__session.headers.update(headers)

        return

    def __update_cookie(self):
        """更新cookie"""

        try:
            self.__session.cookies.update(self.__response.cookies)
        except Exception as e:
            cf.logger.warning('cookie更新失败, 说明当前请求无效\t {0}'.format(e))
        return

    def __update_other_cookie(self, cookie):
        try:
            self.__session.cookies.update(cookie)
        except:
            cf.logger.warning('外部cookie更新无效')

    def __close_session(self):
        """关闭session"""
        self.__session.close()
        return

    def __delete_cookie(self):
        """删除cookie"""

        try:
            del self.__session.cookies
        except:
            pass

        return

if __name__ == '__main__':
    rsa = GeneralRequestServer()
    