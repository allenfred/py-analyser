import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

import tushare as ts
import pandas as pd
from models.trade_calendar import TradeCalendarDao
import time
from config.common import TS_TOKEN

pro = ts.pro_api(TS_TOKEN)
calendarDao = TradeCalendarDao()


if __name__ == "__main__":

    start = time.time()
    is_not_last_req = True
    df = pd.DataFrame(data={})
    offset = 0
    totalGotCount = 0

    while is_not_last_req:

        # 拉取数据
        df = pro.hk_tradecal(**{
            "start_date": "",
            "end_date": "",
            "is_open": "",
            "exchange": "",
            "limit": 2000,
            "offset": offset
        }, fields=[
            "cal_date",
            "is_open",
            "pretrade_date"
        ])

        if len(df) < 2000:
            is_not_last_req = False
        else:
            offset += len(df)

        df['exchange'] = 'HK'
        totalGotCount += len(df)
        calendarDao.bulk_insert(df)

        print('已获取 HK calendar ', totalGotCount, ' 条数据，用时 ',
              round(time.time() - start, 2), ' s')

    end = time.time()
    print('用时', round(end-start, 2), 's')

        