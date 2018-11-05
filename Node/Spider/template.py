# coding=utf-8

"""
    author = wangjiawei

    state:
    小程序的模板

    要求：
    启动程序后，同时告知监听和输出的消息队列

    模块内容，只根据提供的数据执行相应的操作
    负责和msgcenter沟通交由给相应的模块
"""

from redis import StrictRedis

# 加入导入的 demoSeed.py 的 demoSeed



# 先写好消息中心的代码

class MsgCenter():

    def connect_redis(self):
        try:
            redis_cli = StrictRedis(host='loacalhost', port=6379, db=1)
        except:
            print('链接\tRedis\t失败....')
            redis_cli = None
        return redis_cli

    def push_msg_2_que(self, que, msg):
        """将数据推入到指定的队列里

        :param que: 指定的队列
        :param msg: json格式的数据
        :return 是否成功推入数据
        """

        done = False
        redis_cli = self.connect_redis()
        if redis_cli is not None:
            redis_cli.lpush(que, msg)
            done = True
        return done

    def receive_msg_from_que(self, que):
        """从指定的队列里获取消息

        没有消息，就等候，
        :param que: 指定的队列
        :return: msg: 消息队列里的数据，没有则为None
        """

        msg = None
        redis_cli = self.connect_redis()
        if redis_cli is not None:
            msg = redis_cli.rpop(que)
            # 没有数据则为None
        return msg


# 执行部分，这次写一个seed 的demo

class DemoSeed():

    def execute(self):
        seed = 'test'
        return seed

seed_in = 'demo_seedin'

seed_out = 'demo_seedout'

import time

def execute():
    msgc = MsgCenter()
    sed = DemoSeed()


    while True:

        # 获取消息
        msg = msgc.receive_msg_from_que(seed_in)
        if msg is not None:
            # 获取种子
            seed = sed.execute()
            # 放入队列
            msgc.push_msg_2_que(seed_out, seed)
        else:
            time.sleep(0.1)
            continue

if __name__ == '__main__':
    execute()