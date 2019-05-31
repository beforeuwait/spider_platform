之前写的那版http api不好用
    
1. 执行时间长

2. session.proxies里有代理，但是请求仍旧从本地发出

3. 自动判断网页编码出错

4. 逻辑复杂

5. 日志看不懂

6. 引用不便捷

重写一遍

写好顺手为止

发现需要的功能 requests的作者都帮我想到了

我直接二次封装就行了

### 使用

    from requestApi import HttpApi
    api = HttpApi()
    html = api.send_args_get_html(
        url=xxxxx,
        headers=xxxxxx,
        params=xxxxxx,
        payloads=xxxxxx,
        cookies=xxxxxx,
        method='get/post',
        isProxy='yes/no',
        isSession='yes/no',
        code='gbk/utf-8/xxx'
    )

    需要传入的参数包括
    url:    链接
    headers:    请求该链接的headers
    cookies:    该链接的cookie
    params:     get请求的params
    payloads:   post请求的data
    method:     这是个get/post 请求
    isProxy:    是否使用代理
    isSession:  在有复杂操作的请求建议用session
    code:       html解码 utf-8/gbk...