import tushare as ts
import pandas as pd
from models.daily_candles import DailyCandleDao
import time
from datetime import datetime, date
from config.common import TS_TOKEN

pro = ts.pro_api(TS_TOKEN)
dailyCandleDao = DailyCandleDao()

if __name__ == "__main__":

    today = date.today().strftime("%Y%m%d")
    start = time.time()
    is_not_last_req = True
    df = pd.DataFrame(data={})
    offset = 0
    reqPageNum = 1

    while is_not_last_req:
        print("请求获取第 ", reqPageNum, ' 页数据')

        # 拉取数据
        df = pro.hk_daily(**{
            "ts_code": "",
            "trade_date": today,
            "start_date": "",
            "end_date": "",
            "limit": "",
            "offset": offset
        }, fields=[
            "ts_code",
            "trade_date",
            "open",
            "high",
            "low",
            "close",
            "pre_close",
            "change",
            "pct_chg",
            "vol",
            "amount"
        ])

        if len(df) < 3000:
            is_not_last_req = False
        else:
            offset += len(df)
            reqPageNum += 1

        if len(df) > 0:
            print('拉取 HK candles ', len(df), ' 条数据')
            dailyCandleDao.batch_add(df)
            print('更新 daily_candles ', len(df), ' 条数据')

    end = time.time()
    print('用时', round(end - start, 2), 's')