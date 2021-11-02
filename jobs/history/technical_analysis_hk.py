import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

import pandas as pd
from models.db import DBSession
from models.hk_daily_candles import HKDailyCandleDao
from models.daily_indicators import DailyIndicatorDao
from models.daily_long_signals import DailyLongSignalDao
from models.daily_short_signals import DailyShortSignalDao
from models.stock_long_signals import StockLongSignalDao
from models.stock_short_signals import StockShortSignalDao
from models.stocks import StockDao
from sqlalchemy import text
from talib import SMA, EMA, MACD
from lib.bias import bias
from lib.ma_slope import slope
from lib.magic_nine_turn import td
from lib.ma_shape import long_signals
import time
from datetime import datetime, date
import numpy as np
from api.daily_candle import get_hk_candles

stockDao = StockDao()
dailyCandleDao = HKDailyCandleDao()
dailyIndicatorDao = DailyIndicatorDao()
dailyLongSignalDao = DailyLongSignalDao()
dailyShortSignalDao = DailyShortSignalDao()

stockLongSignalDao = StockLongSignalDao()
stockShortSignalDao = StockShortSignalDao()

if __name__ == "__main__":
    job_start = time.time()

    all_scan_set = False
    today = datetime.now().strftime("%Y-%m-%d")

    while not all_scan_set:
        used_time = round(time.time() - job_start, 0)
        if used_time > 3600 * 5:
            break

        circle_start = time.time()

        ts_code = ''
        stock_stmts = stockDao.session.execute(text("select ts_code from stocks where (scan_date is null or scan_date"
                                                    " < :scan_date) and exchange = 'HK'  limit 1").params(scan_date=today))
        stock_result = stock_stmts.fetchone()

        if stock_result:
            ts_code = stock_result[0]
            print('开始扫描: ', ts_code)
        else:
            all_scan_set = True
        #
        # s = text("select trade_date, open, close, high, low, pct_chg from daily_candles where ts_code = :ts_code "
        #          + "and trade_date > '2015-01-01' and open is not null and close is not null and high is not null and"
        #          + " low is not null "
        #          + "order by trade_date desc limit 0,500")
        # statement = dailyCandleDao.session.execute(s.params(ts_code=ts_code))
        # df = pd.DataFrame(statement.fetchall(), columns=['trade_date', 'open', 'close', 'high', 'low', 'pct_chg'])

        df = get_hk_candles({"ts_code": ts_code, "limit": 2000})
        df = df.sort_values(by='trade_date', ascending=True)
        close = df.close.to_numpy()
        df['ts_code'] = ts_code

        if len(df):
            try:
                df['ma5'] = SMA(close, 5)
                df['ma10'] = SMA(close, 10)
                df['ma20'] = SMA(close, 20)
                df['ma30'] = SMA(close, 30)
                df['ma34'] = SMA(close, 34)
                df['ma55'] = SMA(close, 55)
                df['ma60'] = SMA(close, 60)
                df['ma120'] = SMA(close, 120)
                df['ma144'] = SMA(close, 144)
                df['ma169'] = SMA(close, 169)

                df['ema5'] = EMA(close, 5)
                df['ema10'] = EMA(close, 10)
                df['ema20'] = EMA(close, 20)
                df['ema30'] = EMA(close, 30)
                df['ema34'] = EMA(close, 34)
                df['ema55'] = EMA(close, 55)
                df['ema60'] = EMA(close, 60)
                df['ema120'] = EMA(close, 120)
                df['ema144'] = EMA(close, 144)
                df['ema169'] = EMA(close, 169)

                df['ma5_slope'] = slope(close, 'SMA', 5)
                df['ma10_slope'] = slope(close, 'SMA', 10)
                df['ma20_slope'] = slope(close, 'SMA', 20)
                df['ma30_slope'] = slope(close, 'SMA', 30)
                df['ma34_slope'] = slope(close, 'SMA', 34)
                df['ma55_slope'] = slope(close, 'SMA', 55)
                df['ma60_slope'] = slope(close, 'SMA', 60)
                df['ma120_slope'] = slope(close, 'SMA', 120)
                df['ma144_slope'] = slope(close, 'SMA', 144)
                df['ma169_slope'] = slope(close, 'SMA', 169)

                df['ema5_slope'] = slope(close, 'EMA', 5)
                df['ema10_slope'] = slope(close, 'EMA', 10)
                df['ema20_slope'] = slope(close, 'EMA', 20)
                df['ema30_slope'] = slope(close, 'EMA', 30)
                df['ema34_slope'] = slope(close, 'EMA', 34)
                df['ema55_slope'] = slope(close, 'EMA', 55)
                df['ema60_slope'] = slope(close, 'EMA', 60)
                df['ema120_slope'] = slope(close, 'EMA', 120)
                df['ema144_slope'] = slope(close, 'EMA', 144)
                df['ema169_slope'] = slope(close, 'EMA', 169)

                DIFF, DEA, MACD_BAR = MACD(close)

                df['diff'] = DIFF
                df['dea'] = DEA
                df['macd'] = MACD_BAR

                bias6, bias12, bias24, bias72 = bias(close)
                df['bias6'] = bias6
                df['bias12'] = bias12
                df['bias24'] = bias24
                df['bias72'] = bias72

                high_td, low_td = td(close)
                df['high_td'] = high_td
                df['low_td'] = low_td

                long_signals(df)

                df_len = len(df)
                small_df = df.iloc[df_len - 10: df_len]
                item = df.iloc[df_len - 1].to_dict()

                dailyCandleDao.reinsert(df)
                dailyLongSignalDao.reinsert(small_df)
                stockLongSignalDao.upsert(item)

                stockDao.update({'ts_code': ts_code, 'scan_date': today})
                print('扫描成功: ', ts_code, ', 扫描最新K线时间: ', today, '，用时 ',
                      round(time.time() - circle_start, 1), ' s')
            except Exception as e:
                stockDao.update({'ts_code': ts_code, 'scan_date': today})
                print('更新扫描结果 Catch Error:', e, '，用时 ',
                      round(time.time() - circle_start, 1), ' s')
        else:
            stockDao.update({'ts_code': ts_code, 'scan_date': today})
            print('股票代码: ', ts_code, ' 没有行情数据', '，用时 ',
                  round(time.time() - circle_start, 1), ' s')
