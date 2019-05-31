# coding=utf-8

"""
    author: wangjiawei
    version: 2.0

    笔者重构一个版本的请求库
    我自己的轻框架非得scrapy？

    在之前的版本里，遇到以下的问题
    1. 执行时间长
    2. session.proxies里有代理，但是请求仍旧从本地发出
    3. 自动判断网页编码出错
    4. 逻辑复杂
    5. 日志看不懂
    6. 引用不便捷
    
    update:
    05-16: todo: 如何引入时候，将日志也如项目当前的路径

    05-20: 完成第一版的开发
    todo:
        当需要输出cookie的情况如何处理?
    
    5-23:
        完了，这版还不如上一版呢，问题更多
        哎，能力不够啊

        接上，没有一根烟不能解决的问题
        有的话，两根
        解决啦
"""

__all__ = ['HttpApi']

from .requestApi import HttpApi