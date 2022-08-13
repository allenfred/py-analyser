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
from lib.stock.analyze import analyze
from lib.util import set_quota, used_time_fmt
import time
from datetime import datetime
from config.common import TS_TOKEN


pro = ts.pro_api(TS_TOKEN)
weeklyCandleDao = WeeklyCandleDao()
weeklyIndicatorDao = WeeklyIndicatorDao()
weeklySignalDao = WeeklySignalDao()
stockDao = StockDao()


if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    start = time.time()
    flag = True

    while flag:
        circle_start = time.time()
        ts_code = stockDao.find_one_weekly_not_ready(today)
        time.sleep(0.2)

        if ts_code is None:
            break

        df = weeklyCandleDao.find_by_ts_code(ts_code, 200)
        df_len = len(df)

        try:
            if df_len > 30:
                df = df.sort_values(by='trade_date', ascending=True)
                df['trade_date'] = pd.to_datetime(df["trade_date"], format='%Y-%m-%d')
                df['num'] = df.index[::-1].to_numpy()
                df = df.set_index('num')
                df['ts_code'] = ts_code

                df = set_quota(df)

                # 更新weekly signal
                df = analyze(df)
                small_df = df.iloc[df_len - 10: df_len]
                weeklySignalDao.reinsert(small_df, ts_code)

                print('分析完成 :', ts_code, ', 用时 ',
                      used_time_fmt(circle_start, time.time()), ', 总用时 ', used_time_fmt(start, time.time()))
            else:
                print('新股周K线不足30')

            stockDao.update({'ts_code': ts_code, 'weekly_date': today})

        except Exception as e:
            print(ts_code, 'Error:', e)
            break

    print(today, '用时', used_time_fmt(start, time.time()))
