# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

import pandas as pd
from models.db import DBSession
from models.cn_daily_candles import CNDailyCandleDao
from models.daily_indicators import DailyIndicatorDao
from models.daily_long_signals import DailyLongSignalDao
from models.daily_short_signals import DailyShortSignalDao
from models.stock_long_signals import StockLongSignalDao
from models.stock_short_signals import StockShortSignalDao
from models.analytic_signals import AnalyticSignalDao

from models.stocks import StockDao
from sqlalchemy import text
from talib import SMA, EMA, MACD
from lib.bias import bias
from lib.ma_slope import slope
from lib.magic_nine_turn import td
from lib.signals import long_signals
from lib.analytic_signals import analytic_signals
from lib.util import wrap_technical_indicator, used_time_fmt
import time
from datetime import datetime, date
import numpy as np
from api.daily_candle import get_cn_candles
import time
import threading

stockDao = StockDao()
dailyCandleDao = CNDailyCandleDao()
dailyIndicatorDao = DailyIndicatorDao()
dailyLongSignalDao = DailyLongSignalDao()
dailyShortSignalDao = DailyShortSignalDao()
stockLongSignalDao = StockLongSignalDao()
stockShortSignalDao = StockShortSignalDao()
analyticDao = AnalyticSignalDao()


def scan_daily_candles(ts_code, exchange_type, scan_date):
    table_name = 'cn_daily_candles'
    if exchange_type == 'HK':
        table_name = 'hk_daily_candles'
    if exchange_type == 'US':
        table_name = 'us_daily_candles'

    start = time.time()
    statement = dailyCandleDao.session.execute(text("select trade_date, open, close, high, low, pct_chg from "
                                                    + table_name + " where ts_code = :ts_code "
                                                    + "and trade_date > '2015-01-01' and open is not null "
                                                      "and close is not null and high is not null and"
                                                    + " low is not null "
                                                    + "order by trade_date desc "
                                                      "limit 250").params(ts_code=ts_code))

    df = pd.DataFrame(statement.fetchall(), columns=['trade_date', 'open', 'close', 'high', 'low', 'pct_chg'])

    if len(df) > 60:
        df = df.sort_values(by='trade_date', ascending=True)
        df['num'] = df.index[::-1].to_numpy()
        df = df.set_index('num')
        df['ts_code'] = ts_code
        df['exchange'] = exchange_type

        try:
            df = wrap_technical_indicator(df)
            dailyIndicatorDao.bulk_insert(df, ts_code)

            # 会对 bias6/bias12/bias24/bias60/bias72/bias120 发生替换
            long_signals(df)
            analytic_signals(df)
            df_len = len(df)

            small_df = df.iloc[df_len - 60: df_len]
            item = df.iloc[df_len - 1].to_dict()

            analyticDao.bulk_insert(small_df, ts_code)
            dailyLongSignalDao.bulk_insert(small_df, ts_code)
            stockLongSignalDao.upsert(item)

            stockDao.update({'ts_code': ts_code, 'scan_date': scan_date})

            print_str = '扫描成功: ' + str(ts_code) + ', 最新K线时间: ' + str(scan_date) + \
                        ', 用时 ' + str(used_time_fmt(start, time.time()))
            print(print_str)
        except Exception as e:
            print('更新 ', ts_code, 'Catch Error:', e)
            stockDao.update({'ts_code': ts_code, 'scan_date': scan_date})
    else:
        stockDao.update({'ts_code': ts_code, 'scan_date': scan_date})
        print('股票代码: ', ts_code, ' 没有足够行情数据')
