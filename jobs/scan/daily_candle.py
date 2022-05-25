# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

import pandas as pd
from models.cn_daily_candles import CNDailyCandleDao
from models.daily_indicators import DailyIndicatorDao

from models.stock_daily_signals import StockDailySignalDao
from models.daily_pattern_signals import DailyPatternSignalDao
from models.stock_signals import StockSignalDao

from models.stocks import StockDao
from sqlalchemy import text
from lib.stock.analyze import analyze
from lib.util import set_quota, used_time_fmt
from datetime import date, timedelta
import time

stockDao = StockDao()
dailyCandleDao = CNDailyCandleDao()
dailyIndicatorDao = DailyIndicatorDao()

stockDailySignalDao = StockDailySignalDao()
dailyPatternSignalDao = DailyPatternSignalDao()
stockSignalDao = StockSignalDao()


def get_amount(exchange, amount):
    if not amount:
        return 0

    if exchange == 'HK' or exchange == 'US':
        return int(amount) * 1
    else:
        return int(amount) * 1000


def scan_daily_candles(ts_code, exchange_type, scan_date):
    start = time.time()
    table_name = 'cn_daily_candles'
    monthly_ago = date.today() - timedelta(days=20)
    if exchange_type == 'HK':
        table_name = 'hk_daily_candles'
    if exchange_type == 'US':
        table_name = 'us_daily_candles'

    statement = dailyCandleDao.session.execute(text("select trade_date, open, high, close, low, pct_chg, vol, amount "
                                                    "from "
                                                    + table_name + " where ts_code = :ts_code "
                                                    + "and trade_date > '2015-01-01' and open is not null "
                                                      "and close is not null and high is not null and"
                                                    + " low is not null "
                                                    + "order by trade_date desc "
                                                      "limit 300").params(ts_code=ts_code))

    df = pd.DataFrame(statement.fetchall(), columns=['trade_date', 'open', 'high', 'close',
                                                     'low', 'pct_chg', 'vol', 'amount'])
    df = df.fillna(0)
    last_amount = 0
    list_status = 'L'

    if len(df) > 1:
        last_amount = get_amount(exchange_type, df.iloc[0].amount)

        # 剔除退市股
        if df.iloc[0].trade_date < monthly_ago:
            list_status = 'D'

    if list_status == 'L' and len(df) > 60 and last_amount > 10000000:
        df = df.sort_values(by='trade_date', ascending=True)
        df['num'] = df.index[::-1].to_numpy()
        df = df.set_index('num')
        df['ts_code'] = ts_code
        df['exchange'] = exchange_type

        try:
            df = set_quota(df)
            df_len = len(df)

            df = analyze(df)

            small_df = df.iloc[df_len - 10: df_len]
            signal = df.iloc[df_len - 1].to_dict()

            dailyIndicatorDao.bulk_insert(df, ts_code)
            stockSignalDao.upsert(signal)
            stockDailySignalDao.reinsert(small_df, ts_code)
            dailyPatternSignalDao.bulk_insert(small_df, ts_code)

            stockDao.update({'ts_code': ts_code, 'scan_date': scan_date, 'amount': last_amount, 'list_status': 'L'})

            print_str = '扫描成功: ' + str(ts_code) + ', 最新K线时间: ' + str(scan_date) + \
                        ', 用时 ' + str(used_time_fmt(start, time.time()))
            print(print_str)
        except Exception as e:
            print('更新 ', ts_code, 'Catch Error:', e)
            stockDao.update({'ts_code': ts_code, 'scan_date': scan_date, 'amount': last_amount, 'list_status': 'L'})
    else:
        stockDao.update({'ts_code': ts_code, 'scan_date': scan_date, 'amount': last_amount, 'list_status': list_status})
        print('股票代码: ', ts_code, ' 不满足扫描条件')
