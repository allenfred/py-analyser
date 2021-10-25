import os
import sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import pandas as pd
from models.daily_candles import DailyCandleDao
from models.stocks import StockDao
from sqlalchemy import text
from talib import SMA, EMA, MACD
import time
from datetime import datetime, date
import numpy as np
from api.daily_candle import get_cn_candles
from lib.bias import bias
# from lib.magic_nine_turn import td_8_9

stockDao = StockDao()
dailyCandleDao = DailyCandleDao()

if __name__ == "__main__":
    ts_code = '600733.SH'

    s = text("select trade_date, close from daily_candles where ts_code = :ts_code order by trade_date asc limit 0,10")
    statement = dailyCandleDao.session.execute(s.params(ts_code=ts_code))
    df = pd.DataFrame(statement.fetchall(), columns=['trade_date', 'close'])
    df = df.sort_values(by='trade_date', ascending=True)
    # close = df.close
    # close = df.close.to_numpy()
    for index, item in df.iterrows():
        if index == 0 or index == 1:
            if index == 1:
                print(df.iloc[index - 1])
            print(item.close)


    # print(start)