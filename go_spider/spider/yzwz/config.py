# coding=utf-8

# 每个省/城的代码

prov_code = {
    '四川': 'sc',
    '重庆': 'cq',
    '北京': 'bj',
    '天津': 'tj',
    '河北': 'he',
    '山西': 'sx',
    '内蒙古': 'nm',
    '辽宁': 'ln',
    '吉林': 'jl',
    '黑龙江': 'hl',
    '上海': 'sh',
    '江苏南京': 'nkg',
    '江苏无锡': 'wux',
    '江苏徐州': 'xuz',
    '江苏常州': 'czx',
    '江苏苏州': 'szv',
    '江苏南通': 'ntg',
    '江苏连云港': 'lyg',
    '江苏淮安': 'has',
    '江苏盐城': 'ynz',
    '江苏扬州': 'yzo',
    '江苏镇江': 'zhe',
    '江苏泰州': 'tzs',
    '江苏宿迁': 'suq',
    '浙江杭州': 'hgh',
    '浙江宁波': 'ngb',
    '浙江温州': 'wnz',
    '浙江嘉兴': 'jix',
    '浙江湖州': 'hzh',
    '浙江绍兴': 'sxg',
    '浙江金华': 'jha',
    '浙江衢州': 'quz',
    '浙江舟山': 'zos',
    '浙江台州': 'tzz',
    '浙江丽水': 'lss',
    '安徽': 'ah',
    '福建': 'fj',
    '江西': 'jx',
    '山东': 'sd',
    '河南': 'ha',
    '湖北': 'hb',
    '湖南': 'hn',
    '广东': 'gd',
    '广西': 'gx',
    '海南': 'hi',
    '贵州': 'gz',
    '云南': 'yn',
    '西藏': 'xz',
    '陕西': 'sn',
    '甘肃': 'gs',
    '青海': 'qh',
    '宁夏': 'nx',
    '新疆': 'xj',
}

# 不同类型的checkType的代码

check_type = {
    'yzwz': 'pZodtaHnfvXgevYt',   # 重点车辆严重违章
    'kszb': 'mRhjvihNkSGFKvFN',   # 驾驶人考试作弊
    'm12f': 'KTqvhMPrjsWfsZWG',   # 满12分被降级
    'swsg': 'YhIXAvDLcynICIFh'    # 死亡事故
}

# headers

headers_home = {
    'Host': 'cq.122.gov.cn',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
    }

headers_vio = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'sc.122.gov.cn',
    'Referer': 'https://sc.122.gov.cn/views/notice.html',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    }

headers_captcha = {
    'Host': 'cq.122.gov.cn',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://cq.122.gov.cn/views/viopub.html',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
    }

headers_check = {
    'Host': 'cq.122.gov.cn',
    'Connection': 'keep-alive',
    'Content-Length': '26',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'https://sc.122.gov.cn',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://sc.122.gov.cn/views/viopub.html',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
    }

headers_list = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '76',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'xz.122.gov.cn',
    'Origin': 'https://xz.122.gov.cn',
    'Referer': 'https://xz.122.gov.cn/views/viopub.html',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

headers_detail = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '23',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'sc.122.gov.cn',
    'Origin': 'https://sc.122.gov.cn',
    'Referer': 'https://sc.122.gov.cn/views/viopubdetail.html?vioid=51000110000001917901',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

# urls

url_home = 'https://{0}.122.gov.cn'

url_viopub = 'https://{0}.122.gov.cn/views/viopub.html'

url_check = 'https://{0}.122.gov.cn/m/tmri/captcha/checkType'

url_c = 'https://{0}.122.gov.cn/m/tmri/captcha/math?nocache={1}'

url_list = 'https://{0}.122.gov.cn/m/viopub/getVioPubList'

url_detail = 'https://sc.122.gov.cn/m/viopub/getVioPubDetail'

# params

payloads_list = {
    'page': '0',
    'size': '20',
    'startTime': '2019-04-27',
    'endTime': '2019-05-27',
    'gsyw': '01',
    'csessionid': '14'
}