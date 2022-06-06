# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

from lib.crypto.analyze import analyze
import time
from lib.util import set_quota, used_time_fmt
from df import get_inst_df, get_klines_df


if __name__ == "__main__":
    start = time.time()

    # inst_id = 'KNCUSDT'
    # inst_id = 'RSRUSDT'
    # inst_id = 'DENTUSDT'
    inst_id = 'BELUSDT'
    # inst_id = 'BLZUSDT'
    # inst_id = 'GRTUSDT'
    inst_id = 'AVAX-USDT-SWAP'
    # df = get_swap_df(inst_id, "3600", 500)
    # df = get_swap_df(inst_id, "900", 1200)
    df = get_klines_df(inst_id, "900", 300)
    if len(df) == 0:
        print('没有K线数据')
    # print(df)
    print('获取K线用时 ', used_time_fmt(start, time.time()))

    df = df.sort_values(by='trade_date', ascending=True)
    # df['trade_date'] = pd.to_datetime(df["trade_date"], format='%Y-%m-%d')
    df['num'] = df.index[::-1].to_numpy()
    df = df.set_index('num')

    df = set_quota(df)
    df = analyze(df)

    print('总用时 ', used_time_fmt(start, time.time()))
