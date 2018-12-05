# coding=utf-8

from utils import make_file
from utils import make_main_script


# type

class MsgCenterDealer:
    """消息中心处理器
    1. 接受任务
    2. 反馈
    """
    pass


class TaskHandler:
    """Task处理
    1. 生成大脚本
    2. 生成小脚本
    """
    pass


class IndexHandler:
    """索引处理
    1. 维护旧索引
    2. 写入新索引
    """
    pass

    
class TaskReader:
    """任务阅读器

    负责：
    1. 同msgCenter通信接受任务
    2. 拆分任务
    3. 维护索引
    """

    # todo: 待msgCenter架构好先
    def receive_task_from_msgcenter(self) -> None:
        """负责从消息队列获取任务"""
        pass
    
    def msg_temp(self) -> dict:
        """临时的任务"""
        msg = open('./msg.txt', 'r', encoding='utf8').read()
        import json
        msg_dict = json.loads(msg)
        return msg_dict

    def task_reader(self):
        """拿到msg"""
        msg_dict = self.msg_temp()
        code = msg_dict.get('code')
        task_name = msg_dict.get('task_name')

        # 先是在 ../spider/目录下创建对应目录
        make_file(task_name)
        # 接下来是在 ../spider/目录下创建对应的大脚本
        make_main_script(task_name, code)

        # todo: 接下来开始生成小脚本
        pass

        # todo: 接下来维护索引
    

if __name__ == '__main__':
    tr = TaskReader()
    tr.task_reader()