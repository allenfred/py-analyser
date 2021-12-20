# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

import numpy as np
import tushare as ts
import pandas as pd
from models.cn_daily_candles import CNDailyCandleDao
from models.trade_calendar import TradeCalendarDao
from models.stocks import StockDao
import time
from datetime import datetime
from config.common import TS_TOKEN
from api.daily_candle import get_cn_candles
from lib.util import used_time_fmt

pro = ts.pro_api(TS_TOKEN)
dailyCandleDao = CNDailyCandleDao()
calendarDao = TradeCalendarDao()
stockDao = StockDao()


if __name__ == "__main__":
    start = time.time()
    today = datetime.now().strftime("%Y-%m-%d")

    ts_code = '601857.SH'

    try:
        df = get_cn_candles({"ts_code": ts_code, "limit": 2000, "offset": 0})
        df = df.sort_values(by='trade_date', ascending=False)

        # 过滤出最新candle数据 (相较于db)
        db_df = dailyCandleDao.find_by_ts_code(ts_code)
        new_df = df.loc[~pd.to_datetime(df["trade_date"], format='%Y-%m-%d').isin(db_df["trade_date"].to_numpy())]

        dailyCandleDao.bulk_insert(new_df)
        stockDao.update({'ts_code': ts_code, 'candle_date': today})

        print('已更新 CN daily_candles :', ts_code, ': ', len(new_df), ' 条数据，用时 ',
              used_time_fmt(circle_start, time.time()), ', 总用时 ', used_time_fmt(start_time, time.time()))
    except Exception as e:
        stockDao.update({'ts_code': ts_code, 'candle_date': today})
        print('Error:', e)

    end = time.time()

    print('用时', used_time_fmt(start, end))
