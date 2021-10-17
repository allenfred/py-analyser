import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

import tushare as ts
from models.trade_calendar import TradeCalendarDao
import time
from config.common import TS_TOKEN

pro = ts.pro_api(TS_TOKEN)
calendarDao = TradeCalendarDao()

if __name__ == "__main__":
    start = time.time()

    # 拉取上交所交易日历数据
    sse_df = pro.trade_cal(**{
        "exchange": "SSE",
        "cal_date": "",
        "start_date": "",
        "end_date": "",
        "is_open": "",
        "limit": "",
        "offset": ""
    }, fields=[
        "exchange",
        "cal_date",
        "is_open",
        "pretrade_date"
    ])

    print('拉取SSE calendar ', len(sse_df), ' 条数据')

    # 拉取深交所交易日历数据
    szse_df = pro.trade_cal(**{
        "exchange": "SZSE",
        "cal_date": "",
        "start_date": "",
        "end_date": "",
        "is_open": "",
        "limit": "",
        "offset": ""
    }, fields=[
        "exchange",
        "cal_date",
        "is_open",
        "pretrade_date"
    ])

    print('拉取SZSE calendar ', len(szse_df), ' 条数据')

    calendarDao.bulk_insert(sse_df)
    print('更新 SSE calendar 完成', len(sse_df), ' 条数据')

    calendarDao.bulk_insert(szse_df)
    print('更新 SZSE calendar 完成', len(szse_df), ' 条数据')

    end = time.time()
    print('拉取数据用时', round(end - start, 2), 's')
