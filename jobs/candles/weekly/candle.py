# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

import tushare as ts
import pandas as pd
from models.weekly_candles import WeeklyCandleDao
from models.weekly_indicators import WeeklyIndicatorDao
from models.weekly_signals import WeeklySignalDao
from models.stocks import StockDao
from lib.util import used_time_fmt
import time
from datetime import datetime
from config.common import TS_TOKEN
from api.weekly_candle import get_weekly_candles

pro = ts.pro_api(TS_TOKEN)
weeklyCandleDao = WeeklyCandleDao()
weeklyIndicatorDao = WeeklyIndicatorDao()
weeklySignalDao = WeeklySignalDao()
stockDao = StockDao()


if __name__ == "__main__":
    today = datetime.now().strftime("%Y%m%d")
    trade_dte = today
    start = time.time()
    is_last_req = False
    total_got_count = 0
    offset = 0

    while not is_last_req:
        circle_start = time.time()
        df = get_weekly_candles({"trade_date": trade_dte, "limit": 2000, "offset": offset})
        df_len = len(df)
        if len(df) < 2000:
            is_last_req = True
        else:
            offset += len(df)

        try:
            if df_len > 0:
                df['trade_date'] = pd.to_datetime(df["trade_date"], format='%Y-%m-%d')

                # 过滤出最新candle数据 (相较于db)
                db_df = weeklyCandleDao.find_by_trade_date(df['trade_date'][0])
                new_df = df.loc[~df["ts_code"].isin(db_df["ts_code"])]

                weeklyCandleDao.bulk_insert(new_df)

                print('已更新 CN weekly_candles :', len(new_df), ' 条数据，用时 ',
                      used_time_fmt(circle_start, time.time()), ', 总用时 ', used_time_fmt(start, time.time()))
            else:
                print(trade_dte, '没有周K线')

        except Exception as e:
            print(trade_dte, 'Error:', e)
            break

    print(today, '更新周K用时', used_time_fmt(start, time.time()))
