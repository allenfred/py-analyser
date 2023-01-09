# -- coding: utf-8 -
from config.common import START_INDEX
import lib.signal.common.hline_fractal as Hlines


def hline_analyze(org_df):
    candle = org_df[['open', 'high', 'low', 'close', 'pct_chg', 'trade_date']].to_numpy()

    hlines = [[] for _ in range(len(org_df))]

    _start_at = START_INDEX

    for index in range(len(candle)):
        if index >= _start_at:
            # 计算水平位
            hlines[index] = Hlines.calc_hlines(org_df, index)

    org_df['hlines'] = hlines

    return org_df
