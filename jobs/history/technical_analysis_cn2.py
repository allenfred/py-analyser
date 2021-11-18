# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

from sqlalchemy.orm import scoped_session
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
from lib.signals import long_signals
from lib.analytic_signals import analytic_signals
from lib.util import wrap_technical_indicator, used_time_fmt, is_mac_os
import time
from datetime import datetime, date
import numpy as np
from api.daily_candle import get_cn_candles
import time
from jobs.scan.daily_candle import scan_daily_candles
import threading
from models.analytic_signals import AnalyticSignalDao

stockDao = StockDao()
dailyCandleDao = CNDailyCandleDao()
dailyIndicatorDao = DailyIndicatorDao()
dailyLongSignalDao = DailyLongSignalDao()
dailyShortSignalDao = DailyShortSignalDao()
stockLongSignalDao = StockLongSignalDao()
stockShortSignalDao = StockShortSignalDao()
analyticDao = AnalyticSignalDao()


def scan(ts_code):
    circle_start = time.time()
    s = text("select trade_date, open, close, high, low, `pct_chg` from cn_daily_candles where ts_code = :ts_code "
             + "order by trade_date desc limit 300")

    session = Session()
    statement = session.execute(s.params(ts_code=ts_code))
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

    analyticDao.reinsert(small_df, ts_code, session)
    dailyLongSignalDao.reinsert(small_df, ts_code, session)
    stockLongSignalDao.upsert(item, session)

    stockDao.update({'ts_code': ts_code, 'scan_date': scan_date}, session)

    print(ts_code, '扫描成功', used_time_fmt(circle_start, time.time()))


def work_parallel(stocks):
    threads = []
    for stock in stocks:
        thread = threading.Thread(target=scan, args=(stock[0],), name=stock[0])
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    job_start = time.time()
    candle = dailyCandleDao.find_latest_candle()
    total_scan_cnt = 0
    limit = 4
    Session = scoped_session(DBSession)
    session = Session()

    if candle is None:
        print('没有K线数据')
        quit()

    if is_mac_os():
        limit = 5

    scan_date = candle['trade_date']

    while True:
        used_time = round(time.time() - job_start, 0)
        if used_time > 3600 * 5:
            break

        stock_stmts = session.execute(text("select ts_code from stocks where (scan_date is null or scan_date"
                                           "< :scan_date) and (exchange = 'SSE' or exchange = 'SZSE') limit "
                                           + str(limit)).params(scan_date=scan_date))
        stock_result = stock_stmts.fetchall()
        session.commit()

        if len(stock_result) == 0:
            print('没有需要扫描的股票')
            break

        work_parallel(stock_result)
        total_scan_cnt += len(stock_result)
        print("当前已扫描股票个数", total_scan_cnt, ",总用时", used_time_fmt(job_start, time.time()))
