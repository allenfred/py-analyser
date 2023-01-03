# -- coding: utf-8 -
from config.common import START_INDEX
from lib.signal.stock.ma60 import is_ma60_first, is_ma60_second, is_ma60_third, is_ma60_fourth, \
    is_ma60_fifth, is_ma60_sixth, is_ma60_seventh, is_ma60_eighth
from lib.signal.common.ma import is_up_hill, is_up_wave
import lib.signal.stock.candle as patterns
from lib.signal.common.hlines import calc_hlines


def ma_analyze(org_df):
    candle = org_df[['open', 'high', 'low', 'close', 'pct_chg', 'trade_date']].to_numpy()
    ma = org_df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    ma_slope = org_df[['ma5_slope', 'ma10_slope', 'ma20_slope', 'ma30_slope', 'ma55_slope',
                       'ma60_slope', 'ma120_slope']].to_numpy()
    bias = org_df[['bias6', 'bias12', 'bias24', 'bias55', 'bias60', 'bias72', 'bias120']].to_numpy()

    ma60_first = [0 for _ in range(len(org_df))]
    ma60_second = [0 for _ in range(len(org_df))]
    ma60_third = [0 for _ in range(len(org_df))]
    ma60_fourth = [0 for _ in range(len(org_df))]
    ma60_fifth = [0 for _ in range(len(org_df))]
    ma60_sixth = [0 for _ in range(len(org_df))]
    ma60_seventh = [0 for _ in range(len(org_df))]
    ma60_eighth = [0 for _ in range(len(org_df))]

    up_hill = [0 for _ in range(len(org_df))]
    up_wave = [0 for _ in range(len(org_df))]
    limit_up_gene = [0 for _ in range(len(org_df))]
    hlines = [[] for _ in range(len(org_df))]

    _start_at = START_INDEX

    for index in range(len(candle)):
        if index > _start_at:
            # MA60 葛南维第一大法则
            if is_ma60_first(index, candle, bias, ma, ma_slope, org_df):
                ma60_first[index] = 1

            # MA60 葛南维第二大法则
            if is_ma60_second(index, candle, bias, ma, ma_slope, org_df):
                ma60_second[index] = 1

            # MA60 葛南维第三大法则
            if is_ma60_third(index, candle, bias, ma, ma_slope, org_df):
                ma60_third[index] = 1

            # MA60 葛南维第四大法则
            if is_ma60_fourth(index, candle, bias, ma, ma_slope, org_df):
                ma60_fourth[index] = 1

            # MA60 葛南维第5大法则
            if is_ma60_fifth(index, candle, bias, ma, ma_slope, org_df):
                ma60_fifth[index] = 1

            # MA60 葛南维第6大法则
            if is_ma60_sixth(index, candle, bias, ma, ma_slope, org_df):
                ma60_sixth[index] = 1

            # MA60 葛南维第7大法则
            if is_ma60_seventh(index, candle, bias, ma, ma_slope, org_df):
                ma60_seventh[index] = 1

            # MA60 葛南维第8大法则
            if is_ma60_eighth(index, candle, bias, ma, ma_slope, org_df):
                ma60_eighth[index] = 1

            # 上山爬坡
            if is_up_hill(index, org_df):
                up_hill[index] = 1

            # 逐浪上升
            if is_up_wave(index, org_df):
                up_wave[index] = 1

            # 涨停基因
            if patterns.limit_up_gene(index, candle, org_df):
                limit_up_gene[index] = 1

            hlines[index] = calc_hlines(org_df, index)

    org_df['ma60_first'] = ma60_first
    org_df['ma60_second'] = ma60_second
    org_df['ma60_third'] = ma60_third
    org_df['ma60_fourth'] = ma60_fourth
    org_df['ma60_fifth'] = ma60_fifth
    org_df['ma60_sixth'] = ma60_sixth
    org_df['ma60_seventh'] = ma60_seventh
    org_df['ma60_eighth'] = ma60_eighth

    org_df['up_hill'] = up_hill
    org_df['up_wave'] = up_wave
    org_df['limit_up_gene'] = limit_up_gene

    return org_df
