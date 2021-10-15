import tushare as ts
import pandas as pd
from models.daily_candles import DailyCandleDao
import time
from datetime import date
from config.common import TS_TOKEN

pro = ts.pro_api(TS_TOKEN)
dailyCandleDao = DailyCandleDao()

if __name__ == "__main__":

    today = date.today().strftime("%Y%m%d")
    start = time.time()
    is_not_last_req = True
    df = pd.DataFrame(data={})
    offset = 0
    totalGotCount = 0

    while is_not_last_req:

        # 拉取日线数据
        df = pro.daily(**{
            "ts_code": "",
            "trade_date": today,
            "start_date": "",
            "end_date": "",
            "offset": offset,
            "limit": 5000
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

        totalGotCount += len(df)
        if len(df) < 5000:
            is_not_last_req = False
        else:
            offset += len(df)

        print('已获取 CN daily_candles ', totalGotCount, ' 条数据，用时 ',
              round(time.time() - start, 2), ' s')

        dailyCandleDao.batch_add(df)

    end = time.time()
    print('用时', round(end - start, 2), 's')
