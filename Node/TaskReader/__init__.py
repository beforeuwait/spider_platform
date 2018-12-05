# coding=utf-8

__auther__ = 'wangjiawei'
__date__ = '2018-12-05'

"""
    TaskReader 这个模块的作用
    从msgCenter接受到任务后

    1. 将脚本拆分， 形成若干小程序
    2. 维护 task_index.ini 任务索引
    3. 维护 que_index.ini 消息队列索引
"""
