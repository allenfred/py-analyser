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


pro = ts.pro_api(TS_TOKEN)
dailyCandleDao = CNDailyCandleDao()
calendarDao = TradeCalendarDao()
stockDao = StockDao()


def ready_candles_by_date():
    all_history_candle_set = False
    is_last_req = False
    offset = 0
    total_got_count = 0

    while not all_history_candle_set:
        circle_start = time.time()

        item = calendarDao.find_one_candle_not_ready('CN')
        trade_dte = ''

        if item:
            trade_dte = datetime.strftime(item.cal_date, "%Y%m%d")
            is_last_req = False
            total_got_count = 0
            offset = 0
        else:
            all_history_candle_set = True

        while not is_last_req:

            try:
                df = pro.daily(**{
                    "ts_code": "",
                    "trade_date": trade_dte,
                    "start_date": "",
                    "end_date": "",
                    "offset": offset,
                    "limit": 5000
                }, fields=[
                    "ts_code",
                    "trade_date",
                    "open",
                    "high",
                    "low",
                    "close",
                    "pre_close",
                    "change",
                    "pct_chg",
                    "vol",
                    "amount"
                ])

                total_got_count += len(df)
                if len(df) < 5000:
                    is_last_req = True
                else:
                    offset += len(df)
                df['exchange'] = 'CN'

                dailyCandleDao.bulk_insert(df)

            except Exception as e:
                print('Error:', e)

        if item:
            print('已更新 CN daily_candles ', item.cal_date, ': ', total_got_count, ' 条数据，用时 ',
                  round(time.time() - circle_start, 2), ' s')
            calendarDao.set_candle_ready('CN', item.cal_date)


def ready_candles_by_stock():
    all_history_candle_set = False
    today = datetime.now().strftime("%Y-%m-%d")

    while not all_history_candle_set:
        circle_start = time.time()
        total_got_count = 0
        ts_code = stockDao.find_one_candle_not_ready('CN', )

        if ts_code is None:
            break

        try:
            df = pro.daily(**{
                "ts_code": ts_code,
                "trade_date": "",
                "start_date": "",
                "end_date": "",
                "offset": 0,
                "limit": 2000
            }, fields=[
                "ts_code",
                "trade_date",
                "open",
                "high",
                "low",
                "close",
                "pre_close",
                "change",
                "pct_chg",
                "vol",
                "amount"
            ])

            total_got_count += len(df)
            df['exchange'] = 'CN'

            db_df = dailyCandleDao.find_all(ts_code)
            new_df = df.loc[~pd.to_datetime(df["trade_date"], format='%Y-%m-%d').isin(db_df["trade_date"].to_numpy())]
            dailyCandleDao.bulk_insert(new_df)
        except Exception as e:
            print('Error:', e)

        if ts_code:
            print('已更新 CN daily_candles :', ts_code, ': ', total_got_count, ' 条数据，用时 ',
                  round(time.time() - circle_start, 2), ' s')
            stockDao.set_candle_ready(ts_code, today)


if __name__ == "__main__":
    start = time.time()
    # ready_candles_by_date()
    ready_candles_by_stock()
    end = time.time()
    print('用时', round(end - start, 2), 's')
