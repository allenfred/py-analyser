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
from models.stock_long_signals import StockLongSignalDao

from models.stocks import StockDao
from sqlalchemy import text
from lib.analytic_signals import analytic_signals
from lib.util import wrap_quota, used_time_fmt
import time
from datetime import datetime, date, timedelta
import numpy as np
from api.daily_candle import get_cn_candles
import time
import threading

stockDao = StockDao()
dailyCandleDao = CNDailyCandleDao()
dailyIndicatorDao = DailyIndicatorDao()
dailyLongSignalDao = DailyLongSignalDao()
stockLongSignalDao = StockLongSignalDao()


def get_amount(exchange, amount):
    if not amount:
        return 0

    if exchange == 'HK' or exchange == 'US':
        return int(amount) * 1
    else:
        return int(amount) * 1000


def scan_daily_candles(ts_code, exchange_type, scan_date):
    start = time.time()
    table_name = 'cn_daily_candles'
    monthly_ago = date.today() - timedelta(days=20)
    if exchange_type == 'HK':
        table_name = 'hk_daily_candles'
    if exchange_type == 'US':
        table_name = 'us_daily_candles'

    statement = dailyCandleDao.session.execute(text("select trade_date, open, high, close, low, pct_chg, amount from "
                                                    + table_name + " where ts_code = :ts_code "
                                                    + "and trade_date > '2015-01-01' and open is not null "
                                                      "and close is not null and high is not null and"
                                                    + " low is not null "
                                                    + "order by trade_date desc "
                                                      "limit 360").params(ts_code=ts_code))

    df = pd.DataFrame(statement.fetchall(), columns=['trade_date', 'open', 'high', 'close', 'low', 'pct_chg', 'amount'])
    df = df.fillna(0)
    last_amount = 0
    list_status = 'L'

    if len(df) > 1:
        last_amount = get_amount(exchange_type, df.iloc[len(df) - 1].amount)

        # 剔除退市股
        if df.iloc[0].trade_date < monthly_ago:
            list_status = 'D'

    if list_status == 'L' and len(df) > 60 and last_amount > 10000000:
        df = df.sort_values(by='trade_date', ascending=True)
        df['num'] = df.index[::-1].to_numpy()
        df = df.set_index('num')
        df['ts_code'] = ts_code

        try:
            df = wrap_quota(df)
            dailyIndicatorDao.bulk_insert(df, ts_code)
            # 会对 bias6/bias12/bias24/bias60/bias72/bias120 发生替换
            df = analytic_signals(df)
            df_len = len(df)

            small_df = df.iloc[df_len - 30: df_len]
            signal = df.iloc[df_len - 1].to_dict()

            dailyLongSignalDao.bulk_insert(small_df, ts_code)
            stockLongSignalDao.upsert(signal)

            stockDao.update({'ts_code': ts_code, 'scan_date': scan_date, 'amount': last_amount, 'list_status': 'L'})

            print_str = '扫描成功: ' + str(ts_code) + ', 最新K线时间: ' + str(scan_date) + \
                        ', 用时 ' + str(used_time_fmt(start, time.time()))
            print(print_str)
        except Exception as e:
            print('更新 ', ts_code, 'Catch Error:', e)
            stockDao.update({'ts_code': ts_code, 'scan_date': scan_date, 'amount': last_amount, 'list_status': 'L'})
    else:
        stockDao.update({'ts_code': ts_code, 'scan_date': scan_date, 'amount': last_amount, 'list_status': list_status})
        print('股票代码: ', ts_code, ' 不满足扫描条件')
