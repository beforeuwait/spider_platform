# coding=utf-8



import redis
import json
import sys

cli = redis.Redis(host='192.168.2.88', password='QWE123', port=6379, db=1)





if __name__ == '__main__':
    prov = sys.argv[1]
    msg = {"task": "yzwz_list", "args": prov}

    cli.lpush('task', json.dumps(msg))