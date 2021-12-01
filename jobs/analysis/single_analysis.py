import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

from sqlalchemy import text
import pandas as pd
import time
from datetime import datetime, date
import numpy as np

from models.db import DBSession
from models.cn_daily_candles import CNDailyCandleDao
from models.daily_indicators import DailyIndicatorDao
from models.daily_long_signals import DailyLongSignalDao
from models.daily_short_signals import DailyShortSignalDao
from models.stock_long_signals import StockLongSignalDao
from models.stock_short_signals import StockShortSignalDao
from models.stocks import StockDao

from lib.analytic_signals import analytic_signals
from lib.util import wrap_technical_indicator, used_time_fmt
from api.daily_candle import get_cn_candles
from jobs.scan.daily_candle import scan_daily_candles

stockDao = StockDao()
dailyCandleDao = CNDailyCandleDao()
dailyIndicatorDao = DailyIndicatorDao()
dailyLongSignalDao = DailyLongSignalDao()

stockLongSignalDao = StockLongSignalDao()

if __name__ == "__main__":
    ts_code = '300692.SZ'
    scan_daily_candles(ts_code, 'CN', '2021-11-30')
    print('扫描成功')

