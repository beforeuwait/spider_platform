# coding=utf-8


"""作为临时的slave，当时队列负载过高的情况
调度会开启好几个temp_slave
当执行完毕后，检索队列，当队列任务为空的情况，自行结束该进程

流程:
    由ps去启动，判断队列种子数量来决定是否增加slave
    slave启动后，从队列获取种子，并执行
    该temp_slave执行完毕后，判断队列中是否还有种子，没有种子随机完成执行，并退出
"""

from spider.routing_table import parser_switch as switcher
from utils import json_parse, json_dump
from middleware.middleware import listen_queue
from middleware.middleware import push_msg_2_queue


# config
task_queue = 'task'
html_queue = 'html'


def run():
    # 执行
    # 监听队列
    # 若队列为空，这结束该进程
    while True:
        msg = listen_queue(task_queue)
        if msg:
            next_msg = deal_msg(msg)
            # 拿到数据后，推入html队列
            push_msg_2_queue(html_queue, next_msg)
        else:
            break


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