# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

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
            break

        while not is_last_req:
            req_start = time.time()
            try:
                df = get_us_candles({"trade_date": trade_dte, "limit": 2000, "offset": offset})
                df = df.sort_values(by='trade_date', ascending=False)
                df['pct_chg'] = df['pct_change']
                df['turnover_rate'] = df['turnover_ratio']

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


def ready_candles_by_stock(start_time):
    all_history_candle_set = False
    yesterday = (datetime.now() + timedelta(hours=-24)).strftime("%Y-%m-%d")

    df = get_us_candles({"limit": 1, "offset": 0})
    latest_candle_date = datetime.strftime(datetime.strptime(df["trade_date"][0], "%Y%m%d"), '%Y-%m-%d')

    if not latest_candle_date == yesterday:
        print('tushare 尚未同步 US 最新行情数据:', yesterday)
        quit()

    while not all_history_candle_set:
        circle_start = time.time()
        ts_code = stockDao.find_one_candle_not_ready('US', yesterday)

        if ts_code is None:
            break

        try:
            df = get_us_candles({"ts_code": ts_code, "limit": 2000, "offset": 0})
            df = df.sort_values(by='trade_date', ascending=False)
            df['pct_chg'] = df['pct_change']

            # 过滤出最新candle数据 (相较于db)
            db_df = dailyCandleDao.find_by_ts_code(ts_code)
            new_df = df.loc[~pd.to_datetime(df["trade_date"], format='%Y-%m-%d').isin(db_df["trade_date"].to_numpy())]

            dailyCandleDao.bulk_insert(new_df)
            stockDao.update({'ts_code': ts_code, 'candle_date': today})

            print('已更新 US daily_candles :', ts_code, ': ', len(new_df), ' 条数据，用时 ',
                  used_time_fmt(circle_start, time.time()), ', 总用时 ', used_time_fmt(start_time, time.time()))
        except Exception as e:
            stockDao.update({'ts_code': ts_code, 'candle_date': today})
            print('Error:', e)


if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    # yesterday = (datetime.now() + timedelta(hours=-24)).strftime("%Y-%m-%d")
    start = time.time()
    # ready_candles_by_date(start)
    ready_candles_by_stock(start)

    end = time.time()

    print(today, '用时', used_time_fmt(start, end))
