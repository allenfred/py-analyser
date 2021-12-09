from talib import SMA
import pandas as pd
import numpy as np
import math
from .candle import is_hammer, is_pour_hammer, is_short_end, is_swallow_up, \
    is_sunrise, is_first_light, is_attack_short, is_flat_base
from .long_signals import stand_on_ma, stand_on_ema, ma_hold, is_stand_up_ma60, \
    is_stand_up_ma120, is_stand_up_ema60, is_stand_up_ema120, is_ma60_steady_up, \
    is_ma120_steady_up, is_ema60_steady_up, is_ema120_steady_up, is_ma60_support, \
    is_ma120_support, is_ema60_support, is_ema120_support, is_ma_group_glue, \
    is_ema_group_glue, is_ma_up_arrange51020, is_ma_up_arrange5102030, is_ma_up_arrange510203060, \
    is_ma_up_arrange203060, is_ma_up_arrange2060120, is_ema_up_arrange51020, \
    is_ema_up_arrange5102030, is_ema_up_arrange510203060, is_ema_up_arrange203060, \
    is_ema_up_arrange2055120, is_ma_spider, is_ema_spider,is_ma_hold_moon, \
    is_ema_hold_moon, is_ma_over_gate, is_ema_over_gate, is_ma_up_ground, is_ema_up_ground, \
    is_ma_glue, is_ema_glue, is_ma_silver_valley, is_ema_silver_valley, \
    is_ma_gold_valley, is_ema_gold_valley
import time

"""
df: indicators with signals (long signals or short signals)
"""


def analytic_signals(org_df):
    candle = org_df[['open', 'high', 'low', 'close', 'pct_chg']].to_numpy()
    ma = org_df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    ema = org_df[['ema5', 'ema10', 'ema20', 'ema30', 'ema55', 'ema60', 'ema120']].to_numpy()
    ma_slope = org_df[['ma5_slope', 'ma10_slope', 'ma20_slope', 'ma30_slope', 'ma55_slope',
                       'ma60_slope', 'ma120_slope']].to_numpy()
    ema_slope = org_df[['ema5_slope', 'ema10_slope', 'ema20_slope', 'ema30_slope', 'ema55_slope',
                        'ema60_slope', 'ema120_slope']].to_numpy()
    bias = org_df[['bias6', 'bias12', 'bias24', 'bias60', 'bias72', 'bias120']].to_numpy()
    td = org_df[['high_td', 'low_td']].to_numpy()

    yearly_price_position, yearly_price_position10, yearly_price_position20, \
    yearly_price_position30, yearly_price_position50, yearly_price_position70, \
    ma20_up, ema20_up, ma30_up, ema30_up, ma60_up, ema60_up, ma120_up, ema120_up, ma_arrange, ema_arrange, \
    short_ma_arrange1, short_ma_arrange2, short_ema_arrange1, short_ema_arrange2, \
    middle_ma_arrange1, middle_ma_arrange2, middle_ema_arrange1, middle_ema_arrange2, \
    long_ma_arrange1, long_ma_arrange2, long_ema_arrange1, long_ema_arrange2, \
    ma_gold_cross1, ma_gold_cross2, ma_gold_cross3, ma_gold_cross4, \
    ema_gold_cross1, ema_gold_cross2, ema_gold_cross3, ema_gold_cross4, \
    ma_silver_valley, ema_silver_valley, ma_gold_valley, ema_gold_valley, \
    ma_spider, ma_spider2, ema_spider, ema_spider2, \
    ma_glue, ema_glue, ma_out_sea, ema_out_sea, ma_hold_moon, ema_hold_moon, \
    ma_over_gate, ema_over_gate, ma_up_ground, ema_up_ground, \
    td8, td9, bias6, bias12, bias24, bias60, bias72, bias120, \
    stand_up_ma60, stand_up_ma120, stand_up_ema60, stand_up_ema120, \
    ma60_support, ema60_support, ma120_support, ema120_support, \
    ma_group_glue, ema_group_glue, ma_up_arrange51020, ma_up_arrange5102030, \
    ma_up_arrange510203060, ma_up_arrange203060, ma_up_arrange2060120, \
    ema_up_arrange51020, ema_up_arrange5102030, ema_up_arrange510203060, \
    ema_up_arrange203060, ema_up_arrange2055120, \
    hammer, pour_hammer, short_end, swallow_up, attack_short, \
    first_light, sunrise, flat_base = analytic(candle, ma, ema, ma_slope, ema_slope, bias, td)

    org_df['yearly_price_position'] = yearly_price_position
    org_df['yearly_price_position10'] = yearly_price_position10
    org_df['yearly_price_position20'] = yearly_price_position20
    org_df['yearly_price_position30'] = yearly_price_position30
    org_df['yearly_price_position50'] = yearly_price_position50
    org_df['yearly_price_position70'] = yearly_price_position70

    org_df['ma20_up'] = ma20_up
    org_df['ema20_up'] = ema20_up
    org_df['ma30_up'] = ma30_up
    org_df['ema30_up'] = ema30_up
    org_df['ma60_up'] = ma60_up
    org_df['ema60_up'] = ema60_up
    org_df['ma120_up'] = ma120_up
    org_df['ema120_up'] = ema120_up
    org_df['ma_arrange'] = ma_arrange
    org_df['ema_arrange'] = ema_arrange

    org_df['short_ma_arrange1'] = short_ma_arrange1
    org_df['short_ma_arrange2'] = short_ma_arrange2
    org_df['short_ema_arrange1'] = short_ema_arrange1
    org_df['short_ema_arrange2'] = short_ema_arrange2

    org_df['middle_ma_arrange1'] = middle_ma_arrange1
    org_df['middle_ma_arrange2'] = middle_ma_arrange2
    org_df['middle_ema_arrange1'] = middle_ema_arrange1
    org_df['middle_ema_arrange2'] = middle_ema_arrange2

    org_df['long_ma_arrange1'] = long_ma_arrange1
    org_df['long_ma_arrange2'] = long_ma_arrange2
    org_df['long_ema_arrange1'] = long_ema_arrange1
    org_df['long_ema_arrange2'] = long_ema_arrange2

    org_df['ma_gold_cross1'] = ma_gold_cross1
    org_df['ma_gold_cross2'] = ma_gold_cross2
    org_df['ma_gold_cross3'] = ma_gold_cross3
    org_df['ma_gold_cross4'] = ma_gold_cross4
    org_df['ema_gold_cross1'] = ema_gold_cross1
    org_df['ema_gold_cross2'] = ema_gold_cross2
    org_df['ema_gold_cross3'] = ema_gold_cross3
    org_df['ema_gold_cross4'] = ema_gold_cross4

    org_df['ma_silver_valley'] = ma_silver_valley
    org_df['ema_silver_valley'] = ema_silver_valley
    org_df['ma_gold_valley'] = ma_gold_valley
    org_df['ema_gold_valley'] = ema_gold_valley
    org_df['ma_spider'] = ma_spider
    org_df['ma_spider2'] = ma_spider2
    org_df['ema_spider'] = ema_spider
    org_df['ema_spider2'] = ema_spider2

    org_df['ma_glue'] = ma_glue
    org_df['ema_glue'] = ema_glue
    org_df['ma_out_sea'] = ma_out_sea
    org_df['ema_out_sea'] = ema_out_sea
    org_df['ma_hold_moon'] = ma_hold_moon
    org_df['ema_hold_moon'] = ema_hold_moon
    org_df['ma_over_gate'] = ma_over_gate
    org_df['ema_over_gate'] = ema_over_gate
    org_df['ma_up_ground'] = ma_up_ground
    org_df['ema_up_ground'] = ema_up_ground

    org_df['td8'] = td8
    org_df['td9'] = td9

    org_df['bias6'] = bias6
    org_df['bias12'] = bias12
    org_df['bias24'] = bias24
    org_df['bias60'] = bias60
    org_df['bias72'] = bias72
    org_df['bias120'] = bias120

    org_df['stand_up_ma60'] = stand_up_ma60
    org_df['stand_up_ma120'] = stand_up_ma120
    org_df['stand_up_ema60'] = stand_up_ema60
    org_df['stand_up_ema120'] = stand_up_ema120

    org_df['ma60_support'] = ma60_support
    org_df['ema60_support'] = ema60_support
    org_df['ma120_support'] = ma120_support
    org_df['ema120_support'] = ema120_support

    org_df['ma_group_glue'] = ma_group_glue
    org_df['ema_group_glue'] = ema_group_glue

    org_df['ma_up_arrange51020'] = ma_up_arrange51020
    org_df['ma_up_arrange5102030'] = ma_up_arrange5102030
    org_df['ma_up_arrange510203060'] = ma_up_arrange510203060
    org_df['ma_up_arrange203060'] = ma_up_arrange203060
    org_df['ma_up_arrange2060120'] = ma_up_arrange2060120

    org_df['ema_up_arrange51020'] = ema_up_arrange51020
    org_df['ema_up_arrange5102030'] = ema_up_arrange5102030
    org_df['ema_up_arrange510203060'] = ema_up_arrange510203060
    org_df['ema_up_arrange203060'] = ema_up_arrange203060
    org_df['ema_up_arrange2055120'] = ema_up_arrange2055120

    org_df['hammer'] = hammer
    org_df['pour_hammer'] = pour_hammer
    org_df['short_end'] = short_end
    org_df['swallow_up'] = swallow_up
    org_df['attack_short'] = attack_short
    org_df['first_light'] = first_light
    org_df['sunrise'] = sunrise
    org_df['flat_base'] = flat_base

    return org_df


def analytic(candle, ma, ema, ma_slope, ema_slope, bias, td):
    open = candle[:, 0]
    high = candle[:, 1]
    low = candle[:, 2]
    close = candle[:, 3]
    pct_chg = candle[:, 4]

    ma5 = ma[:, 0]
    ma10 = ma[:, 1]
    ma20 = ma[:, 2]
    ma30 = ma[:, 3]
    ma55 = ma[:, 4]
    ma60 = ma[:, 5]
    ma120 = ma[:, 6]

    ma5_slope = ma_slope[:, 0]
    ma10_slope = ma_slope[:, 1]
    ma20_slope = ma_slope[:, 2]
    ma30_slope = ma_slope[:, 3]
    ma55_slope = ma_slope[:, 4]
    ma60_slope = ma_slope[:, 5]
    ma120_slope = ma_slope[:, 6]

    ema5 = ema[:, 0]
    ema10 = ema[:, 1]
    ema20 = ema[:, 2]
    ema30 = ema[:, 3]
    ema55 = ema[:, 4]
    ema60 = ema[:, 5]
    ema120 = ema[:, 6]

    ema5_slope = ema_slope[:, 0]
    ema10_slope = ema_slope[:, 1]
    ema20_slope = ema_slope[:, 2]
    ema30_slope = ema_slope[:, 3]
    ema55_slope = ema_slope[:, 4]
    ema60_slope = ema_slope[:, 5]
    ema120_slope = ema_slope[:, 6]

    yearly_price_position = []
    yearly_price_position10 = []
    yearly_price_position20 = []
    yearly_price_position30 = []
    yearly_price_position50 = []
    yearly_price_position70 = []

    ma20_up = []
    ema20_up = []
    ma30_up = []
    ema30_up = []
    ma60_up = []
    ema60_up = []
    ma120_up = []
    ema120_up = []

    ma_arrange = []
    ema_arrange = []

    short_ma_arrange1 = []
    short_ma_arrange2 = []
    short_ema_arrange1 = []
    short_ema_arrange2 = []

    middle_ma_arrange1 = []
    middle_ma_arrange2 = []
    middle_ema_arrange1 = []
    middle_ema_arrange2 = []

    long_ma_arrange1 = []
    long_ma_arrange2 = []
    long_ema_arrange1 = []
    long_ema_arrange2 = []

    ma_gold_cross1 = []
    ma_gold_cross2 = []
    ma_gold_cross3 = []
    ma_gold_cross4 = []
    ema_gold_cross1 = []
    ema_gold_cross2 = []
    ema_gold_cross3 = []
    ema_gold_cross4 = []

    ma_silver_valley = []
    ema_silver_valley = []
    ma_gold_valley = []
    ema_gold_valley = []
    ma_spider = []
    ma_spider2 = []
    ema_spider = []
    ema_spider2 = []

    ma_out_sea = []
    ema_out_sea = []

    ma_hold_moon = []
    ema_hold_moon = []

    ma_over_gate = []
    ema_over_gate = []

    ma_up_ground = []
    ema_up_ground = []

    ma_glue = []
    ema_glue = []

    td8 = []
    td9 = []

    bias6 = []
    bias12 = []
    bias24 = []
    bias60 = []
    bias72 = []
    bias120 = []

    ma60_support = []
    ema60_support = []
    ma120_support = []
    ema120_support = []

    stand_up_ma60 = []
    stand_up_ema60 = []
    stand_up_ma120 = []
    stand_up_ema120 = []

    ma_group_glue = []
    ema_group_glue = []

    ma_up_arrange51020 = []
    ma_up_arrange5102030 = []
    ma_up_arrange510203060 = []
    ma_up_arrange203060 = []
    ma_up_arrange2060120 = []
    ema_up_arrange51020 = []
    ema_up_arrange5102030 = []
    ema_up_arrange510203060 = []
    ema_up_arrange203060 = []
    ema_up_arrange2055120 = []

    hammer = []
    pour_hammer = []
    short_end = []
    swallow_up = []
    attack_short = []
    first_light = []
    sunrise = []
    flat_base = []

    # 连续两日K线在ma60上方止跌
    # 连续两日K线在ma120上方止跌
    # 最近20个交易日 沿着ma30上行 未曾跌破ma30
    for index in range(len(candle)):
        _open = open[index]
        _high = high[index]
        _low = low[index]
        _close = close[index]
        _pct_chg = pct_chg[index]

        _ma5 = ma5[index]
        _ma10 = ma10[index]
        _ma20 = ma20[index]
        _ma30 = ma30[index]
        _ma55 = ma55[index]
        _ma60 = ma60[index]
        _ma120 = ma120[index]

        _ma5_slope = ma5_slope[index]
        _ma10_slope = ma10_slope[index]
        _ma20_slope = ma20_slope[index]
        _ma30_slope = ma30_slope[index]
        _ma55_slope = ma55_slope[index]
        _ma60_slope = ma60_slope[index]
        _ma120_slope = ma120_slope[index]

        _ema5 = ema5[index]
        _ema10 = ema10[index]
        _ema20 = ema20[index]
        _ema30 = ema30[index]
        _ema55 = ema55[index]
        _ema60 = ema60[index]
        _ema120 = ema120[index]

        _ema5_slope = ema5_slope[index]
        _ema10_slope = ema10_slope[index]
        _ema20_slope = ema20_slope[index]
        _ema30_slope = ema30_slope[index]
        _ema55_slope = ema55_slope[index]
        _ema60_slope = ema60_slope[index]
        _ema120_slope = ema120_slope[index]

        # set_yearly_price_position
        if index >= 260:
            high_price = max(high[index - 259: index + 1])
            low_price = min(low[index - 259: index + 1])
        else:
            high_price = max(high)
            low_price = min(low)

        price_range = high_price - low_price
        price_pct_position = round((_close - low_price) * 100 / price_range, 1)
        yearly_price_position.insert(index, price_pct_position)

        # yearly_price_position10
        if 10 >= yearly_price_position[index]:
            yearly_price_position10.insert(index, 1)
        else:
            yearly_price_position10.insert(index, 0)

        # yearly_price_position20
        if 20 >= yearly_price_position[index]:
            yearly_price_position20.insert(index, 0)
        else:
            yearly_price_position20.insert(index, 0)

        # yearly_price_position30
        if 30 >= yearly_price_position[index]:
            yearly_price_position30.insert(index, 1)
        else:
            yearly_price_position30.insert(index, 0)

        # yearly_price_position50
        if 50 >= yearly_price_position[index]:
            yearly_price_position50.insert(index, 1)
        else:
            yearly_price_position50.insert(index, 0)

        # yearly_price_position70
        if 70 >= yearly_price_position[index]:
            yearly_price_position70.insert(index, 1)
        else:
            yearly_price_position70.insert(index, 0)

        # MA20上行
        if _ma20_slope > 0:
            ma20_up.insert(index, 1)
        else:
            ma20_up.insert(index, 0)

        # EMA20上行
        if _ema20_slope > 0:
            ema20_up.insert(index, 1)
        else:
            ema20_up.insert(index, 0)

        # MA30上行
        if _ma30_slope > 0:
            ma30_up.insert(index, 1)
        else:
            ma30_up.insert(index, 0)

        # EMA30上行
        if _ema30_slope > 0:
            ema30_up.insert(index, 1)
        else:
            ema30_up.insert(index, 0)

        # MA60上行
        if _ma60_slope > 0:
            ma60_up.insert(index, 1)
        else:
            ma60_up.insert(index, 0)

        # EMA60上行
        if _ema60_slope > 0:
            ema60_up.insert(index, 1)
        else:
            ema60_up.insert(index, 0)

        # MA120上行
        if _ma120_slope > 0:
            ma120_up.insert(index, 1)
        else:
            ma120_up.insert(index, 0)

        # EMA120上行
        if _ema120_slope > 0:
            ema120_up.insert(index, 1)
        else:
            ema120_up.insert(index, 0)

        # MA多头排列（5/10/20/60）
        if _ma5_slope > 0 and _ma10_slope > 0 and _ma20_slope > 0 and _ma60_slope > 0 \
                and _ma5 > _ma10 > _ma20 > _ma60:
            ma_arrange.insert(index, 1)
        else:
            ma_arrange.insert(index, 0)

        # EMA多头排列（5/10/20/60）
        if _ema5_slope > 0 and _ema10_slope > 0 and _ema20_slope > 0 and _ema60_slope > 0 \
                and _ema5 > _ema10 > _ema20 > _ema60:
            ema_arrange.insert(index, 1)
        else:
            ema_arrange.insert(index, 0)

        # MA短期组合多头排列（5/10/20）
        if _ma5_slope > 0 and _ma10_slope > 0 and _ma20_slope > 0 \
                and _ma5 > _ma10 > _ma20:
            short_ma_arrange1.insert(index, 1)
        else:
            short_ma_arrange1.insert(index, 0)

        # MA短期组合多头排列（5/10/30）
        if _ma5_slope > 0 and _ma10_slope > 0 and _ma30_slope > 0 \
                and _ma5 > _ma10 > _ma30:
            short_ma_arrange2.insert(index, 1)
        else:
            short_ma_arrange2.insert(index, 0)

        # EMA短期组合多头排列（5/10/20）
        if _ema5_slope > 0 and _ema10_slope > 0 and _ema20_slope > 0 \
                and _ema5 > _ema10 > _ema20:
            short_ema_arrange1.insert(index, 1)
        else:
            short_ema_arrange1.insert(index, 0)

        # EMA短期组合多头排列（5/10/30）
        if _ema5_slope > 0 and _ema10_slope > 0 and _ema30_slope > 0 \
                and _ema5 > _ema10 > _ema30:
            short_ema_arrange2.insert(index, 1)
        else:
            short_ema_arrange2.insert(index, 0)

        # MA中期组合多头排列（10/20/60）
        if _ma10_slope > 0 and _ma20_slope > 0 and _ma60_slope > 0 \
                and _ma10 > _ma20 > _ma60:
            middle_ma_arrange1.insert(index, 1)
        else:
            middle_ma_arrange1.insert(index, 0)

        # MA中期组合多头排列（10/20/55）
        if _ma10_slope > 0 and _ma20_slope > 0 and _ma55_slope > 0 \
                and _ma10 > _ma20 > _ma55:
            middle_ma_arrange2.insert(index, 1)
        else:
            middle_ma_arrange2.insert(index, 0)

        # EMA中期组合多头排列（10/20/60）
        if _ema10_slope > 0 and _ema20_slope > 0 and _ema60_slope > 0 \
                and _ema10 > _ema20 > _ema60:
            middle_ema_arrange1.insert(index, 1)
        else:
            middle_ema_arrange1.insert(index, 0)

        # EMA中期组合多头排列（10/20/55）
        if _ema10_slope > 0 and _ema20_slope > 0 and _ema55_slope > 0 \
                and _ema10 > _ema20 > _ema55:
            middle_ema_arrange2.insert(index, 1)
        else:
            middle_ema_arrange2.insert(index, 0)

        # MA长期组合多头排列（20/55/120）
        if _ma20_slope > 0 and _ma55_slope > 0 and _ma120_slope > 0 \
                and _ma20 > _ma55 > _ma120:
            long_ma_arrange1.insert(index, 1)
        else:
            long_ma_arrange1.insert(index, 0)

        # MA长期组合多头排列（30/60/120）
        if _ma30_slope > 0 and _ma60_slope > 0 and _ma120_slope > 0 \
                and _ma30 > _ma60 > _ma120:
            long_ma_arrange2.insert(index, 1)
        else:
            long_ma_arrange2.insert(index, 0)

        # EMA长期组合多头排列（20/55/120）
        if _ema20_slope > 0 and _ema55_slope > 0 and _ema120_slope > 0 \
                and _ema20 > _ema55 > _ema120:
            long_ema_arrange1.insert(index, 1)
        else:
            long_ema_arrange1.insert(index, 0)

        # EMA长期组合多头排列（30/60/120）
        if _ema30_slope > 0 and _ema60_slope > 0 and _ema120_slope > 0 \
                and _ema30 > _ema60 > _ema120:
            long_ema_arrange2.insert(index, 1)
        else:
            long_ema_arrange2.insert(index, 0)

        # MA黄金交叉（5/10）
        if ma[index][0] > ma[index][1] and ma[index - 1][0] < ma[index - 1][1] and \
                ma_slope[index][0] > 0 and ma_slope[index][1] > 0:
            ma_gold_cross1.insert(index, 1)
        else:
            ma_gold_cross1.insert(index, 0)

        # MA黄金交叉（5/20）
        if ma[index][0] > ma[index][2] and ma[index - 1][0] < ma[index - 1][2] and \
                ma_slope[index][0] > 0 and ma_slope[index][2] > 0:
            ma_gold_cross2.insert(index, 1)
        else:
            ma_gold_cross2.insert(index, 0)

        # MA黄金交叉（10/20）
        if ma[index][1] > ma[index][2] and ma[index - 1][1] < ma[index - 1][2] and \
                ma_slope[index][1] > 0 and ma_slope[index][2] > 0:
            ma_gold_cross3.insert(index, 1)
        else:
            ma_gold_cross3.insert(index, 0)

        # MA黄金交叉（10/30）
        if ma[index][1] > ma[index][3] and ma[index - 1][1] < ma[index - 1][3] and \
                ma_slope[index][1] > 0 and ma_slope[index][3] > 0:
            ma_gold_cross4.insert(index, 1)
        else:
            ma_gold_cross4.insert(index, 0)

        # EMA黄金交叉（5/10）
        if ema[index][0] > ema[index][1] and ema[index - 1][0] < ema[index - 1][1] and \
                ema_slope[index][0] > 0 and ema_slope[index][1] > 0:
            ema_gold_cross1.insert(index, 1)
        else:
            ema_gold_cross1.insert(index, 0)

        # EMA黄金交叉（5/20）
        if ema[index][0] > ema[index][2] and ema[index - 1][0] < ema[index - 1][2] and \
                ema_slope[index][0] > 0 and ema_slope[index][2] > 0:
            ema_gold_cross2.insert(index, 1)
        else:
            ema_gold_cross2.insert(index, 0)

        # EMA黄金交叉（10/20）
        if ema[index][1] > ma[index][2] and ema[index - 1][1] < ema[index - 1][2] and \
                ema_slope[index][1] > 0 and ema_slope[index][2] > 0:
            ema_gold_cross3.insert(index, 1)
        else:
            ema_gold_cross3.insert(index, 0)

        # EMA黄金交叉（10/30）
        if ema[index][1] > ma[index][3] and ema[index - 1][1] < ema[index - 1][3] and \
                ema_slope[index][1] > 0 and ema_slope[index][3] > 0:
            ema_gold_cross4.insert(index, 1)
        else:
            ema_gold_cross4.insert(index, 0)

        # MA银山谷
        if is_ma_silver_valley(index, ma_gold_cross1, ma_gold_cross2, ma_gold_cross3):
            ma_silver_valley.insert(index, 1)
        else:
            ma_silver_valley.insert(index, 0)

        # EMA银山谷
        if is_ema_silver_valley(index, ema_gold_cross1, ema_gold_cross2, ema_gold_cross3):
            ema_silver_valley.insert(index, 1)
        else:
            ema_silver_valley.insert(index, 0)

        # MA金山谷
        if is_ma_gold_valley(index, ma, ma_slope, ma_silver_valley):
            ma_gold_valley.insert(index, 1)
        else:
            ma_gold_valley.insert(index, 0)

        # EMA金山谷
        if is_ema_gold_valley(index, ema, ema_slope, ema_silver_valley):
            ema_gold_valley.insert(index, 1)
        else:
            ema_gold_valley.insert(index, 0)

        is_ma_spider1, is_ma_spider2 = is_ma_spider(index, ma, ma_gold_cross1, ma_gold_cross2,
                                                    ma_gold_cross3, ma_gold_cross4)

        # MA金蜘蛛
        if is_ma_spider1:
            ma_spider.insert(index, 1)
        else:
            ma_spider.insert(index, 0)

        # MA金蜘蛛2
        if is_ma_spider2:
            ma_spider2.insert(index, 1)
        else:
            ma_spider2.insert(index, 0)

        is_ema_spider1, is_ema_spider2 = is_ema_spider(index, ema, ema_gold_cross1, ema_gold_cross2,
                                                       ema_gold_cross3, ema_gold_cross4)

        # EMA金蜘蛛
        if is_ema_spider1:
            ema_spider.insert(index, 1)
        else:
            ema_spider.insert(index, 0)

        # EMA金蜘蛛2
        if is_ema_spider2:
            ema_spider2.insert(index, 1)
        else:
            ema_spider2.insert(index, 0)

        # MA蛟龙出海(5/10/20)
        # 大阳线 贯穿ma5/ma10/ma20
        # ma20 上行

        if _pct_chg >= 4 and _open < _ma5 and _open < _ma10 and _open < _ma20 and \
                _close > _ma5 and _close > _ma10 and _close > _ma20 and _ma60_slope > 0:
            ma_out_sea.insert(index, 1)
        else:
            ma_out_sea.insert(index, 0)

        # EMA蛟龙出海(5/10/20)
        # 大阳线 贯穿ema5/ema10/ema20
        # ema20/ema60 上行
        if _pct_chg >= 4 and _open < _ema5 and _open < _ema10 and _open < _ema20 and \
                _close > _ema5 and _close > _ema10 and _close > _ema20 and _ema60_slope > 0:
            ema_out_sea.insert(index, 1)
        else:
            ema_out_sea.insert(index, 0)

        # MA烘云托月(5/10/20)
        if is_ma_hold_moon(index, candle, ma, ma_slope, _ma5, _ma10, _ma20, _ma5_slope, _ma10_slope):
            ma_hold_moon.insert(index, 1)
        else:
            ma_hold_moon.insert(index, 0)

        # EMA烘云托月(5/10/20)
        if is_ema_hold_moon(index, candle, ema, ema_slope, _ema5, _ema10, _ema20, _ema5_slope, _ema10_slope):
            ema_hold_moon.insert(index, 1)
        else:
            ema_hold_moon.insert(index, 0)

        # MA鱼跃龙门(5/10/20)
        if is_ma_over_gate(index, _close, _pct_chg, candle, ma, _ma5, _ma10, _ma20, ma_slope):
            ma_over_gate.insert(index, 1)
        else:
            ma_over_gate.insert(index, 0)

        # EMA鱼跃龙门(5/10/20)
        if is_ema_over_gate(index, _close, _pct_chg, candle, ema, _ema5, _ema10, _ema20, ema_slope):
            ema_over_gate.insert(index, 1)
        else:
            ema_over_gate.insert(index, 0)

        # MA旱地拔葱(5/10/20)
        if is_ma_up_ground(index, _pct_chg, open, high, low, close, ma5, ma10, ma20):
            ma_up_ground.insert(index, 1)
        else:
            ma_up_ground.insert(index, 0)

        # EMA旱地拔葱(5/10/20)
        if is_ema_up_ground(index, _pct_chg, open, high, low, close, ema5, ema10, ema20):
            ema_up_ground.insert(index, 1)
        else:
            ema_up_ground.insert(index, 0)

        # MA均线粘合(5/10/20)
        if is_ma_glue(index, ma5_slope, ma10_slope, ma20_slope):
            ma_glue.insert(index, 1)
        else:
            ma_glue.insert(index, 0)

        # EMA均线粘合(5/10/20)
        if is_ema_glue(index, ema5_slope, ema10_slope, ema20_slope):
            ema_glue.insert(index, 1)
        else:
            ema_glue.insert(index, 0)

        # TD_8
        if td[index][1] == 8:
            td8.insert(index, 1)
        else:
            td8.insert(index, 0)

        # TD_9
        if td[index][1] == 9:
            td9.insert(index, 1)
        else:
            td9.insert(index, 0)

        # bias6
        if bias[index][0] < -3:
            bias6.insert(index, 1)
        else:
            bias6.insert(index, 0)

        # bias12
        if bias[index][1] < -4.5:
            bias12.insert(index, 1)
        else:
            bias12.insert(index, 0)

        # bias24
        if bias[index][2] < -7:
            bias24.insert(index, 1)
        else:
            bias24.insert(index, 0)

        # bias72
        if bias[index][4] < -11:
            bias72.insert(index, 1)
        else:
            bias72.insert(index, 0)

        # bias60 不作为单独信号 需结合趋势判断上涨回踩形态
        if 1.5 >= bias[index][3] >= -1.5:
            bias60.insert(index, 1)
        else:
            bias60.insert(index, 0)

        # bias120 不作为单独信号 需结合趋势判断上涨回踩形态
        if 1 >= bias[index][5] >= -1:
            bias120.insert(index, 1)
        else:
            bias120.insert(index, 0)

        # 最近3个交易日站上 ma60/ma120 ema60/ema120
        if is_stand_up_ma60(index, open, close, ma60, ma60_slope):
            stand_up_ma60.insert(index, 1)
        else:
            stand_up_ma60.insert(index, 0)

        if is_stand_up_ma120(index, open, close, ma120, ma120_slope):
            stand_up_ma120.insert(index, 1)
        else:
            stand_up_ma120.insert(index, 0)

        if is_stand_up_ema60(index, open, close, ema60, ema60_slope):
            stand_up_ema60.insert(index, 1)
        else:
            stand_up_ema60.insert(index, 0)

        if is_stand_up_ema120(index, open, close, ema120, ema120_slope):
            stand_up_ema120.insert(index, 1)
        else:
            stand_up_ema120.insert(index, 0)

        # 连续两日K线在ma60上方收出下影线 / 或遇支撑
        if stand_on_ma(_open, _high, _low, _close, _ma60, _ma60_slope) \
                and is_ma60_steady_up(index, ma60_slope):
            ma60_support.insert(index, 1)
        else:
            ma60_support.insert(index, 0)

        # 连续两日K线在ema60上方收出下影线 / 或遇支撑
        if stand_on_ema(_open, _high, _low, _close, _ema60, _ema60_slope) \
                and is_ema60_steady_up(index, ema60_slope):
            ema60_support.insert(index, 1)
        else:
            ema60_support.insert(index, 0)

        # 连续两日K线在ma120上方收出下影线 / 或遇支撑
        if stand_on_ma(_open, _high, _low, _close, _ma120, _ma120_slope) \
                and is_ma120_steady_up(index, ma120_slope):
            ma120_support.insert(index, 1)
        else:
            ma120_support.insert(index, 0)

        # 连续两日K线在ema120上方收出下影线 / 或遇支撑
        if stand_on_ema(_open, _high, _low, _close, _ema120, _ema120_slope) \
                and is_ema120_steady_up(index, ema120_slope):
            ema120_support.insert(index, 1)
        else:
            ema120_support.insert(index, 0)

        if is_ma_group_glue(index, ma10_slope, ma20_slope, ma30_slope, ma60_slope):
            ma_group_glue.insert(index, 1)
        else:
            ma_group_glue.insert(index, 0)

        if is_ema_group_glue(index, ema10_slope, ema20_slope, ema30_slope, ema60_slope):
            ema_group_glue.insert(index, 1)
        else:
            ema_group_glue.insert(index, 0)

        # ma5/ma10/ma20 出现多头排列
        if is_ma_up_arrange51020(index, ma5, ma10, ma20, ma5_slope, ma10_slope, ma20_slope):
            ma_up_arrange51020.insert(index, 1)
        else:
            ma_up_arrange51020.insert(index, 0)

        # ma5/ma10/ma20/ma30 出现多头排列
        if is_ma_up_arrange5102030(index, ma5, ma10, ma20, ma30, ma5_slope, ma10_slope, ma20_slope, ma30_slope):
            ma_up_arrange5102030.insert(index, 1)
        else:
            ma_up_arrange5102030.insert(index, 0)

        # ma5/ma10/ma20/ma30/ma60 出现多头排列
        if is_ma_up_arrange510203060(index, ma5, ma10, ma20, ma30, ma60, ma5_slope, ma10_slope, ma20_slope,
                                     ma30_slope,
                                     ma60_slope):
            ma_up_arrange510203060.insert(index, 1)
        else:
            ma_up_arrange510203060.insert(index, 0)

        # ma20/ma30/ma60 出现多头排列
        if is_ma_up_arrange203060(index, ma20, ma30, ma60, ma20_slope, ma30_slope, ma60_slope):
            ma_up_arrange203060.insert(index, 1)
        else:
            ma_up_arrange203060.insert(index, 0)

        # ma20/ma60/ma120 出现多头排列
        if is_ma_up_arrange2060120(index, ma20, ma60, ma120, ma20_slope, ma60_slope, ma120_slope):
            ma_up_arrange2060120.insert(index, 1)
        else:
            ma_up_arrange2060120.insert(index, 0)

        # ema5/ema10/ema20 出现多头排列
        if is_ema_up_arrange51020(index, ema5, ema10, ema20, ema5_slope, ema10_slope, ema20_slope):
            ema_up_arrange51020.insert(index, 1)
        else:
            ema_up_arrange51020.insert(index, 0)

        # ema5/ema10/ema20/ema30 出现多头排列
        if is_ema_up_arrange5102030(index, ema5, ema10, ema20, ema30, ema5_slope, ema10_slope, ema20_slope,
                                    ema30_slope):
            ema_up_arrange5102030.insert(index, 1)
        else:
            ema_up_arrange5102030.insert(index, 0)

        # ema5/ema10/ema20/ema30/ema60 出现多头排列
        if is_ema_up_arrange510203060(index, ema5, ema10, ema20, ema30, ema60, ema5_slope, ema10_slope, ema20_slope,
                                      ema30_slope, ema60_slope):
            ema_up_arrange510203060.insert(index, 1)
        else:
            ema_up_arrange510203060.insert(index, 0)

        # ema20/ema30/ema60 出现多头排列
        if is_ema_up_arrange203060(index, ema20, ema30, ema60, ema20_slope, ema30_slope, ema60_slope):
            ema_up_arrange203060.insert(index, 1)
        else:
            ema_up_arrange203060.insert(index, 0)

        # ema20/ema60/ema120 出现多头排列
        if is_ema_up_arrange2055120(index, ema20, ema55, ema120, ema20_slope, ema55_slope, ema120_slope):
            ema_up_arrange2055120.insert(index, 1)
        else:
            ema_up_arrange2055120.insert(index, 0)

        # 锤子线
        if is_hammer(index, open, high, low, close, pct_chg):
            hammer.insert(index, 1)
        else:
            hammer.insert(index, 0)

        # 倒锤子线
        if is_pour_hammer(index, open, high, low, close, pct_chg):
            pour_hammer.insert(index, 1)
        else:
            pour_hammer.insert(index, 0)

        # 看涨尽头线
        if is_short_end(index, open, high, low, close, pct_chg):
            short_end.insert(index, 1)
        else:
            short_end.insert(index, 0)

        # 看涨吞没
        if is_swallow_up(index, open, high, low, close, pct_chg):
            swallow_up.insert(index, 1)
        else:
            swallow_up.insert(index, 0)

        # 好友反攻
        if is_attack_short(index, open, high, low, close, pct_chg):
            attack_short.insert(index, 1)
        else:
            attack_short.insert(index, 0)

        # 曙光初现
        if is_first_light(index, open, high, low, close, pct_chg):
            first_light.insert(index, 1)
        else:
            first_light.insert(index, 0)

        # 旭日东升
        if is_sunrise(index, open, high, low, close, pct_chg):
            sunrise.insert(index, 1)
        else:
            sunrise.insert(index, 0)

        # 平底
        if is_flat_base(index, open, high, low, close, pct_chg):
            flat_base.insert(index, 1)
        else:
            flat_base.insert(index, 0)

    return yearly_price_position, yearly_price_position10, yearly_price_position20, \
           yearly_price_position30, yearly_price_position50, yearly_price_position70, \
           ma20_up, ema20_up, ma30_up, ema30_up, ma60_up, ema60_up, ma120_up, ema120_up, \
           ma_arrange, ema_arrange, \
           short_ma_arrange1, short_ma_arrange2, short_ema_arrange1, short_ema_arrange2, \
           middle_ma_arrange1, middle_ma_arrange2, middle_ema_arrange1, middle_ema_arrange2, \
           long_ma_arrange1, long_ma_arrange2, long_ema_arrange1, long_ema_arrange2, \
           ma_gold_cross1, ma_gold_cross2, ma_gold_cross3, ma_gold_cross4, \
           ema_gold_cross1, ema_gold_cross2, ema_gold_cross3, ema_gold_cross4, \
           ma_silver_valley, ema_silver_valley, ma_gold_valley, ema_gold_valley, \
           ma_spider, ma_spider2, ema_spider, ema_spider2, \
           ma_glue, ema_glue, ma_out_sea, ema_out_sea, ma_hold_moon, ema_hold_moon, \
           ma_over_gate, ema_over_gate, ma_up_ground, ema_up_ground, td8, td9, \
           bias6, bias12, bias24, bias60, bias72, bias120, \
           stand_up_ma60, stand_up_ma120, stand_up_ema60, stand_up_ema120, \
           ma60_support, ema60_support, ma120_support, ema120_support, \
           ma_group_glue, ema_group_glue, \
           ma_up_arrange51020, ma_up_arrange5102030, ma_up_arrange510203060, \
           ma_up_arrange203060, ma_up_arrange2060120, \
           ema_up_arrange51020, ema_up_arrange5102030, ema_up_arrange510203060, \
           ema_up_arrange203060, ema_up_arrange2055120, \
           hammer, pour_hammer, short_end, swallow_up, attack_short, \
           first_light, sunrise, flat_base
