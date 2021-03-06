# coding=utf-8

"""
    中间件模块

    负责整个节点部分的 通信
    
"""


__author__ = 'wangjiawei'
__date__ = '2018-12-10'


"""
    消息中心的作用：
    
    1. 同Schedule通信
        1.1 接收任务
        1.2 反馈节点信息
    2. 同TaskReader通信
        2.1 接收反馈，并保存一个 任务散列表
        2.2 接收反馈，并保存一个 消息散列表
    3. 同taskExecutor通信
        3.1 执行任务散列表里的任务
    4. 同各进程的通信
        4.1 各进程相互独立
        4.2 消息中心根据 消息散列表 执行 进程->消息中心->进程 的通信
"""

__all__ = ['executor2msgc', 'msgc_engine', 'process2msgc', 'schedule2msgc', 'taskreader2msgc']