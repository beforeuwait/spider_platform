# coding=utf8

"""

    author = wangjiawei
    date = 2018-11-02

    state:
    该脚本的功能就是，在 ./spider/xxxx/xxxxspider.py下
    写对于模块的小程序
    目的是方便 nodeExecutor 来启动
    ########################################################
    2018-11-02 配置一个模板来实现
"""

template_path = './spider/template.txt'
template = open(template_path, 'r', encoding='utf8').read()

print(template)