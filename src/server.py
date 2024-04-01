import time
import os
import sys
import redis
import json

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

from lib.util import get_timestamp
from jobs.crypto.all import analysis

r = redis.Redis(host='8.210.170.98', port=6371, password='Uwy0Pf8mi', db=0)


def message_handler(message):
    print(json.dumps(message))


def jsonDefault(o):
    return o.decode('utf-8')


p = r.pubsub()
p.subscribe('klines')

while True:
    msg = p.get_message()
    if msg is not None:
        print(get_timestamp(), msg)
        
        if type(msg['data']) == bytes:
            data = json.loads(msg['data'])
            print(get_timestamp(), data)
            analysis()