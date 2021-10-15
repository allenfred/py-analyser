import tushare as ts
import pandas as pd
from models.daily_candles import DailyCandleDao
from models.trade_calendar import TradeCalendarDao
import time
from datetime import datetime
from config.common import TS_TOKEN

pro = ts.pro_api(TS_TOKEN)
dailyCandleDao = DailyCandleDao()
calendarDao = TradeCalendarDao()

if __name__ == "__main__":

    start = time.time()
    all_history_candle_set = False
    is_last_req = False
    df = pd.DataFrame(data={})
    offset = 0
    totalGotCount = 0
    limit = 3000

    while not all_history_candle_set:
        circle_start = time.time()
        item = calendarDao.find_one_candle_not_ready('HK')
        trade_dte = ''

        if item:
            trade_dte = datetime.strftime(item.cal_date, "%Y%m%d")
            is_last_req = False
            totalGotCount = 0
            offset = 0
        else:
            all_history_candle_set = True

        while not is_last_req:

            df = pro.hk_daily(**{
                "ts_code": "",
                "trade_date": trade_dte,
                "start_date": "",
                "end_date": "",
                "limit": limit,
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

            totalGotCount += len(df)
            if len(df) < limit:
                is_last_req = True
            else:
                offset += len(df)

            dailyCandleDao.batch_add(df)
            calendarDao.set_candle_ready('HK', item.cal_date)

            print('已更新 HK daily_candles ', item.cal_date, ': ', totalGotCount, ' 条数据，用时 ',
                  round(time.time() - circle_start, 2), ' s')

    end = time.time()
    print('用时', round(end - start, 2), 's')
