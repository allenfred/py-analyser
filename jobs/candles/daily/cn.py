# -- coding: utf-8 -

import os
import sys
import pandas as pd

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

import tushare as ts
from models.cn_daily_candles import CNDailyCandleDao
from models.cn_limit_list import CNLimitListDao
from models.cn_daily_limit import CNDailyLimitDao
from models.weekly_candles import WeeklyCandleDao
from models.trade_calendar import TradeCalendarDao
from models.stocks import StockDao
import time
from datetime import datetime, timedelta
from config.common import TS_TOKEN
from api.daily_candle import get_cn_candles
from lib.util import used_time_fmt

pro = ts.pro_api(TS_TOKEN)
dailyCandleDao = CNDailyCandleDao()
dailyLimitDao = CNDailyLimitDao()
limitListDao = CNLimitListDao()
weeklyCandleDao = WeeklyCandleDao()
calendarDao = TradeCalendarDao()
stockDao = StockDao()


def ready_daily_klines():
    start_time = time.time()

    while True:
        item = calendarDao.find_one_candle_not_ready('CN')

        if item:
            trade_dte = datetime.strftime(item.cal_date, "%Y%m%d")

            is_last_req = False
            total_got_count = 0
            offset = 0
        else:
            break

        while not is_last_req:
            circle_start = time.time()
            try:
                df = get_cn_candles({"trade_date": trade_dte, "limit": 5000, "offset": offset})
                df = df.sort_values(by='trade_date', ascending=False)

                if len(df) < 5000:
                    is_last_req = True
                else:
                    offset += len(df)

                # 过滤出最新candle数据 (相较于db)
                db_df = dailyCandleDao.find_by_trade_date(item.cal_date)
                new_df = df.loc[~df["ts_code"].isin(db_df["ts_code"].to_numpy())]

                total_got_count += len(new_df)
                dailyCandleDao.bulk_insert(new_df)

            except Exception as e:
                print('Error:', e)

        if total_got_count == 0:
            print('未获取到行情数据')
            break

        print('已更新 CN daily_candles ', item.cal_date, ': ', total_got_count, ' 条数据，用时 ',
              used_time_fmt(circle_start, time.time()), ', 总用时 ', used_time_fmt(start_time, time.time()))
        calendarDao.set_cn_candle_ready(item.cal_date)


def init_limit_list(_today):
    db_df = dailyCandleDao.find_by_trade_date(_today)
    limit_df = dailyLimitDao.find_by_trade_date(_today)
    new_df = pd.merge(db_df, limit_df, on='ts_code')
    new_df['limit'] = 'U'
    limit_df = new_df[new_df.close == new_df.up_limit]
    insert_df = limit_df[['ts_code', 'trade_date', 'close', 'pct_chg', 'limit']]

    limitListDao.reinsert(insert_df)


if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    start = time.time()

    ready_daily_klines()
    init_limit_list(today)

    end = time.time()

    print(today, '总用时', used_time_fmt(start, end))
