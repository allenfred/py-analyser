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
from datetime import datetime, timedelta
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

    data = get_weekly_candles({
        "ts_code": '000001.SZ',
        "start_date": (datetime.now() + timedelta(days=-180)).strftime("%Y%m%d"),
        "end_date": datetime.now().strftime("%Y%m%d"),
        "limit": 20,
        "offset": 0
    })

    for index, item in enumerate(data):
        is_last_req = False
        offset = 0
        trade_dte = data['trade_date'][index]

        while not is_last_req:
            circle_start = time.time()
            df = get_weekly_candles({
                "trade_date": trade_dte,
                "limit": 4000,
                "offset": offset
            })
            df_len = len(df)

            if len(df) < 4000:
                is_last_req = True
            else:
                offset += len(df)

            try:
                if df_len > 0:
                    df['trade_date'] = pd.to_datetime(df["trade_date"], format='%Y-%m-%d')

                    # 过滤出最新candle数据 (相较于db)
                    db_df = weeklyCandleDao.find_by_trade_date(trade_dte)
                    new_df = df.loc[~df["ts_code"].isin(db_df["ts_code"])]

                    weeklyCandleDao.bulk_insert(new_df)

                    print('已更新', trade_dte, ' CN weekly_candles :', len(new_df), ' 条数据，用时 ',
                          used_time_fmt(circle_start, time.time()), ', 总用时 ', used_time_fmt(start, time.time()))
                else:
                    print(trade_dte, '没有周K线')

            except Exception as e:
                print(trade_dte, 'Error:', e)
                break

    print('更新周K用时', used_time_fmt(start, time.time()))
