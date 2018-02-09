# coding=utf8

"""
__author__ = wangjiawei

测试用
大众点评"餐饮，购物，娱乐"脚本
被脚本仓库调用，讲一个完整可执行任务的脚本传递给脚本仓库

***
目前的思路是，脚本库的脚本需要提供：
1. 对应网站的解析规则
2. 该url的请求方式，包括请求头的设置
***
"""

import json

DIANPING = {
    'shop_list': {
        'parse': {
            'list': '//div[@id="shop-all-list"]/ul/li',
            'params': {
                'url': 'div[@class="txt"]/div[@class="tit"]/a/@href',
                'name': 'div[@class="txt"]/div[@class="tit"]/a/h4/text()',
            }
        },
        'request_method': {
            'method': 'GET',
            'headers': {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'Cache-Control': 'max-age=0',
                'Host': 'www.dianping.com',
                'Proxy-Connection': 'keep-alive',
                'Referer': 'http://www.dianping.com/',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
            }
        }
    },
    'shop_info': {},
    'shop_cmt': {}
}


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