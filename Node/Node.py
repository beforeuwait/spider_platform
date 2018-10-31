# coding=utf8

"""
    author = wangjiawei
    date = 2018.10.31

    state:
    该模块作为节点的核心部分，承担:
    
    1. 由调度激活后，进入node角色
    2. 监听任务队列，准备执行相应的任务
    3. 反馈当前节点状态包括：cpu占用率，内存占用率等等
    4. 接受任务，生成脚本，开启进程执行相应的模块
    5. 承担消息中心，负责接受和转发各类消息
    6. 进程管理 

"""

# 启动后，便后台执行，开始执行监听、反馈的工作
# 

class DutyForNode():
    """作为节点的职责

    1. 激活后，反馈调度
    2. 监听任务队列
    3. 上报当前节点的状态
    4. 按顺序执行任务,生成xxxSpider.py脚本
    5. 阅读xxxSpider.py ，执行抓取逻辑

    """
    pass


class FeedBack():
    """反馈模块

    1. 由DutyForNode来实例化
    2. 向schedule模块反馈两样东西
    3. 第一是建立后告知schedule完成建立
    4. 检索自身状态，随时反馈

    """
    pass


class TaskReader():
    """任务拆分
    
    接收任务后，需要做以下几件事
    1. 在 ./spider/目录下创建 xxxSpider.py脚本
    2. 在 call_of_duty.ini 下写入任务索引，告知任务调取顺序
        这个索引的作用是检索当前正执行任务，用于进程检测

    """
    pass


class TaskExecutor():
    """任务执行者

    根据 call_of_duty.ini 里的任务索引
    向下读取，一边检测每个进程的状态
    一边启动相应进程开始执行任务

    """
    pass