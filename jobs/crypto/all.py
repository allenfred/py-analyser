# -- coding: utf-8 -

from lib.util import used_time_fmt
from jobs.crypto.df import get_instruments
import jobs.crypto.analyzer as analyzer
import redis
from datetime import date, datetime, timedelta
import time
import os
import sys

path = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)


r = redis.Redis(host='8.210.170.98', port=6371, password='Uwy0Pf8mi', db=0)


def analysis():
    start = time.time()
    cur_min = time.localtime().tm_min
    cur_hour = time.localtime().tm_hour
    insts = list(filter(lambda x: x['volume_24h'] > 5000000 and not x['exchange']
                 == 'bybit' and x['quote_currency'] == 'USDT', get_instruments()))
    scan_cnt = 0

    for index, item in enumerate(insts):
        time.sleep(0.2)

        scan_cnt += 1
        # job for every 15mins
        analyzer.run(item, 900)

        if cur_min == 15:
            # job for every hour
            analyzer.run(item, 3600)

        if cur_hour % 4 == 0:
            # job for every 4 hour
            analyzer.run(item, 14400)

        if cur_hour % 12 == 0:
            # job for every 12 hour
            analyzer.run(item, 43200)

        if cur_hour == 0:
            # job for every day
            analyzer.run(item, 86400)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    r.publish('analyzer', 'done')

    print(now, 'Analyzer 合约数', scan_cnt, ' 总用时 ',
          used_time_fmt(start, time.time()))


if __name__ == "__main__":
    analysis()
