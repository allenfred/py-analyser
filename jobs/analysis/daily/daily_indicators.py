# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

import pandas as pd
from models.cn_daily_candles import CNDailyCandleDao
from models.daily_indicators import DailyIndicatorDao
from models.stocks import StockDao
from sqlalchemy import text
from lib.util import set_quota, used_time_fmt
import time

stockDao = StockDao()
dailyCandleDao = CNDailyCandleDao()
dailyIndicatorDao = DailyIndicatorDao()

if __name__ == "__main__":
    job_start = time.time()
    candle = dailyCandleDao.find_latest_candle()

    if candle is None:
        print('没有K线数据')
        quit()

    indicator_date = candle['trade_date']

    while True:
        used_time = round(time.time() - job_start, 0)
        if used_time > 3600 * 5:
            break

        circle_start = time.time()

        ts_code = ''
        stock_stmts = stockDao.session.execute(text("select ts_code from stocks where (indicator_date is null or "
                                                    "indicator_date < :indicator_date) and "
                                                    "(exchange = 'SSE' or exchange = 'SZSE')  limit 1").params(
            indicator_date=indicator_date))
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
                df = set_quota(df)
                df_len = len(df)
                # 只更新最新30天的指标
                small_df = df.iloc[df_len - 30: df_len]
                dailyIndicatorDao.reinsert(df)

                print('Calc Indicator 成功: ', ts_code, ',最新K线时间: ', indicator_date, ',用时',
                      used_time_fmt(circle_start, time.time()), ",总用时",
                      used_time_fmt(job_start, time.time()))
            except Exception as e:
                stockDao.update({'ts_code': ts_code, 'indicator_date': indicator_date})
                print('更新 Catch Error:', e)
        else:
            stockDao.update({'ts_code': ts_code, 'indicator_date': indicator_date})
            print('股票代码: ', ts_code, ' 没有行情数据')
