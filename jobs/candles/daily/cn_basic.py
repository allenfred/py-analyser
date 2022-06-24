# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

import tushare as ts
from models.cn_daily_candles import CNDailyCandleDao
from models.weekly_candles import WeeklyCandleDao
from models.trade_calendar import TradeCalendarDao
from models.stocks import StockDao
import time
from datetime import datetime, timedelta
from config.common import TS_TOKEN
from api.daily_basic import get_cn_daily_basic
from lib.util import used_time_fmt

pro = ts.pro_api(TS_TOKEN)
dailyCandleDao = CNDailyCandleDao()
weeklyCandleDao = WeeklyCandleDao()
calendarDao = TradeCalendarDao()
stockDao = StockDao()


def daily_basic_quota():
    _start = time.time()
    _today = datetime.now().strftime("%Y%m%d")
    df = get_cn_daily_basic(_today)
    print(_today, '每日指标 ', len(df))

    for index, row in df.iterrows():
        time.sleep(0.2)
        stockDao.update(row.to_dict())

    _end = time.time()
    print('每日指标 更新总用时', round(_end - _start, 2), 's')


if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    start = time.time()

    daily_basic_quota()

    end = time.time()

    print(today, '总用时', used_time_fmt(start, end))
