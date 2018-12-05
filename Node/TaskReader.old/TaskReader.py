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

import json
import os

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

    def main_logic(self):
        # 先拿到task的name和code
        task_info = self.msg_reader()
        # 存code
        # self.task_maker(task_info)
        # 存索引
        self.index_writer(task_info[1])

    def msg_reader(self):
        """阅读任务, 解析该条msg里的各种配置参数
        当前简单
        后续msg里包含该节点执行的范围
        """
        msg_dict = json.loads(self.msg)
        code = msg_dict.get('code')
        task_name = msg_dict.get('task_name')
        return (code, task_name)
    
    def task_maker(self, task_info):
        """任务创建
        指定目录创建任务
        """
        # 文件名
        file_name = ''.join([task_info[1], 'Spider.py'])
        # 路径
        file_path = os.path.abspath(task_info[1])
        path = os.path.join(os.path.abspath(task_info[1]), file_name)

        # 首先验证目录是否有
        if not os.path.exists(file_path):
            os.mkdir(file_path)

        # 书写文件
        with open(path, 'w', encoding='utf8') as f:
            f.write(task_info[0])

        return

    def index_writer(self, task_name):
        """索引创建
        """
        # 这里要写入2个索引
        # 一个是 task的索引，由TaskExecutor读取
        # 一个是 process_que的索引，由MsgCenter读取

        # 开始写task_index.ini
        path = os.path.abspath('./task_index.ini')
        process_path = os.path.abspath(task_name)
        # 模板task process------ task \t process \t path
        task_index_model = ['{0}_persistence.py', '{0}_parser.py', '{0}_downloader.py', '{0}_seed.py']
        # 开始写入
        for i in task_index_model:
            content = '\t'.join([task_name, i.format(task_name), process_path])
            with open(path, 'a', encoding='utf8') as f:
                f.write(content + '\n')

        # 接下来是写入msg_index.ini
        # 格式是每一行为该任务
        que_index_path = os.path.abspath('./que_index.ini')
        with open(que_index_path, 'a', encoding='utf8') as f:
            f.write(task_name + '\n')

    

class MicroScriptMaker(object):
    """小任务生成器模块
    根据大脚本，生成对应的小脚本
    """
    pass


if __name__ == '__main__':
    msg = open('./msg.txt', 'r', encoding='utf8').read()
    # msg_dict = json.loads(msg)
    # code = msg_dict.get('code')
    # task_name = msg_dict.get('task_name')
    # print(code)
    # print(task_name)
    taim = TaskAndIndexMaker(msg)
    taim.main_logic()
