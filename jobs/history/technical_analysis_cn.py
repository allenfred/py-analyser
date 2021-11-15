# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

import pandas as pd
from models.db import engine, DBSession
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
from lib.signal_analysis import rise_support_analysis
from lib.util import wrap_technical_indicator, used_time_fmt
import time
from datetime import datetime, date
import numpy as np
from api.daily_candle import get_cn_candles
import time
import threading
import psutil
import multiprocessing
from multiprocessing import Pool
from jobs.scan.daily_candle import scan_daily_candles

stockDao = StockDao()
dailyCandleDao = CNDailyCandleDao()
dailyIndicatorDao = DailyIndicatorDao()
dailyLongSignalDao = DailyLongSignalDao()
dailyShortSignalDao = DailyShortSignalDao()
stockLongSignalDao = StockLongSignalDao()
stockShortSignalDao = StockShortSignalDao()
analyticDao = AnalyticSignalDao()


def multi_scan(stocks):
    pool_cnt = multiprocessing.cpu_count()

    if pool_cnt > 8:
        pool_cnt = 8
    else:
        pool_cnt = 8

    p = Pool(pool_cnt)

    for i in range(len(stocks)):
        p.apply_async(scan_daily_candles, args=(stocks[i][0], 'CN', scan_date,))

    p.close()
    p.join()


if __name__ == "__main__":
    job_start = time.time()
    candle = dailyCandleDao.find_latest_candle()
    total_scan_cnt = 0

    if candle is None:
        print('没有K线数据')
        quit()

    scan_date = candle['trade_date']

    while True:
        used_time = round(time.time() - job_start, 0)
        if used_time > 3600 * 5:
            break

        session = DBSession()
        stock_stmts = session.execute(text("select ts_code from stocks where (scan_date is null or scan_date"
                                           " < :scan_date) and "
                                           "(exchange = 'SSE' or exchange = 'SZSE')  limit 20").params(
            scan_date=scan_date))
        stock_result = stock_stmts.fetchall()
        session.commit()
        session.close()
        engine.dispose()

        if len(stock_result) == 0:
            print('没有需要扫描的股票')
            break

        multi_scan(stock_result)
        total_scan_cnt += len(stock_result)
        print("当前已扫描股票个数", total_scan_cnt, ",总用时", used_time_fmt(job_start, time.time()))
