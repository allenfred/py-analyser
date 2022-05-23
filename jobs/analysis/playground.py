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

from api.daily_candle import get_cn_candles
from jobs.scan.daily_candle import scan_daily_candles


if __name__ == "__main__":
    # ts_code = '002603.SZ'
    # ts_code = '000425.SZ'
    # ts_code = '600129.SH'
    # ts_code = '601699.SH'
    # ts_code = '000933.SZ'
    # ts_code = '601666.SH'
    # ts_code = '003002.SZ'
    # ts_code = '600096.SH'
    # ts_code = '600617.SH'
    # ts_code = '600557.SH'
    # ts_code = '600502.SH'
    # ts_code = '600898.SH'
    ts_code = '605098.SH'
    scan_daily_candles(ts_code, 'CN', '2022-05-23')
    print('扫描成功')

