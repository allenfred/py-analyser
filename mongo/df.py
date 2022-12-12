import pandas as pd
import numpy as np
import datetime
# from datetime import datetime, date, timedelta
from .database import InstrumentInfo, UsdtSwapKlines
import mplfinance as mpf
import matplotlib.dates as mpl_dates
from json import loads, dumps


def get_usdt_swap_klines(exchange, inst_id, granularity, limit=500):
    # print(datetime.datetime.utcnow() + datetime.timedelta(hours=-20))
    kline_list = [
        loads(dumps(doc, default=convert_date))
        for doc in UsdtSwapKlines.find(
            {"exchange": exchange, "instrument_id": inst_id, "granularity": int(granularity),
             "timestamp": {
                 '$lte': datetime.datetime.utcnow() + datetime.timedelta(hours=0)}},
            {"_id": 0, "__v": 0, "currency_volume": 0, "granularity": 0, "underlying_index": 0},
        ).sort("timestamp", -1).limit(limit)
    ]

    df = (pd.DataFrame(kline_list))

    return df


def convert_date(date):
    if isinstance(date, (datetime.date, datetime.datetime)):
        # beijing = datetime.timezone(datetime.timedelta(hours=8))
        utc = datetime.timezone(datetime.timedelta(hours=0))
        return date.astimezone(utc).strftime("%Y-%m-%d %H:%M:%S")


def get_instruments(exchange=None):
    if exchange:
        return InstrumentInfo.find(
            {"exchange": exchange},
        ).sort("volume_24h", -1)
    else:
        return InstrumentInfo.find(
            {},
        ).sort("volume_24h", -1)


def get_tickers():
    return InstrumentInfo.aggregate([
        {"$sort": {"exchange": 1}},
        {
            "$group": {
                "_id": "$base_currency",
                "base_currency": {"$first": "$base_currency"},
                "quote_currency": {"$first": "$quote_currency"},
                "exchange": {"$first": "$exchange"},
                "volume_24h": {"$first": "$volume_24h"},
                "instrument_id": {"$first": "$instrument_id"},
            }
        }, {"$sort": {"volume_24h": -1}},
        {
            "$project": {
                "instrument_id": "$instrument_id",
                "base_currency": "$base_currency",
                "quote_currency": "$quote_currency",
                "exchange": "$exchange",
                "volume_24h": "$volume_24h"
            }
        }
    ])


def get_klines_df(exchange, inst_id, granularity, limit=1000):
    df = get_usdt_swap_klines(exchange, inst_id, granularity, limit)
    df = df.sort_values(by='timestamp', ascending=True)
    df['date'] = pd.to_datetime(df.timestamp)
    df = df.set_index('date')

    return df
