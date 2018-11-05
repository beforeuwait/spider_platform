# coding=utf8

"""

    author = wangjiawei
    date = 2018-11-02

    state:
    该脚本的功能就是，在 ./spider/xxxx/xxxxspider.py下
    写对于模块的小程序
    目的是方便 nodeExecutor 来启动
    TaskReader在读任务的时候，就已经生成队列列表

    demoSpider: {
        'demoseed': {
            'in': 'demo_seedin',
            'out': 'demo_seedout',
        },
        'demodownloader': {
            'in': 'demo_downin',
            'out': 'demo_downout',
        },
        'demoparse': {
            'in': 'demo_parsein',
            'out_url': 'demo_parseurlout',
            'out_data': 'demo_parserdataout',
        }
        'demo_persistence': {
            'in': 'demo_persisin'
        }
    }
    可以看出，每个脚本8个队列

    ########################################################
    2018-11-02 配置一个模板来实现
    ########################################################
    2018-11-05 完成这个部分的编写
    要做的事情:
        1. 接收到任务
        2. 开始生成 xxx_seed.py、xxx_downloader.py、xxx_parser.py、xxx_persistence.py
        3. 生成过程中，就已经为各个小脚本配置好同消息中心通信的队列
            parser是个另外，因为涉及到，反馈url的问题
        4. 暂时不写通用的模板，一个部分一个部分的写
"""


class MsgCenter():
    """作为消息中心的
    车间，装配
    """

    def __init__(self, project):
        # 项目名称
        self.project_name = project

    def seed_module(self):
        """
        为seed模块匹配一个队列
        """
        que_in = '{0}_seedin'.format(self.project_name)
        que_out = '{0}_seedout'.format(self.project_name)

        script = """
        
        # 这是种子模块的通信代码
        # 接受到消息，执行seed代码，获取新种子
        # 将新种子放入队列里
        
        
        
        """
