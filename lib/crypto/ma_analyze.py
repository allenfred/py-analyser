# -- coding: utf-8 -

import lib.signal.crypto.ma60 as ma60
import lib.signal.crypto.ma120 as ma120


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

    ma120_first = []
    ma120_second = []
    ma120_third = []
    ma120_fourth = []
    ma120_fifth = []
    ma120_sixth = []
    ma120_seventh = []
    ma120_eighth = []

    for index in range(len(candle)):
        # MA60 葛南维第一大法则
        ma60_first.insert(index, ma60.first(index, candle, bias, ma, org_df))
        # MA60 葛南维第二大法则
        ma60_second.insert(index, ma60.second(index, candle, bias, ma, org_df))
        # MA60 葛南维第三大法则
        ma60_third.insert(index, ma60.third(index, candle, bias, ma, org_df))
        # MA60 葛南维第四大法则
        ma60_fourth.insert(index, ma60.fourth(index, candle, bias, ma, org_df))
        # MA60 葛南维第5大法则
        ma60_fifth.insert(index, ma60.fifth(index, candle, bias, ma, org_df))
        # MA60 葛南维第6大法则
        ma60_sixth.insert(index, ma60.sixth(index, candle, bias, ma, org_df))
        # MA60 葛南维第7大法则
        ma60_seventh.insert(index, ma60.seventh(index, candle, bias, ma, org_df))
        # MA60 葛南维第8大法则
        ma60_eighth.insert(index, ma60.eighth(index, candle, bias, ma, org_df))

        # MA120 葛南维第一大法则
        ma120_first.insert(index, ma120.first(index, candle, bias, ma, org_df))
        # MA120 葛南维第二大法则
        ma120_second.insert(index, ma120.second(index, candle, bias, ma, org_df))
        # MA120 葛南维第三大法则
        ma120_third.insert(index, ma120.third(index, candle, bias, ma, org_df))
        # MA120 葛南维第四大法则
        ma120_fourth.insert(index, ma120.fourth(index, candle, bias, ma, org_df))
        # MA120 葛南维第5大法则
        ma120_fifth.insert(index, ma120.fifth(index, candle, bias, ma, org_df))
        # MA120 葛南维第6大法则
        ma120_sixth.insert(index, ma120.sixth(index, candle, bias, ma, org_df))
        # MA120 葛南维第7大法则
        ma120_seventh.insert(index, ma120.seventh(index, candle, bias, ma, org_df))
        # MA120 葛南维第8大法则
        ma120_eighth.insert(index, ma120.eighth(index, candle, bias, ma, org_df))

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
