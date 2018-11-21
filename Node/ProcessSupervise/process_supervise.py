# coding=utf-8


import os
import psutil
import logging
import platform

DEFAULT_ENCODING = 'utf-8'

# logging

logger = logging.getLogger('__main__')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(os.path.join(os.path.split(__file__)[0], './ps_log.log'))
fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(fmt)
logger.addHandler(handler)

# TypeCode
_AllProcess = list
_AProcessCmdline = list
_NodeState = dict
_TaskList = list
_ProcessState = list
demo = 'nia'


class ProcessSupervise:
    """进程管理工具

    提供以下服务:

    - 启动进程
    - kill进程
    - 检索全部进程
    - 检查指定进程状态
    - 当前节点状态

    """
    def __init__(self, task_list: list = None, task_ctx: str = None) -> None:
        self._task_list = task_list
        self._task_ctx = task_ctx
        self._process_list = None
        self.parse_task_list = None

    @property
    def parse_task_list(self) -> _TaskList:
        # 接收到进程列表
        # 返回加工过后的task_list
        task_list = []
        # 开始处理
        if self._task_ctx is not None:
            for task in self._task_ctx.split('\n'):
                if task != '':
                    task_list.append(task.split('\t'))
            self._task_list = task_list
        return self._task_list

    @parse_task_list.setter
    def parse_task_list(self, task_ctx) -> None:
        """文本形式的task_ctx"""
        if isinstance(self._task_ctx, str):
            self._task_ctx = task_ctx
        else:
            # 抛出错误
            # raise xxxError
            self._task_ctx = ''

    @parse_task_list.deleter
    def parse_task_list(self) -> None:
        """腾内存"""
        self._task_ctx = None
        self._task_list = None

    def start_process(self, task_ctx) -> None:
        """给一个元组，启动进程

        :param task_ctx:元组,任务列表文档
        :return: None
        """
        # 将任务文本变成
        self.parse_task_list = task_ctx

        # 开始执行任务
        # 先确定操作系统,不同的操作系统，文件目录的表示不同
        system = platform.uname().system

        # 拿到当前的进程列表
        process_list = [process[0] for process in self.all_process_list]
        # task_list中每一个元素: [task_name, task_xxx.py, path]
        for task in self.parse_task_list:
            if system == 'Windows':
                # 就windows奇葩一些
                execute_path = '\\'.join([task[-1], task[-2]])
            else:
                execute_path = os.path.join(task[-1], task[-2])
            cmd = 'nohup python3 {0} &'.format(execute_path)
            # cmd代表向shell里输入的执行语句
            # nohup python3 C:\Users\forme\Desktop\Github\spider_platform\Node\demo\demo_persistence.py &
            # nohup python3 C:\Users\forme\Desktop\Github\spider_platform\Node\demo\demo_parser.py &
            # nohup python3 C:\Users\forme\Desktop\Github\spider_platform\Node\demo\demo_downloader.py &
            # nohup python3 C:\Users\forme\Desktop\Github\spider_platform\Node\demo\demo_seed.py &

            # 开始检索每个任务，是否已经存在
            if execute_path not in process_list:
                # 执行该task
                try:
                    os.system(cmd)
                    logger.debug('启动\t{0}'execute_path)
                except Exception as e:
                    logger.warning('进程启动失败\t{0}\n启动命令:\t{1}'.format(e, cmd))

        # 腾内存
        del self.parse_task_list
        del self.all_process_list

    def kill_process(self, *args) -> None:
        """kill掉指定的进程
        需要根据给的任务列表，去检索出该程序的pid
        :param args: 元组，进程列表,需要提供,((xxx.py, ptah), (xxx.py, path))
        :return:
        """
        # 同进程启动类似
        # 需要找到对应pid
        # 然后通过 Process().kill()

        task_list_2_kill = args[0]
        # 获取当前python相关的进程
        # 接下来检索对应的pid
        kill_pids = [i[1] for i in self.all_process_list if i[0] in task_list_2_kill]
        for pid in kill_pids:
            try:
                process = psutil.Process(pid)
                process.kill()
                logger.debug('完成kill\t当前pid:\t{0}'.format(pid))
            except Exception as e:
                logger.warning('kill\t{0}\t出错,没有当前进程\terror:\t{1}'.format(pid, e))

        # 腾内存
        del self.all_process_list

    @property
    def all_process_list(self) -> _AllProcess:
        """获取当前节点，全部的进程及执行路径

        2018-11-18: 同时返回该进程，当前的pid

        """
        process_list = []
        for i in psutil.pids():
            process = psutil.Process(i)
            try:
                # 只看python 的进程
                if process.name() == 'Python':
                    cmdline = process.cmdline()
                    # 判断cmdline的长度, 第一个参数是python 第二个是任务路径
                    if cmdline.__len__() > 1:
                        # 2018-11-18 这里修改，需要返回包括当前进程的pid
                        process_list.append((cmdline[1], i))
            except Exception as e:
                print('error', e)

        self._process_list = process_list
        return self._process_list

    @all_process_list.deleter
    def all_process_list(self) -> None:
        """腾内存"""
        self._process_list = None

    """
    def check_process_state(self, execute_file_name) -> _ProcessState:
        返回当前节点该进程的状态
        通过检测各个进程的执行路径，来确定该进程
        是否存活
        当前的cpu占用率，内存占用率等等等等

        # todo: 从指定状态，到返回全部python程序的状态
        proc_state = {
            'pid': '',          # 该进程的pid
            'servival': 'gone', # 状态
            'cpu_percent': '',  # cpu占用率
            'belong': '',       # 隶属于
            'memeory_percent': '',  # 内存占用率

        }
        # 首先是检索出该进程的pid
        pid = None
        for proc in self.all_process_list:
            if proc[0] == execute_file_name:
                pid = proc[1]
        
        # 然后是汇报状态
        if pid is not None:
            proc_state.update({'servival': 'running'})
            process = psutil.Process(pid)
            proc_state.update({
                'cpu_percent': process.cpu_percent(),
                'belong': process.username(),
                'memeory_percent': process.memory_percent()
            })
        return proc_state
    """
    def check_all_process_state(self) -> _ProcessState:    
        # 所有进程列表
        # 返回当前节点该进程的状态
        # 通过检测各个进程的执行路径，来确定该进程
        # 是否存活
        # 当前的cpu占用率，内存占用率等等等等

        all_process_state = []

        for proc in self.all_process_list:
            process = psutil.Process(proc[1])
            proc_state = {
                'pid': proc[1],                         # 该进程的pid
                'filename': proc[0],                    # 该进程执行文件
                'servival': 'running',                  # 状态
                'cpu_percent': process.cpu_percent(),   # cpu占用率
                'belong': process.username(),           # 隶属于
                'memeory_percent': process.memory_percent(),  # 内存占用率
            }
            all_process_state.append(proc_state)
        
        # 腾内存
        del self.all_process_list

        return all_process_state


    def check_node_state(self) -> _NodeState:
        """返回当前节点的状态
        cpu占用率
        memory占用率
        disk占用率
        :return: 一个字典
        """

        return {
            'cpu_percent': psutil.cpu_percent(),    # cpu使用率
            'memory_percent': psutil.virtual_memory().percent,  # 内存使用率
            'disk_usage': psutil.disk_usage('/').percent,          # 硬盘使用率
        }
