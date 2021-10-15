import tushare as ts
import pandas as pd
from config.common import TS_TOKEN

pro = ts.pro_api(TS_TOKEN)


def get_cn_candles(ts_code):
    is_not_last_req = True
    sum_df = pd.DataFrame(data={})
    limit = 5000
    offset = 0

    while is_not_last_req:

        # 拉取日线数据
        df = pro.daily(**{
            "ts_code": ts_code,
            "trade_date": "",
            "start_date": "",
            "end_date": "",
            "offset": offset,
            "limit": limit
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

        if len(df) < limit:
            is_not_last_req = False
        else:
            offset += len(df)

        if len(sum_df) > 0:
            sum_df.append(df)
        else:
            sum_df = df

    return sum_df


def get_hk_candles(ts_code):

    is_not_last_req = True
    sum_df = pd.DataFrame(data={})
    limit = 3000
    offset = 0

    while is_not_last_req:

        df = pro.hk_daily(**{
            "ts_code": ts_code,
            "trade_date": "",
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

        if len(df) < limit:
            is_not_last_req = False
        else:
            offset += len(df)

        if len(sum_df) > 0:
            sum_df.append(df)
        else:
            sum_df = df

    return sum_df


def get_us_candles(ts_code):

    is_not_last_req = True
    sum_df = pd.DataFrame(data={})
    limit = 6000
    offset = 0

    while is_not_last_req:

        df = pro.us_daily(**{
            "ts_code": ts_code,
            "trade_date": "",
            "start_date": "",
            "end_date": "",
            "offset": offset,
            "limit": limit
        }, fields=[
            "ts_code",
            "trade_date",
            "close",
            "open",
            "high",
            "low",
            "pre_close",
            "pct_change",
            "vol",
            "amount",
            "vwap",
            "total_mv",
            "pe",
            "pb",
            "change",
            "turnover_ratio"
        ])

        if len(df) < limit:
            is_not_last_req = False
        else:
            offset += len(df)

        if len(sum_df) > 0:
            sum_df.append(df)
        else:
            sum_df = df

    return sum_df