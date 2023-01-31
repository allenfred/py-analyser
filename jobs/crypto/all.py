# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

import time
from datetime import date, datetime, timedelta
from lib.util import used_time_fmt
from df import get_instruments
import analyzer
import redis

r = redis.Redis(host='8.210.170.98', port=6371, password='Uwy0Pf8mi', db=0)

if __name__ == "__main__":
    start = time.time()
    cur_min = time.localtime().tm_min
    cur_hour = time.localtime().tm_hour
    insts = list(get_instruments())

    for index, item in enumerate(insts):
        time.sleep(0.2)
        _start = time.time()
        if item['quote_currency'] == 'USDT' and item['volume_24h'] > 10000000:
            analyzer.run(item, 900)
            if cur_min == 0:
                analyzer.run(item, 3600)
            if cur_hour - ((cur_hour % 4) * 4) == 0 and cur_min == 0 and item['volume_24h'] > 100000000:
                analyzer.run(item, 7200)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    r.publish('analyzer', 'done')
    print(now, 'Analyzer 合约数', len(insts), ' 总用时 ', used_time_fmt(start, time.time()))
