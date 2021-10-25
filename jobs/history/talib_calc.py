import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

import pandas as pd
from models.daily_candles import DailyCandleDao
from models.daily_indicators import DailyIndicatorDao
from models.daily_long_signals import DailyLongSignalDao
from models.daily_short_signals import DailyShortSignalDao
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
from api.daily_candle import get_cn_candles

stockDao = StockDao()
dailyCandleDao = DailyCandleDao()
dailyIndicatorDao = DailyIndicatorDao()
dailyLongSignalDao = DailyLongSignalDao()
dailyShortSignalDao = DailyShortSignalDao()

if __name__ == "__main__":
    ts_code = '600859.SH'

    s = text("select trade_date, open, close, high, low, `change`, pct_chg from daily_candles where ts_code = :ts_code "
             + "order by trade_date desc limit 0,100")
    statement = dailyCandleDao.session.execute(s.params(ts_code=ts_code))
    df = pd.DataFrame(statement.fetchall(), columns=['trade_date', 'open', 'close', 'high', 'low',  'change', 'pct_chg'])
    df = df.sort_values(by='trade_date', ascending=True)
    close = df.close.to_numpy()

    df['ts_code'] = ts_code

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

    bias6, bias12, bias24, bias60 = bias(close)
    df['bias6'] = bias6
    df['bias12'] = bias12
    df['bias24'] = bias24
    df['bias60'] = bias60

    high_td, low_td = td(close)
    df['high_td'] = high_td
    df['low_td'] = low_td

    # print(df['close'])
    # print(df['low_td'].to_numpy())
    # print(df['low_td'])

    long_signals(df)

    # dailyLongSignalDao.bulk_insert(df)