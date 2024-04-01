"""
proxy for okex api.
"""
import pandas as pd
import datetime
from jobs.crypto.database import (
    InstrumentInfo,
    UsdtSwapKlines,
)
from json import loads, dumps


def convert_date(date):
    if isinstance(date, (datetime.date, datetime.datetime)):
        # beijing = datetime.timezone(datetime.timedelta(hours=8))
        utc = datetime.timezone(datetime.timedelta(hours=0))
        return date.astimezone(utc).strftime("%Y-%m-%d %H:%M:%S")


def get_usdt_swap_klines(exchange, inst_id, granularity, limit=500):
    kline_list = [
        loads(dumps(doc, default=convert_date))
        for doc in UsdtSwapKlines.find(
            {"exchange": exchange, "instrument_id": inst_id, "granularity": int(granularity)},
            {"_id": 0, "__v": 0, "currency_volume": 0, "granularity": 0, "underlying_index": 0},
        ).sort("timestamp", -1).limit(limit)
    ]

    df = (pd.DataFrame(kline_list))

    return df


# def get_usdt_swap_klines(exchange, inst_id, granularity, limit=500):
#     # schema = Schema({'open': float, 'high': float, 'low': float, 'close': float, 'timestamp': datetime.datetime})
#     # return UsdtSwapKlines. \
#     #     find_pandas_all({"instrument_id": inst_id, "granularity": int(granularity)}, schema=schema,
#     #                     sort=[('timestamp', -1)], limit=limit)
#
#     # schema = Schema({'open': float, 'high': float, 'low': float, 'close': float, 'volume': float,
#     #                  'exchange': pa.string(), 'underlying_index': pa.string(), 'timestamp': datetime.datetime})
#
#     schema = Schema({'open': float, 'high': float, 'low': float, 'close': float, 'volume': float,
#                      'timestamp': pa.timestamp('ms')})
#
#     return UsdtSwapKlines. \
#         find_pandas_all({"exchange": exchange, "instrument_id": inst_id, "granularity": int(granularity)},
#                         schema=schema,
#                         sort=[('timestamp', -1)], limit=limit)


def get_klines_df(exchange, inst_id, granularity, limit=1000):
    df = get_usdt_swap_klines(exchange, inst_id, granularity, limit)
    df = df.sort_values(by='timestamp', ascending=True)
    df["vol"] = df['volume']
    df["trade_date"] = df['timestamp']
    df['pct_chg'] = ((df["close"] - df["open"]) * 100) / df['open']

    return df


def get_instruments(exchange=None):
    if exchange:
        return InstrumentInfo.find(
            {"exchange": exchange},
        ).sort("instrument_id", -1)
    else:
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
