import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

import pandas as pd
from models.daily_candles import DailyCandleDao
from models.stocks import StockDao
from sqlalchemy import text
from talib import SMA, EMA, MACD
from lib.bias import bias
from lib.ma_slope import slope
import time
from datetime import datetime, date
import numpy as np
from api.daily_candle import get_cn_candles

stockDao = StockDao()
dailyCandleDao = DailyCandleDao()

if __name__ == "__main__":
    ts_code = '601766.SH'

    s = text("select trade_date, close from daily_candles where ts_code = :ts_code")
    statement = dailyCandleDao.session.execute(s.params(ts_code=ts_code))
    df = pd.DataFrame(statement.fetchall(), columns=['trade_date', 'close'])
    df = df.sort_values(by='trade_date', ascending=True)

    df['ma5'] = SMA(df.close, 5)
    df['ma10'] = SMA(df.close, 10)
    df['ma20'] = SMA(df.close, 20)
    df['ma30'] = SMA(df.close, 30)
    df['ma34'] = SMA(df.close, 34)
    df['ma55'] = SMA(df.close, 55)
    df['ma60'] = SMA(df.close, 60)
    df['ma120'] = SMA(df.close, 120)
    df['ma144'] = SMA(df.close, 144)
    df['ma169'] = SMA(df.close, 169)

    df['ema5'] = EMA(df.close, 5)
    df['ema10'] = EMA(df.close, 10)
    df['ema20'] = EMA(df.close, 20)
    df['ema30'] = EMA(df.close, 30)
    df['ema34'] = EMA(df.close, 34)
    df['ema55'] = EMA(df.close, 55)
    df['ema60'] = EMA(df.close, 60)
    df['ema120'] = EMA(df.close, 120)
    df['ema144'] = EMA(df.close, 144)
    df['ema169'] = EMA(df.close, 169)

    df['ma5_slope'] = slope(df.close, 5)
    df['ma10_slope'] = SMA(df.close, 10)
    df['ma20_slope'] = SMA(df.close, 20)
    df['ma30_slope'] = SMA(df.close, 30)
    df['ma34_slope'] = SMA(df.close, 34)
    df['ma55_slope'] = SMA(df.close, 55)
    df['ma60_slope'] = SMA(df.close, 60)
    df['ma120_slope'] = SMA(df.close, 120)
    df['ma144_slope'] = SMA(df.close, 144)
    df['ma169_slope'] = SMA(df.close, 169)

    df['ema5_slope'] = EMA(df.close, 5)
    df['ema10_slope'] = EMA(df.close, 10)
    df['ema20_slope'] = EMA(df.close, 20)
    df['ema30_slope'] = EMA(df.close, 30)
    df['ema34_slope'] = EMA(df.close, 34)
    df['ema55_slope'] = EMA(df.close, 55)
    df['ema60_slope'] = EMA(df.close, 60)
    df['ema120_slope'] = EMA(df.close, 120)
    df['ema144_slope'] = EMA(df.close, 144)
    df['ema169_slope'] = EMA(df.close, 169)

    DIFF, DEA, MACD_BAR = MACD(df.close)

    df['diff'] = DIFF
    df['dea'] = DEA
    df['macd'] = MACD_BAR

    bias6, bias12, bias24, bias60 = bias(df.close)
    df['bias6'] = bias6
    df['bias12'] = bias12
    df['bias24'] = bias24
    df['bias60'] = bias60

    print(df)

