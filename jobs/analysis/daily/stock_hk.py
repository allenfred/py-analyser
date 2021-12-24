# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

import pandas as pd
from models.db import DBSession
from models.hk_daily_candles import HKDailyCandleDao
from models.stocks import StockDao
from sqlalchemy import text
from talib import SMA, EMA, MACD
from lib.bias import bias
from lib.ma_slope import slope
from lib.magic_nine_turn import td
from lib.util import used_time_fmt, is_mac_os
import time
from datetime import datetime, date
import numpy as np
from api.daily_candle import get_cn_candles
import time
import threading
import multiprocessing
from multiprocessing import Pool
from jobs.scan.daily_candle import scan_daily_candles

stockDao = StockDao()
dailyCandleDao = HKDailyCandleDao()


def multi_scan(stocks):
    if is_mac_os():
        pool_cnt = 4
        p = Pool(pool_cnt)

        for i in range(len(stocks)):
            p.apply_async(scan_daily_candles, args=(stocks[i][0], 'HK', scan_date,))

        p.close()
        p.join()
    else:
        scan_daily_candles(stocks[0][0], 'HK', scan_date)


if __name__ == "__main__":
    job_start = time.time()
    candle = dailyCandleDao.find_latest_candle()
    total_scan_cnt = 0
    limit = 1
    today = date.today()

    if candle is None:
        print('没有K线数据')
        quit()

    if is_mac_os():
        limit = 10

    scan_date = candle['trade_date']

    while True:
        stock_stmts = stockDao.session.execute(text("select ts_code from stocks where (scan_date is null or scan_date"
                                                    " < :scan_date) and exchange='HK' limit " + str(limit)
                                                    ).params(scan_date=scan_date))
        stock_result = stock_stmts.fetchall()
        stockDao.session.commit()

        if len(stock_result) == 0:
            print('没有需要扫描的股票')
            break

        multi_scan(stock_result)
        total_scan_cnt += len(stock_result)
        print(today, "当前已扫描股票个数", total_scan_cnt, ",总用时", used_time_fmt(job_start, time.time()))
