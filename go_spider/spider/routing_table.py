# coding=utf-8

# 路由表
# 每个项目每个模块的编码

from spider.yzwz.viopub_spider import ViopubLogic

switcher = {
    'yzwz_list': ViopubLogic().run,
}