# coding=utf8

__auther_ = 'wangjiawei'

"""
作为请求模块的存在
状态码:
1XX（信息类）该类型状态码表示接收到请求并且继续处理。
    100，客户端必须继续发出请求。
    101，客户端要求服务器根据请求转换HTTP协议版本。
2XX（响应成功）该类型状态码表示动作被成功接收、理解和接受。
    200，表明该请求被成功地完成，所请求的资源发送到客户端。
    201，提示知道新文件的URL。
    202，接受并处理，但处理未完成。
    203，返回信息不确定或不完整。
    204，收到请求，但返回信息为空。
    205，服务器完成了请求，用户必须复位当前已经浏览过的文件。
    206，服务器已经完成了部分用户的GET请求。
3XX（重定向类）该类型状态码表示为了完成指定的动作，必须接受进一步处理。
    300，请求的资源可在多处获得。
    301，本网页被永久性转移到另一个URL。
    302，请求的网页被重定向到新的地址。
    303，建议用户访问其他URL或访问方式。
    304，自从上次请求后，请求的网页未修改过。
    305，请求的资源必须从服务器指定的地址获得。
    306，前一版本HTTP中使用的代码，现已不再使用。
    307，声明请求的资源临时性删除。
4XX（客户端错误类）该类型状态码表示请求包含错误语法或不能正确执行。
    400，客户端请求有语法错误。
    401，请求未经授权。
    402，保留有效ChargeTo头响应。
    403，禁止访问，服务器收到请求，但拒绝提供服务。
    404，可连接服务器，但服务器无法取得所请求的网页，请求资源不存在。
    405，用户在Request-Line字段定义的方法不被允许。
    406，根据用户发送的Accept，请求资源不可访问。
    407，类似401，用户必须首先在代理服务器上取得授权。
    408，客户端没有在用户指定的时间内完成请求。
    409，对当前资源状态，请求不能完成。
    410，服务器上不再有此资源。
    411，服务器拒绝用户定义的Content-Length属性请求。
    412，一个或多个请求头字段在当前请求中错误。
    413，请求的资源大于服务器允许的大小。
    414，请求的资源URL长于服务器允许的长度。
    415，请求资源不支持请求项目格式。
    416，请求中包含Range请求头字段，在当前请求资源范围内没有range指示值。
    417，服务器不满足请求Expect头字段指定的期望值。
5XX（服务器错误类）该类型状态码表示服务器或网关错误。
    500，服务器错误。
    501，服务器不支持请求的功能。
    502，网关错误。
    503，无法获得服务。
    504，网关超时。
    505，不支持的http版本。
"""


import requests
# 仍旧需要一个独立的log模块
requests.session()

class getModule:
    """
    这里作为 GET 请求执行模块
    1. api调用此类，完成请求
    2. 要完成请求的过程
    3. 异常输出在log里
    """

    def __get_without_params(self, **kwargs):
        """
        作为没有参数的 GET 请求
        1. 参数需要 url, headers, cookies, allow_redirects, proxies, decode
        2. 模仿requests源码里 将allow_redirects 的值为 True, 如果有需要将其设置为False
        3. 处理status_code,按照不同对类型做相应对处理
        4. 重试对次数为5
        """
        kwargs.setdefault('allow_redirects', True)
        kwargs.setdefault('decode', 'utf-8')
        response = connfig.response_error
        retry = connfig.request_retry_times
        while retry > 0:
            try:
                res = requests.get(
                    kwargs.get('url'),
                    headers=kwargs.get('headers'),
                    cookies=kwargs.get('cookies'),
                    allow_redirects=kwargs.get('allow_redirects'),
                    proxies=kwargs.get('proxies'),
                    timeout=connfig.timeout
                )
                # 这里部分对返回值做处理
                status_code = res.status_code
                if repr(status_code).startswith('2'):
                    """状态码为 2xx 时候的处理方法,直接返回html"""
                    try:
                        response = res.content.decode(kwargs.get('decode'))
                    except Exception as e:
                        logging.debug('该网页不支持 %s 格式, %s' % (kwargs.get('decode'), e))
                        response = res.text
                    break
                elif repr(status_code).startswith('3'):
                    """
                    状态码为 3xx 时候的处理方法，只有在默认 allow_redirects=True时候才会出现
                    目前的处理思路为遇到重定向，将 allow_redirects=False 再次请求
                    """
                    kwargs['allow_redirects'] = False
                    logging.info('在请求 %s 时,返回 status_code:%s,将不允许重定向' % (kwargs.get('url'), status_code))

                    continue
                elif repr(status_code).startswith('4'):
                    """
                    状态码为 4xx 时候处理方法，都4xx了，明确是被ban或者是网络都原因
                    目前的处理方法就是 
                            1.有代理的情况下，更改代理ip地址，再请求
                            2.没有代理，那直接跳过
                    """
                    if kwargs.get('proxies'):
                        kwargs.get('headers')['Proxy-Switch-Ip'] = 'yes'
                        continue
                    else:
                        logging.info('在请求 %s 时,返回 status_code:%s' % (kwargs.get('url'), status_code))
                        break
                elif repr(status_code).startswith('5'):
                    """
                    状态码为 5xx 时候处理方法，5xx 服务器的内部错误
                    暂时的处理方法,同 4xx 无代理一致
                    """
                    break
            except Exception as e:
                logging.info('请求过程中出错,%s' % e)
                response = connfig.response_error
            retry -= 1
        return response

    def __get_with_params(self, **kwargs):
        """
        作为有参数的 GET 请求
        1. 参数需要 url, headers, cookies, params, allow_redirects, proxies, decode
        2. 模仿requests源码里 将allow_redirects 的值为 True, 如果有需要将其设置为False
        3. 处理status_code,按照不同对类型做相应对处理
        4. 重试对次数为5
        """
        kwargs.setdefault('allow_redirects', True)
        kwargs.setdefault('decode', 'utf-8')
        response = connfig.response_error
        retry = connfig.request_retry_times
        while retry > 0:
            try:
                res = requests.get(
                    kwargs.get('url'),
                    headers=kwargs.get('headers'),
                    cookies=kwargs.get('cookies'),
                    params=kwargs.get('params'),
                    allow_redirects=kwargs.get('allow_redirects'),
                    proxies=kwargs.get('proxies'),
                    timeout=connfig.timeout
                )
                # 这里部分对返回值做处理
                status_code = res.status_code
                if repr(status_code).startswith('2'):
                    """状态码为 2xx 时候的处理方法,直接返回html"""
                    try:
                        response = res.content.decode(kwargs.get('decode'))
                    except Exception as e:
                        logging.debug('该网页不支持 %s 格式, %s' % (kwargs.get('decode'), e))
                        response = res.text
                    break
                elif repr(status_code).startswith('3'):
                    """
                    状态码为 3xx 时候的处理方法，只有在默认 allow_redirects=True时候才会出现
                    目前的处理思路为遇到重定向，将 allow_redirects=False 再次请求
                    """
                    kwargs['allow_redirects'] = False
                    logging.info('在请求 %s 时,返回 status_code:%s,将不允许重定向' % (kwargs.get('url'), status_code))
                    continue
                elif repr(status_code).startswith('4'):
                    """
                    状态码为 4xx 时候处理方法，都4xx了，明确是被ban或者是网络都原因
                    目前的处理方法就是 
                            1.有代理的情况下，更改代理ip地址，再请求
                            2.没有代理，那直接跳过
                    """
                    if kwargs.get('proxies'):
                        kwargs.get('headers')['Proxy-Switch-Ip'] = 'yes'
                        continue
                    else:
                        logging.info('在请求 %s 时,返回 status_code:%s' % (kwargs.get('url'), status_code))
                        break
                elif repr(status_code).startswith('5'):
                    """
                    状态码为 5xx 时候处理方法，5xx 服务器的内部错误
                    暂时的处理方法,同 4xx 无代理一致
                    """
                    break
            except Exception as e:
                logging.info('请求过程中出错,%s' % e)
                response = connfig.response_error
            retry -= 1
        return response

    def response_status_code_parse(self, response):
        """
        返回response对象，然后通过 状态码的判断，从而相应的处理
        :param response: response 对象
        :return: 正常的html页面 或者 报错的结果
        """
        # 暂时没有思路去撸这个模块，仍旧先复杂再优化
        pass


class postModule:
    pass


class getAPI:
    pass


class postAPI:
    pass


class connfig:
    response_error = 'response_return_none'

    request_retry_times = 5

    timeout = 15
