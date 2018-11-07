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
    #######################################################
    2018-11-07
    继续开发:
        
"""

import os

# 种子模块的
seed_script = """

    # 这是种子模块的通信代码
    # 接受到消息，执行seed代码，获取新种子
    # 将新种子放入队列里
    
    que_in = '{0}'
    que_out = '{1}'
        """

# 下载器模块
downloader_script = """
        
    # 这是请求模块的通信代码
    # 下载器接受任务，请求头啊，cookie提前配置好了的
    # 直接完成一次请求
    
    que_in = '{0}'
    que_out = '{1}'

        """

# 解析器模块
parser_script = """
        
    # 这是解析模块的通信代码
    # 因为存在输出 data or url 的问题
    # 需要匹配2条队列
    
    que_in = '{0}'
    que_urlout = '{1}'
    que_dataout = '{2}'

"""

# 持久化模块
persistence_script = """

    # 这是持久化模块的通信代码
    # 只接受数据，然后处理数据
    
    que_in = '{0}'

"""

# 消息中心
msg_script = '''

from redis import StrictRedis


class MsgCenter():

    def connect_redis(self):
        try:
            redis_cli = StrictRedis(host='loacalhost', port=6379, db=1)
        except:
            print('链接\tRedis\t失败....')
            redis_cli = None
        return redis_cli

    def push_msg_2_que(self, que, msg):
        """将数据推入到指定的队列里

        :param que: 指定的队列
        :param msg: json格式的数据
        :return 是否成功推入数据
        """

        done = False
        redis_cli = self.connect_redis()
        if redis_cli is not None:
            redis_cli.lpush(que, msg)
            done = True
        return done

    def receive_msg_from_que(self, que):
        """从指定的队列里获取消息

        没有消息，就等候，
        :param que: 指定的队列
        :return: msg: 消息队列里的数据，没有则为None
        """

        msg = None
        redis_cli = self.connect_redis()
        if redis_cli is not None:
            msg = redis_cli.rpop(que)
            # 没有数据则为None
        return msg

    '''

# seed模块的填充
seedexe_script = '''
from {0} import SeedsMaker

class Executor():
    """启动器

    - 种子生成器，接到反馈，生产种子
    - 下载器，接到种子，生产html
    - 解析器，接到html，解析url和data
    - 持久化存储，接到data，存储
    """

    def execute(self):
        # 监听队列
        sm = SeedsMaker()

        mc = MsgCenter()

        while True:
            # 从队列获取数据
            msg = mc.receive_msg_from_que(que_in)
            if msg is not None:
                # 代表有消息来了
                # 执行
                seed = sm.execute(msg)
                # 再推入队列
                if seed is not None:
                    mc.push_msg_2_que(que_out, seed)
                else:
                    # 代表推送完毕,退出
                    break

'''

# downloader模块填充
downloaderexe_script = '''
import time
from {0} import Downloader

class Executor():
    """启动器

    - 种子生成器，接到反馈，生产种子
    - 下载器，接到种子，生产html
    - 解析器，接到html，解析url和data
    - 持久化存储，接到data，存储
    """

    def execute(self):
        # 监听队列
        sm = Downloader()

        mc = MsgCenter()

        while True:
            # 从队列获取数据
            msg = mc.receive_msg_from_que(que_in)
            if msg is not None:
                # 代表有消息来了
                # 执行
                html = sm.execute(msg)
                # 再推入队列
                if html is not None:
                    mc.push_msg_2_que(que_out, html)

            time.sleep(0.1)

'''

# parser模块填充
parserexe_script = '''
import time
from {0} import Parser

class Executor():
    """启动器

    - 种子生成器，接到反馈，生产种子
    - 下载器，接到种子，生产html
    - 解析器，接到html，解析url和data
    - 持久化存储，接到data，存储
    """

    def execute(self):
        # 监听队列
        sm = Parser()

        mc = MsgCenter()

        while True:
            # 从队列获取数据
            html = mc.receive_msg_from_que(que_in)
            if html is not None:
                # 代表有消息来了
                # 执行
                data_dict = sm.execute(html)
                # 这里就要判断了，是否有数据
                if data_dict.get('url') != []:
                    # 说明有url数据
                    # 将url_list 推入队列
                    url_msg = data_dict.get('url')
                    # todo: 转换为json
                    mc.push_msg_2_que(que_urlout, url_msg)
                else:
                    # 接下来推入数据队列
                    data_msg = data_dict.get('data')
                    mc.push_msg_2_que(que_dataout, data_msg)

            time.sleep(0.1)
'''

# persistence模块填充
persistenceexe_script = '''
import time
from {0} import Persistence

class Executor():
    """启动器

    - 种子生成器，接到反馈，生产种子
    - 下载器，接到种子，生产html
    - 解析器，接到html，解析url和data
    - 持久化存储，接到data，存储
    """

    def execute(self):
        # 监听队列
        sm = Persistence()

        mc = MsgCenter()

        while True:
            # 从队列获取数据
            data = mc.receive_msg_from_que(que_in)
            if data is not None:
                # 代表有消息来了
                # 执行
                seed = sm.execute(data)

            time.sleep(0.1)
'''


class QueMaker():
    """作为消息中心的
    车间，装配车间
    """

    def __init__(self, project):
        # 项目名称
        self.project_name = project
        self.path = os.path.abspath('./Spider/{0}'.format(self.project_name))

    def load_que_2_file(self):
        """向文件里写入队列"""

        # 放入字典
        choice = {
            os.path.join(self.path, '{0}_seed.py'.format(self.project_name)): seed_script.format('{0}_seedin'.format(self.project_name), '{0}_seedout'.format(self.project_name)).replace('    ', ''),
            os.path.join(self.path, '{0}_downloader.py'.format(self.project_name)): downloader_script.format('{0}_downin'.format(self.project_name), '{0}_downout'.format(self.project_name)).replace('    ', ''),
            os.path.join(self.path, '{0}_parser.py'.format(self.project_name)): parser_script.format('{0}_parsein'.format(self.project_name), '{0}_parseurlout'.format(self.project_name), '{0}_parsedataout'.format(self.project_name)).replace('    ', ''),
            os.path.join(self.path, '{0}_persistence.py'.format(self.project_name)): persistence_script.format('{0}_persisin'.format(self.project_name)).replace('    ', '')
        }

        # 写入文档
        for path, ctx in choice.items():
            with open(path, 'a', encoding='utf8') as f:
                f.write(ctx)

class FileMaker():
    """文档创建器"""

    def __init__(self, project_name):
        self.project_name = project_name

    def check_and_make_file(self):
        """检测以及创建文档
        分别为 seed、downloader、parser、persistence
        """

        # 该目录在TaskReader下是存在的

        path = os.path.abspath('./Spider/{0}'.format(self.project_name))
        # 接下来在目录下面创建4个小脚本
        file_list = ['{0}_seed.py', '{0}_downloader.py', '{0}_parser.py', '{0}_persistence.py']
        for each in file_list:
            file_name = os.path.join(path, each.format(self.project_name))
            with open(file_name, 'w', encoding='utf8') as f:
                script = "# coding=utf8\n"
                f.write(script)


class ContentMaker:
    """内容填充"""

    def __init__(self, project_name):
        self.project_name = project_name
        self.path = os.path.abspath('./Spider/{0}'.format(self.project_name))


    def load_each_file_msg_center(self):
        """向每个文档放入消息中心代码"""

        path = os.path.abspath('./Spider/{0}'.format(self.project_name))
        # 接下来在目录下面创建4个小脚本
        file_list = ['{0}_seed.py', '{0}_downloader.py', '{0}_parser.py', '{0}_persistence.py']
        for each in file_list:
            file_name = os.path.join(path, each.format(self.project_name))
            with open(file_name, 'a', encoding='utf8') as f:
                f.write(msg_script)
    
    def load_each_file_execute_content(self):
        """针对不同的文件，放入不同的执行"""
        # 放入字典
        choice = {
            os.path.join(self.path, '{0}_seed.py'.format(self.project_name)): seedexe_script.format(self.project_name),
            os.path.join(self.path, '{0}_downloader.py'.format(self.project_name)): downloaderexe_script.format(self.project_name),
            os.path.join(self.path, '{0}_parser.py'.format(self.project_name)): parserexe_script.format(self.project_name),
            os.path.join(self.path, '{0}_persistence.py'.format(self.project_name)): persistenceexe_script.format(self.project_name)
        }

        # 写入文档
        for path, ctx in choice.items():
            with open(path, 'a', encoding='utf8') as f:
                f.write(ctx)
    

def main_logic():
    """主逻辑部分"""
    pass




if __name__ == '__main__':
    # t = FileMaker('demo')
    # t.check_and_make_file()
    # cm = ContentMaker('demo')
    # cm.load_each_file_msg_center()
    q = QueMaker('demo')
    q.load_que_2_file()

    # 1. 创建文件，写头
    # 2. 放入消息中心
    # 3. 放入执行内容