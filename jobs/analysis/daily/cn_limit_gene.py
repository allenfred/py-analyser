# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

from models.cn_daily_candles import CNDailyCandleDao
from models.stocks import StockDao
from sqlalchemy import text
from lib.util import used_time_fmt, is_mac_os
from datetime import datetime, date, timedelta
import time
from multiprocessing import Pool
from jobs.scan.daily_candle import scan_daily_candles

stockDao = StockDao()
dailyCandleDao = CNDailyCandleDao()


def multi_scan(stocks):
    if is_mac_os():
        pool_cnt = 4
        p = Pool(pool_cnt)

        for i in range(len(stocks)):
            p.apply_async(scan_daily_candles, args=(stocks[i][0], 'CN', scan_date,))

        p.close()
        p.join()
    else:
        scan_daily_candles(stocks[0][0], 'CN', scan_date)


if __name__ == "__main__":
    job_start = time.time()
    candle = dailyCandleDao.find_latest_candle()
    total_scan_cnt = 0
    limit = 1
    today = date.today()
    # month_ago = (today - timedelta(days=22)).strptime("%Y-%m-%d")
    month_ago = today - timedelta(days=22)

    if candle is None:
        print('没有K线数据')
        quit()

    if is_mac_os():
        limit = 5

    scan_date = candle['trade_date']

    while True:
        time.sleep(0.2)
        stock_stmts = stockDao.session.execute(text("select a.ts_code as ts_code from cn_limit_list a "
                                                    "JOIN stocks b ON a.ts_code = b.ts_code "
                                                    "where (b.scan_date is null or "
                                                    "b.scan_date < :scan_date) and a.trade_date > :before_date "
                                                    "GROUP BY a.ts_code limit "
                                                    + str(limit)).params(before_date=month_ago, scan_date=scan_date))
        stock_result = stock_stmts.fetchall()
        stockDao.session.commit()

        if len(stock_result) == 0:
            print(today, 'CN 扫描完成: ', ",总用时", used_time_fmt(job_start, time.time()))
            break

        multi_scan(stock_result)
        total_scan_cnt += len(stock_result)
        print(today, "当前已扫描过去20个交易日涨停股票个数", total_scan_cnt, ",总用时", used_time_fmt(job_start, time.time()))
