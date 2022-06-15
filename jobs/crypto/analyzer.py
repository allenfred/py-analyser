# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

from lib.crypto.analyze import analyze
import time
from datetime import date, datetime, timedelta
from lib.util import set_quota, used_time_fmt
from df import get_klines_df
from database import UsdtSwapSignal


def run(inst, gran):
    inst_id = inst['instrument_id']
    exchange = inst['exchange']
    # underlying_index = inst['underlying_index']
    underlying_index = ''

    if exchange == 'biance':
        underlying_index = inst_id.replace('USDT', '')
    elif exchange == 'okex':
        underlying_index = inst_id.replace('-USDT-SWAP', '')

    _start = time.time()
    df = get_klines_df(inst_id, gran, 300)
    kline_used = used_time_fmt(_start, time.time())

    if len(df) == 0:
        print('没有K线数据')
        return

    try:
        # df = df.sort_values(by='trade_date', ascending=True)
        # df['trade_date'] = pd.to_datetime(df["trade_date"], format='%Y-%m-%d')
        df['num'] = df.index[::-1].to_numpy()
        df = df.set_index('num')
        df['gran'] = gran
        df['granularity'] = gran
        df['exchange'] = exchange
        df['underlying_index'] = underlying_index

        _last = df.iloc[len(df) - 1]['timestamp']
        _last = _last.replace(tzinfo=None)

        # 剔除最新一根未完成K线
        if _last + timedelta(minutes=15) > datetime.utcnow():
            df = df.drop(index=[len(df) - 1])

        _analyze_start = time.time()
        df = set_quota(df)
        df = analyze(df)
        signal = df.iloc[len(df) - 1].to_dict()

        keys = ['exchange', 'timestamp', 'underlying_index',
                'granularity', 'max_vol', 'huge_vol', 'large_vol', 'high_vol', 'common_vol', 'low_vol', 'increase_vol',
                'decrease_vol', 'increasingly_vol', 'decreasingly_vol', 'hammer', 't_line', 'pour_hammer', 'short_end',
                'swallow_up', 'attack_short', 'first_light', 'sunrise', 'flat_base', 'down_screw', 'long_end',
                'swallow_down',
                'hang_neck', 'shooting', 'up_screw', 'down_rise', 'up_cross3ma', 'up_cross4ma', 'drop_cross3ma',
                'drop_cross4ma',
                'resistance_shadow', 'support_shadow', 'down_pour', 'marubozu', 'long_line', 'CDLDRAGONFLYDOJI',
                'CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLMARUBOZU', 'CDLSHOOTINGSTAR', 'CDLDARKCLOUDCOVER', 'CDLHARAMI',
                'CDLHARAMICROSS', 'CDLENGULFING', 'CDLPIERCING', 'CDLMORNINGSTAR', 'CDLMORNINGDOJISTAR',
                'CDLEVENINGSTAR',
                'CDLEVENINGDOJISTAR', 'CDLLADDERBOTTOM', 'ma60_first', 'ma60_second', 'ma60_third', 'ma60_fourth',
                'ma60_fifth',
                'ma60_sixth', 'ma60_seventh', 'ma60_eighth', 'ma120_first', 'ma120_second', 'ma120_third',
                'ma120_fourth',
                'ma120_fifth', 'ma120_sixth', 'ma120_seventh', 'ma120_eighth']

        _data = {}
        for i, v in enumerate(keys):
            if v == 'exchange' or v == 'trade_date' or v == 'timestamp' or v == 'underlying_index':
                _data[v] = signal.get(v)
            else:
                _data[v] = int(signal.get(v))

        UsdtSwapSignal.update_one({"time": _data["timestamp"], "inst_id": inst_id,
                                   "granularity": gran, "exchange": _data["exchange"]}, {"$set": _data}, upsert=True)
        print(inst_id, gran, 'K线用时', kline_used, ',Analyze用时 ', used_time_fmt(_analyze_start, time.time()))
    except Exception as e:
        print('更新 ', inst_id, gran, 'Catch Error:', e)

