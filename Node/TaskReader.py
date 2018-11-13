# coding=utf-8

"""
    author: wangjiawei
    date: 2018-11-13

    info:
        TaskReader模块
        承担的角色：
            1. 任务生成，即将收到的任务，创建xxxSpider.py文件
            2. 任务分发，将创建的任务，指派4个小任务，负责调用xxxSpider.py相应模块
            3. 维护一个任务目录索引，记录该节点下所有的任务--小任务，由TaskExecutor按照顺序检索和执行
                3.1 针对已经执行完毕的模块，比如seed模块，及时从索引里删除
            4. 维护一个消息队列索引，由MsgCenter负责维护，MsgCenter根据消息队列索引，每一次检索每一条管道，然后执行相应操作

    ###############################################
    # 2018-11-13: 开始开发索引模块
"""

class TaskReader(object):
    """TaskReader主逻辑模块
    """

    pass

class TaskAndIndexMaker(object):
    """任务生成器模块
    根据接收到的任务，执行文件创建
    索引文件的创建
    """

    # index索引长这个样:
    # task_index.ini 放在 NODE 这个目录下
    # 每一行代表一个任务，包括 task_name \t 目录(./spider/xxxx/)
    def __init__(self, msg):
        # msg 是从schedule传来的任务
        # 当前的版本是一个node只能执行一个task -全程
        # 后续版本task可以指定抓取范围，这样实现同一个任务可以在多个node下执行
        self.msg = msg
    
    def msg_reader(self, msg):
        """阅读任务, 解析该条msg里的各种配置参数
        当前简单
        后续msg里包含该节点执行的范围
        """
        pass
    
    def task_maker(self):
        """任务创建
        指定目录创建任务
        """
        pass
    
    def index_writer(self):
        """索引创建
        """
        # 这里要写入2个索引
        # 一个是 task的索引，由TaskExecutor读取
        # 一个是 process_que的索引，由MsgCenter读取
        pass
    


class MicroScriptMaker(object):
    """小任务生成器模块
    根据大脚本，生成对应的小脚本
    """
    pass