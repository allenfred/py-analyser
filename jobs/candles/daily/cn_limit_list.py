# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

import numpy as np
import tushare as ts
import pandas as pd
from models.cn_daily_candles import CNDailyCandleDao
from models.cn_limit_list import CNLimitListDao
from models.weekly_candles import WeeklyCandleDao
from models.trade_calendar import TradeCalendarDao
from models.stocks import StockDao
import time
from datetime import datetime, timedelta
from config.common import TS_TOKEN
from lib.util import used_time_fmt

pro = ts.pro_api(TS_TOKEN)
limitListDao = CNLimitListDao()
dailyCandleDao = CNDailyCandleDao()
weeklyCandleDao = WeeklyCandleDao()
calendarDao = TradeCalendarDao()
stockDao = StockDao()


# 获取单日涨跌停统计数据
def daily_limit_list():
    _start = time.time()
    _today = datetime.now().strftime("%Y%m%d")
    df = pro.limit_list_d(trade_date=_today)

    print(today, '当日涨跌停统计数据', len(df))

    if len(df) > 0:
        limitListDao.reinsert(df)


if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    start = time.time()

    daily_limit_list()

    end = time.time()

    print(today, '总用时', used_time_fmt(start, end))
