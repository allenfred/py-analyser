# -- coding: utf-8 -
from config.common import START_INDEX
import lib.signal.common.limit as limit
import lib.signal.common.hline_strategy as Hlines


def trend_analyze(org_df):
    candle = org_df[['open', 'high', 'low', 'close', 'pct_chg', 'trade_date']].to_numpy()

    limit_pullback = [0 for _ in range(len(org_df))]
    up_pullback = [0 for _ in range(len(org_df))]
    up_break = [0 for _ in range(len(org_df))]
    hline_support = [0 for _ in range(len(org_df))]

    _start_at = len(org_df) - 20

    for index in range(len(candle)):
        if index > _start_at:
            # 涨停回调
            if limit.limit_pullback(org_df, index):
                limit_pullback[index] = 1

            # 上涨回调
            if Hlines.up_pullback(org_df, index):
                up_pullback[index] = 1

            # 向上突破
            if Hlines.up_break(org_df, index):
                up_break[index] = 1

            # 向上突破
            if Hlines.hline_support(org_df, index):
                hline_support[index] = 1

    org_df['limit_pullback'] = limit_pullback
    org_df['up_pullback'] = up_pullback
    org_df['up_break'] = up_break
    org_df['hline_support'] = hline_support

    return org_df
