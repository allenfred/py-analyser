# 导入tushare
import tushare as ts
import pandas as pd
from models.stocks import StockDao
import time
from config.common import TS_TOKEN

pro = ts.pro_api(TS_TOKEN)
stockDao = StockDao()

if __name__ == "__main__":

    start = time.time()
    is_not_last_req = True
    df = pd.DataFrame(data={})
    offset = 0
    totalGotCount = 0

    while is_not_last_req:

        df = pro.hk_basic(**{
            "ts_code": "",
            "list_status": "",
            "limit": 5000,
            "offset": offset
        }, fields=[
            "ts_code",
            "name",
            "fullname",
            "enname",
            "cn_spell",
            "market",
            "list_status",
            "list_date",
            "delist_date",
            "trade_unit",
        ])

        if len(df) < 5000:
            is_not_last_req = False
        else:
            offset += len(df)

        df['exchange'] = 'HK'

        print('拉取 HK 股票列表 ', len(df), ' 条数据')
        stockDao.batch_add(df)
        print('更新 HK stocks 完成', len(df), ' 条数据')

    end = time.time()
    print('用时', round(end - start, 2), 's')