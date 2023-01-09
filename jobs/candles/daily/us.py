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


def update_daily(start_time):
    while True:
        circle_start = time.time()
        item = calendarDao.find_one_candle_not_ready('US')

        if not item:
            print('所有交易日K线已准备完成')
            break

        trade_dte = datetime.strftime(item.cal_date, "%Y%m%d")
        is_last_req = False
        total_got_count = 0
        offset = 0
        kline_df = []

        while not is_last_req:
            req_start = time.time()
            try:
                df = get_us_candles({"trade_date": trade_dte, "limit": 5000, "offset": offset})
                kline_df.append(df.sort_values(by='trade_date', ascending=False))

                total_got_count += len(df)

                if len(df) < 5000:
                    is_last_req = True
                else:
                    offset += len(df)

                print('当前请求 US daily_candles ', item.cal_date, ': ', len(df), ' 条数据，用时 ',
                      used_time_fmt(req_start, time.time()))
            except Exception as e:
                print('Error:', e)

        if total_got_count == 0:
            print(trade_dte, '未获取到行情数据')
            break

        filepath = Path(path + '/csv/us/daily/' + trade_dte + '.csv')
        filepath.parent.mkdir(parents=True, exist_ok=True)
        result = pd.concat(kline_df)
        result = result.sort_values(by='ts_code', ascending=True)
        result.to_csv(filepath, index=False)

        update_stocks(result)
        dailyCandleDao.load_local_file(str(filepath))

        print('已更新 US daily_candles ', item.cal_date, ': ', total_got_count, ' 条数据，用时 ',
              used_time_fmt(circle_start, time.time()), ', 总用时 ', used_time_fmt(start_time, time.time()))

        calendarDao.set_us_candle_ready(item.cal_date)


def update_stocks(df):
    item = calendarDao.find_one_candle_not_ready('US')
    trade_dte = datetime.strftime(item.cal_date, "%Y%m%d")
    filepath = Path(path + '/csv/us/stock/' + trade_dte + '.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)

    stocks = stockDao.find_all('US')
    stocks = stocks.drop(columns=['amount', 'close', 'total_mv'])
    kline_df = df[['amount', 'close', 'ts_code', 'total_mv']]

    result = stocks.merge(kline_df, left_index=True, how='left', on='ts_code')

    result = result[['id', 'ts_code', 'symbol', 'name', 'area', 'industry',
                     'fullname', 'enname', 'cnspell', 'market', 'exchange', 'list_status',
                     'list_date', 'delist_date', 'is_hs',
                     'turnover_rate', 'turnover_rate_f', 'volume_ratio', 'pe',
                     'pe_ttm', 'pb', 'ps', 'ps_ttm', 'dv_ratio', 'dv_ttm',
                     'total_share', 'float_share', 'free_share', 'total_mv', 'circ_mv',
                     'scan_date', 'candle_date', 'indicator_date', 'weekly_date', 'amount',
                     'ex_date', 'close']]
    result.to_csv(filepath, index=False)

    stockDao.update_us_from_file(str(filepath))


if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    # yesterday = (datetime.now() + timedelta(hours=-24)).strftime("%Y-%m-%d")

    start = time.time()

    # ready_candles_by_date(start)
    update_daily(start)

    end = time.time()

    print(today, '用时', used_time_fmt(start, end))
