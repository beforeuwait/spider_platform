# coding=utf-8


import os
import redis
import logging
from MsgCenter.config import redis_conf


# type
_cli = object

# logging模块
logger = logging.getLogger(name='MsgCenter')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(os.path.join(os.path.split(__file__)[0], './messageCenter_log.log'))
fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(fmt)
logger.addHandler(handler)


# redis的基础部分
def connect_redis() -> _cli:
    """连接到redis"""
    cli = None
    try:
        cli = redis.StrictRedis(host=redis_conf.get('host'),
                                port=redis_conf.get('port'),
                                db=redis_conf.get('db'))
    except Exception as e:
        logger.warning('链接Redis失败\t{0}'.format(e))
    return cli

