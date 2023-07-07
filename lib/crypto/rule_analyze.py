# -- coding: utf-8 -
from config.common import START_INDEX

import lib.signal.crypto.ma60 as ma60
import lib.signal.crypto.ma120 as ma120


def rule_analyze(org_df):
    candle = org_df[['open', 'high', 'low', 'close', 'pct_chg', 'trade_date']].to_numpy()
    ma = org_df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    bias = org_df[['bias6', 'bias12', 'bias24', 'bias55', 'bias60', 'bias72', 'bias120']].to_numpy()

    ma60_first = [0 for _ in range(len(org_df))]
    ma60_second = [0 for _ in range(len(org_df))]
    ma60_third = [0 for _ in range(len(org_df))]
    ma60_fourth = [0 for _ in range(len(org_df))]
    ma60_fifth = [0 for _ in range(len(org_df))]
    ma60_sixth = [0 for _ in range(len(org_df))]
    ma60_seventh = [0 for _ in range(len(org_df))]
    ma60_eighth = [0 for _ in range(len(org_df))]

    ma120_first = [0 for _ in range(len(org_df))]
    ma120_second = [0 for _ in range(len(org_df))]
    ma120_third = [0 for _ in range(len(org_df))]
    ma120_fourth = [0 for _ in range(len(org_df))]
    ma120_fifth = [0 for _ in range(len(org_df))]
    ma120_sixth = [0 for _ in range(len(org_df))]
    ma120_seventh = [0 for _ in range(len(org_df))]
    ma120_eighth = [0 for _ in range(len(org_df))]

    _start_at = START_INDEX

    for index in range(len(candle)):
        if index > _start_at:
            ma60_first[index] = ma60.first(index, candle, bias, ma, org_df)
            ma60_second[index] = ma60.second(index, candle, bias, ma, org_df)
            ma60_third[index] = ma60.third(index, candle, bias, ma, org_df)
            ma60_fourth[index] = ma60.fourth(index, candle, bias, ma, org_df)
            ma60_fifth[index] = ma60.fifth(index, candle, bias, ma, org_df)
            ma60_sixth[index] = ma60.sixth(index, candle, bias, ma, org_df)
            ma60_seventh[index] = ma60.seventh(index, candle, bias, ma, org_df)
            ma60_eighth[index] = ma60.eighth(index, candle, bias, ma, org_df)

            ma120_first[index] = ma120.first(index, candle, bias, ma, org_df)
            ma120_second[index] = ma120.second(index, candle, bias, ma, org_df)
            ma120_third[index] = ma120.third(index, candle, bias, ma, org_df)
            ma120_fourth[index] = ma120.fourth(index, candle, bias, ma, org_df)
            ma120_fifth[index] = ma120.fifth(index, candle, bias, ma, org_df)
            ma120_sixth[index] = ma120.sixth(index, candle, bias, ma, org_df)
            ma120_seventh[index] = ma120.seventh(index, candle, bias, ma, org_df)
            ma120_eighth[index] = ma120.eighth(index, candle, bias, ma, org_df)

    org_df['ma60_first'] = ma60_first
    org_df['ma60_second'] = ma60_second
    org_df['ma60_third'] = ma60_third
    org_df['ma60_fourth'] = ma60_fourth
    org_df['ma60_fifth'] = ma60_fifth
    org_df['ma60_sixth'] = ma60_sixth
    org_df['ma60_seventh'] = ma60_seventh
    org_df['ma60_eighth'] = ma60_eighth

    org_df['ma120_first'] = ma120_first
    org_df['ma120_second'] = ma120_second
    org_df['ma120_third'] = ma120_third
    org_df['ma120_fourth'] = ma120_fourth
    org_df['ma120_fifth'] = ma120_fifth
    org_df['ma120_sixth'] = ma120_sixth
    org_df['ma120_seventh'] = ma120_seventh
    org_df['ma120_eighth'] = ma120_eighth

    return org_df
