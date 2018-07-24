# coding=utf8

"""
    author: wangjiawei
    date: 2018/07/09

    TODO LIST:
    1. GeneralRequest
    2. RequestAPI
    3. test_unit
"""
import requests
import requests_server_config as scf
from requests_server_config import logger, filter_dict


class GeneralRequest():
    """请求模块
    
    承载了大部分功能
    """

    def __init__(self):
        # 初始化的时候就创建session,并带上proxy
        self.s = self.establish_session()
        self.update_proxy()
    
    def establish_session(self):
        """创建一个session

        session在笔者看来就是cookie管理
        使用session的目的在于，容易操作cookie
        """
        return requests.Session()
    
    def cloes_session(self):
        """关闭session

        针对页面跳转，会出现打开新的session，
        当前的session也应该相应的关闭
        关闭所有adapter(适配器) such as the session
        """
        self.s.close()
        return 

    def GET_request(self, url, params):
        """执行get请求

        首先是判断是否有参数
        默认是不允许跳转的
        """
        response = self.s.get(url, params=params, allow_redirects=False) \
                    if params is not None \
                    else self.s.get(url, allow_redirects=False)

        return response

    def POST_request(self, url, payloads):
        """执行post请求

        默认是不允许跳转的
        """

        response = self.s.post(url, data=payloads)

        return response
    
    def OTHER_request(self):
        """执行别的请求，后期添加
        
        接口留在这,比如 put, delete等
        """
        pass
    
    def update_cookie_with_response(self, cookie):
        """通过response这个对象去更新cookie

        **这里一个强制性的要求就是，请求后，更新cookie**

        这里需要关注，当请求的response是无效的
        更新cookie时候会报错，这里需要一个错误提示
        """
        try:
            self.s.cookies.update(cookie)
        except:
            # TODO 这里做一个日志输出
            logger.info("response更新cookie数据失败,可能请求失败", extra=filter_dict)
    
    def update_cookie_with_outer(self, cookies):
        """通过外部加载去更新cookie
        通常使用场景
        1. 带cookie绕过服务器验证
        2. 带cookie模仿用户去请求数据
        """

        self.s.cookies.update(cookies)
        return

    
    def update_headers(self, params):
        """通过外部传入headers更新自身的headers

        可以是更新headers里的某一个字段
        也可以是更新headers里的全部

        执行之前应该先把其session.headers.clear()
        """

        self.s.headers.clear()
        self.s.headers.update(params)
        return
    
    def update_proxy(self):
        """这个在默认的状态下是要携带代理的
        可以指定情况，不要代理
        """
        proxy = scf.proxy
        self.s.proxies.update(proxy)
        return
    
    def discard_proxy(self):
        """因为在默认的状态下，session是携带proxy了的
        该function就是在当前实例中取消代理
        """

        self.s.proxies.clear()
        return
    
    def discard_cookies(self):
        """discard all cookies
        删除/扔掉 所有cookie
        """
        self.s.cookies.clear_session_cookies()
        return

    def do_request(self, url, method, params, payloads):
        """根据指定的请求方式去请求"""
        retry = scf.retry
        html = 'null_html'
        while retry > 0:
            response = None
            is_go_on = False
            try:
                # TODO 选择执行的方式
                if method == 'GET':
                    response = self.GET_request(url, params)

                elif method == 'POST':

                    response = self.POST_request(url, payloads)                 
            except:
                # 输出log, 这里的错误都是网络上的错误
                logger.info('请求出错, 错误原因:', exc_info=True, extra=filter_dict)
            
            # 拿到response后，处理 
            if response is not None:
                status_code = response.status_code
                is_go_on = self.deal_status_code(status_code)

                # 更新cookie
                self.update_cookie_with_response(response.cookies)

            if is_go_on:
                # 返回html
                try:
                    html = response.content.decode(scf.ec_u)
                except:
                    html = response.text
                break
            retry -= 1

        return html 
            

    def deal_status_code(self, status_code):
        """这个方法的意义在于服务器相应后，针对相应内容做处理

        2xx: 200是正常， 203正常响应，但是返回别的东西
        3xx: 重定向，在请求中已经规避了这部分
        4xx: 客户端错误
        5xx: 服务器错误
        """
        result = True
        if status_code >= 300 or status_code == 203:
            result = False
            # TODO: 添加logging
            logger.info('请求出现状态码异常:\t{0}'.format(status_code), extra=filter_dict)
        return result

        
class RequestAPI(GeneralRequest):
    """这个类作为外部调用的api
    功能：
    """

    def __init__(self):
        # 实例化GeneralRequest 准备请求
        super(RequestAPI, self).__init__()

    def receive_and_request(self, **kwargs):
        """接收参数
        处理参数
        选择请求方式
        默认是带代理的
        """
        
        # 先获取参数， 目前就想了这么多
        url = kwargs.get('url')
        headers = kwargs.get('headers')
        method = kwargs.get('method')
        cookie = kwargs.get('cookie')
        params = kwargs.get('params')
        payloads = kwargs.get('payloads')
        
        # 构建请求头
        self.update_headers(headers)
        if cookie is not None:
            self.update_cookie_with_outer(cookie)

        # 开始请求
        html = self.do_request(url=url,
                                params=params, 
                                method=method, 
                                payloads=payloads)
        return html
    
    def user_define_request(self):
        """这个方法的意义在于用户自己去设计请求过程
        一般登录啊
        绕过js啊
        。。。
        都这这里自己定义
        """
        pass



def temp_test_unit():
    """测试该库
    
    test_1: 
        url = 'http://www.baidu.com'
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Host": "www.baidu.com",
            "Upgrade-Insecure-Requests": "1"
        }
    

    """
    url = 'http://www.baidu.com'
    headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Host": "www.baidu.com",
            "Upgrade-Insecure-Requests": "1"
        }
    api = RequestAPI()
    html = api.receive_and_request(url=url, headers=headers, method='GET')
    print(html)


if __name__ == '__main__':
    temp_test_unit()