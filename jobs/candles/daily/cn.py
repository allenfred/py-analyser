# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

import numpy as np
import tushare as ts
import pandas as pd
from models.cn_daily_candles import CNDailyCandleDao
from models.weekly_candles import WeeklyCandleDao
from models.trade_calendar import TradeCalendarDao
from models.stocks import StockDao
import time
from datetime import datetime, timedelta
from config.common import TS_TOKEN
from api.daily_candle import get_cn_candles
from api.weekly_candle import get_weekly_candles
from api.daily_basic import get_cn_daily_basic
from lib.util import used_time_fmt

pro = ts.pro_api(TS_TOKEN)
dailyCandleDao = CNDailyCandleDao()
weeklyCandleDao = WeeklyCandleDao()
calendarDao = TradeCalendarDao()
stockDao = StockDao()


def daily_limit_list():
    _start = time.time()
    _today = datetime.now().strftime("%Y%m%d")
    # 获取单日统计数据
    df = pro.limit_list(trade_date=_today)
    print(df)


def daily_basic_quota():
    _start = time.time()
    _today = datetime.now().strftime("%Y%m%d")
    df = get_cn_daily_basic(_today)
    for index, row in df.iterrows():
        time.sleep(0.2)
        stockDao.update(row.to_dict())
        print('更新每日指标完成: ', row.ts_code, '已更新股票', index + 1, '只')

    _end = time.time()
    print('每日指标 更新总用时', round(_end - _start, 2), 's')


def check_daily():
    _start = time.time()
    _today = datetime.now().strftime("%Y%m%d")

    # 获取当天是除权除息日的股票
    df = pro.dividend(ex_date=_today, fields='ts_code,div_proc,stk_div,record_date,ex_date')
    df = df.loc[~df['ts_code'].str.contains('BJ')]
    year_ago = (datetime.now() - timedelta(days=600)).strftime("%Y%m%d")
    print(_today, '当日除权除息股票(除BJ): ', len(df), '只')

    for row in df.itertuples():
        _t = time.time()
        time.sleep(0.2)
        k_df = ts.pro_bar(ts_code=row.ts_code, adj='qfq', start_date=year_ago, end_date=today)
        print(row.ts_code, '获取K线用时', round(time.time() - _t, 2), 's')
        k_df = k_df.round(2)

        stockDao.update({'ts_code': row.ts_code, 'ex_date': row.ex_date})
        cnt = dailyCandleDao.reinsert(k_df)
        print(row.ts_code, '更新K线完成: ', cnt, ',当前用时', round(time.time() - _start, 2), 's')

    _end = time.time()
    print('除权除息 更新总用时', round(_end - _start, 2), 's')


def check_all():
    _start = time.time()
    _today = datetime.now().strftime("%Y%m%d")
    year_ago = (datetime.now() - timedelta(days=360)).strftime("%Y%m%d")

    check_days = 200
    while check_days < 360:
        ex_date = (datetime.now() - timedelta(days=check_days)).strftime("%Y%m%d")
        # 获取除权除息日的股票
        df = pro.dividend(ex_date=ex_date, fields='ts_code,div_proc,stk_div,record_date,ex_date')
        print(ex_date, df['ts_code'].to_numpy())

        for row in df.itertuples():
            k_df = ts.pro_bar(ts_code=row.ts_code, adj='qfq', start_date=year_ago, end_date=_today)
            print(row.ts_code, '获取行情完成, 当前用时', round(time.time() - start, 2), 's')

            stockDao.update({'ts_code': row.ts_code, 'ex_date': row.ex_date})
            dailyCandleDao.bulk_update(k_df)
            print(row.ts_code, '更新行情完成, 当前用时', round(time.time() - _start, 2), 's')

        check_days += 1

    _end = time.time()
    print('除权除息 更新总用时', round(_end - _start, 2), 's')


def ready_weekly_klines():
    _today = datetime.now().strftime("%Y%m%d")
    _start_time = time.time()
    is_last_req = False
    offset = 0

    while not is_last_req:
        circle_start = time.time()
        df = get_weekly_candles({"trade_date": _today, "limit": 2000, "offset": offset})
        df_len = len(df)
        if len(df) < 2000:
            is_last_req = True
        else:
            offset += len(df)

        try:
            if df_len > 0:
                df['trade_date'] = pd.to_datetime(df["trade_date"], format='%Y-%m-%d')

                # 过滤出最新candle数据 (相较于db)
                db_df = weeklyCandleDao.find_by_trade_date(df['trade_date'][0])
                new_df = df.loc[~df["ts_code"].isin(db_df["ts_code"])]

                weeklyCandleDao.bulk_insert(new_df)

                print('已更新 CN weekly_candles :', len(new_df), ' 条，用时 ',
                      used_time_fmt(circle_start, time.time()), ', 总用时 ', used_time_fmt(_start_time, time.time()))
            else:
                print(_today, '没有周K线')

        except Exception as e:
            print(_today, 'Error:', e)
            break

    print(_today, '更新周K用时', used_time_fmt(_start_time, time.time()))


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
              used_time_fmt(circle_start, time.time()), ', 总用时 ',  used_time_fmt(start_time, time.time()))
        calendarDao.set_cn_candle_ready(item.cal_date)

#
# def ready_candles_by_stock(start_time):
#     today = datetime.now().strftime("%Y-%m-%d")
#     df = get_cn_candles({"ts_code": ts_code, "limit": 1, "offset": 0})
#     latest_candle_date = datetime.strftime(datetime.strptime(df["trade_date"][0], "%Y%m%d"), '%Y-%m-%d')
#
#     if not latest_candle_date == today:
#         print('tushare 尚未同步最新行情数据:', today)
#         quit()
#
#     while True:
#         circle_start = time.time()
#         ts_code = stockDao.find_one_candle_not_ready('CN', today)
#
#         if ts_code is None:
#             break
#
#         try:
#             df = get_cn_candles({"ts_code": ts_code, "limit": 2000, "offset": 0})
#             df = df.sort_values(by='trade_date', ascending=False)
#
#             # 过滤出最新candle数据 (相较于db)
#             db_df = dailyCandleDao.find_by_ts_code(ts_code)
#             new_df = df.loc[~pd.to_datetime(df["trade_date"], format='%Y-%m-%d').isin(db_df["trade_date"].to_numpy())]
#
#             dailyCandleDao.bulk_insert(new_df)
#             stockDao.update({'ts_code': ts_code, 'candle_date': today})
#
#             print('已更新 CN daily_candles :', ts_code, ': ', len(new_df), ' 条数据，用时 ',
#                   used_time_fmt(circle_start, time.time()), ', 总用时 ', used_time_fmt(start_time, time.time()))
#         except Exception as e:
#             stockDao.update({'ts_code': ts_code, 'candle_date': today})
#             print('Error:', e)


if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    start = time.time()

    ready_daily_klines()
    ready_weekly_klines()
    check_daily()
    daily_basic_quota()
    daily_limit_list()

    end = time.time()

    print(today, '总用时', used_time_fmt(start, end))
