# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

import numpy as np
import tushare as ts
import pandas as pd
from models.weekly_candles import WeeklyCandleDao
from models.weekly_indicators import WeeklyIndicatorDao
from models.weekly_long_signals import WeeklyLongSignalDao
from models.stocks import StockDao
from lib.analytic_signals import analytic_signals
from lib.util import wrap_quota, used_time_fmt
import time
from datetime import datetime
from config.common import TS_TOKEN
from api.weekly_candle import get_candles

pro = ts.pro_api(TS_TOKEN)
weeklyCandleDao = WeeklyCandleDao()
weeklyIndicatorDao = WeeklyIndicatorDao()
weeklyLongSignalDao = WeeklyLongSignalDao()
stockDao = StockDao()

if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    start = time.time()

    while True:
        circle_start = time.time()
        ts_code = stockDao.find_one_weekly_not_ready(today)

        if ts_code is None:
            break

        df = get_candles({"ts_code": ts_code, "limit": 500, "offset": 0})

        try:
            df = df.sort_values(by='trade_date', ascending=True)
            df['trade_date'] = pd.to_datetime(df["trade_date"], format='%Y-%m-%d')
            df['num'] = df.index[::-1].to_numpy()
            df = df.set_index('num')

            df = wrap_quota(df)
            df_len = len(df)

            # 过滤出最新candle数据 (相较于db)
            db_df = weeklyCandleDao.find_by_ts_code(ts_code)
            new_df = df.loc[~df["trade_date"].isin(db_df["trade_date"].to_numpy())]

            weeklyCandleDao.bulk_insert(new_df)
            weeklyIndicatorDao.bulk_insert(df, ts_code)

            # 更新weekly signal
            df = analytic_signals(df)
            small_df = df.iloc[df_len - 30: df_len]
            weeklyLongSignalDao.bulk_insert(small_df, ts_code)
            stockDao.update({'ts_code': ts_code, 'weekly_date': today})

            print('已更新 CN weekly_candles :', ts_code, ': ', len(new_df), ' 条数据，用时 ',
                  used_time_fmt(circle_start, time.time()), ', 总用时 ', used_time_fmt(start, time.time()))
        except Exception as e:
            print('Error:', e)
            break
            stockDao.update({'ts_code': ts_code, 'weekly_date': today})

    print('用时', used_time_fmt(start, time.time()))
