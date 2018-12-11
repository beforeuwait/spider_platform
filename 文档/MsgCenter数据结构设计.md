# 消息中心数据结构设计

## 调度  **--task-->** MsgCenter

从调度派发**任务**到消息中心
	
	task = {
		'task_name': 'demo',
		'execute': 'go/kill',		# 执行or kill 掉任务
		'code': 'xxxxx(完整的代码)',
		'other': '别的交代'
	}

## MsgCenter --feedback--> 调度
由消息中心向调度反馈节点当前状态和任务执行状态

	feed_back = {
		'msg_type': 'task/node',		# 任务反馈/节点状态
		'task_state': 'xxxxxx',			# 任务状态
		'node_state': 'xxxxxx',			# 节点状态
	}

## MsgCenter **--task-->** TaskReader
向TaskReader发布任务，由TaskReader去维护在MsgC里的两个索引

	task = {
		'task_name': 'demo',
		'execute': 'go/kill',
		'code': 'xxxxxxxx',
	}


### TaskReader

> task_ini
		
	存redis里,以hash方式存储
	task_info = {
		'demo': {
			'demo_persistence': 'C:\Users\forme\Desktop\Github\spider_platform\Node\demo',
			'demo_parser': 'C:\Users\forme\Desktop\Github\spider_platform\Node\demo',
			'demo_downloader': 'C:\Users\forme\Desktop\Github\spider_platform\Node\demo',
			'demo_seed': 'C:\Users\forme\Desktop\Github\spider_platform\Node\demo'
			},
		'task2': {
			'task2_persistence': 'path',
			'task2_seed': 'path',
			'task2_downloader': 'path',
			'task2_parser': 'path'
		}，
			
	}

> que_ini

	存redis里，放集合里
	que_ini = (
		'demo', 'task2', 'task3', 'task4'
	)

## MsgCenter --msg--> TaskReader

向TaskReader发送消息， 在索引中去掉某某任务

	task = {
		'task_name': 'demo',
		'execute': 'kill',
		'code': 'xxxxxxxx',
	}

## TaskExecutor --msg--> MsgCenter

由TaskExecutor向MsgC反馈 任务的状态

	task_state = {
		'task_name': '',
		''
	}
	## 实际中再设计

## MsgCenter <--msg--> process

各个功能进程同MsgC通信
	
	实际中再设计