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

    insts = get_inst_df('biance')

    for index, item in enumerate(insts):
        _start = time.time()
        inst_id = item['instrument_id']
        # print(inst_id)
        # df = get_klines_df(inst_id, "3600", 300)
        df = get_klines_df(inst_id, "900", 300)

        if len(df) > 0:
            df = df.sort_values(by='trade_date', ascending=True)
            # df['trade_date'] = pd.to_datetime(df["trade_date"], format='%Y-%m-%d')
            df['num'] = df.index[::-1].to_numpy()
            df = df.set_index('num')
            df['gran'] = 900

            try:
                df = set_quota(df)
                df = analyze(df)

                # for i, v in range(len(df)):
                #     _last = i
                    # if _last > 260:
                    #     if df.iloc[_last]['ma60_second'] > 0 or df.iloc[_last]['ma60_third'] or \
                    #             df.iloc[_last]['ma60_seventh'] > 0 or df.iloc[_last]['ma60_eighth'] > 0:
                    #         print(df.iloc[_last]['ma60_second'], df.iloc[_last]['ma60_third'],
                    #               df.iloc[_last]['ma60_seventh'], df.iloc[_last]['ma60_eighth'])
            except Exception as e:
                print(inst_id, 'Exception', e)

            print(inst_id, '总用时 ', used_time_fmt(_start, time.time()))
        else:
            print('没有K线数据')
