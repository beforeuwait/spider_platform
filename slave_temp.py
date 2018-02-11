# coding=utf8

__author__ = 'wangjaiwei'

"""
测试 script_repository 的临时slave

获取脚本，这里通过读取的操作
执行脚本，


"""

import os
import json
from lxml import etree
from script_repository import load_project_parse_2_json

goal = 'list'


def get_json_str():
    projcet = 'dianping'
    json_str = load_project_parse_2_json(projcet)
    js_dict = json.loads(json_str)
    return js_dict

js_dict = get_json_str()

class Downloader(object):
    def the_page(self):
        html = open('dianping_shop_list.txt', 'r', encoding='utf8').read()
        return html

class Spider(object):

    def parse_html_xpath(self, html):
        try:
            selector = etree.HTML(html)
        except Exception as e:
            print(e)
            selector = None
        return selector

    def deal_parse_xpath(self, html):
        selector = self.parse_html_xpath(html)
        data = []
        if selector is not None:
            parse = js_dict.get('shop_list').get('parse')
            shop_list = selector.xpath(parse.get(goal))
            for shop in shop_list:
                data_temp = {}
                for key, value in parse.get('params').items():
                    data_temp[key] = shop.xpath(value)[0]
                data.append(data_temp)
            data = json.dumps(data)
        return data


if __name__ == '__main__':
    spider = Spider()
    down = Downloader()
    html = down.the_page()
    data = spider.deal_parse_xpath(html)
    # 放入持久化队列里
    with open(os.path.abspath('persistence_queue.txt'), 'a', encoding='utf8') as f:
        f.write(data)