import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

import tushare as ts
import pandas as pd
from models.daily_candles import DailyCandleDao
import time
from datetime import date
from config.common import TS_TOKEN

pro = ts.pro_api(TS_TOKEN)
dailyCandleDao = DailyCandleDao()

if __name__ == "__main__":

    today = date.today().strftime("%Y%m%d")
    start = time.time()
    is_not_last_req = True
    df = pd.DataFrame(data={})
    offset = 0
    totalGotCount = 0

    while is_not_last_req:

        # 拉取日线数据
        df = pro.us_daily(**{
            "ts_code": "",
            "trade_date": today,
            "start_date": "",
            "end_date": "",
            "offset": "",
            "limit": ""
        }, fields=[
            "ts_code",
            "trade_date",
            "close",
            "open",
            "high",
            "low",
            "pre_close",
            "pct_change",
            "vol",
            "amount",
            "vwap",
            "total_mv",
            "pe",
            "pb",
            "change",
            "turnover_ratio"
        ])

        totalGotCount += len(df)
        if len(df) < 6000:
            is_not_last_req = False
        else:
            offset += len(df)

        print('已获取 US daily_candles ', totalGotCount, ' 条数据，用时 ',
              round(time.time() - start, 2), ' s')

        dailyCandleDao.bulk_upsert(df)

    end = time.time()
    print('用时', round(end - start, 2), 's')