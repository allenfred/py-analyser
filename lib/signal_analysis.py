from talib import SMA
import numpy as np
import math
from .candle import stand_on_ma, stand_on_ema

"""
df: indicators with signals (long signals or short signals)
"""


def rise_support_analysis(df):
    # 连续两日K线在ma60上方止跌

    # 连续两日K线在ma120上方止跌

    # 最近3个交易日站上 ma60/ma120 ema60/ema120
    set_stand_up_ma60(df)
    set_stand_up_ma120(df)
    set_stand_up_ema60(df)
    set_stand_up_ema120(df)

    # 连续两日K线在ma60上方收出下影线 / 或遇支撑
    set_ma60_support(df)
    set_ema60_support(df)

    # 连续两日K线在ma120上方收出下影线 / 或遇支撑
    set_ma120_support(df)
    set_ema120_support(df)

    # 收盘价 yearly_price_position
    set_yearly_price_position(df)

    # 收盘价处于最近一年 10% 以下分位点 price_position10
    set_yearly_price_position10(df)

    # 收盘价处于最近一年 20% 以下分位点 price_position20
    set_yearly_price_position20(df)

    # 收盘价处于最近一年 30% 以下分位点 price_position30
    set_yearly_price_position30(df)

    # 收盘价处于最近一年 50% 以下分位点 price_position50
    set_yearly_price_position50(df)

    # 收盘价处于最近一年 70% 以下分位点 price_position70
    set_yearly_price_position70(df)

    # 最近20个交易日 沿着ma30上行 未曾跌破ma30

    # MA均线粘合 ma10/ma20/ma30/ma60
    set_ma_group_glue(df)

    # EMA均线粘合 ema10/ema20/ema30/ema60
    set_ema_group_glue(df)

    # ma5/ma10/ma20 出现多头排列
    set_ma_up_arrange51020(df)

    # ma5/ma10/ma20/ma30 出现多头排列
    set_ma_up_arrange5102030(df)

    # ma5/ma10/ma20/ma30/ma60 出现多头排列
    set_ma_up_arrange510203060(df)

    # ma20/ma30/ma60 出现多头排列
    set_ma_up_arrange203060(df)

    # ma20/ma60/ma120 出现多头排列
    set_ma_up_arrange2060120(df)

    # ema5/ema10/ema20 出现多头排列
    set_ema_up_arrange51020(df)

    # ema5/ema10/ema20/ema30 出现多头排列
    set_ema_up_arrange5102030(df)

    # ema5/ema10/ema20/ema30/ema60 出现多头排列
    set_ema_up_arrange510203060(df)

    # ema20/ema30/ema60 出现多头排列
    set_ema_up_arrange203060(df)

    # ema20/ema60/ema120 出现多头排列
    set_ema_up_arrange2055120(df)


def set_stand_up_ma60(df):
    # 前55个交易日(除最近3个交易日外) 收盘价位于ma60下方
    # 前55个交易日(除最近3个交易日外) ma60向下运行

    arr = []
    for index, row in df.iterrows():
        small_set = df.iloc[index - 55: index - 2]
        pre_row = df.iloc[index - 1]
        before_pre_row = df.iloc[index - 2]
        ma60_down_still = True
        ma60_up_recently = False

        for index_2, row_2 in small_set.iterrows():
            if row_2.close > row_2.ma60 or row_2.ma60_slope >= 0:
                ma60_down_still = False

        # 最近3个交易日收盘价高于 ma60
        # 最近3个交易日 ma60 开始向上
        if row.close > row.ma60 and pre_row.close > pre_row.ma60 and before_pre_row.close > before_pre_row.ma60 \
                and row.ma60_slope > 0 and pre_row.ma60_slope > 0 and before_pre_row.ma60_slope > 0:
            ma60_up_recently = True

        if len(df) > 81 and ma60_down_still and ma60_up_recently:
            arr.insert(index, 1)
        else:
            arr.insert(index, 0)

    df['stand_up_ma60'] = arr


def set_stand_up_ma120(df):
    # 前89个交易日(除最近3个交易日外) 收盘价位于ma120下方
    # 前89个交易日(除最近3个交易日外) ma120向下运行

    arr = []
    for index, row in df.iterrows():
        small_set = df.iloc[index - 89: index - 2]
        pre_row = df.iloc[index - 1]
        before_pre_row = df.iloc[index - 2]
        ma120_down_still = True
        ma120_up_recently = False

        for index_2, row_2 in small_set.iterrows():
            if row_2.close > row_2.ma120 or row_2.ma120_slope > 0:
                ma120_down_still = False

        # 最近3个交易日收盘价高于 ma120
        # 最近3个交易日 ma120 开始向上
        if row.close > row.ma120 and pre_row.close > pre_row.ma120 and before_pre_row.close > before_pre_row.ma120 \
                and row.ma120_slope > 0 and pre_row.ma120_slope > 0 and before_pre_row.ma120_slope > 0:
            ma120_up_recently = True

        if len(df) > 154 and ma120_down_still and ma120_up_recently:
            arr.insert(index, 1)
        else:
            arr.insert(index, 0)

    df['stand_up_ma120'] = arr


def set_stand_up_ema60(df):
    # 前55个交易日(除最近3个交易日外) 收盘价位于 ema60 下方
    # 前55个交易日(除最近3个交易日外) ema60 向下运行

    arr = []
    for index, row in df.iterrows():
        small_set = df.iloc[index - 55: index - 2]
        pre_row = df.iloc[index - 1]
        before_pre_row = df.iloc[index - 2]
        ma60_down_still = True
        ma60_up_recently = False

        for index_2, row_2 in small_set.iterrows():
            if row_2.close > row_2.ema60 or row_2.ema60_slope >= 0:
                ma60_down_still = False

        # 最近3个交易日收盘价高于 ema60
        # 最近3个交易日 ema60 开始向上
        if row.close > row.ema60 and pre_row.close > pre_row.ema60 and before_pre_row.close > before_pre_row.ema60 \
                and row.ema60_slope > 0 and pre_row.ema60_slope > 0 and before_pre_row.ema60_slope > 0:
            ma60_up_recently = True

        if len(df) > 81 and ma60_down_still and ma60_up_recently:
            arr.insert(index, 1)
        else:
            arr.insert(index, 0)

    df['stand_up_ema60'] = arr


def set_stand_up_ema120(df):
    # 前89个交易日(除最近3个交易日外) 收盘价位于ma120下方
    # 前89个交易日(除最近3个交易日外) ma120向下运行

    arr = []
    for index, row in df.iterrows():
        small_set = df.iloc[index - 89: index - 2]
        pre_row = df.iloc[index - 1]
        before_pre_row = df.iloc[index - 2]
        ma120_down_still = True
        ma120_up_recently = False

        for index_2, row_2 in small_set.iterrows():
            if row_2.close > row_2.ma120 or row_2.ma120_slope > 0:
                ma120_down_still = False

        # 最近3个交易日收盘价高于 ma120
        # 最近3个交易日 ma120 开始向上
        if row.close > row.ema120 and pre_row.close > pre_row.ema120 and before_pre_row.close > before_pre_row.ema120 \
                and row.ema120_slope > 0 and pre_row.ema120_slope > 0 and before_pre_row.ema120_slope > 0:
            ma120_up_recently = True

        if len(df) > 154 and ma120_down_still and ma120_up_recently:
            arr.insert(index, 1)
        else:
            arr.insert(index, 0)

    df['stand_up_ema120'] = arr


def is_ma60_steady_up(df, row, index):
    # 最近21个交易日 ma60 稳步向上
    if len(df) > 81 and df['ma60_slope'][index - 20: index].min() > 0:
        return True
    else:
        return False


def is_ma120_steady_up(df, row, index):
    # 最近34个交易日 ma120 稳步向上
    if len(df) > 154 and df['ma120_slope'][index - 33: index].min() > 0:
        return True
    else:
        return False


def is_ema60_steady_up(df, row, index):
    # 最近21个交易日 ma60 稳步向上
    if len(df) > 81 and df['ema60_slope'][index - 20: index].min() > 0:
        return True
    else:
        return False


def is_ema120_steady_up(df, row, index):
    # 最近34个交易日 ma120 稳步向上
    if len(df) > 154 and df['ema120_slope'][index - 33: index].min() > 0:
        return True
    else:
        return False


def set_ma60_support(df):
    ma60_support = []

    for index, row in df.iterrows():
        if stand_on_ma(df, row, 60) and is_ma60_steady_up(df, row, index):
            ma60_support.insert(index, 1)
        else:
            ma60_support.insert(index, 0)

    df['ma60_support'] = ma60_support


def set_ma120_support(df):
    ma120_support = []

    for index, row in df.iterrows():
        if stand_on_ma(df, row, 120) and is_ma120_steady_up(df, row, index):
            ma120_support.insert(index, 1)
        else:
            ma120_support.insert(index, 0)

    df['ma120_support'] = ma120_support


def set_ema60_support(df):
    ema60_support = []

    for index, row in df.iterrows():
        if stand_on_ema(df, row, 60) and is_ema60_steady_up(df, row, index):
            ema60_support.insert(index, 1)
        else:
            ema60_support.insert(index, 0)

    df['ema60_support'] = ema60_support


def set_ema120_support(df):
    ema120_support = []

    for index, row in df.iterrows():
        if stand_on_ema(df, row, 120) and is_ema120_steady_up(df, row, index):
            ema120_support.insert(index, 1)
        else:
            ema120_support.insert(index, 0)

    df['ema120_support'] = ema120_support


def set_yearly_price_position(df):
    yearly_price_position = []

    for index, row in df.iterrows():
        if index >= 260:
            high_price = df['high'][index - 259: index + 1].max()
            low_price = df['low'][index - 259: index + 1].min()
            price_range = high_price - low_price
            price_pct_position = round((row.close - low_price) * 100 / price_range, 1)
            yearly_price_position.insert(index, price_pct_position)
        else:
            yearly_price_position.insert(index, 0)

    df['yearly_price_position'] = yearly_price_position


def set_yearly_price_position10(df):
    yearly_price_position = []

    for index, row in df.iterrows():
        if 10 >= row.yearly_price_position > 0:
            yearly_price_position.insert(index, 1)
        else:
            yearly_price_position.insert(index, 0)

    df['yearly_price_position10'] = yearly_price_position


def set_yearly_price_position20(df):
    yearly_price_position = []

    for index, row in df.iterrows():
        if 20 >= row.yearly_price_position:
            yearly_price_position.insert(index, 1)
        else:
            yearly_price_position.insert(index, 0)

    df['yearly_price_position20'] = yearly_price_position


def set_yearly_price_position30(df):
    yearly_price_position = []

    for index, row in df.iterrows():
        if 30 >= row.yearly_price_position:
            yearly_price_position.insert(index, 1)
        else:
            yearly_price_position.insert(index, 0)

    df['yearly_price_position30'] = yearly_price_position


def set_yearly_price_position50(df):
    yearly_price_position = []

    for index, row in df.iterrows():
        if 50 >= row.yearly_price_position:
            yearly_price_position.insert(index, 1)
        else:
            yearly_price_position.insert(index, 0)

    df['yearly_price_position50'] = yearly_price_position


def set_yearly_price_position70(df):
    yearly_price_position = []

    for index, row in df.iterrows():
        if 70 >= row.yearly_price_position:
            yearly_price_position.insert(index, 1)
        else:
            yearly_price_position.insert(index, 0)

    df['yearly_price_position70'] = yearly_price_position


def set_ma_group_glue(df):
    ma_group_glue = []
    for index, row in df.iterrows():
        # 最近9个交易日 0 <= ma60_slope <= 1
        # 最近9个交易日 0 <= ma30_slope <= 1
        # 最近9个交易日 0 <= ma20_slope <= 1
        # 最近9个交易日 -1.5 < ma10_slope < 1.5
        if df.ma60_slope[index - 8: index + 1].min() >= 0 \
                and df.ma60_slope[index - 8: index + 1].max() <= 1 \
                and df.ma30_slope[index - 8: index + 1].min() >= 0 \
                and df.ma30_slope[index - 8: index + 1].max() <= 1 \
                and df.ma20_slope[index - 8: index + 1].min() >= 0 \
                and df.ma20_slope[index - 8: index + 1].max() < 1 \
                and df.ma10_slope[index - 8: index + 1].min() > -1.5 \
                and df.ma10_slope[index - 8: index + 1].max() < 1.5:
            ma_group_glue.insert(index, 1)
        else:
            ma_group_glue.insert(index, 0)

    df['ma_group_glue'] = ma_group_glue


def set_ema_group_glue(df):
    ema_group_glue = []
    for index, row in df.iterrows():
        # 最近9个交易日 0 <= ma60_slope <= 1
        # 最近9个交易日 0 <= ma30_slope <= 1
        # 最近9个交易日 0 <= ma20_slope <= 1
        # 最近9个交易日 -1.5 < ma10_slope < 1.5
        if df.ema60_slope[index - 8: index + 1].min() >= 0 \
                and df.ema60_slope[index - 8: index + 1].max() <= 1 \
                and df.ema30_slope[index - 8: index + 1].min() >= 0 \
                and df.ema30_slope[index - 8: index + 1].max() <= 1 \
                and df.ema20_slope[index - 8: index + 1].min() >= 0 \
                and df.ema20_slope[index - 8: index + 1].max() <= 1 \
                and df.ema10_slope[index - 8: index + 1].min() > -1.5 \
                and df.ema10_slope[index - 8: index + 1].max() < 1.5:
            ema_group_glue.insert(index, 1)
        else:
            ema_group_glue.insert(index, 0)

    df['ema_group_glue'] = ema_group_glue


def set_ma_up_arrange51020(df):
    # ma5/ma10/ma20 出现多头排列
    ma_up_arrange = []
    for index, row in df.iterrows():
        if index == 0:
            ma_up_arrange.insert(index, 0)
        else:
            pre_row = df.iloc[index - 1]
            # 前一交易日 未形成多头排列
            # 当前交易日 形成多头排列
            if (not (pre_row.ma5 > pre_row.ma10 > pre_row.ma20 and
                     pre_row.ma5_slope > 0 and pre_row.ma10_slope > 0 and pre_row.ma20_slope > 0)) \
                    and row.ma5 > row.ma10 > row.ma20 and row.ma5_slope > 0 and row.ma10_slope > 0 and row.ma20_slope > 0:
                ma_up_arrange.insert(index, 1)
            else:
                ma_up_arrange.insert(index, 0)

    df['ma_up_arrange51020'] = ma_up_arrange


def set_ma_up_arrange5102030(df):
    # ma5/ma10/ma20/ma30 出现多头排列
    ma_up_arrange = []
    for index, row in df.iterrows():
        if index == 0:
            ma_up_arrange.insert(index, 0)
        else:
            pre_row = df.iloc[index - 1]
            # 前一交易日 未形成多头排列
            # 当前交易日 形成多头排列
            if (not (pre_row.ma5 > pre_row.ma10 > pre_row.ma20 > pre_row.ma30 and
                     pre_row.ma5_slope > 0 and pre_row.ma10_slope > 0 and
                     pre_row.ma20_slope > 0 and pre_row.ma30_slope > 0)) \
                    and row.ma5 > row.ma10 > row.ma20 > row.ma30 and \
                    row.ma5_slope > 0 and row.ma10_slope > 0 and row.ma20_slope > 0 and row.ma30_slope > 0:
                ma_up_arrange.insert(index, 1)
            else:
                ma_up_arrange.insert(index, 0)

    df['ma_up_arrange5102030'] = ma_up_arrange


def set_ma_up_arrange510203060(df):
    # ma5/ma10/ma20/ma30/ma60 出现多头排列
    ma_up_arrange = []
    for index, row in df.iterrows():
        if index == 0:
            ma_up_arrange.insert(index, 0)
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
                ma_up_arrange.insert(index, 1)
            else:
                ma_up_arrange.insert(index, 0)

    df['ma_up_arrange510203060'] = ma_up_arrange


def set_ma_up_arrange203060(df):
    # ma20/ma30/ma60 出现多头排列
    ma_up_arrange = []
    for index, row in df.iterrows():
        if index == 0:
            ma_up_arrange.insert(index, 0)
        else:
            pre_row = df.iloc[index - 1]
            # 前一交易日 未形成多头排列
            # 当前交易日 形成多头排列
            if (not (pre_row.ma20 > pre_row.ma30 > pre_row.ma60 and
                     pre_row.ma20_slope > 0 and pre_row.ma30_slope > 0 and row.ma60_slope > 0)) \
                    and row.ma20 > row.ma30 > row.ma60 \
                    and row.ma20_slope > 0 and row.ma30_slope > 0 and row.ma60_slope > 0:
                ma_up_arrange.insert(index, 1)
            else:
                ma_up_arrange.insert(index, 0)

    df['ma_up_arrange203060'] = ma_up_arrange


def set_ma_up_arrange2060120(df):
    # ma20/ma60/ma120 出现多头排列
    ma_up_arrange = []
    for index, row in df.iterrows():
        if index == 0:
            ma_up_arrange.insert(index, 0)
        else:
            pre_row = df.iloc[index - 1]
            # 前一交易日 未形成多头排列
            # 当前交易日 形成多头排列
            if (not (pre_row.ma20 > pre_row.ma60 > pre_row.ma120 and
                     pre_row.ma20_slope > 0 and pre_row.ma60_slope > 0 and row.ma120_slope > 0)) \
                    and row.ma20 > row.ma60 > row.ma120 \
                    and row.ma20_slope > 0 and row.ma60_slope > 0 and row.ma120_slope > 0:
                ma_up_arrange.insert(index, 1)
            else:
                ma_up_arrange.insert(index, 0)

    df['ma_up_arrange2060120'] = ma_up_arrange


def set_ema_up_arrange51020(df):
    # ema5/ema10/ema20 出现多头排列
    ma_up_arrange = []
    for index, row in df.iterrows():
        if index == 0:
            ma_up_arrange.insert(index, 0)
        else:
            pre_row = df.iloc[index - 1]
            # 前一交易日 未形成多头排列
            # 当前交易日 形成多头排列
            if (not (pre_row.ema5 > pre_row.ema10 > pre_row.ema20 and
                     pre_row.ema5_slope > 0 and pre_row.ema10_slope > 0 and pre_row.ema20_slope > 0)) \
                    and row.ema5 > row.ema10 > row.ema20 \
                    and row.ema5_slope > 0 and row.ema10_slope > 0 and row.ema20_slope > 0:
                ma_up_arrange.insert(index, 1)
            else:
                ma_up_arrange.insert(index, 0)

    df['ema_up_arrange51020'] = ma_up_arrange


def set_ema_up_arrange5102030(df):
    # ema5/ema10/ema20/ema30 出现多头排列
    ma_up_arrange = []
    for index, row in df.iterrows():
        if index == 0:
            ma_up_arrange.insert(index, 0)
        else:
            pre_row = df.iloc[index - 1]
            # 前一交易日 未形成多头排列
            # 当前交易日 形成多头排列
            if (not (pre_row.ema5 > pre_row.ema10 > pre_row.ema20 > pre_row.ema30 and
                     pre_row.ema5_slope > 0 and pre_row.ema10_slope > 0 and
                     pre_row.ema20_slope > 0 and pre_row.ema30_slope > 0)) \
                    and row.ema5 > row.ema10 > row.ema20 > row.ema30 and \
                    row.ema5_slope > 0 and row.ema10_slope > 0 and row.ema20_slope > 0 and row.ema30_slope > 0:
                ma_up_arrange.insert(index, 1)
            else:
                ma_up_arrange.insert(index, 0)

    df['ema_up_arrange5102030'] = ma_up_arrange


def set_ema_up_arrange510203060(df):
    # ema5/ema10/ema20/ema30/ema60 出现多头排列
    ma_up_arrange = []
    for index, row in df.iterrows():
        if index == 0:
            ma_up_arrange.insert(index, 0)
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
                ma_up_arrange.insert(index, 1)
            else:
                ma_up_arrange.insert(index, 0)

    df['ema_up_arrange510203060'] = ma_up_arrange


def set_ema_up_arrange203060(df):
    # ema20/ema30/ema60 出现多头排列
    ma_up_arrange = []
    for index, row in df.iterrows():
        if index == 0:
            ma_up_arrange.insert(index, 0)
        else:
            pre_row = df.iloc[index - 1]

            # 前一交易日 未形成多头排列
            # 当前交易日 形成多头排列
            if (not (pre_row.ema20 > pre_row.ema30 > pre_row.ema60 and
                     pre_row.ema20_slope > 0 and pre_row.ema30_slope > 0 and row.ema60_slope > 0)) \
                    and row.ema20 > row.ema30 > row.ema60 \
                    and row.ema20_slope > 0 and row.ema30_slope > 0 and row.ema60_slope > 0:
                ma_up_arrange.insert(index, 1)
            else:
                ma_up_arrange.insert(index, 0)

    df['ema_up_arrange203060'] = ma_up_arrange


def set_ema_up_arrange2055120(df):
    # ema20/ema55/ema120 出现多头排列
    ma_up_arrange = []
    for index, row in df.iterrows():
        if index == 0:
            ma_up_arrange.insert(index, 0)
        else:
            pre_row = df.iloc[index - 1]

            # 前一交易日 未形成多头排列
            # 当前交易日 形成多头排列
            if (not (pre_row.ema20 > pre_row.ema55 > pre_row.ema120 and
                     pre_row.ema20_slope > 0 and pre_row.ema55_slope > 0 and row.ema120_slope > 0)) \
                    and row.ema20 > row.ema55 > row.ema120 \
                    and row.ema20_slope > 0 and row.ema55_slope > 0 and row.ema120_slope > 0:
                ma_up_arrange.insert(index, 1)
            else:
                ma_up_arrange.insert(index, 0)

    df['ema_up_arrange2055120'] = ma_up_arrange
