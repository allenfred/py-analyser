import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

import numpy as np
import tushare as ts
import pandas as pd
from models.cn_daily_candles import CNDailyCandleDao
from models.trade_calendar import TradeCalendarDao
from models.stocks import StockDao
import time
from datetime import datetime
from config.common import TS_TOKEN
from api.daily_candle import get_cn_candles
from lib.util import used_time_fmt

pro = ts.pro_api(TS_TOKEN)
dailyCandleDao = CNDailyCandleDao()
calendarDao = TradeCalendarDao()
stockDao = StockDao()


def ready_candles_by_date(start_time):
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
              used_time_fmt(circle_start, time.time()), ', 总用时 ',  used_time_fmt(start_time, time.time()))
        calendarDao.set_cn_candle_ready(item.cal_date)


def ready_candles_by_stock(start_time):
    today = datetime.now().strftime("%Y-%m-%d")
    df = get_cn_candles({"ts_code": ts_code, "limit": 1, "offset": 0})
    latest_candle_date = datetime.strftime(datetime.strptime(df["trade_date"][0], "%Y%m%d"), '%Y-%m-%d')

    if not latest_candle_date == today:
        print('tushare 尚未同步最新行情数据:', today)
        quit()

    while True:
        circle_start = time.time()
        ts_code = stockDao.find_one_candle_not_ready('CN', today)

        if ts_code is None:
            break

        try:
            df = get_cn_candles({"ts_code": ts_code, "limit": 2000, "offset": 0})
            df = df.sort_values(by='trade_date', ascending=False)

            # 过滤出最新candle数据 (相较于db)
            db_df = dailyCandleDao.find_by_ts_code(ts_code)
            new_df = df.loc[~pd.to_datetime(df["trade_date"], format='%Y-%m-%d').isin(db_df["trade_date"].to_numpy())]

            dailyCandleDao.bulk_insert(new_df)
            stockDao.set_candle_ready(ts_code, today)

            print('已更新 CN daily_candles :', ts_code, ': ', len(new_df), ' 条数据，用时 ',
                  used_time_fmt(circle_start, time.time()), ', 总用时 ', used_time_fmt(start_time, time.time()))
        except Exception as e:
            stockDao.set_candle_ready(ts_code, today)
            print('Error:', e)


if __name__ == "__main__":
    start = time.time()
    ready_candles_by_date(start)
    end = time.time()

    print('用时', used_time_fmt(start, end))
