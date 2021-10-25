import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

import tushare as ts
import pandas as pd
from models.daily_candles import DailyCandleDao
import time
from datetime import datetime, date
from config.common import TS_TOKEN

pro = ts.pro_api(TS_TOKEN)
dailyCandleDao = DailyCandleDao()

if __name__ == "__main__":

    today = date.today().strftime("%Y%m%d")
    start = time.time()
    is_not_last_req = True
    df = pd.DataFrame(data={})
    limit = 3000
    offset = 0
    totalGotCount = 0

    while is_not_last_req:
        df = pro.hk_daily(**{
            "ts_code": "",
            "trade_date": today,
            "start_date": "",
            "end_date": "",
            "limit": limit,
            "offset": offset
        }, fields=[
            "ts_code",
            "trade_date",
            "open",
            "high",
            "low",
            "close",
            "pre_close",
            "change",
            "pct_chg",
            "vol",
            "amount"
        ])

        totalGotCount += len(df)
        if len(df) < limit:
            is_not_last_req = False
        else:
            offset += len(df)
        df['exchange'] = 'HK'

        if len(df) > 0:
            print('拉取 HK candles ', len(df), ' 条数据')
            dailyCandleDao.bulk_upsert(df)
            print('更新 HK daily_candles ', len(df), ' 条数据')

    calendarDao.set_candle_ready('HK', datetime.strftime(today, "%Y-%m-%d"))

    end = time.time()
    print('用时', round(end - start, 2), 's')