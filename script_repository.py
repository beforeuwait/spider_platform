# coding=utf8
"""
__auther__ = wangjiawei
__version__ = 0.1
作为脚本库的测试版本
1.确定脚本库，脚本的写法，调用方式
2.确定接口
3.脚本仅仅执行请求和解析部分的

--测试脚本，大众点评"吃住行游购娱"
"""

import json
from temp_script_repository.dianping import DIANPING

def load_project_parse_2_json(project):
    """
    json格式传递参数
    :param project:项目名称
    :return: json格式字符串
    """
    json_dict = {}
    if project == 'dianping':
        json_dict = DIANPING
    return json.dumps(json_dict)

if __name__ == '__main__':
    json_str = load_project_parse_2_json('dianping')
    print(json_str)