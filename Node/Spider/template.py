# coding=utf-8

"""
    author = wangjiawei

    state:
    小程序的模板

    要求：
    启动程序后，同时告知监听和输出的消息队列

    模块内容，只根据提供的数据执行相应的操作
    负责和msgcenter沟通交由给相应的模块
"""

from redis import StrictRedis

# 导入 xxxSpider.py里的 xxx 模块

from {0} import {1}


def template():
    """ 链接redis，或者redis的操作
    """
    pass


def do():
    """主方法
    """
    # 实例化该模块，然后调用，同时监听和输出对应的队列
    instance = {2}()
    instance.do()


if __name__ == '__main__':
    do()