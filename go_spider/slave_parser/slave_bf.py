# coding=utf-8

"""
date = 2019-06-04
    接受数据，然后去重
    重复则不推入 task队列
"""

import time
from utils import json_parse, json_dump
from slave_parser.bloom_fliter import BloomFilter
from middleware.middleware import listen_queue
from middleware.middleware import push_msg_2_queue


# config
que = 'bmf'
que_task = 'task'


def run():
    # 监听队列
    bf = BloomFilter()
    while True:
        msg = listen_queue(que)
        if msg:
            # 执行相应模块
            msg_dict = json_parse(msg)
            url = msg_dict.get('args')[1]
            if not bf.isContains(url):
                # 说明不存在
                # 推入task队列
                print('该url是new\t{0}'.format(url))
                bf.insert(url)
                push_msg_2_queue(que_task, msg)
        else:
            time.sleep(0.1)
            continue
