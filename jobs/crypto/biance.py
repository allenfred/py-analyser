# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

import time
from lib.util import used_time_fmt
from df import get_inst_df
import analyzer


if __name__ == "__main__":
    start = time.time()
    cur_min = time.localtime().tm_min
    insts = get_inst_df('biance')

    for index, item in enumerate(insts):
        time.sleep(0.1)
        _start = time.time()
        inst_id = item['instrument_id']
        analyzer.run(item, 900)
        if cur_min == 0:
            analyzer.run(item, 3600)

    print('Analyzer 合约数', len(insts), ' 总用时 ', used_time_fmt(start, time.time()))

