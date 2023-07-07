# -- coding: utf-8 -
from config.common import START_INDEX

import lib.signal.common.ma as ma
from lib.signal.common.macd import is_macd_gold_cross, is_macd_zero_gold_cross


def ma_analyze(org_df):
    candle = org_df[['open', 'high', 'low', 'close', 'pct_chg', 'trade_date']].to_numpy()

    steady_below_ma60 = [0 for _ in range(len(org_df))]
    steady_on_ma60 = [0 for _ in range(len(org_df))]
    steady_below_ma120 = [0 for _ in range(len(org_df))]
    steady_on_ma120 = [0 for _ in range(len(org_df))]

    macd_zero_gold_cross = [0 for _ in range(len(org_df))]
    macd_gold_cross = [0 for _ in range(len(org_df))]

    _start_at = START_INDEX

    for index in range(len(candle)):
        if index > _start_at:
            if ma.steady_below_ma60(index, org_df):
                steady_below_ma60[index] = 1

            if ma.steady_on_ma60(index, org_df):
                steady_on_ma60[index] = 1

            if ma.steady_below_ma120(index, org_df):
                steady_below_ma120[index] = 1

            if ma.steady_on_ma120(index, org_df):
                steady_on_ma120[index] = 1

            if is_macd_gold_cross(index, org_df):
                macd_gold_cross[index] = 1

            if is_macd_zero_gold_cross(index, org_df):
                macd_zero_gold_cross[index] = 1

    org_df['steady_below_ma60'] = steady_below_ma60
    org_df['steady_on_ma60'] = steady_on_ma60
    org_df['steady_below_ma120'] = steady_below_ma120
    org_df['steady_on_ma120'] = steady_on_ma120

    org_df['macd_gold_cross'] = macd_gold_cross
    org_df['macd_zero_gold_cross'] = macd_zero_gold_cross

    return org_df
