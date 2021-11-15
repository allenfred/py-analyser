# -- coding: utf-8 -
import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

import tushare as ts
from config.common import TS_TOKEN

ts.set_token(TS_TOKEN)

if __name__ == "__main__":
    # 棕榈油2210 P2210.DCE
    df = ts.pro_bar(ts_code='600000.SH',
                    freq='1min',
                    limit=100,
                    start_date='2021-11-01 09:00:00',
                    end_date='2021-11-01 15:00:00'
                    )

    print(df)

    # 棕榈油2210 P2210.DCE
    df = ts.pro_bar(ts_code='P2210.DCE',
                    freq='1min',
                    limit=100,
                    asset='FT',
                    start_date='2021-11-01 09:00:00',
                    end_date='2021-11-01 15:00:00'
                    )

    print(df)
