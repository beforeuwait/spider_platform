
# 抓取平台
> 架构图

![平台框架图][1]


- 模块解析
	
	1. 后台
	2. 调度器
	3. 任务引擎
	4. 脚本库
	5. slave
	6. 持久化引擎
	7. 消息队列

- 开发环境

        python version: 3.6.2


## 日志:

2018/02/09 开始项目

* 代码库：主要作为存放对应脚本的解析规则和请求方式

* 代码形式？ dict形式以json传递？slave又如何调用？

* 放在哪？本地写一个包？还是放介质里

Done:

今日主要用来编写代码库，目前的思路主要体现在，代码库使用mongo，而不同的项目则以json放入mongo中，长这个样子
		
		'大众点评' = {
			'shop_list': {
				'requests_methed': {
					'method': 'GET',
					'headers': {
						'xxxx': 'xxxxx',
						'xxxx': 'xxxxx'
					},
				}
				'parse': {
					'list': '//div[@class="xxxxx"]'
					'params': {
						'key1': 'div[@class="xxxx"]/text()'
						'........'
					}
				}
			},
			'shop_info': {
				'........'
			},
			'shop_cmt': {
				'........'
			}
		}

消息队列的通信，目前暂时没有引入，通过写入本地文件，模块间通过读取文件“假装实现通信”
‘slave’这个模块，不仅要从人物队列里拿到人物，还要从代码库里请求相应的请求/解析数据

2018/02/11

* 今日计划开发 request请求model

2018/02/24

* 继续开工

[1]:https://github.com/beforeuwait/spider_platform/blob/master/%E5%B9%B3%E5%8F%B0%E6%A1%86%E6%9E%B6.png?raw=true
