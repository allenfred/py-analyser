"""
proxy for okex api.
"""
import numpy as np
import pandas as pd
import datetime
from json import dumps, loads
from database import (
    InstrumentInfos,
    UsdtSwapKlines,
)


def convert_date(date):
    if isinstance(date, (datetime.date, datetime.datetime)):
        beijing = datetime.timezone(datetime.timedelta(hours=8))
        return date.astimezone(beijing).strftime("%Y-%m-%d %H:%M:%S")


#
# def getKlines(
#     model=InstrumentCandles,
#     underlying_index="BTC",
#     alias="swap",
#     granularity="86400",
#     limit=500,
# ):
#     # return swapAPI.get_kline("BTC-USD-SWAP", granularity)
#     return [
#         loads(dumps(doc, default=convert_date))
#         for doc in model.find(
#             {
#                 "underlying_index": underlying_index,
#                 "granularity": int(granularity),
#             },
#             {"_id": 0, "_v": 0},
#         )
#         .sort("timestamp", -1)
#         .limit(limit)
#     ]

def get_usdt_swap_klines(inst_id, granularity, limit=500):
    # return [
    #     loads(dumps(doc, default=convert_date))
    #     for doc in UsdtSwapKlines.find(
    #         {"granularity": int(granularity), "instrument_id": inst_id},
    #         {"_id": 0, "_v": 0},
    #     )
    #         .sort("timestamp", -1)
    #         .limit(limit)
    # ]
    return UsdtSwapKlines.find(
        {"granularity": int(granularity), "instrument_id": inst_id},
        {"_id": 0, "_v": 0},
    ).sort("timestamp", -1).limit(limit)


def clean_klines(klines):
    """
    获取k线对应的DataFrame
    klines 默认为根据时间升序排序
    """
    df = pd.DataFrame(
        columns=["trade_date", "open", "high", "low", "close", "vol",
                 "pct_chg", "exchange", "time", "underlying_index"],
        # index=range(len(klines)),
    )

    for index, item in enumerate(klines):
        df.loc[index] = {
            "trade_date": item["timestamp"],
            "open": item["open"],
            "high": item["high"],
            "low": item["low"],
            "close": item["close"],
            "vol": float(item["volume"]),
            "pct_chg": ((item["close"] - item["open"]) * 100) / item["open"],
            "exchange": item["exchange"],
            "time": item["timestamp"],
            "underlying_index": item["underlying_index"]
        }

    return df


def get_klines_df(inst_id, granularity, limit=1000):
    klines = get_usdt_swap_klines(inst_id, granularity, limit)
    return clean_klines(klines)


def get_inst_df(exchange=None):
    if exchange:
        return InstrumentInfos.find(
            {"exchange": exchange}
        ).sort("instrument_id", -1)
    else:
        return InstrumentInfos.find({}).sort("instrument_id", -1)
