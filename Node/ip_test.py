# coding=utf-8

from HTTP import RequestAPI

url = 'http://2019.ip138.com/ic.asp'
# headers = {'Proxy-Switch-Ip': 'yes'}
api = RequestAPI()

p = api.receive_and_request(url=url, method='get')
print(p)
api.dr.sh.discard_proxy()
p = api.receive_and_request(url=url, method='get')

print(p)
