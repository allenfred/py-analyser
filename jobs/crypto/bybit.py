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


if __name__ == "__main__":
    start = time.time()
    cur_min = time.localtime().tm_min
    insts = list(get_instruments('bybit'))

    for index, item in enumerate(insts):
        time.sleep(0.1)
        _start = time.time()
        if item['instrument_id'].endswith('USDT'):
            analyzer.run(item, 900)
            if cur_min == 0:
                analyzer.run(item, 3600)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now, 'Analyzer 合约数', len(insts), ' 总用时 ', used_time_fmt(start, time.time()))

