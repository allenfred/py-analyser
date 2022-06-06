# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

from lib.crypto.analyze import analyze
import time
from lib.util import set_quota, used_time_fmt
from df import get_inst_df, get_klines_df


if __name__ == "__main__":
    start = time.time()

    insts = get_inst_df()

    for index, item in enumerate(insts):
        # df.loc[index] = {
        #     "trade_date": item["timestamp"],
        #     "open": item["open"],
        #     "high": item["high"],
        #     "low": item["low"],
        #     "close": item["close"],
        #     "vol": float(item["volume"]),
        #     "pct_chg": ((item["close"] - item["open"]) * 100) / item["open"]
        # }

        print(item['instrument_id'])
