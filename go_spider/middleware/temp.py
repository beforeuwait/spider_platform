# coding=utf-8


msg = {"task": "yzwz_list", "args": "四川"}

import redis
import json

cli = redis.Redis(host='localhost', port=6379, db=1)

cli.lpush('task', json.dumps(msg))