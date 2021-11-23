import tushare as ts
import pandas as pd
from config.common import TS_TOKEN

pro = ts.pro_api(TS_TOKEN)


def get_cn_daily_basic(trade_date):
    df = pro.daily_basic(**{
        "ts_code": "",
        "trade_date": trade_date,
        "start_date": "",
        "end_date": "",
        "limit": "",
        "offset": ""
    }, fields=[
        "ts_code",
        "trade_date",
        "close",
        "turnover_rate",
        "turnover_rate_f",
        "volume_ratio",
        "pe",
        "pe_ttm",
        "pb",
        "ps",
        "ps_ttm",
        "dv_ratio",
        "dv_ttm",
        "total_share",
        "float_share",
        "free_share",
        "total_mv",
        "circ_mv",
        "limit_status"
    ])

    return df
