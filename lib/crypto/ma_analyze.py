# -- coding: utf-8 -

from lib.signal.crypto.ma60 import is_ma60_first, is_ma60_second, is_ma60_third, is_ma60_fourth, \
    is_ma60_fifth, is_ma60_sixth, is_ma60_seventh, is_ma60_eighth


def ma_analyze(org_df):
    candle = org_df[['open', 'high', 'low', 'close', 'pct_chg', 'trade_date']].to_numpy()
    ma = org_df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    ma_slope = org_df[['ma5_slope', 'ma10_slope', 'ma20_slope', 'ma30_slope', 'ma55_slope',
                       'ma60_slope', 'ma120_slope']].to_numpy()
    bias = org_df[['bias6', 'bias12', 'bias24', 'bias55', 'bias60', 'bias72', 'bias120']].to_numpy()

    ma60_first = []
    ma60_second = []
    ma60_third = []
    ma60_fourth = []
    ma60_fifth = []
    ma60_sixth = []
    ma60_seventh = []
    ma60_eighth = []

    for index in range(len(candle)):
        # MA60 葛南维第一大法则
        if is_ma60_first(index, candle, bias, ma, ma_slope, org_df):
            ma60_first.insert(index, 1)
        else:
            ma60_first.insert(index, 0)

        # MA60 葛南维第二大法则
        if is_ma60_second(index, candle, bias, ma, ma_slope, org_df):
            ma60_second.insert(index, 1)
        else:
            ma60_second.insert(index, 0)

        # MA60 葛南维第三大法则
        if is_ma60_third(index, candle, bias, ma, ma_slope, org_df):
            ma60_third.insert(index, 1)
        else:
            ma60_third.insert(index, 0)

        # MA60 葛南维第四大法则
        if is_ma60_fourth(index, candle, bias, ma, ma_slope, org_df):
            ma60_fourth.insert(index, 1)
        else:
            ma60_fourth.insert(index, 0)

        # MA60 葛南维第5大法则
        if is_ma60_fifth(index, candle, bias, ma, ma_slope, org_df):
            ma60_fifth.insert(index, 1)
        else:
            ma60_fifth.insert(index, 0)

        # MA60 葛南维第6大法则
        if is_ma60_sixth(index, candle, bias, ma, ma_slope, org_df):
            ma60_sixth.insert(index, 1)
        else:
            ma60_sixth.insert(index, 0)

        # MA60 葛南维第7大法则
        if is_ma60_seventh(index, candle, bias, ma, ma_slope, org_df):
            ma60_seventh.insert(index, 1)
        else:
            ma60_seventh.insert(index, 0)

        # MA60 葛南维第8大法则
        if is_ma60_eighth(index, candle, bias, ma, ma_slope, org_df):
            ma60_eighth.insert(index, 1)
        else:
            ma60_eighth.insert(index, 0)

    org_df['ma60_first'] = ma60_first
    org_df['ma60_second'] = ma60_second
    org_df['ma60_third'] = ma60_third
    org_df['ma60_fourth'] = ma60_fourth
    org_df['ma60_fifth'] = ma60_fifth
    org_df['ma60_sixth'] = ma60_sixth
    org_df['ma60_seventh'] = ma60_seventh
    org_df['ma60_eighth'] = ma60_eighth

    return org_df