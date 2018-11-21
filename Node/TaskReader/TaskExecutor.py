# coding=utf-8

"""
    author: wangjiawei
    date: 2018-11-14

    quote:
        该模块的功能为:
            1. 检索任务目录
            2. 执行相应的进程
            3. 检测已kill的进程，判断是否启动

    #############################################
    # 跪舔 psutil库
    # 可以凭借这个库，开发一套进程管理
    ############################################
"""

# 阅读索引，拼接 xxx.py和path，然后调用终端去执行
# 执行前，先检测该进程是否存在
# 发现神库 psutil

import psutil
import os
import platform


class TaskExecutor(object):
    """进程执行者
    负责根据目录索引开始执行各个进程

    """

    def __init__(self):
        pass

    def task_index_reader(self):
        """读取任务索引文件
        把任务丢入一个任务列表里
        """
        task_list = []
        task_index_file = os.path.abspath('./task_index.ini')
        # 检测该索引是否存在，若不存在，创建新的
        if not os.path.exists(task_index_file):
            f = open(task_index_file, 'w', encoding='utf8')
            f.close()
        # 读取内容
        for i in open(task_index_file, 'r', encoding='utf8'):
            task_list.append(i.strip().split('\t'))

        return task_list

    def search_start_process(self):
        """检索任务，是否存在，若不存在，则启动
        这里需要区分操作系统
        """
        current_system = platform.uname().system
        print(current_system)
        if current_system == 'Windows':
            # 针对windows,因为输出的进程都在后缀,与task_list里的进程名字一致
            pass


if __name__ == '__main__':
    te = TaskExecutor()
    # te.task_index_reader()
    te.search_start_process()
