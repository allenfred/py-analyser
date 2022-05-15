import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)

import tushare as ts
import time
from datetime import datetime, timedelta
from config.common import TS_TOKEN
from models.stocks import StockDao
from models.cn_daily_candles import CNDailyCandleDao

ts.set_token(TS_TOKEN)
pro = ts.pro_api()
stockDao = StockDao()
dailyCandleDao = CNDailyCandleDao()


def check_daily():
    start = time.time()
    today = datetime.now().strftime("%Y%m%d")

    # 获取当天是除权除息日的股票
    df = pro.dividend(ex_date=today, fields='ts_code,div_proc,stk_div,record_date,ex_date')
    year_ago = (datetime.now() - timedelta(days=360)).strftime("%Y%m%d")
    print(df['ts_code'])

    for row in df.itertuples():
        df = ts.pro_bar(ts_code=row.ts_code, adj='qfq', start_date=year_ago, end_date=today)
        print(row.ts_code, '获取行情完成, 当前用时', round(time.time() - start, 2), 's')

        stockDao.update({'ts_code': row.ts_code, 'ex_date': row.ex_date})
        dailyCandleDao.bulk_update(df)
        print(row.ts_code, '更新行情完成, 当前用时', round(time.time() - start, 2), 's')

    end = time.time()
    print('总用时', round(end - start, 2), 's')


def check_all():
    start = time.time()
    today = datetime.now().strftime("%Y%m%d")
    year_ago = (datetime.now() - timedelta(days=360)).strftime("%Y%m%d")

    check_days = 200
    while check_days < 360:
        ex_date = (datetime.now() - timedelta(days=check_days)).strftime("%Y%m%d")
        # 获取除权除息日的股票
        df = pro.dividend(ex_date=ex_date, fields='ts_code,div_proc,stk_div,record_date,ex_date')
        print(ex_date, df['ts_code'].to_numpy())

        for row in df.itertuples():
            df = ts.pro_bar(ts_code=row.ts_code, adj='qfq', start_date=year_ago, end_date=today)
            print(row.ts_code, '获取行情完成, 当前用时', round(time.time() - start, 2), 's')

            stockDao.update({'ts_code': row.ts_code, 'ex_date': row.ex_date})
            dailyCandleDao.bulk_update(df)
            print(row.ts_code, '更新行情完成, 当前用时', round(time.time() - start, 2), 's')

        check_days += 1

    end = time.time()
    print('总用时', round(end - start, 2), 's')


if __name__ == "__main__":
    check_all()