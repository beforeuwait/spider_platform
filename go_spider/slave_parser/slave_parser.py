# coding=utf-8

"""
    从消息队列里获取html数据
    消息格式: {
                'url': 'https://wwww.xxxx.com?d=1&d=2',
                'content': 'xxxxxxxxxxxxxxxxxxxxxx'
                }
    解析数据放入持久化队列
    传入时候，需要携带 源 url
    解析新的url 并通过bloomfilter验证放入新队列

    todo:
        1. 从各个项目导入解析模块
        2. 连接redis 监听html 队列
        3. 调用对应解析模块，完成解析
        4. 将数据放入 data 队列， 同时将原url，新url放入bloom filter 里

"""
import time
from spider.routing_table import switcher
from utils import json_parse, json_dump
from middleware.middleware import listen_queue

# config
que = 'html'


def statistic_run_time(fun):

    def executor(*args):
        start = time.time()
        data = fun(*args)
        end = time.time()
        run_time = end-start
        # todo: 记录执行时间
        return data
    return executor


def run():
    # 监听队列
    while True:
        msg = listen_queue(que)
        if msg:
            # 执行相应模块
            pass
        else:
            continue
            time.sleep(0.1)


@statistic_run_time
def parse_msg(msg):
    # 将msg解析，并调用相应的模块执行
    # 在spider目录下维护一份路由表
    msg_dict = json_parse(msg)
    # 在msg_dict 拿到编码，调用switcher，并执行函数
    # 执行完毕，返回的json 有data字段， url， new url字段
    # 构造url不在 普通的url和api 的区别


