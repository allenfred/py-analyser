import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

import tushare as ts
from models.stocks import StockDao
import time
from config.common import TS_TOKEN

pro = ts.pro_api(TS_TOKEN)
stockDao = StockDao()

if __name__ == "__main__":

    start = time.time()

    # 查询当前所有正常上市交易的股票列表
    df = pro.stock_basic(**{
        "ts_code": "",
        "name": "",
        "exchange": "",
        "market": "",
        "is_hs": "",
        "list_status": "L",
        "limit": "",
        "offset": ""
    }, fields=[
        "ts_code",
        "symbol",
        "name",
        "area",
        "industry",
        "market",
        "list_date",
        "delist_date",
        "cnspell",
        "enname",
        "fullname",
        "exchange",
        "list_status",
        "is_hs"
    ])

    stockDao.bulk_upsert(df)
    print('更新 stocks 完成', len(df), ' 条数据')

    end = time.time()
    print('用时', round(end - start, 2), 's')