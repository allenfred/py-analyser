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
    insts = get_instruments('okex')

    for index, item in enumerate(insts):
        time.sleep(0.1)
        _start = time.time()
        if item['volume_24h'] * item['last'] * item['contract_val'] > 10000000 and not item['last'] < 0.00001:
            analyzer.run(item, 900)
            if cur_min == 0:
                analyzer.run(item, 3600)
        else:
            print(item['instrument_id'], '成交量或价格过低')

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now, 'Analyzer 合约数', len(insts), ' 总用时 ', used_time_fmt(start, time.time()))



