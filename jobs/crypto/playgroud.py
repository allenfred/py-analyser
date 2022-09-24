# -- coding: utf-8 -

import os
import sys
import numpy as np

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

from lib.crypto.analyze import analyze
import time
from datetime import date, datetime, timedelta, timezone
from lib.util import set_quota, used_time_fmt
from df import get_klines_df
from database import UsdtSwapSignal

#
# ['trade_date', 'open', 'high', 'low', 'close', 'vol', 'pct_chg', 'exchange', 'timestamp',
#  'underlying_index', 'gran', 'granularity', 'vol5', 'vol10', 'vol20', 'vol30', 'ma5', 'ma10',
#  'ma20', 'ma30', 'ma34', 'ma55', 'ma60', 'ma120', 'ma144', 'ma169', 'ema5', 'ema10', 'ema20',
#  'ema30', 'ema34', 'ema55', 'ema60', 'ema120', 'ema144', 'ema169', 'ema288', 'ema338', 'ema576',
#  'ema676', 'ma5_slope', 'ma10_slope', 'ma20_slope', 'ma30_slope', 'ma34_slope', 'ma55_slope',
#  'ma60_slope', 'ma72_slope', 'ma120_slope', 'ma144_slope', 'ma169_slope', 'ema5_slope', 'ema10_slope',
#  'ema20_slope', 'ema30_slope', 'ema34_slope', 'ema55_slope', 'ema60_slope', 'ema120_slope', 'ema144_slope',
#  'ema169_slope', 'ema288_slope', 'ema338_slope', 'ema576_slope', 'ema676_slope', 'diff', 'dea', 'macd',
#  'bias6', 'bias12', 'bias24', 'bias55', 'bias60', 'bias72', 'bias120', 'high_td', 'low_td',
#  'atr', 'pct_range', 'max_vol', 'huge_vol', 'large_vol', 'high_vol', 'common_vol', 'low_vol',
#  'increase_vol', 'decrease_vol', 'increasingly_vol', 'decreasingly_vol', 'hammer', 't_line',
#  'pour_hammer', 'short_end', 'swallow_up', 'attack_short', 'first_light', 'sunrise', 'flat_base',
#  'down_screw', 'long_end', 'swallow_down', 'hang_neck', 'shooting', 'up_screw', 'down_rise', 'up_cross3ma',
#  'up_cross4ma', 'drop_cross3ma', 'drop_cross4ma', 'resistance_shadow', 'support_shadow', 'down_pour',
#  'marubozu', 'long_line', 'CDLDRAGONFLYDOJI', 'CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLMARUBOZU',
#  'CDLSHOOTINGSTAR', 'CDLDARKCLOUDCOVER', 'CDLHARAMI', 'CDLHARAMICROSS', 'CDLENGULFING', 'CDLPIERCING',
#  'CDLMORNINGSTAR', 'CDLMORNINGDOJISTAR', 'CDLEVENINGSTAR', 'CDLEVENINGDOJISTAR', 'CDLLADDERBOTTOM',
#  'ma60_first', 'ma60_second', 'ma60_third', 'ma60_fourth', 'ma60_fifth', 'ma60_sixth', 'ma60_seventh',
#  'ma60_eighth', 'ma120_first', 'ma120_second', 'ma120_third', 'ma120_fourth', 'ma120_fifth', 'ma120_sixth',
#  'ma120_seventh', 'ma120_eighth']


if __name__ == "__main__":
    start = time.time()

    # inst_id = 'KNCUSDT'
    # inst_id = 'RSRUSDT'
    # inst_id = 'DENTUSDT'
    inst_id = 'BELUSDT'
    inst_id = 'BLZUSDT'
    # inst_id = 'GRTUSDT'
    inst_id = 'ADAUSDT'
    inst_id = 'BTCUSDT'
    inst_id = 'ETHUSDT'
    inst_id = 'SOLUSDT'

    gran = 900
    exchange = 'binance'
    # exchange = 'okex'
    df = get_klines_df(exchange, inst_id, gran, 300)
    # df = get_swap_df(inst_id, "900", 1200)
    # df = get_klines_df(inst_id, "900", 300)
    exchange = ''
    base_currency = ''

    if inst_id.endswith('USDT'):
        exchange = 'biance'
        base_currency = inst_id.replace('USDT', '')
    else:
        exchange = 'okex'
        base_currency = inst_id.replace('-USDT-SWAP', '')

    if len(df) == 0:
        print('没有K线数据')

    print('获取K线用时 ', used_time_fmt(start, time.time()))

    # df = df.sort_values(by='timestamp', ascending=True)
    # df['trade_date'] = pd.to_datetime(df["trade_date"], format='%Y-%m-%d')
    df['num'] = df.index[::-1].to_numpy()
    df = df.set_index('num')
    df['granularity'] = int(gran)
    df['exchange'] = exchange
    df['base_currency'] = base_currency

    _last = df.iloc[len(df) - 1]['timestamp']
    _last = datetime.strptime(_last, '%Y-%m-%d %H:%M:%S')

    # 剔除最新一根未完成K线
    if _last + timedelta(minutes=15) > datetime.utcnow():
        df.drop(index=len(df) - 1, inplace=True)

    df = set_quota(df)
    df = analyze(df)
    signal = df.iloc[len(df) - 1].to_dict()
    print(signal)
    _data = {}
    for i, v in enumerate(signal.keys()):

        if isinstance(signal.get(v), np.int64) or isinstance(signal.get(v), np.int32):
            _data[v] = int(signal.get(v))
        elif isinstance(signal.get(v), np.float64):
            _data[v] = float(signal.get(v))
        elif v == 'timestamp':
            _data[v] = datetime.strptime(signal.get("timestamp"), '%Y-%m-%d %H:%M:%S'). \
                replace(tzinfo=timezone.utc). \
                astimezone(timezone.utc)
        else:
            _data[v] = signal.get(v)

    UsdtSwapSignal.update_one({"timestamp": _data["timestamp"], "instrument_id": inst_id,
                               "granularity": gran, "exchange": _data["exchange"]}, {"$set": _data}, upsert=True)

    print('总用时 ', used_time_fmt(start, time.time()))
