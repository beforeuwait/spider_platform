# coding=utf8

"""
测试 http/2 协议，使用hyper库

通过实践证明 携程app不是基于http/2的
"""

from hyper import HTTPConnection
import json

headers = {
    ':authority': 'sec-m.ctrip.com',
    ':method': 'POST',
    ':path': '/restapi/soa2/12530/json/scenicSpotDescription?_fxpcqlniredt=09031027110141432611',
    ':scheme': 'https',
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'content-length': '270',
    'content-type': 'application/json',
    'cookieorigin': 'https://m.ctrip.com',
    'origin': 'https://m.ctrip.com',
    'referer': 'https://m.ctrip.com/webapp/ticket/jianjie/1412255.html?gscid=2&sightid=1412255',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36',
    'x-ctrip-pageid': '214427'
}

host = 'sec-m.ctrip.com'
path = '/restapi/soa2/12530/json/scenicSpotDescription'
payloads = {"viewid": 1412255,"retype": 1,"searchtype": 1,"pageid": 238013,"ver": "7.10.1.0131180001","head": {"cid": "09031027110141432611","ctok": "","cver": "1.0","lang": "01","sid": "8888","syscode": "09","auth": "null","extension": [{"name": "protocal","value": "https"}]},"contentType": "json"}
client = HTTPConnection(host)
a = client.request('POST', path, headers=headers, body=json.dumps(payloads).encode())
print(a)
resp = client.get_response()

print(resp.status)
print('='*20)
print(resp.headers)
print('='*20)
print(resp.read().decode('utf8'))
print('='*20)
