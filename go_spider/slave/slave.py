# coding=utf-8

"""
    监听队列
    解析任务
    调爬虫
"""

import time
from spider.routing_table import switcher
from utils import json_parse, json_dump
from middleware.middleware import listen_queue
from middleware.middleware import push_msg_2_queue


# config
task_queue = 'task'
html_queue = 'html'

def run():
    # 监听队列
    while True:
        msg = listen_queue(task_queue)
        if msg:
            next_msg = deal_msg(msg)
            # 拿到数据后，推入html队列
            push_msg_2_queue(html_queue, next_msg)
        else:
            time.sleep(0.1)
            continue


# 处理消息
def deal_msg(msg):
    # 处理消息
    # 找到任务名
    # 参数
    msg_dict = json_parse(msg)
    task_name = msg_dict.get('task')
    args = msg_dict.get('args', None)
    func = switcher.get(task_name)
    html = func(args)
    next_msg = {"task": task_name, "content": html}
    return json_dump(next_msg)


if __name__ == '__main__':
    run()