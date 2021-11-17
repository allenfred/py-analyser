import pandas as pd
from models.db import DBSession
from models.cn_daily_candles import CNDailyCandleDao
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
import time
from datetime import datetime, date
import numpy as np
from api.daily_candle import get_cn_candles
import platform

stockDao = StockDao()
dailyCandleDao = CNDailyCandleDao()
dailyIndicatorDao = DailyIndicatorDao()
dailyLongSignalDao = DailyLongSignalDao()
dailyShortSignalDao = DailyShortSignalDao()

stockLongSignalDao = StockLongSignalDao()
stockShortSignalDao = StockShortSignalDao()

if __name__ == "__main__":
    # print("platform.platform()=%s", platform.platform())
    system_p = platform.platform()
    if "macOS" in system_p:
        print('is macos ', system_p)
