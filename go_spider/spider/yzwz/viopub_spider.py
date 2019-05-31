# coding=utf-8

"""
    通用主干爬虫
    不同省份，继承重写不同的方法

"""

import random
import time
import json
import datetime
from spider.requestApi.UserAgent import user_agent_list
import spider.yzwz.config as cnf
from spider.requestApi import HttpApi
from copy import deepcopy


class ViopubLogic:
    # 主逻辑
    # 若有不同省份
    # 继承重写就成
    # 目前是通用的思路

    def __init__(self):
        super(ViopubLogic, self).__init__()
        self.headers = random.choice(user_agent_list)
        self.api = HttpApi()

    def construct_params(self, prov):
        return cnf.prov_code.get(prov)

    def visit_home_page(self, p_code):
        # 请求主页 获取 jsessionId
        url = deepcopy(cnf.url_home.format(p_code))
        headers = cnf.headers_home
        headers.update({'User-Agent': self.headers,
                        'Host': '{0}.122.gov.cn'.format(p_code)})
        # 请求主页
        self.api.send_args_get_html(url=url, headers=headers, method='get', isSession='yes', isProxy='yes', isVerify=False)

    def visit_viopub_page(self, p_code):
        # 进入目标页面 获取cookie
        url = deepcopy(cnf.url_viopub.format(p_code))
        headers = cnf.headers_vio
        headers.update({'User-Agent': self.headers,
                        'Referer': 'https://{0}.122.gov.cn/views/notice.html'.format(p_code),
                        'Host': '{0}.122.gov.cn'.format(p_code),
                        })
        self.api.send_args_get_html(url=url, headers=headers, method='get', isSession='yes', isProxy='yes', isVerify=False)

    def do_check_type(self, p_code):
        # 请求 check_type
        url = deepcopy(cnf.url_check.format(p_code))
        headers = cnf.headers_check
        headers.update({'User-Agent': self.headers,
                        'Referer': deepcopy(cnf.url_viopub.format(p_code)),
                        'Host': '{0}.122.gov.cn'.format(p_code),
                        'Origin': deepcopy(cnf.url_home).format(p_code),
                        })
        payloads = {'checktype': cnf.check_type.get('yzwz')}
        self.api.send_args_get_html(url=url, headers=headers, method='post', payloads=payloads, isSession='yes', isProxy='yes', isVerify=False)


    def download_captcha_ocr(self, p_code):
        # 下载以及ocr
        url = deepcopy(cnf.url_c.format(p_code, int(time.time())))
        headers = cnf.headers_captcha
        headers.update({'Host': '{0}.122.gov.cn'.format(p_code)})
        captcha = self.api.send_args_get_html(url=url, headers=headers, method='get', isSession='yes', isProxy='yes', isVerify=False, isByte=True)
        # with open('{}.png'.format(int(time.time())), 'wb') as f:
        with open('ca.png'.format(int(time.time())), 'wb') as f:
            f.write(captcha)
        ca = input('请输入验证码:\t')
        return ca

    def download_data_list(self, ca, p_code):
        # 下载列表
        url = cnf.url_list.format(p_code)
        headers = cnf.headers_list
        headers.update({
            'User-Agent': self.headers,
            'Referer': deepcopy(cnf.url_viopub.format(p_code)),
            'Host': '{0}.122.gov.cn'.format(p_code),
            'Origin': deepcopy(cnf.url_home).format(p_code),
        })
        payloads = cnf.payloads_list
        payloads.update({'startTime': (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
                         'endTime': (datetime.datetime.today()).strftime('%Y-%m-%d'),
                         'csessionid': ca})
        html = self.api.send_args_get_html(url=url, headers=headers, method='post', payloads=payloads, isSession='yes', isProxy='yes', isVerify=False, code='utf-8')
        return html

    def download_data_detail(self):
        # 下载详情
        pass

    def run(self, prov):
        p_code = self.construct_params(prov)
        # 主流程
        self.visit_home_page(p_code)
        time.sleep(1)
        # 请求目标页面
        self.visit_viopub_page(p_code)
        time.sleep(1)
        # 请求check——type
        self.do_check_type(p_code)
        time.sleep(1)
        # 请求验证码
        ca = self.download_captcha_ocr(p_code)
        # 以上可以当做一个循环
        html = self.download_data_list(ca, p_code)
        return html


if __name__ == '__main__':
    gl = ViopubLogic()
    gl.run('四川')