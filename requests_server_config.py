# coding=utf8

"""
该文件作为 requests_api的配置文件

    作为 api 返回的数据结构为

    response = {
        "status_code": 200,     # 服务器状态码
        ”content“: "xxxx",      # 返回html/json/xml等等
    }
"""

from __future__ import absolute_import
import os
import logging

os.chdir(os.path.split(os.path.abspath(__file__))[0])

# 请求模块日志
logging.basicConfig(level=logging.INFO,   # requests库会自动写入debug,故将level设置为 INFO
                    filename='requests_server.log',
                    datefmt='%Y/%m%d %H:%M:%S',
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

# 代理

proxy = {
        "http": "http://HUICU80ZV6SK58WP:21CE6FB2A2AE49B0@proxy.abuyun.com:9010",
        "https": "http://HUICU80ZV6SK58WP:21CE6FB2A2AE49B0@proxy.abuyun.com:9010",
    }

# 重试次数我

retry = 5

# 请求间隔睡眠时间

r_sleep = 2

# 网页编码

ec_u = 'utf8'

ec_g = 'gbk'