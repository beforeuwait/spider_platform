# coding=utf-8


"""作为临时的slave，当时队列负载过高的情况
调度会开启好几个temp_slave
当执行完毕后，检索队列，当队列任务为空的情况，自行结束该进程

流程:
    由ps去启动，判断队列种子数量来决定是否增加slave
    slave启动后，从队列获取种子，并执行
    该temp_slave执行完毕后，判断队列中是否还有种子，没有种子随机完成执行，并退出
"""

import time
from spider.routing_table import switcher
from utils import json_parse, json_dump
from middleware.middleware import listen_queue
from middleware.middleware import push_msg_2_queue


# config
task_queue = 'task'
html_queue = 'html'

