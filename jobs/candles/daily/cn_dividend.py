# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

import tushare as ts
from models.cn_daily_candles import CNDailyCandleDao
from models.trade_calendar import TradeCalendarDao
from models.stocks import StockDao
import time
from datetime import datetime, timedelta
from config.common import TS_TOKEN
from lib.util import used_time_fmt

pro = ts.pro_api(TS_TOKEN)
dailyCandleDao = CNDailyCandleDao()
calendarDao = TradeCalendarDao()
stockDao = StockDao()


def check_daily_dividend():
    _start = time.time()
    _today = datetime.now().strftime("%Y%m%d")

    # 获取当天是除权除息日的股票
    df = pro.dividend(ex_date=_today, fields='ts_code,div_proc,stk_div,record_date,ex_date')
    df = df.loc[~df['ts_code'].str.contains('BJ')]
    year_ago = (datetime.now() - timedelta(days=600)).strftime("%Y%m%d")
    print(_today, '当日除权除息股票(除BJ): ', len(df), '只')

    for row in df.itertuples():
        _t = time.time()
        time.sleep(0.2)
        k_df = ts.pro_bar(ts_code=row.ts_code, adj='qfq', start_date=year_ago, end_date=today)
        print(row.ts_code, '获取K线用时', round(time.time() - _t, 2), 's')
        k_df = k_df.round(2)

        stockDao.update({'ts_code': row.ts_code, 'ex_date': row.ex_date})
        cnt = dailyCandleDao.reinsert(k_df)
        print(row.ts_code, '更新K线完成: ', cnt, ',当前用时', round(time.time() - _start, 2), 's')

    _end = time.time()
    print('除权除息 更新总用时', round(_end - _start, 2), 's')


def check_history_dividend():
    _start = time.time()
    _today = datetime.now().strftime("%Y%m%d")
    year_ago = (datetime.now() - timedelta(days=360)).strftime("%Y%m%d")

    check_days = 200
    while check_days < 360:
        ex_date = (datetime.now() - timedelta(days=check_days)).strftime("%Y%m%d")
        # 获取除权除息日的股票
        df = pro.dividend(ex_date=ex_date, fields='ts_code,div_proc,stk_div,record_date,ex_date')
        print(ex_date, df['ts_code'].to_numpy())

        for row in df.itertuples():
            k_df = ts.pro_bar(ts_code=row.ts_code, adj='qfq', start_date=year_ago, end_date=_today)

            stockDao.update({'ts_code': row.ts_code, 'ex_date': row.ex_date})
            dailyCandleDao.bulk_update(k_df)
            print(row.ts_code, '更新行情完成, 当前用时', round(time.time() - _start, 2), 's')

        check_days += 1

    _end = time.time()
    print('除权除息 更新总用时', round(_end - _start, 2), 's')


if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    start = time.time()

    check_daily_dividend()

    end = time.time()

    print(today, '总用时', used_time_fmt(start, end))
