# coding=utf-8

"""
    解析器，用来接收队列数据，然后解析，然后加工丢给持久化队列
"""

from utils import json_parse
from utils import json_dump


def yzwz_parser(task_name, args, content):
    if task_name == 'yzwz_list':
        msg = parse_list(args, content)
    else:
        msg = parse_detail(args, content)
    return msg


def parse_list(args, content):
    # 解析列表
    # 返回列表数据
    js_dict = json_parse(content)
    data_list = js_dict.get('data', {}).get('list', {}).get('content', [])
    for data in data_list:
        task_id = data.get('id')
        # 异步返回推入队列
        yield {'task': 'yzwz_detail', 'args': [args, task_id]}


def parse_detail(args, html):
    # 解析详情
    # 返回详情数据
    pass


if __name__ == '__main__':
    with open('./demo.txt', 'r', encoding='utf-8') as f:
        for i in yzwz_parser('yzwz_list', '四川', f.read()):
            print(i)