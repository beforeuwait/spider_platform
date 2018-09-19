# 抓取平台概要设计

|**时间**|**撰写人**|**修改内容**|**备注**|
|:-----:|:-------:|:---------:|:-----:|
|2018-09-12|王家葳|建立文档|初稿|
|2018-09-18|王家葳|修改|初稿|

## 目录

- 背景
- 总体设计
- 总流程设计
- 各模块功能
	- 调度节点
	- 代理节点
- 消息框架设计


## 背景

采集的数据越多，积累的抓取脚本就越多

由此产生额外的维护工作变多

需要一个抓取平台，负责调度，抓取，监控各任务状态

同时提升抓取效率

## 总体设计

![总设计架构图][20]

该抓取平台采取并列计算的架构模式

需要一个调度节点，负责监控各节点状态，分发任务

其余的均为代理节点，通过调度节点启动，负责执行调度发来的任务

## 总流程设计

![总流程图][10]

可以看出，每一个Agent节点作为一个MsgCenter，肩负

- 启动进程
- 通信
- 类似路由查询的作用

## 消息框架设计

![消息框架设计][30]


[1]: https://github.com/beforeuwait/spider_platform/blob/master/%E8%AE%BE%E8%AE%A1%E6%96%87%E6%A1%A3/%E6%8A%93%E5%8F%96%E5%B9%B3%E5%8F%B0%E6%B5%81%E7%A8%8B%E5%9B%BE.jpg?raw=true

[2]: https://github.com/beforeuwait/spider_platform/blob/master/%E8%AE%BE%E8%AE%A1%E6%96%87%E6%A1%A3/%E6%8A%93%E5%8F%96%E5%B9%B3%E5%8F%B0%E6%B5%81%E7%A8%8B%E5%9B%BE09-18.jpg?raw=true

[3]: https://github.com/beforeuwait/spider_platform/blob/master/%E8%AE%BE%E8%AE%A1%E6%96%87%E6%A1%A3/%E6%B6%88%E6%81%AF%E6%A1%86%E6%9E%B6.jpg?raw=true