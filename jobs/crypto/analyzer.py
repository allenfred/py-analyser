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


def run(inst, gran):
    inst_id = inst['instrument_id']
    exchange = inst['exchange']
    base_currency = inst['base_currency']

    _start = time.time()
    df = get_klines_df(exchange, inst_id, gran, 300)
    kline_used = used_time_fmt(_start, time.time())

    if len(df) == 0:
        print('没有K线数据')
        return

    if min(df['close']) < 0.00001:
        print('价格过低', exchange, inst_id)
        return

    try:
        # df = df.sort_values(by='trade_date', ascending=True)
        # df['trade_date'] = pd.to_datetime(df["trade_date"], format='%Y-%m-%d')
        df['num'] = df.index[::-1].to_numpy()
        df = df.set_index('num')
        df['granularity'] = gran
        df['exchange'] = exchange
        df['base_currency'] = base_currency

        _last = df.iloc[len(df) - 1]['timestamp']
        _last = datetime.strptime(_last, '%Y-%m-%d %H:%M:%S')

        # 剔除最新一根未完成K线
        if _last + timedelta(minutes=15) > datetime.utcnow():
            df.drop(index=len(df) - 1, inplace=True)

        _analyze_start = time.time()
        df = set_quota(df)
        df = analyze(df)
        signal = df.iloc[len(df) - 1].to_dict()

        keys = ['exchange', 'timestamp', 'base_currency',
                'granularity', 'max_vol', 'huge_vol', 'large_vol', 'high_vol', 'common_vol',
                'low_vol', 'increase_vol', 'decrease_vol', 'increasingly_vol', 'decreasingly_vol',
                'hammer', 't_line', 'pour_hammer', 'short_end', 'swallow_up', 'attack_short',
                'first_light', 'sunrise', 'flat_base', 'down_screw', 'long_end', 'swallow_down',
                'hang_neck', 'shooting', 'up_screw', 'down_rise',
                'up_cross3ma', 'up_cross4ma', 'up_cross5ma',
                'drop_cross3ma', 'drop_cross4ma', 'drop_cross5ma',
                'resistance_shadow', 'support_shadow', 'down_pour', 'marubozu', 'long_line',
                'ma60_first', 'ma60_second', 'ma60_third', 'ma60_fourth',
                'ma60_fifth', 'ma60_sixth', 'ma60_seventh', 'ma60_eighth',
                'ma120_first', 'ma120_second', 'ma120_third', 'ma120_fourth',
                'ma120_fifth', 'ma120_sixth', 'ma120_seventh', 'ma120_eighth',
                'ma20_up', 'ema20_up', 'ma30_up', 'ema30_up', 'ma60_up', 'ema60_up', 'ma120_up', 'ema120_up',
                'ma_gold_cross1', 'ma_gold_cross2', 'ma_gold_cross3', 'ma_gold_cross4',
                'up_trend', 'down_trend', 'strong_rise', 'strong_decline']

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

        print(_data['down_trend'])
        UsdtSwapSignal.update_one({"timestamp": _data["timestamp"], "instrument_id": inst_id,
                                   "granularity": gran, "exchange": _data["exchange"]}, {"$set": _data}, upsert=True)
        print(exchange, inst_id, gran, ', Analyze用时 ', used_time_fmt(_analyze_start, time.time()))
    except Exception as e:
        print('更新 ', inst_id, gran, 'Catch Error:', e)
