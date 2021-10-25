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
    limit = 6000
    offset = 0
    totalGotCount = 0

    while is_not_last_req:

        df = pro.us_daily(**{
            "ts_code": "",
            "trade_date": today,
            "start_date": "",
            "end_date": "",
            "offset": offset,
            "limit": limit
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
        if len(df) < limit:
            is_not_last_req = False
        else:
            offset += len(df)
        df['exchange'] = 'US'

        if len(df) > 0:
            print('拉取 US candles ', len(df), ' 条数据')
            dailyCandleDao.bulk_upsert(df)
            print('已获取 US daily_candles ', totalGotCount, ' 条数据，用时 ',
                  round(time.time() - start, 2), ' s')

    calendarDao.set_candle_ready('US', datetime.strftime(today, "%Y-%m-%d"))

    end = time.time()
    print('用时', round(end - start, 2), 's')
