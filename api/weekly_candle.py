import tushare as ts
import pandas as pd
from config.common import TS_TOKEN

pro = ts.pro_api(TS_TOKEN)


def get_candles(options):
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

    return df
