# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

import pandas as pd
from models.db import DBSession
from models.cn_daily_candles import CNDailyCandleDao
from models.stocks import StockDao
from sqlalchemy import text
from talib import SMA, EMA, MACD
from lib.bias import bias
from lib.ma_slope import slope
from lib.magic_nine_turn import td
from lib.util import used_time_fmt, is_mac_os
import time
from datetime import datetime, date, timedelta
import numpy as np
from api.daily_candle import get_cn_candles
import time
import threading
import multiprocessing
from multiprocessing import Pool
from jobs.scan.daily_candle import scan_daily_candles

stockDao = StockDao()
dailyCandleDao = CNDailyCandleDao()

if __name__ == "__main__":
    job_start = time.time()

    end = (datetime.now() + timedelta(days=-1)).strftime("%Y-%m-%d")
    start = (datetime.now() + timedelta(days=-301)).strftime("%Y-%m-%d")
    exchange = 'SSE'
    candle_relation = 'cn_daily_candles'

    session = DBSession()
    calendar_stmts = session.execute(text("select count(id) from trade_calendar where cal_date >= :start"
                                          " and cal_date <= :end and is_open = 1 and exchange = :exchange"
                                          ).params(exchange=exchange, start=start, end=end))
    result = calendar_stmts.fetchall()
    session.commit()
    session.close()
    print(result[0][0])

    ts_code = '601857.SH'
    candle_stmts = session.execute(text("select count(id) from " + candle_relation
                                        + " where trade_date >= :start and trade_date <= :end "
                                          "and ts_code = :ts_code").params(
                                            ts_code=ts_code, start=start, end=end))

    candle_result = candle_stmts.fetchall()
    session.commit()
    print(candle_result[0][0])
