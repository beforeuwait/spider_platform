# coding=utf-8

__author__ = 'wangjiawei'
__date__ = '2018-11-21'

"""
    TaskExecutor作为任务执行者

    1. 从task_index.ini 读取任务
    随后调用ps相应接口，启动任务

    2. 同样从task_index.ini 读取各个任务启动状态
    生成kill_list 随后调用相应ps接口，kill掉进程
"""
