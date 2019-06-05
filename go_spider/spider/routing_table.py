# coding=utf-8

# 路由表
# 每个项目每个模块的编码

from spider.yzwz.viopub_spider import ViopubLogic
from spider.yzwz.viopub_parser import yzwz_parser


spider_switcher = {
    'yzwz_list': ViopubLogic().run,
    'yzwz_detail': ViopubLogic().run_detail,
}

parser_switch = {
    'yzwz_list': yzwz_parser,
    'yzwz_detail': yzwz_parser,
}