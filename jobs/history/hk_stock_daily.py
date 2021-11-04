import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

import tushare as ts
import pandas as pd
from models.hk_daily_candles import HKDailyCandleDao
from models.stocks import StockDao
import time
from datetime import datetime
from config.common import TS_TOKEN
from api.daily_candle import get_hk_candles

pro = ts.pro_api(TS_TOKEN)
dailyCandleDao = HKDailyCandleDao()
stockDao = StockDao()


def ready_candles_by_stock():
    all_history_candle_set = False
    today = datetime.now().strftime("%Y-%m-%d")

    df = get_hk_candles({"limit": 1, "offset": 0})
    latest_candle_date = datetime.strftime(datetime.strptime(df["trade_date"][0], "%Y%m%d"), '%Y-%m-%d')

    if not latest_candle_date == today:
        print('tushare 尚未同步 HK 最新行情数据:', today)
        quit()

    while not all_history_candle_set:
        circle_start = time.time()
        ts_code = stockDao.find_one_candle_not_ready('HK', today)

        if ts_code is None:
            break

        try:
            df = get_hk_candles({"ts_code": ts_code, "limit": 2000, "offset": 0})
            df = df.sort_values(by='trade_date', ascending=False)

            # 过滤出最新candle数据 (相较于db)
            db_df = dailyCandleDao.find_all(ts_code)
            new_df = df.loc[~pd.to_datetime(df["trade_date"], format='%Y-%m-%d').isin(db_df["trade_date"].to_numpy())]

            dailyCandleDao.bulk_insert(new_df)
            stockDao.set_candle_ready(ts_code, today)

            print('已更新 HK daily_candles / ', ts_code, ': ', len(df), ' 条数据，用时 ',
                  round(time.time() - circle_start, 2), ' s')
        except Exception as e:
            stockDao.set_candle_ready(ts_code, today)
            print('Error:', e)


if __name__ == "__main__":
    start = time.time()
    ready_candles_by_stock()
    end = time.time()

    print('用时', round(end - start, 2), 's')
