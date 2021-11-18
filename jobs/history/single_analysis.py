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
from jobs.scan.daily_candle import scan_daily_candles
import threading

stockDao = StockDao()
dailyCandleDao = CNDailyCandleDao()
dailyIndicatorDao = DailyIndicatorDao()
dailyLongSignalDao = DailyLongSignalDao()
dailyShortSignalDao = DailyShortSignalDao()

stockLongSignalDao = StockLongSignalDao()
stockShortSignalDao = StockShortSignalDao()

analyticDao = AnalyticSignalDao()


def scan():
    job_start = time.time()

    ts_code = 'BIDU'
    s = text("select trade_date, open, close, high, low, `pct_chg` from us_daily_candles where ts_code = :ts_code "
             + "order by trade_date desc limit 300")

    statement = dailyCandleDao.session.execute(s.params(ts_code=ts_code))
    df = pd.DataFrame(statement.fetchall(), columns=['trade_date', 'open', 'close', 'high', 'low', 'pct_chg'])
    df = df.sort_values(by='trade_date', ascending=True)
    df['num'] = df.index[::-1].to_numpy()
    df = df.set_index('num')
    df['ts_code'] = ts_code
    df['exchange'] = 'US'

    # calc ma/slope/...
    df = wrap_technical_indicator(df)

    # 会对 bias6/bias12/bias24/bias60/bias72/bias120 发生替换
    long_signals(df)
    analytic_signals(df)

    df_len = len(df)

    small_df = df.iloc[df_len - 60: df_len]
    item = df.iloc[df_len - 1].to_dict()

    scan_date = df.iloc[len(df) - 1].trade_date

    analyticDao.reinsert(small_df, ts_code)
    dailyLongSignalDao.reinsert(small_df, ts_code)
    stockLongSignalDao.upsert(item)

    stockDao.update({'ts_code': ts_code, 'scan_date': scan_date})

    print('扫描成功', used_time_fmt(job_start, time.time()))


if __name__ == "__main__":
    ts_code = '600183.SH'
    # scan_daily_candles(ts_code, 'CN', '2021-11-16')
    # scan()
    scan_date = '2021-11-17'
    stock_stmts = stockDao.session.execute(text("select ts_code from stocks where (scan_date is null or scan_date"
                                                "< :scan_date) and (exchange = 'SSE' or exchange = 'SZSE') limit 1"
                                                ).params(scan_date=scan_date))
    stock_result = stock_stmts.fetchall()
    stockDao.session.commit()
    print(stock_result)
    print('扫描成功')

