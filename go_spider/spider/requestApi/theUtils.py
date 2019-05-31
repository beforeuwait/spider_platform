# coding=utf-8

"""
import time
import random
from importlib import reload
import requestApi.config as cnf
from copy import deepcopy
from .loggerHandler import logger, filter_dict


def do_cycle_request(fun):

    def do_request(url, headers, params, payloads, cookies, code):
        html = 'null_html'
        reload(cnf)
        retryc = deepcopy(cnf.retry)
        while retryc > 0:
            try:
                html = fun(
                           url=url,
                           headers=headers,
                           params=params,
                           payloads=payloads,
                           cookies=cookies,
                           code=code)
                if html != 'null_html':
                    break
            except Exception as e:
                logger.warning('请求过程中出错:\t{0}'.format(e), extra=filter_dict)
                time.sleep(random.choice(cnf.sleep_w))
            retryc -= 1
        return html

    return do_request
"""

