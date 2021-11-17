from talib import SMA
import pandas as pd
import numpy as np
import math
from .candle import stand_on_ma, stand_on_ema
import time

"""
df: indicators with signals (long signals or short signals)
"""
yearly_price_position = []
yearly_price_position10 = []
yearly_price_position20 = []
yearly_price_position30 = []
yearly_price_position50 = []
yearly_price_position70 = []

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


def analytic_signals(df):
    global yearly_price_position
    global yearly_price_position10
    global yearly_price_position20
    global yearly_price_position30
    global yearly_price_position50
    global yearly_price_position70

    global ma60_support
    global ema60_support
    global ma120_support
    global ema120_support

    global stand_up_ma60
    global stand_up_ema60
    global stand_up_ma120
    global stand_up_ema120

    global ma_group_glue
    global ema_group_glue

    global ma_up_arrange51020
    global ma_up_arrange5102030
    global ma_up_arrange510203060
    global ma_up_arrange203060
    global ma_up_arrange2060120
    global ema_up_arrange51020
    global ema_up_arrange5102030
    global ema_up_arrange510203060
    global ema_up_arrange203060
    global ema_up_arrange2055120

    yearly_price_position = []
    yearly_price_position10 = []
    yearly_price_position20 = []
    yearly_price_position30 = []
    yearly_price_position50 = []
    yearly_price_position70 = []

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

    # 连续两日K线在ma60上方止跌
    # 连续两日K线在ma120上方止跌
    # 最近20个交易日 沿着ma30上行 未曾跌破ma30

    df['yearly_price_position'] = np.nan
    df['yearly_price_position10'] = np.nan
    df['yearly_price_position20'] = np.nan
    df['yearly_price_position30'] = np.nan
    df['yearly_price_position50'] = np.nan
    df['yearly_price_position70'] = np.nan

    df['stand_up_ma60'] = np.nan
    df['stand_up_ma120'] = np.nan
    df['stand_up_ema60'] = np.nan
    df['stand_up_ema120'] = np.nan

    df['ma60_support'] = np.nan
    df['ma120_support'] = np.nan
    df['ema60_support'] = np.nan
    df['ema120_support'] = np.nan

    df['ma_group_glue'] = np.nan
    df['ema_group_glue'] = np.nan

    df['ma_up_arrange51020'] = np.nan
    df['ma_up_arrange5102030'] = np.nan
    df['ma_up_arrange510203060'] = np.nan
    df['ma_up_arrange203060'] = np.nan
    df['ma_up_arrange2060120'] = np.nan

    df['ema_up_arrange51020'] = np.nan
    df['ema_up_arrange5102030'] = np.nan
    df['ema_up_arrange510203060'] = np.nan
    df['ema_up_arrange203060'] = np.nan
    df['ema_up_arrange2055120'] = np.nan

    df.fillna(0, inplace=True)
    df.apply(lambda row: item_apply(df, row), axis=1)


def item_apply(df, row):
    index = row.name

    # set_yearly_price_position
    if index >= 260:
        high_price = df['high'][index - 259: index + 1].max()
        low_price = df['low'][index - 259: index + 1].min()
        price_range = high_price - low_price
        price_pct_position = round((row.close - low_price) * 100 / price_range, 1)
        yearly_price_position.insert(index, price_pct_position)
    else:
        yearly_price_position.insert(index, 0)

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

    # 最近3个交易日站上 ma60/ma120 ema60/ema120
    if is_stand_up_ma60(df, row):
        stand_up_ma60.insert(index, 1)
    else:
        stand_up_ma60.insert(index, 0)

    if is_stand_up_ma120(df, row):
        stand_up_ma120.insert(index, 1)
    else:
        stand_up_ma120.insert(index, 0)

    if is_stand_up_ema60(df, row):
        stand_up_ema60.insert(index, 1)
    else:
        stand_up_ema60.insert(index, 0)

    if is_stand_up_ema120(df, row):
        stand_up_ema120.insert(index, 1)
    else:
        stand_up_ema120.insert(index, 0)

    # 连续两日K线在ma60上方收出下影线 / 或遇支撑
    if stand_on_ma(df, row, 60) and is_ma60_steady_up(df, row):
        ma60_support.insert(index, 1)
    else:
        ma60_support.insert(index, 0)

    # 连续两日K线在ema60上方收出下影线 / 或遇支撑
    if stand_on_ema(df, row, 60) and is_ema60_steady_up(df, row):
        ema60_support.insert(index, 1)
    else:
        ema60_support.insert(index, 0)

    # 连续两日K线在ma120上方收出下影线 / 或遇支撑
    if stand_on_ma(df, row, 120) and is_ma120_steady_up(df, row):
        ma120_support.insert(index, 1)
    else:
        ma120_support.insert(index, 0)

    # 连续两日K线在ema120上方收出下影线 / 或遇支撑
    if stand_on_ema(df, row, 120) and is_ema120_steady_up(df, row):
        ema120_support.insert(index, 1)
    else:
        ema120_support.insert(index, 0)

    # 最近9个交易日 0 <= ma60_slope <= 1
    # 最近9个交易日 0 <= ma30_slope <= 1
    # 最近9个交易日 0 <= ma20_slope <= 1
    # 最近9个交易日 -1.5 < ma10_slope < 1.5
    if is_ma_group_glue(df, row):
        ma_group_glue.insert(index, 1)
    else:
        ma_group_glue.insert(index, 0)

    # 最近9个交易日 0 <= ma60_slope <= 1
    # 最近9个交易日 0 <= ma30_slope <= 1
    # 最近9个交易日 0 <= ma20_slope <= 1
    # 最近9个交易日 -1.5 < ma10_slope < 1.5
    if is_ema_group_glue(df, row):
        ema_group_glue.insert(index, 1)
    else:
        ema_group_glue.insert(index, 0)

    # ma5/ma10/ma20 出现多头排列
    if is_ma_up_arrange51020(df, row):
        ma_up_arrange51020.insert(index, 1)
    else:
        ma_up_arrange51020.insert(index, 0)

    # ma5/ma10/ma20/ma30 出现多头排列
    if is_ma_up_arrange5102030(df, row):
        ma_up_arrange5102030.insert(index, 1)
    else:
        ma_up_arrange5102030.insert(index, 0)

    # ma5/ma10/ma20/ma30/ma60 出现多头排列
    if is_ma_up_arrange510203060(df, row):
        ma_up_arrange510203060.insert(index, 1)
    else:
        ma_up_arrange510203060.insert(index, 0)

    # ma20/ma30/ma60 出现多头排列
    if is_ma_up_arrange203060(df, row):
        ma_up_arrange203060.insert(index, 1)
    else:
        ma_up_arrange203060.insert(index, 0)

    # ma20/ma60/ma120 出现多头排列
    if is_ma_up_arrange2060120(df, row):
        ma_up_arrange2060120.insert(index, 1)
    else:
        ma_up_arrange2060120.insert(index, 0)

    # ema5/ema10/ema20 出现多头排列
    if is_ema_up_arrange51020(df, row):
        ema_up_arrange51020.insert(index, 1)
    else:
        ema_up_arrange51020.insert(index, 0)

    # ema5/ema10/ema20/ema30 出现多头排列
    if is_ema_up_arrange5102030(df, row):
        ema_up_arrange5102030.insert(index, 1)
    else:
        ema_up_arrange5102030.insert(index, 0)

    # ema5/ema10/ema20/ema30/ema60 出现多头排列
    if is_ema_up_arrange510203060(df, row):
        ema_up_arrange510203060.insert(index, 1)
    else:
        ema_up_arrange510203060.insert(index, 0)

    # ema20/ema30/ema60 出现多头排列
    if is_ema_up_arrange203060(df, row):
        ema_up_arrange203060.insert(index, 1)
    else:
        ema_up_arrange203060.insert(index, 0)

    # ema20/ema60/ema120 出现多头排列
    if is_ema_up_arrange2055120(df, row):
        ema_up_arrange2055120.insert(index, 1)
    else:
        ema_up_arrange2055120.insert(index, 0)

    if index == len(df) - 1:
        df['yearly_price_position'] = yearly_price_position
        df['yearly_price_position10'] = yearly_price_position10
        df['yearly_price_position20'] = yearly_price_position20
        df['yearly_price_position30'] = yearly_price_position30
        df['yearly_price_position50'] = yearly_price_position50
        df['yearly_price_position70'] = yearly_price_position70

        df['stand_up_ma60'] = stand_up_ma60
        df['stand_up_ma120'] = stand_up_ma120
        df['stand_up_ema60'] = stand_up_ema60
        df['stand_up_ema120'] = stand_up_ema120

        df['ma60_support'] = ma60_support
        df['ema60_support'] = ema60_support
        df['ma120_support'] = ma120_support
        df['ema120_support'] = ema120_support

        df['ma_group_glue'] = ma_group_glue
        df['ema_group_glue'] = ema_group_glue

        df['ma_up_arrange51020'] = ma_up_arrange51020
        df['ma_up_arrange5102030'] = ma_up_arrange5102030
        df['ma_up_arrange510203060'] = ma_up_arrange510203060
        df['ma_up_arrange203060'] = ma_up_arrange203060
        df['ma_up_arrange2060120'] = ma_up_arrange2060120

        df['ema_up_arrange51020'] = ema_up_arrange51020
        df['ema_up_arrange5102030'] = ema_up_arrange5102030
        df['ema_up_arrange510203060'] = ema_up_arrange510203060
        df['ema_up_arrange203060'] = ema_up_arrange203060
        df['ema_up_arrange2055120'] = ema_up_arrange2055120


def is_stand_up_ma60(df, row):
    # 前55个交易日(除最近3个交易日外) ma60向下运行
    index = row.name
    small_set = df.iloc[index - 55: index - 2]
    pre_row = df.iloc[index - 1]
    before_pre_row = df.iloc[index - 2]
    ma60_down_still = True
    ma60_up_recently = False

    if small_set['ma60_slope'].max() >= 0:
        ma60_down_still = False

    # 最近3个交易日收盘价高于 ma60
    # 最近3个交易日 ma60 开始向上
    if row.close > row.ma60 and pre_row.close > pre_row.ma60 and before_pre_row.close > before_pre_row.ma60 \
            and row.ma60_slope > 0 and pre_row.ma60_slope > 0 and before_pre_row.ma60_slope > 0:
        ma60_up_recently = True

    if len(df) > 81 and ma60_down_still and ma60_up_recently:
        return 1
    else:
        return 0


def is_stand_up_ma120(df, row):
    # 前89个交易日(除最近3个交易日外) ma120向下运行
    index = row.name
    small_set = df.iloc[index - 89: index - 2]
    pre_row = df.iloc[index - 1]
    before_pre_row = df.iloc[index - 2]
    ma120_down_still = True
    ma120_up_recently = False

    if small_set['ma120_slope'].max() >= 0:
        ma120_down_still = False

    # 最近3个交易日收盘价高于 ma120
    # 最近3个交易日 ma120 开始向上
    if row.close > row.ma120 and pre_row.close > pre_row.ma120 and before_pre_row.close > before_pre_row.ma120 \
            and row.ma120_slope > 0 and pre_row.ma120_slope > 0 and before_pre_row.ma120_slope > 0:
        ma120_up_recently = True

    if len(df) > 154 and ma120_down_still and ma120_up_recently:
        return True
    else:
        return False


def is_stand_up_ema60(df, row):
    # 前55个交易日(除最近3个交易日外) ema60 向下运行
    index = row.name
    small_set = df.iloc[index - 55: index - 2]
    pre_row = df.iloc[index - 1]
    before_pre_row = df.iloc[index - 2]
    ma60_down_still = True
    ma60_up_recently = False

    if small_set['ema60_slope'].max() >= 0:
        ma60_down_still = False

    # 最近3个交易日收盘价高于 ema60
    # 最近3个交易日 ema60 开始向上
    if row.close > row.ema60 and pre_row.close > pre_row.ema60 and before_pre_row.close > before_pre_row.ema60 \
            and row.ema60_slope > 0 and pre_row.ema60_slope > 0 and before_pre_row.ema60_slope > 0:
        ma60_up_recently = True

    if len(df) > 81 and ma60_down_still and ma60_up_recently:
        return True
    else:
        return False


def is_stand_up_ema120(df, row):
    # 前89个交易日(除最近3个交易日外) ma120向下运行
    index = row.name

    small_set = df.iloc[index - 89: index - 2]
    pre_row = df.iloc[index - 1]
    before_pre_row = df.iloc[index - 2]
    ma120_down_still = True
    ma120_up_recently = False

    if small_set['ema120_slope'].max() >= 0:
        ma120_down_still = False

    # 最近3个交易日收盘价高于 ma120
    # 最近3个交易日 ma120 开始向上
    if row.close > row.ema120 and pre_row.close > pre_row.ema120 and before_pre_row.close > before_pre_row.ema120 \
            and row.ema120_slope > 0 and pre_row.ema120_slope > 0 and before_pre_row.ema120_slope > 0:
        ma120_up_recently = True

    if len(df) > 154 and ma120_down_still and ma120_up_recently:
        return True
    else:
        return False


def is_ma60_steady_up(df, row):
    index = row.name
    # 最近21个交易日 ma60 稳步向上
    if len(df) > 81 and df['ma60_slope'][index - 20: index].min() > 0:
        return True
    else:
        return False


def is_ma120_steady_up(df, row):
    index = row.name
    # 最近34个交易日 ma120 稳步向上
    if len(df) > 154 and df['ma120_slope'][index - 33: index].min() > 0:
        return True
    else:
        return False


def is_ema60_steady_up(df, row):
    index = row.name
    # 最近21个交易日 ma60 稳步向上
    if len(df) > 81 and df['ema60_slope'][index - 20: index].min() > 0:
        return True
    else:
        return False


def is_ema120_steady_up(df, row):
    index = row.name
    # 最近34个交易日 ma120 稳步向上
    if len(df) > 154 and df['ema120_slope'][index - 33: index].min() > 0:
        return True
    else:
        return False


def is_ma60_support(df, row):
    # 连续两日K线在ma60上方收出下影线 / 或遇支撑
    if stand_on_ma(df, row, 60) and is_ma60_steady_up(df, row):
        return 1
    else:
        return 0


def is_ma120_support(df, row):
    # 连续两日K线在ma120上方收出下影线 / 或遇支撑
    if stand_on_ma(df, row, 120) and is_ma120_steady_up(df, row):
        return 1
    else:
        return 0


def is_ema60_support(df, row):
    # 连续两日K线在ema60上方收出下影线 / 或遇支撑
    if stand_on_ema(df, row, 60) and is_ema60_steady_up(df, row):
        return 1
    else:
        return 0


def is_ema120_support(df, row):
    # 连续两日K线在ema120上方收出下影线 / 或遇支撑
    if stand_on_ema(df, row, 120) and is_ema120_steady_up(df, row):
        return 1
    else:
        return 0


def is_ma_group_glue(df, row):
    index = row.name
    # 最近9个交易日 0 <= ma60_slope < 0.6
    # 最近9个交易日 0 <= ma30_slope < 0.6
    # 最近9个交易日 0 <= ma20_slope < 0.6
    # 最近9个交易日 -1 < ma10_slope < 1.2
    if df.ma60_slope[index - 8: index + 1].min() >= 0 \
            and df.ma60_slope[index - 8: index + 1].max() < 0.6 \
            and df.ma30_slope[index - 8: index + 1].min() >= 0 \
            and df.ma30_slope[index - 8: index + 1].max() < 0.6 \
            and df.ma20_slope[index - 8: index + 1].min() >= 0 \
            and df.ma20_slope[index - 8: index + 1].max() < 0.6 \
            and df.ma10_slope[index - 8: index + 1].min() > -1 \
            and df.ma10_slope[index - 8: index + 1].max() < 1.2:
        return True
    else:
        return False


def is_ema_group_glue(df, row):
    index = row.name
    # 最近9个交易日 0 <= ema60_slope < 0.6
    # 最近9个交易日 0 <= ema30_slope < 0.6
    # 最近9个交易日 0 <= ema20_slope < 0.6
    # 最近9个交易日 -1 < ema10_slope < 1.2
    if df.ema60_slope[index - 8: index + 1].min() >= 0 \
            and df.ema60_slope[index - 8: index + 1].max() < 0.6 \
            and df.ema30_slope[index - 8: index + 1].min() >= 0 \
            and df.ema30_slope[index - 8: index + 1].max() < 0.6 \
            and df.ema20_slope[index - 8: index + 1].min() >= 0 \
            and df.ema20_slope[index - 8: index + 1].max() < 0.6 \
            and df.ema10_slope[index - 8: index + 1].min() > -1 \
            and df.ema10_slope[index - 8: index + 1].max() < 1.2:
        return True
    else:
        return False


def is_ma_up_arrange51020(df, row):
    index = row.name
    # ma5/ma10/ma20 出现多头排列
    if index == 0:
        return False
    else:
        pre_row = df.iloc[index - 1]
        # 前一交易日 未形成多头排列
        # 当前交易日 形成多头排列
        if (not (pre_row.ma5 > pre_row.ma10 > pre_row.ma20 and
                 pre_row.ma5_slope > 0 and pre_row.ma10_slope > 0 and pre_row.ma20_slope > 0)) \
                and row.ma5 > row.ma10 > row.ma20 and row.ma5_slope > 0 and row.ma10_slope > 0 and row.ma20_slope > 0:
            return True
        else:
            return False


def is_ma_up_arrange5102030(df, row):
    index = row.name
    # ma5/ma10/ma20/ma30 出现多头排列
    if index == 0:
        return False
    else:
        pre_row = df.iloc[index - 1]
        # 前一交易日 未形成多头排列
        # 当前交易日 形成多头排列
        if (not (pre_row.ma5 > pre_row.ma10 > pre_row.ma20 > pre_row.ma30 and
                 pre_row.ma5_slope > 0 and pre_row.ma10_slope > 0 and
                 pre_row.ma20_slope > 0 and pre_row.ma30_slope > 0)) \
                and row.ma5 > row.ma10 > row.ma20 > row.ma30 and \
                row.ma5_slope > 0 and row.ma10_slope > 0 and row.ma20_slope > 0 and row.ma30_slope > 0:
            return True
        else:
            return False


def is_ma_up_arrange510203060(df, row):
    index = row.name
    # ma5/ma10/ma20/ma30/ma60 出现多头排列
    if index == 0:
        return False
    else:
        pre_row = df.iloc[index - 1]
        # 前一交易日 未形成多头排列
        # 当前交易日 形成多头排列
        if (not (pre_row.ma5 > pre_row.ma10 > pre_row.ma20 > pre_row.ma30 > pre_row.ma60 and
                 pre_row.ma5_slope > 0 and pre_row.ma10_slope > 0 and
                 pre_row.ma20_slope > 0 and pre_row.ma30_slope > 0 and row.ma60_slope > 0)) \
                and row.ma5 > row.ma10 > row.ma20 > row.ma30 > row.ma60 \
                and row.ma5_slope > 0 and row.ma10_slope > 0 and row.ma20_slope > 0 \
                and row.ma30_slope > 0 and row.ma60_slope > 0:
            return True
        else:
            return False


def is_ma_up_arrange203060(df, row):
    index = row.name
    # ma20/ma30/ma60 出现多头排列
    if index == 0:
        return False
    else:
        pre_row = df.iloc[index - 1]
        # 前一交易日 未形成多头排列
        # 当前交易日 形成多头排列
        if (not (pre_row.ma20 > pre_row.ma30 > pre_row.ma60 and
                 pre_row.ma20_slope > 0 and pre_row.ma30_slope > 0 and row.ma60_slope > 0)) \
                and row.ma20 > row.ma30 > row.ma60 \
                and row.ma20_slope > 0 and row.ma30_slope > 0 and row.ma60_slope > 0:
            return True
        else:
            return False


def is_ma_up_arrange2060120(df, row):
    index = row.name
    # ma20/ma60/ma120 出现多头排列
    if index == 0:
        return False
    else:
        pre_row = df.iloc[index - 1]
        # 前一交易日 未形成多头排列
        # 当前交易日 形成多头排列
        if (not (pre_row.ma20 > pre_row.ma60 > pre_row.ma120 and
                 pre_row.ma20_slope > 0 and pre_row.ma60_slope > 0 and row.ma120_slope > 0)) \
                and row.ma20 > row.ma60 > row.ma120 \
                and row.ma20_slope > 0 and row.ma60_slope > 0 and row.ma120_slope > 0:
            return True
        else:
            return False


def is_ema_up_arrange51020(df, row):
    index = row.name
    # ema5/ema10/ema20 出现多头排列
    if index == 0:
        return False
    else:
        pre_row = df.iloc[index - 1]
        # 前一交易日 未形成多头排列
        # 当前交易日 形成多头排列
        if (not (pre_row.ema5 > pre_row.ema10 > pre_row.ema20 and
                 pre_row.ema5_slope > 0 and pre_row.ema10_slope > 0 and pre_row.ema20_slope > 0)) \
                and row.ema5 > row.ema10 > row.ema20 \
                and row.ema5_slope > 0 and row.ema10_slope > 0 and row.ema20_slope > 0:
            return True
        else:
            return False


def is_ema_up_arrange5102030(df, row):
    index = row.name
    # ema5/ema10/ema20/ema30 出现多头排列
    if index == 0:
        return False
    else:
        pre_row = df.iloc[index - 1]
        # 前一交易日 未形成多头排列
        # 当前交易日 形成多头排列
        if (not (pre_row.ema5 > pre_row.ema10 > pre_row.ema20 > pre_row.ema30 and
                 pre_row.ema5_slope > 0 and pre_row.ema10_slope > 0 and
                 pre_row.ema20_slope > 0 and pre_row.ema30_slope > 0)) \
                and row.ema5 > row.ema10 > row.ema20 > row.ema30 and \
                row.ema5_slope > 0 and row.ema10_slope > 0 and row.ema20_slope > 0 and row.ema30_slope > 0:
            return True
        else:
            return False


def is_ema_up_arrange510203060(df, row):
    index = row.name
    # ema5/ema10/ema20/ema30/ema60 出现多头排列
    if index == 0:
        return False
    else:
        pre_row = df.iloc[index - 1]
        # 前一交易日 未形成多头排列
        # 当前交易日 形成多头排列
        if (not (pre_row.ema5 > pre_row.ema10 > pre_row.ema20 > pre_row.ema30 > pre_row.ema60 and
                 pre_row.ema5_slope > 0 and pre_row.ema10_slope > 0 and
                 pre_row.ema20_slope > 0 and pre_row.ema30_slope > 0 and row.ema60_slope > 0)) \
                and row.ema5 > row.ema10 > row.ema20 > row.ema30 > row.ema60 \
                and row.ema5_slope > 0 and row.ema10_slope > 0 and row.ema20_slope > 0 \
                and row.ema30_slope > 0 and row.ema60_slope > 0:
            return True
        else:
            return False


def is_ema_up_arrange203060(df, row):
    index = row.name
    # ema20/ema30/ema60 出现多头排列
    if index == 0:
        return False
    else:
        pre_row = df.iloc[index - 1]

        # 前一交易日 未形成多头排列
        # 当前交易日 形成多头排列
        if (not (pre_row.ema20 > pre_row.ema30 > pre_row.ema60 and
                 pre_row.ema20_slope > 0 and pre_row.ema30_slope > 0 and row.ema60_slope > 0)) \
                and row.ema20 > row.ema30 > row.ema60 \
                and row.ema20_slope > 0 and row.ema30_slope > 0 and row.ema60_slope > 0:
            return True
        else:
            return False


def is_ema_up_arrange2055120(df, row):
    index = row.name
    # ema20/ema55/ema120 出现多头排列
    if index == 0:
        return False
    else:
        pre_row = df.iloc[index - 1]

        # 前一交易日 未形成多头排列
        # 当前交易日 形成多头排列
        if (not (pre_row.ema20 > pre_row.ema55 > pre_row.ema120 and
                 pre_row.ema20_slope > 0 and pre_row.ema55_slope > 0 and row.ema120_slope > 0)) \
                and row.ema20 > row.ema55 > row.ema120 \
                and row.ema20_slope > 0 and row.ema55_slope > 0 and row.ema120_slope > 0:
            return True
        else:
            return False

