# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

import pandas as pd
from models.us_daily_candles import USDailyCandleDao
from models.stocks import StockDao
from sqlalchemy import text
from datetime import datetime, date
import time
from multiprocessing import Pool
from jobs.scan.daily_candle import scan_daily_candles
from lib.util import used_time_fmt, is_mac_os

stockDao = StockDao()
dailyCandleDao = USDailyCandleDao()


def multi_scan(stocks):
    if is_mac_os():
        pool_cnt = 4
        p = Pool(pool_cnt)

        for i in range(len(stocks)):
            p.apply_async(scan_daily_candles, args=(stocks[i][0], 'US', scan_date,))

        p.close()
        p.join()
    else:
        scan_daily_candles(stocks[0][0], 'US', scan_date)


if __name__ == "__main__":
    job_start = time.time()
    candle = dailyCandleDao.find_latest_candle()
    total_scan_cnt = 0
    limit = 1
    today = date.today()

    if candle is None:
        print('没有K线数据')
        quit()

    scan_date = candle['trade_date']

    while True:
        time.sleep(0.2)
        stock_stmts = stockDao.session.execute(text("select ts_code, total_mv from stocks where ("
                                                    "scan_date is null or scan_date"
                                                    " < :scan_date) and exchange = 'US' and amount > 10000000 "
                                                    "order by ts_code limit "
                                                    + str(limit)).params(scan_date=scan_date))

        df = pd.DataFrame(stock_stmts.fetchall(), columns=['ts_code', 'total_mv'])
        stockDao.session.commit()

        if len(df) == 0:
            print(today, 'US 没有需要扫描的股票')
            break
        ts_code = df.iloc[0]['ts_code']
        total_mv = df.iloc[0]['total_mv']

        if total_mv is not None and total_mv < 1000000000:
            stockDao.update({'ts_code': ts_code, 'scan_date': scan_date, 'list_status': 'L'})
        else:
            scan_daily_candles(ts_code, 'US', scan_date)

        total_scan_cnt += 1
        print(today, "US 当前已扫描股票个数", total_scan_cnt, ",总用时", used_time_fmt(job_start, time.time()))
