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

ts.set_token(TS_TOKEN)
pro = ts.pro_api()
dailyCandleDao = CNDailyCandleDao()
calendarDao = TradeCalendarDao()
stockDao = StockDao()


def check_stock_dividend():
    _start = time.time()
    _today = datetime.now().strftime("%Y%m%d")
    year_ago = (datetime.now() - timedelta(days=360)).strftime("%Y%m%d")

    k_df = ts.pro_bar(ts_code=ts_code, adj='qfq', start_date=year_ago, end_date=_today)

    stockDao.update({'ts_code': ts_code, 'ex_date': _today})
    dailyCandleDao.bulk_update(k_df)
    print(ts_code, '更新K线完成, 当前用时', round(time.time() - _start, 2), 's')

    _end = time.time()
    print('除权除息 更新总用时', round(_end - _start, 2), 's')


if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    start = time.time()

    ts_code = '601086.SH'
    ts_code = '830964.BJ'
    check_stock_dividend()

    end = time.time()

    print(today, '总用时', used_time_fmt(start, end))
