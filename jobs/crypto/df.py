"""
proxy for okex api.
"""
import pandas as pd
import datetime
from database import (
    InstrumentInfo,
    UsdtSwapKlines,
)
from pymongoarrow.monkey import patch_all
import pyarrow as pa
from pymongoarrow.api import Schema

patch_all()


def convert_date(date):
    if isinstance(date, (datetime.date, datetime.datetime)):
        # beijing = datetime.timezone(datetime.timedelta(hours=8))
        utc = datetime.timezone(datetime.timedelta(hours=0))
        return date.astimezone(utc).strftime("%Y-%m-%d %H:%M:%S")


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

def get_usdt_swap_klines(exchange, inst_id, granularity, limit=500):
    # return UsdtSwapKlines.find(
    #     {"instrument_id": inst_id, "granularity": int(granularity)},
    #     {"_id": 0, "_v": 0, "exchange": 0, "granularity": 0, "instrument_id": 0, "currency_volume": 0},
    #     # ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'underlying_index']
    # ).sort("timestamp", -1).limit(limit)

    # cursor = UsdtSwapKlines.find(
    #     {"instrument_id": inst_id, "granularity": int(granularity)},
    #     {"_id": 0, "__v": 0, "exchange": 0, "granularity": 0, "instrument_id": 0, "currency_volume": 0},
    # ).sort("timestamp", -1).limit(limit)

    # return [
    #     loads(dumps(doc, default=convert_date))
    #     for doc in UsdtSwapKlines.find(
    #         {"instrument_id": inst_id, "granularity": int(granularity)},
    #         # {"_id": 0, "__v": 0, "exchange": 0, "granularity": 0, "instrument_id": 0, "currency_volume": 0},
    #         {"_id": 0, "__v": 0, "granularity": 0, "instrument_id": 0, "currency_volume": 0},
    #     ).sort("timestamp", -1).limit(limit)
    # ]

    # schema = Schema({'open': float, 'high': float, 'low': float, 'close': float, 'timestamp': datetime.datetime})
    # return UsdtSwapKlines. \
    #     find_pandas_all({"instrument_id": inst_id, "granularity": int(granularity)}, schema=schema,
    #                     sort=[('timestamp', -1)], limit=limit)

    # schema = Schema({'open': float, 'high': float, 'low': float, 'close': float, 'volume': float,
    #                  'exchange': pa.string(), 'underlying_index': pa.string(), 'timestamp': datetime.datetime})

    schema = Schema({'open': float, 'high': float, 'low': float, 'close': float, 'volume': float,
                     'timestamp': pa.timestamp('ms')})

    return UsdtSwapKlines. \
        find_pandas_all({"exchange": exchange, "instrument_id": inst_id, "granularity": int(granularity)},
                        schema=schema,
                        sort=[('timestamp', -1)], limit=limit)


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

    # for index, item in enumerate(klines):
    for index in range(len(klines)):
        item = klines.iloc[index]
        # print(index, item.timestamp)
        pct_chg = 0
        if index > 0:
            pct_chg = ((item["close"] - klines.iloc[index]["close"]) * 100) / klines.iloc[index]["close"]

        df.loc[index] = {
            "trade_date": item["timestamp"],
            "open": item["open"],
            "high": item["high"],
            "low": item["low"],
            "close": item["close"],
            "vol": item["volume"],
            # "pct_chg": ((item["close"] - item["open"]) * 100) / item["open"],
            "pct_chg": pct_chg,
            "exchange": item["exchange"],
            "time": item["timestamp"],
            "underlying_index": item["underlying_index"]
        }

    return df


def get_klines_df(exchange, inst_id, granularity, limit=1000):
    df = get_usdt_swap_klines(exchange, inst_id, granularity, limit)
    df = df.sort_values(by='timestamp', ascending=True)
    df["vol"] = df['volume']
    df["trade_date"] = df['timestamp']
    df['pct_chg'] = ((df["close"] - df["open"]) * 100) / df['open']

    return df


# def get_instruments(exchange=None):
#     if exchange:
#         tickers = list(InstrumentTicker.find(
#             {"exchange": exchange},
#             # {"_id": 0, "__v": 0, "exchange": 1, "instrument_id": 1, "last": 1, "volume_24h": 1},
#             {"exchange": 1, "instrument_id": 1, "last": 1, "volume_24h": 1},
#         ).sort("instrument_id", -1))
#         infos = list(InstrumentInfo.find(
#             {"exchange": exchange},
#             # {"_id": 0, "__v": 0, "exchange": 1, "instrument_id": 1, "contract_val": 1},
#             {"exchange": 1, "instrument_id": 1, "contract_val": 1},
#         ).sort("instrument_id", -1))
#     else:
#         tickers = list(InstrumentTicker.find({},
#                                              {"exchange": 1, "instrument_id": 1, "last": 1,
#                                               "volume_24h": 1},
#                                              ).sort("instrument_id", -1))
#         infos = list(InstrumentInfo.find({},
#                                          {"exchange": 1, "instrument_id": 1, "contract_val": 1},
#                                          ).sort("instrument_id", -1))
#
#     for i in range(len(infos)):
#         for j in range(len(tickers)):
#             if infos[i]['instrument_id'] == tickers[j]['instrument_id']:
#                 infos[i]['last'] = tickers[j]['last']
#                 infos[i]['volume_24h'] = tickers[j]['volume_24h']
#
#     return infos


def get_instruments(exchange=None):
    if exchange:
        return InstrumentInfo.find(
            {"exchange": exchange},
        ).sort("instrument_id", -1)
    else:
        return InstrumentInfo.find({}).sort("instrument_id", -1)
