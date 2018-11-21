# coding=utf-8


class Demo():

    def __init__(self, name):
        self.name = name

    def oupt(self):
        print('当前实例名字:{0}'.format(self.name))

    def __del__(self):
        print('删除 {0}'.format(self.name))
        del self.name

d = Demo('xiaoming')
d.oupt()