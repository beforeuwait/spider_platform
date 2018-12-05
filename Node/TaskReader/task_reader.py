# coding=utf-8

# type

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
        print(msg_dict.get('code'))

if __name__ == '__main__':
    tr = TaskReader()
    tr.task_reader()