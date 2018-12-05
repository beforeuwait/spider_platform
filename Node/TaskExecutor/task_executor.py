# coding=utf-8

import os
from ProcessSupervise import *


# type
_TaskIndex = str

class TaskExecutor:
    """任务执行

    当前模块主要承担两件事
    1. 向ps里喂 task_index
    2. 向ps里为 kill_list
    """

    def __init__(self, task_index: _TaskIndex = '') -> None:
        self._task_index = task_index
        self.ps = PS()

    @property
    def task_index_reader(self) -> _TaskIndex:
        """读取task_index上面的数据"""
        # 要判断该文件是否存在
        if not os.path.exists(os.path.abspath('../task_index.ini')):
            f = open(os.path.abspath('../task_index.ini'), 'w')
            f.close()
        self._task_index = open(os.path.abspath('../task_index.ini'), 'r', encoding='utf8').read()
        return self._task_index

    @task_index_reader.deleter
    def task_index_reader(self) -> None:
        self._task_index = ''

    def execute_all_task(self) -> None:
        """执行task_index里全部任务"""
        self.ps.start_process(self.task_index_reader)

    def kill_process(self) -> None:
        """将task_index里任务标识为1的任务kill掉"""
        # 先获取待kill的任务列表
        kill_list = [i.split('\t')[1] for i in self.task_index_reader.split('\n') if i.split('\t')[-1] == '1']
        # 执行kill功能
        self.ps.kill_process(kill_list)

    def __del__(self):
        # 删实例
        del self.ps
        # 腾内存
        del self.task_index_reader
