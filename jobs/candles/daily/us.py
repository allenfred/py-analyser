# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

from pathlib import Path
import tushare as ts
import pandas as pd
from models.us_daily_candles import USDailyCandleDao
from models.trade_calendar import TradeCalendarDao
from models.stocks import StockDao
import time
from datetime import datetime, timedelta
from config.common import TS_TOKEN
from api.daily_candle import get_us_candles
from lib.util import used_time_fmt

pro = ts.pro_api(TS_TOKEN)
dailyCandleDao = USDailyCandleDao()
calendarDao = TradeCalendarDao()
stockDao = StockDao()


def ready_candles_by_date(start_time):
    while True:
        circle_start = time.time()
        item = calendarDao.find_one_candle_not_ready('US')

        if item:
            trade_dte = datetime.strftime(item.cal_date, "%Y%m%d")
            is_last_req = False
            total_got_count = 0
            offset = 0
        else:
            print('所有交易日K线已准备完成')
            break

        while not is_last_req:
            req_start = time.time()
            try:
                df = get_us_candles({"trade_date": trade_dte, "limit": 2000, "offset": offset})
                df = df.sort_values(by='trade_date', ascending=False)

                if len(df) < 2000:
                    is_last_req = True
                else:
                    offset += len(df)

                # 过滤出最新candle数据 (相较于db)
                db_df = dailyCandleDao.find_by_trade_date(item.cal_date)
                new_df = df.loc[~df["ts_code"].isin(db_df["ts_code"].to_numpy())]

                total_got_count += len(new_df)
                dailyCandleDao.bulk_insert(new_df)

                print('当前请求 US daily_candles ', item.cal_date, ': ', len(df), ' 条数据，用时 ',
                      used_time_fmt(req_start, time.time()))
            except Exception as e:
                print('Error:', e)

        if total_got_count == 0:
            print(trade_dte, '未获取到行情数据')
            break

        print('已更新 US daily_candles ', item.cal_date, ': ', total_got_count, ' 条数据，用时 ',
              used_time_fmt(circle_start, time.time()), ', 总用时 ', used_time_fmt(start_time, time.time()))
        calendarDao.set_us_candle_ready(item.cal_date)


if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    # yesterday = (datetime.now() + timedelta(hours=-24)).strftime("%Y-%m-%d")

    start = time.time()
    ready_candles_by_date(start)

    end = time.time()

    print(today, '用时', used_time_fmt(start, end))
