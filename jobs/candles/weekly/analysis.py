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
from api.weekly_candle import get_weekly_candles


pro = ts.pro_api(TS_TOKEN)
weeklyCandleDao = WeeklyCandleDao()
weeklyIndicatorDao = WeeklyIndicatorDao()
weeklySignalDao = WeeklySignalDao()
stockDao = StockDao()


def ready_weekly_klines():
    _today = datetime.now().strftime("%Y%m%d")
    _today = '20220602'
    _start_time = time.time()
    is_last_req = False
    offset = 0
    _cnt = 0

    while not is_last_req:
        klines_df = get_weekly_candles({"trade_date": _today, "limit": 2000, "offset": offset})

        if len(klines_df) < 2000:
            is_last_req = True
        else:
            offset += len(klines_df)

        try:
            if len(klines_df) > 0:
                klines_df['trade_date'] = pd.to_datetime(klines_df["trade_date"], format='%Y-%m-%d')

                # 过滤出最新candle数据 (相较于db)
                db_df = weeklyCandleDao.find_by_trade_date(klines_df['trade_date'][0])
                new_df = klines_df.loc[~klines_df["ts_code"].isin(db_df["ts_code"])]
                if len(new_df) == 0:
                    break

                _cnt += len(new_df)
                weeklyCandleDao.bulk_insert(new_df)

                print('已更新 CN weekly_candles :', len(new_df))
            else:
                print(_today, '没有周K线')

        except Exception as e:
            print(_today, 'Error:', e)
            break

    return _cnt


if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    start = time.time()
    flag = True

    ready_weekly_klines()

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

                print('分析完成 :', ts_code, '，用时 ',
                      used_time_fmt(circle_start, time.time()), ', 总用时 ', used_time_fmt(start, time.time()))
            else:
                print('新股周K线不足30')

            stockDao.update({'ts_code': ts_code, 'weekly_date': today})

        except Exception as e:
            print(ts_code, 'Error:', e)
            break
            stockDao.update({'ts_code': ts_code, 'weekly_date': today})

    print(today, '用时', used_time_fmt(start, time.time()))
