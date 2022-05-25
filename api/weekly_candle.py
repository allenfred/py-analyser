import tushare as ts
import pandas as pd
from config.common import TS_TOKEN

pro = ts.pro_api(TS_TOKEN)


def get_candles(options):
    onging = True
    retry_times = 0
    df = []

    while onging:
        try:
            retry_times += 1
            df = pro.weekly(**{
                "ts_code": options.get("ts_code", ""),
                "trade_date": "",
                "start_date": "",
                "end_date": "",
                "limit": options.get("limit", 500),
                "offset": ""
            }, fields=[
                "ts_code",
                "trade_date",
                "close",
                "open",
                "high",
                "low",
                "pre_close",
                "change",
                "pct_chg",
                "vol",
                "amount"
            ])
            onging = False
        except Exception as e:
            if retry_times < 5:
                print('请求失败, 重试')
            else:
                print('tushare API网络不通, 终止请求')
                break

    return df