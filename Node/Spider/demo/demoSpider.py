# coding=utf8

"""
this is a demo project for a simply spider

该平台的爬虫文件，在节点接收到任务后
TaskReader 生成 ./spider/xxx/目录
在 ./spider/xxx/目录下 生成 xxxSpider.py 脚本

程序自动生成 xxx_seed.py、xxx_downloader.py、xxx_parser.py、xxx_persistence.py
调用xxxSpider.py脚本里对于的模块，然后持续执行
"""


# 各类库导入部分
# 正常的爬虫导入

import requests
# from xxx import xxx
# from yyy import zzz

class SeedsMaker():
    """种子生成器

    作用就是提供一个逻辑，去生产种子
    
    向消息中心源源不断的丢种子进去
    """
    
    def fun1(self):
        pass

    def fun2(self):
        pass
    
    def execute(self):
        """固定的调用函数"""
        print('执行')


class Downloader():
    """下载器

    其作用就是根据url，执行一次请求
    
    至于 headers
    cookie啊
    什么的，都写在这个模块里
    """

    # from HTTP.RequestServerApi import ReqestApi
    def fun1(self):
        pass
    
    def fun2(self):
        pass
    
    def execute(self):
        """固定的调用函数"""
        pass


class Parser():
    """解析器

    接收html，然后解析
    当然在该Parser里，要承担的是好几个页面的解析
    因为需要一个 switcher
    """

    def parse1(self):
        pass
    
    def parse2(self):
        pass
    
    def switch(self):
        pass
    
    def execute(self):
        pass
    

class Persistence():
    """持久化模块

    根据要求，将相应的数据放入 hdfs、mysql、local里

    """

    def execute(self):
        pass
    