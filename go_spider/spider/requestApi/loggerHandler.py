# coding=utf-8

import os
import logging


# logging部分
# 定义个过滤器
class RequestFilter(logging.Filter):
    """这是一个过滤request_log的过滤器
    """

    def filter(self, record):
        result = False
        try:
            filter_key = record.isRequest
        except AttributeError:
            filter_key = 'error_record'

        if filter_key == 'notRequestLog':
            result = True
        return result


logger = logging.getLogger(name='HTTP')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(os.path.join(os.path.split(__file__)[0], './http_log.log'))
fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(fmt)
logger.addHandler(handler)

# 添加过滤器
logger.addFilter(RequestFilter())

filter_dict = {"isRequest": "notRequestLog"}
