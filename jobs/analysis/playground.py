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
    ts_code = '300913.SZ'
    ts_code = '300315.SZ'
    ts_code = '300308.SZ'
    ts_code = '300660.SZ'
    ts_code = '002292.SZ'
    ts_code = '002281.SZ'
    ts_code = '301183.SZ'
    ts_code = '300315.SZ'

    scan_daily_candles(ts_code, 'CN', '2023-07-05')
    print('扫描成功')
