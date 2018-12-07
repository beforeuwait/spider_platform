# coding=utf-8

import os
import json

"""
这个文件的io操作都是针对 spider目录 和 前一个大目录
"""

def make_file(name) -> None:
    """在指定目录下创建文件"""
    file_path = os.path.join(os.path.abspath('../spider/'), name)
    # 判断目录是否存在
    if not os.path.exists(file_path):
        os.mkdir(file_path)


def make_main_script(name, code) -> None:
    """在指定的目录下创建大脚本"""
    file_path = os.path.join(os.path.abspath('../spider/'), name)
    script_path = os.path.join(file_path, name + '.py')
    with open(script_path, 'w', encoding='utf-8') as f:
            f.write(code)
    

def loads_json(js_ctx) -> dict:
    """导入json文件"""
    js_dict = None
    try:
        js_dict = json.loads(js_ctx)
    except Exception as e:
        print('json解析出错', e)
        # todo: 加入logging
    return js_dict