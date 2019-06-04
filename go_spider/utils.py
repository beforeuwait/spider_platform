# coding=utf-8

"""集成常用的方法
author: wangjiawei
date: 2019-05-30

"""

import json


# json的解析
def json_parse(js_ctx):
    js_dict = None
    try:
        js_dict = json.loads(js_ctx)
    except Exception as e:
        # todo: 添加logger
        print(e)
        pass
    return js_dict


# json的构造
def json_dump(js_dict):
    js_ctx = None
    try:
        js_ctx = json.dumps(js_dict, ensure_ascii=False)
    except Exception as e:
        # todo: 添加logger
        print(e)
    return js_ctx