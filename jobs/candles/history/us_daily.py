# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

from pathlib import Path
import tushare as ts
import pandas as pd
from models.us_daily_candles import USDailyCandleDao
from models.trade_calendar import TradeCalendarDao
from models.stocks import StockDao
import time
from datetime import datetime, timedelta
from config.common import TS_TOKEN
from api.daily_candle import get_us_candles
from lib.util import used_time_fmt

pro = ts.pro_api(TS_TOKEN)
dailyCandleDao = USDailyCandleDao()
calendarDao = TradeCalendarDao()
stockDao = StockDao()


def ready_candles_by_stock(start_time):
    all_history_candle_set = False
    yesterday = (datetime.now() + timedelta(hours=-24)).strftime("%Y-%m-%d")

    df = get_us_candles({"limit": 1, "offset": 0})
    latest_candle_date = datetime.strftime(datetime.strptime(df["trade_date"][0], "%Y%m%d"), '%Y-%m-%d')
    #
    # if not latest_candle_date == yesterday:
    #     print('tushare 尚未同步 US 最新行情数据:', yesterday)
    #     quit()

    while not all_history_candle_set:
        circle_start = time.time()
        ts_code = stockDao.find_one_candle_not_ready('US', latest_candle_date)

        if ts_code is None:
            break

        try:
            df = get_us_candles({"ts_code": ts_code, "limit": 2000, "offset": 0})
            df = df.sort_values(by='trade_date', ascending=False)

            # 过滤出最新candle数据 (相较于db)
            db_df = dailyCandleDao.find_by_ts_code(ts_code)
            new_df = df.loc[~pd.to_datetime(df["trade_date"], format='%Y-%m-%d').isin(db_df["trade_date"].to_numpy())]

            filepath = Path(path + '/csv/us/' + ts_code + '.csv')
            filepath.parent.mkdir(parents=True, exist_ok=True)
            new_df.to_csv(filepath, index=False)

            dailyCandleDao.load_local_file(str(filepath))
            stockDao.update({'ts_code': ts_code, 'candle_date': today})

            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '已更新 ', ts_code, '/', len(new_df),
                  ' 条K线，用时 ',
                  used_time_fmt(circle_start, time.time()), ', 总用时 ', used_time_fmt(start_time, time.time()))
        except Exception as e:
            stockDao.update({'ts_code': ts_code, 'candle_date': today})
            print('Error:', e)


if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")

    start = time.time()
    ready_candles_by_stock(start)

    end = time.time()

    print(today, '用时', used_time_fmt(start, end))
