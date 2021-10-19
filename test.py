import os
import sys
print(sys.path)
print(os.path.dirname(__file__))
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(path)

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

stockDao = StockDao()
dailyCandleDao = DailyCandleDao()

if __name__ == "__main__":
    ts_code = '600733.SH'

    # candles = get_cn_candles(ts_code)
    # dailyCandleDao.batch_add(candles)
    #
    # bias()

    print('hello world!!!')
    # start = date.today().isoformat()
    # print(start)