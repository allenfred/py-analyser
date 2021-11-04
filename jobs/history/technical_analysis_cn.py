import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

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
from lib.ma_shape import long_signals
from lib.util import wrap_technical_quota
import time
from datetime import datetime, date
import numpy as np
from api.daily_candle import get_cn_candles

stockDao = StockDao()
dailyCandleDao = CNDailyCandleDao()
dailyIndicatorDao = DailyIndicatorDao()
dailyLongSignalDao = DailyLongSignalDao()
dailyShortSignalDao = DailyShortSignalDao()

stockLongSignalDao = StockLongSignalDao()
stockShortSignalDao = StockShortSignalDao()

if __name__ == "__main__":
    job_start = time.time()
    today = datetime.now().strftime("%Y-%m-%d")

    while True:
        used_time = round(time.time() - job_start, 0)
        if used_time > 3600 * 5:
            break

        circle_start = time.time()

        ts_code = ''
        stock_stmts = stockDao.session.execute(text("select ts_code from stocks where (scan_date is null or scan_date"
                                                    " < :scan_date) and "
                                                    "(exchange = 'SSE' or exchange = 'SZSE')  limit 1").params(
            scan_date=today))
        stock_result = stock_stmts.fetchone()

        if stock_result:
            ts_code = stock_result[0]
            print('开始扫描: ', ts_code)
        else:
            break

        statement = dailyCandleDao.session.execute(text("select trade_date, open, close, high, low, pct_chg "
                                                        "from cn_daily_candles where ts_code = :ts_code "
                                                        + "and trade_date > '2015-01-01' and open is not null "
                                                          "and close is not null and high is not null and"
                                                        + " low is not null "
                                                        + "order by trade_date desc "
                                                          "limit 0,500").params(ts_code=ts_code))

        df = pd.DataFrame(statement.fetchall(), columns=['trade_date', 'open', 'close', 'high', 'low', 'pct_chg'])
        df = df.sort_values(by='trade_date', ascending=True)
        df['ts_code'] = ts_code

        if len(df):
            try:
                df = wrap_technical_quota(df)
                df_len = len(df)

                small_df = df.iloc[df_len - 10: df_len]
                item = df.iloc[df_len - 1].to_dict()

                dailyLongSignalDao.reinsert(small_df)
                stockLongSignalDao.upsert(item)

                stockDao.update({'ts_code': ts_code, 'scan_date': today})
                print('扫描成功: ', ts_code, ', 扫描最新K线时间: ', today, '，用时 ',
                      round(time.time() - circle_start, 1), ' s')
            except Exception as e:
                stockDao.update({'ts_code': ts_code, 'scan_date': today})
                print('更新扫描结果 Catch Error:', e, '，用时 ',
                      round(time.time() - circle_start, 1), ' s')
        else:
            stockDao.update({'ts_code': ts_code, 'scan_date': today})
            print('股票代码: ', ts_code, ' 没有行情数据', '，用时 ',
                  round(time.time() - circle_start, 1), ' s')
