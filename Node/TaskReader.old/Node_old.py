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

    ##################################################
    2018-11-01： 今日解决2个棘手的问题
    1. 单例爬虫，多网页提取，断点、增量爬虫在该系统如何运行
    2. 消息中心的架构

    消息中心和节点控制相互独立，消息中心通过不断的reload 配置文件，负责消息分发
    ##################################################
    2018-11-2：对于小程序
    爬虫各个模块，只负责爬虫的事
    而消息通信，那是消息模块的事情，在被创建的时候，就已经被指定了监听和输出队列
    至于每个爬虫，那就是严格的标准化进行了，在 TaskReader里就需要一套严格的报错机制了

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

    # 激活消息中心
    def activate_msgcenter(self):
        pass

    # 激活后向调度反馈
    def wakeup_and_feedback(self):
        pass
    
    # 汇报节点当前状态 
    def report_node_state(self):
        pass
    
    # 该节点主逻辑
    def working(self):
        """启动好后，该节点进入工作状态

        1. 扫描任务队列，有任务则拿出一个任务
        2. 启动TaskReader，做任务拆分，生成若干小任务
        3. 启动TaskExecutor，根据配置文件，检索当前进程，并启动未执行的进程

        """
        pass
    



class MsgCenter():
    """消息中心

    1. 由DutyForNode来实例化
    2. 向schedule模块反馈两样东西
    3. 第一是建立后告知schedule完成建立
    4. 检索自身状态，随时反馈
    作为消息中心
    5. 维护一个路由表
    5. 监听各个进程的反馈数据
    6. 转发数据

    """

    pass



class TaskReader():
    """任务拆分
    
    接收任务后，需要做以下几件事
    1. 在 ./spider/目录下创建 xxxSpider.py脚本
    2. 在 call_of_duty.conf 下写入任务索引，告知任务调取顺序
        这个索引的作用是检索当前正执行任务，用于进程检测
    3. 维护一个映射表，用来记录各个消息队列对应的程序
    4. 维护这个索引和映射表
    """
    pass


class TaskExecutor():
    """任务执行者

    根据 call_of_duty.conf 里的任务索引
    向下读取，一边检测每个进程的状态
    一边启动相应进程开始执行任务

    """
    pass

