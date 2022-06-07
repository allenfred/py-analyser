# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

import tushare as ts
from models.cn_daily_limit import CNDailyLimitDao
import time
from datetime import datetime, timedelta
from config.common import TS_TOKEN
from lib.util import used_time_fmt

pro = ts.pro_api(TS_TOKEN)
dailyLimitDao = CNDailyLimitDao()


def daily_limit():
    _start = time.time()
    _today = datetime.now().strftime("%Y%m%d")
    # 获取单日统计数据
    df = pro.stk_limit(trade_date=_today)
    print(df)
    dailyLimitDao.reinsert(df)


if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    start = time.time()

    daily_limit()

    end = time.time()

    print(today, '总用时', used_time_fmt(start, end))
