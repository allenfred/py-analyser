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
    ts_code = '002561.SZ'  # 徐家汇
    ts_code = '000722.SZ'  # 湖南发展
    # ts_code = '600502.SH' # 安徽建工
    # ts_code = '600313.SH' # 农发种业
    ts_code = '002207.SZ'
    ts_code = '600470.SH'
    ts_code = '600724.SH'
    ts_code = '600053.SH'
    ts_code = '003037.SZ'
    ts_code = '603359.SH'
    ts_code = '600028.SH'
    ts_code = '002446.SZ'
    ts_code = '003029.SZ'
    # ts_code = '300379.SZ'
    # ts_code = '300206.SZ'
    ts_code = '688677.SH'
    # ts_code = '002908.SZ'
    ts_code = '002952.SZ'
    ts_code = '600546.SH'
    ts_code = '600766.SH'
    ts_code = '000975.SZ'
    ts_code = '002334.SZ'
    ts_code = '002868.SZ'
    # ts_code = '002197.SZ'
    ts_code = '000948.SZ'
    # ts_code = '600992.SH'
    # ts_code = '002829.SZ'
    # ts_code = '688385.SH'
    # ts_code = '300138.SZ'
    # ts_code = '600875.SH'
    # ts_code = '003029.SZ'
    ts_code = '003029.SZ'
    ts_code = '002853.SZ'
    ts_code = '605020.SH'
    ts_code = '601098.SH'
    ts_code = '000722.SZ'  # 湖南发展
    ts_code = '002799.SZ'  # 湖南发展
    ts_code = '002246.SZ'  # 湖南发展
    ts_code = '000721.SZ'  # 西安饮食
    ts_code = '600056.SH'  # 中国医药
    # ts_code = '000610.SZ'  # 西安旅游
    # ts_code = '000721.SZ'  # 西安饮食

    scan_daily_candles(ts_code, 'CN', '2023-02-06')
    print('扫描成功')
