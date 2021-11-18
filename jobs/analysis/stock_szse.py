# -- coding: utf-8 -

from jobs.scan.daily_candle import scan_daily_candles
from multiprocessing import Pool
import multiprocessing
import threading
from api.daily_candle import get_cn_candles
import numpy as np
from datetime import datetime, date
import time
from lib.util import wrap_technical_indicator, used_time_fmt, is_mac_os
from lib.magic_nine_turn import td
from lib.ma_slope import slope
from lib.bias import bias
from talib import SMA, EMA, MACD
from sqlalchemy import text
from models.stocks import StockDao
from models.cn_daily_candles import CNDailyCandleDao
from models.db import DBSession
import pandas as pd
import os
import sys

path = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)


stockDao = StockDao()
dailyCandleDao = CNDailyCandleDao()


def multi_scan(stocks):
    if len(stocks) > 1:
        pool_cnt = 8
    else:
        pool_cnt = 1

    p = Pool(pool_cnt)

    for i in range(len(stocks)):
        p.apply_async(scan_daily_candles, args=(
            stocks[i][0], 'CN', scan_date,))

    p.close()
    p.join()


if __name__ == "__main__":
    job_start = time.time()
    candle = dailyCandleDao.find_latest_candle()
    total_scan_cnt = 0
    limit = 1

    if candle is None:
        print('没有K线数据')
        quit()

    if is_mac_os():
        limit = 10

    scan_date = candle['trade_date']

    while True:
        used_time = round(time.time() - job_start, 0)
        if used_time > 3600 * 5:
            break

        stock_stmts = stockDao.session.execute(text("select ts_code from stocks where (scan_date is null or scan_date"
                                                        "< :scan_date) and exchange = 'SZSE' limit "
                                                        + str(limit)).params(scan_date=scan_date))

        stock_result = stock_stmts.fetchall()
        stockDao.session.commit()

        if len(stock_result) == 0:
            print('SZSE 没有需要扫描的股票')
            break

        multi_scan(stock_result)
        total_scan_cnt += len(stock_result)
        print("当前已扫描 SZSE 股票个数", total_scan_cnt, ",总用时",
              used_time_fmt(job_start, time.time()))
