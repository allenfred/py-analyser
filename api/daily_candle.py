import tushare as ts
import pandas as pd
from config.common import TS_TOKEN
import yfinance as yf

pro = ts.pro_api(TS_TOKEN)


def get_cn_candles(options):
    df = pro.daily(**{
        "ts_code": options.get("ts_code", ""),
        "trade_date": options.get("trade_date", ""),
        "start_date": options.get("start_date", ""),
        "end_date": options.get("end_date", ""),
        "offset": options.get("offset", 0),
        "limit": options.get("limit", 5000)
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

    return df


def get_hk_candles(options):
    df = pro.hk_daily(**{
        "ts_code": options.get("ts_code", ""),
        "trade_date": options.get("trade_date", ""),
        "start_date": options.get("start_date", ""),
        "end_date": options.get("end_date", ""),
        "offset": options.get("offset", 0),
        "limit": options.get("limit", 3000)
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

    return df


def get_us_candles(options):
    df = pro.us_daily(**{
        "ts_code": options.get("ts_code", ""),
        "trade_date": options.get("trade_date", ""),
        "start_date": options.get("start_date", ""),
        "end_date": options.get("end_date", ""),
        "offset": options.get("offset", 0),
        "limit": options.get("limit", 5000)
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
        "total_mv",
        "pe",
        "pb",
        "change",
        "turnover_ratio"
    ])

    df['turnover_rate'] = df['turnover_ratio']
    df['pct_chg'] = df['pct_change']
    df['chg'] = df['change']
    
    df = df[
        ['ts_code', 'trade_date', 'close', 'open', 'high', 'low', 'chg',
         'pre_close', 'pct_chg', 'vol', 'amount', 'total_mv', 'pe', 'pb', 'turnover_rate']]

    return df
