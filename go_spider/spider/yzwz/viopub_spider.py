# coding=utf-8

"""
    通用主干爬虫
    不同省份，继承重写不同的方法

"""

import random
import time
import json
import datetime
from requestApi.UserAgent import user_agent_list
import zdwz.config as cnf
from requestApi import HttpApi
from copy import deepcopy


class GeneralLogic:
    # 主逻辑
    # 若有不同省份
    # 继承重写就成
    # 目前是通用的思路

    def __init__(self, prov):
        super(GeneralLogic, self).__init__()
        self.prov = prov
        self.p_code = self.construct_params()
        self.headers = random.choice(user_agent_list)
        self.api = HttpApi()

    def construct_params(self):
        return cnf.prov_code.get(self.prov)

    def visit_home_page(self):
        # 请求主页 获取 jsessionId
        url = deepcopy(cnf.url_home.format(self.p_code))
        headers = cnf.headers_home
        headers.update({'User-Agent': self.headers,
                        'Host': '{0}.122.gov.cn'.format(self.p_code)})
        # 请求主页
        self.api.send_args_get_html(url=url, headers=headers, method='get', isSession='yes', isProxy='yes', isVerify=False)

    def visit_viopub_page(self):
        # 进入目标页面 获取cookie
        url = deepcopy(cnf.url_viopub.format(self.p_code))
        headers = cnf.headers_vio
        headers.update({'User-Agent': self.headers,
                        'Referer': 'https://{0}.122.gov.cn/views/notice.html'.format(self.p_code),
                        'Host': '{0}.122.gov.cn'.format(self.p_code),
                        })
        self.api.send_args_get_html(url=url, headers=headers, method='get', isSession='yes', isProxy='yes', isVerify=False)

    def do_check_type(self):
        # 请求 check_type
        url = deepcopy(cnf.url_check.format(self.p_code))
        headers = cnf.headers_check
        headers.update({'User-Agent': self.headers,
                        'Referer': deepcopy(cnf.url_viopub.format(self.p_code)),
                        'Host': '{0}.122.gov.cn'.format(self.p_code),
                        'Origin': deepcopy(cnf.url_home).format(self.p_code),
                        })
        payloads = {'checktype': cnf.check_type.get('yzwz')}
        self.api.send_args_get_html(url=url, headers=headers, method='post', payloads=payloads, isSession='yes', isProxy='yes', isVerify=False)


    def download_captcha_ocr(self):
        # 下载以及ocr
        url = deepcopy(cnf.url_c.format(self.p_code, int(time.time())))
        headers = cnf.headers_captcha
        headers.update({'Host': '{0}.122.gov.cn'.format(self.p_code)})
        captcha = self.api.send_args_get_html(url=url, headers=headers, method='get', isSession='yes', isProxy='yes', isVerify=False, isByte=True)
        # with open('{}.png'.format(int(time.time())), 'wb') as f:
        with open('ca.png'.format(int(time.time())), 'wb') as f:
            f.write(captcha)
        ca = input('请输入验证码:\t')
        return ca

    def download_data_list(self, ca):
        # 下载列表
        url = cnf.url_list.format(self.p_code)
        headers = cnf.headers_list
        headers.update({
            'User-Agent': self.headers,
            'Referer': deepcopy(cnf.url_viopub.format(self.p_code)),
            'Host': '{0}.122.gov.cn'.format(self.p_code),
            'Origin': deepcopy(cnf.url_home).format(self.p_code),
        })
        payloads = cnf.payloads_list
        payloads.update({'startTime': (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
                         'endTime': (datetime.datetime.today()).strftime('%Y-%m-%d'),
                         'csessionid': ca})
        html = self.api.send_args_get_html(url=url, headers=headers, method='post', payloads=payloads, isSession='yes', isProxy='yes', isVerify=False)
        print(json.loads(html))
        return html

    def download_data_detail(self):
        # 下载详情
        pass

    def run(self):
        # 主流程
        self.visit_home_page()
        time.sleep(1)
        # 请求目标页面
        self.visit_viopub_page()
        time.sleep(1)
        # 请求check——type
        self.do_check_type()
        time.sleep(1)
        # 请求验证码
        ca = self.download_captcha_ocr()
        # 以上可以当做一个循环
        self.download_data_list(ca)



if __name__ == '__main__':
    gl = GeneralLogic('四川')
    gl.run()