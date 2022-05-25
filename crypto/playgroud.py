# -- coding: utf-8 -

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

from lib.crypto.analyze import analyze
from lib.util import set_quota
from api import get_swap_df


if __name__ == "__main__":
    inst_id = 'KNCUSDT'
    df = get_swap_df(inst_id, "3600", 1000)

    if len(df) == 0:
        print('没有K线数据')
    # print(df)

    #
    df = df.sort_values(by='trade_date', ascending=True)
    # df['trade_date'] = pd.to_datetime(df["trade_date"], format='%Y-%m-%d')
    df['num'] = df.index[::-1].to_numpy()
    df = df.set_index('num')

    df = set_quota(df)

    # 更新weekly signal
    df = analyze(df)
    #
    # print('总用时 ', used_time_fmt(start, time.time()))
    #
    # stockDao.update({'ts_code': ts_code, 'weekly_date': today})
    #
    # print(today, '用时', used_time_fmt(start, time.time()))
