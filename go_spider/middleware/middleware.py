# coding=utf-8

"""中间件部分
定义，调用，配置都放到这个文件里
"""

from redis import StrictRedis

# config
host = '192.168.2.88'
port = 6379
db = 1
pwd = 'QWE123'


# 连接 redis
def connect_redis():
    return StrictRedis(host=host, port=port, db=db, password=pwd)


# 监听队列
def listen_queue(queue):
    # 无论抢到没抢到
    # msg一开始就为 None
    msg = None
    redis = connect_redis()
    if redis.exists(queue):
        msg = redis.rpop(queue)
    return msg


# 推数据进入队列
def push_msg_2_queue(queue, msg):
    cli = connect_redis()
    cli.lpush(queue, msg)