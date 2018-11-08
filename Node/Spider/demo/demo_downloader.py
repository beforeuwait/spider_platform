# coding=utf8


from redis import StrictRedis


class MsgCenter():

    def connect_redis(self):
        try:
            redis_cli = StrictRedis(host='loacalhost', port=6379, db=1)
        except:
            print('链接	Redis	失败....')
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

    

# 这是请求模块的通信代码
# 下载器接受任务，请求头啊，cookie提前配置好了的
# 直接完成一次请求

que_in = 'demo_downin'
que_out = 'demo_downout'


import time
from demo import Downloader

class Executor():
    """启动器

    - 种子生成器，接到反馈，生产种子
    - 下载器，接到种子，生产html
    - 解析器，接到html，解析url和data
    - 持久化存储，接到data，存储
    """

    def execute(self):
        # 监听队列
        sm = Downloader()

        mc = MsgCenter()

        while True:
            # 从队列获取数据
            msg = mc.receive_msg_from_que(que_in)
            if msg is not None:
                # 代表有消息来了
                # 执行
                html = sm.execute(msg)
                # 再推入队列
                if html is not None:
                    mc.push_msg_2_que(que_out, html)

            time.sleep(0.1)

