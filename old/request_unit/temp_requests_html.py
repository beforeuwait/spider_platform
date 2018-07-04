"""
测试学习 requests_html库

"""

"""
from __future__ import absolute_import
from requests_html import HTMLSession


DEFAULT_ENCODE = 'utf8'

session = HTMLSession()

r = session.get('https://www.ctrip.com/')

print(r.html.text)

for each in r.html.absolute_links:
    print(each)
"""

# 测试 pyquery
TEST_HTML = """
<html>
    <head>
        <p title="wang">hello</p>
        <p id="1">我会带着笑脸</p>
    </head>
    <body>
        <div class="part">
            <tr>
                <td>wang</td>
                <td>jia</td>
                <td>wei</td>
            </tr>
        </div>
    </body>
</html>
"""
from pyquery import PyQuery as pq
from lxml import etree

d = pq(TEST_HTML)
# print(d(".part"))
# print(d("#1").text())
print(d("body").text())

# e = etree.fromstring(TEST_HTML)
# print(e.xpath('//head/p[2]/text()'))