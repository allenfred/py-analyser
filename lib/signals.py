from talib import SMA
import numpy as np
import math


def long_signals(df):
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

    ma_out_sea = []
    ema_out_sea = []

    ma_hold_moon = []
    ema_hold_moon = []

    ma_over_gate = []
    ema_over_gate = []

    ma_up_group = []
    ema_up_group = []

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

    for index, row in df.iterrows():
        # MA20上行
        if row.ma20_slope > 0:
            ma20_up.insert(index, 1)
        else:
            ma20_up.insert(index, 0)

        # EMA20上行
        if row.ema20_slope > 0:
            ema20_up.insert(index, 1)
        else:
            ema20_up.insert(index, 0)

        # MA30上行
        if row.ma30_slope > 0:
            ma30_up.insert(index, 1)
        else:
            ma30_up.insert(index, 0)

        # EMA30上行
        if row.ema30_slope > 0:
            ema30_up.insert(index, 1)
        else:
            ema30_up.insert(index, 0)

        # MA60上行
        if row.ma60_slope > 0:
            ma60_up.insert(index, 1)
        else:
            ma60_up.insert(index, 0)

        # EMA60上行
        if row.ema60_slope > 0:
            ema60_up.insert(index, 1)
        else:
            ema60_up.insert(index, 0)

        # MA120上行
        if row.ma120_slope > 0:
            ma120_up.insert(index, 1)
        else:
            ma120_up.insert(index, 0)

        # EMA120上行
        if row.ema120_slope > 0:
            ema120_up.insert(index, 1)
        else:
            ema120_up.insert(index, 0)

        # MA多头排列（5/10/20/60）
        if row.ma5_slope > 0 and row.ma10_slope > 0 and row.ma20_slope > 0 and row.ma60_slope > 0 \
                and row.ma5 > row.ma10 > row.ma20 > row.ma60:
            ma_arrange.insert(index, 1)
        else:
            ma_arrange.insert(index, 0)

        # EMA多头排列（5/10/20/60）
        if row.ema5_slope > 0 and row.ema10_slope > 0 and row.ema20_slope > 0 and row.ema60_slope > 0 \
                and row.ema5 > row.ema10 > row.ema20 > row.ema60:
            ema_arrange.insert(index, 1)
        else:
            ema_arrange.insert(index, 0)

        # MA短期组合多头排列（5/10/20）
        if row.ma5_slope > 0 and row.ma10_slope > 0 and row.ma20_slope > 0 \
                and row.ma5 > row.ma10 > row.ma20:
            short_ma_arrange1.insert(index, 1)
        else:
            short_ma_arrange1.insert(index, 0)

        # MA短期组合多头排列（5/10/30）
        if row.ma5_slope > 0 and row.ma10_slope > 0 and row.ma30_slope > 0 \
                and row.ma5 > row.ma10 > row.ma30:
            short_ma_arrange2.insert(index, 1)
        else:
            short_ma_arrange2.insert(index, 0)

        # EMA短期组合多头排列（5/10/20）
        if row.ema5_slope > 0 and row.ema10_slope > 0 and row.ema20_slope > 0 \
                and row.ema5 > row.ema10 > row.ema20:
            short_ema_arrange1.insert(index, 1)
        else:
            short_ema_arrange1.insert(index, 0)

        # EMA短期组合多头排列（5/10/30）
        if row.ema5_slope > 0 and row.ema10_slope > 0 and row.ema30_slope > 0 \
                and row.ema5 > row.ema10 > row.ema30:
            short_ema_arrange2.insert(index, 1)
        else:
            short_ema_arrange2.insert(index, 0)

        # MA中期组合多头排列（10/20/60）
        if row.ma10_slope > 0 and row.ma20_slope > 0 and row.ma60_slope > 0 \
                and row.ma10 > row.ma20 > row.ma60:
            middle_ma_arrange1.insert(index, 1)
        else:
            middle_ma_arrange1.insert(index, 0)

        # MA中期组合多头排列（10/20/55）
        if row.ma10_slope > 0 and row.ma20_slope > 0 and row.ma55_slope > 0 \
                and row.ma10 > row.ma20 > row.ma55:
            middle_ma_arrange2.insert(index, 1)
        else:
            middle_ma_arrange2.insert(index, 0)

        # EMA中期组合多头排列（10/20/60）
        if row.ema10_slope > 0 and row.ema20_slope > 0 and row.ema60_slope > 0 \
                and row.ema10 > row.ema20 > row.ema60:
            middle_ema_arrange1.insert(index, 1)
        else:
            middle_ema_arrange1.insert(index, 0)

        # EMA中期组合多头排列（10/20/55）
        if row.ema10_slope > 0 and row.ema20_slope > 0 and row.ema55_slope > 0 \
                and row.ema10 > row.ema20 > row.ema55:
            middle_ema_arrange2.insert(index, 1)
        else:
            middle_ema_arrange2.insert(index, 0)

        # MA长期组合多头排列（20/55/120）
        if row.ma20_slope > 0 and row.ma55_slope > 0 and row.ma120_slope > 0 \
                and row.ma20 > row.ma55 > row.ma120:
            long_ma_arrange1.insert(index, 1)
        else:
            long_ma_arrange1.insert(index, 0)

        # MA长期组合多头排列（30/60/120）
        if row.ma30_slope > 0 and row.ma60_slope > 0 and row.ma120_slope > 0 \
                and row.ma30 > row.ma60 > row.ma120:
            long_ma_arrange2.insert(index, 1)
        else:
            long_ma_arrange2.insert(index, 0)

        # EMA长期组合多头排列（20/55/120）
        if row.ema20_slope > 0 and row.ema55_slope > 0 and row.ema120_slope > 0 \
                and row.ema20 > row.ema55 > row.ema120:
            long_ema_arrange1.insert(index, 1)
        else:
            long_ema_arrange1.insert(index, 0)

        # EMA长期组合多头排列（30/60/120）
        if row.ema30_slope > 0 and row.ema60_slope > 0 and row.ema120_slope > 0 \
                and row.ema30 > row.ema60 > row.ema120:
            long_ema_arrange2.insert(index, 1)
        else:
            long_ema_arrange2.insert(index, 0)

        # MA黄金交叉（5/10）
        if is_ma_gold_cross1(df, row, index):
            ma_gold_cross1.insert(index, 1)
        else:
            ma_gold_cross1.insert(index, 0)

        # MA黄金交叉（5/20）
        if is_ma_gold_cross2(df, row, index):
            ma_gold_cross2.insert(index, 1)
        else:
            ma_gold_cross2.insert(index, 0)

        # MA黄金交叉（10/20）
        if is_ma_gold_cross3(df, row, index):
            ma_gold_cross3.insert(index, 1)
        else:
            ma_gold_cross3.insert(index, 0)

        # MA黄金交叉（10/30）
        if is_ma_gold_cross4(df, row, index):
            ma_gold_cross4.insert(index, 1)
        else:
            ma_gold_cross4.insert(index, 0)

        # EMA黄金交叉（5/10）
        if is_ema_gold_cross1(df, row, index):
            ema_gold_cross1.insert(index, 1)
        else:
            ema_gold_cross1.insert(index, 0)

        # EMA黄金交叉（5/20）
        if is_ema_gold_cross2(df, row, index):
            ema_gold_cross2.insert(index, 1)
        else:
            ema_gold_cross2.insert(index, 0)

        # EMA黄金交叉（10/20）
        if is_ema_gold_cross3(df, row, index):
            ema_gold_cross3.insert(index, 1)
        else:
            ema_gold_cross3.insert(index, 0)

        # EMA黄金交叉（10/30）
        if is_ema_gold_cross4(df, row, index):
            ema_gold_cross4.insert(index, 1)
        else:
            ema_gold_cross4.insert(index, 0)

        # MA蛟龙出海(5/10/20)
        if is_ma_out_sea(row):
            ma_out_sea.insert(index, 1)
        else:
            ma_out_sea.insert(index, 0)

        # EMA蛟龙出海(5/10/20)
        if is_ema_out_sea(row):
            ema_out_sea.insert(index, 1)
        else:
            ema_out_sea.insert(index, 0)

        # MA烘云托月(5/10/20)
        if is_ma_hold_moon(df, row, index):
            ma_hold_moon.insert(index, 1)
        else:
            ma_hold_moon.insert(index, 0)

        # EMA烘云托月(5/10/20)
        if is_ema_hold_moon(df, row, index):
            ema_hold_moon.insert(index, 1)
        else:
            ema_hold_moon.insert(index, 0)

        # MA鱼跃龙门(5/10/20)
        if is_ma_over_gate(df, row, index):
            ma_over_gate.insert(index, 1)
        else:
            ma_over_gate.insert(index, 0)

        # EMA鱼跃龙门(5/10/20)
        if is_ema_over_gate(df, row, index):
            ema_over_gate.insert(index, 1)
        else:
            ema_over_gate.insert(index, 0)

        # MA旱地拔葱(5/10/20)
        if is_ma_up_group(df, row, index):
            ma_up_group.insert(index, 1)
        else:
            ma_up_group.insert(index, 0)

        # EMA旱地拔葱(5/10/20)
        if is_ema_up_group(df, row, index):
            ema_up_group.insert(index, 1)
        else:
            ema_up_group.insert(index, 0)

        # MA均线粘合(5/10/20)
        if is_ma_glue(df, row, index):
            ma_glue.insert(index, 1)
        else:
            ma_glue.insert(index, 0)

        # EMA均线粘合(5/10/20)
        if is_ema_glue(df, row, index):
            ema_glue.insert(index, 1)
        else:
            ema_glue.insert(index, 0)

        # TD_8
        if row.low_td == 8:
            td8.insert(index, 1)
        else:
            td8.insert(index, 0)

        # TD_9
        if row.low_td == 9:
            td9.insert(index, 1)
        else:
            td9.insert(index, 0)

        # bias6
        if row.bias6 < -3:
            bias6.insert(index, 1)
        else:
            bias6.insert(index, 0)

        # bias12
        if row.bias12 < -4.5:
            bias12.insert(index, 1)
        else:
            bias12.insert(index, 0)

        # bias24
        if row.bias24 < -7:
            bias24.insert(index, 1)
        else:
            bias24.insert(index, 0)

        # bias72
        if row.bias72 < -11:
            bias72.insert(index, 1)
        else:
            bias72.insert(index, 0)

        # bias60 不作为单独信号 需结合趋势判断上涨回踩形态
        if 1.5 >= row.bias60 >= -1.5:
            bias60.insert(index, 1)
        else:
            bias60.insert(index, 0)

        # bias120 不作为单独信号 需结合趋势判断上涨回踩形态
        if 1 >= row.bias120 >= -1:
            bias120.insert(index, 1)
        else:
            bias120.insert(index, 0)

    df['ma20_up'] = ma20_up
    df['ema20_up'] = ema20_up
    df['ma30_up'] = ma30_up
    df['ema30_up'] = ema30_up
    df['ma60_up'] = ma60_up
    df['ema60_up'] = ema60_up
    df['ma120_up'] = ma120_up
    df['ema120_up'] = ema120_up
    df['ma_arrange'] = ma_arrange
    df['ema_arrange'] = ema_arrange

    df['short_ma_arrange1'] = short_ma_arrange1
    df['short_ma_arrange2'] = short_ma_arrange2
    df['short_ema_arrange1'] = short_ema_arrange1
    df['short_ema_arrange2'] = short_ema_arrange2

    df['middle_ma_arrange1'] = middle_ma_arrange1
    df['middle_ma_arrange2'] = middle_ma_arrange2
    df['middle_ema_arrange1'] = middle_ema_arrange1
    df['middle_ema_arrange2'] = middle_ema_arrange2

    df['long_ma_arrange1'] = long_ma_arrange1
    df['long_ma_arrange2'] = long_ma_arrange2
    df['long_ema_arrange1'] = long_ema_arrange1
    df['long_ema_arrange2'] = long_ema_arrange2

    df['ma_gold_cross1'] = ma_gold_cross1
    df['ma_gold_cross2'] = ma_gold_cross2
    df['ma_gold_cross3'] = ma_gold_cross3
    df['ma_gold_cross4'] = ma_gold_cross4
    df['ema_gold_cross1'] = ema_gold_cross1
    df['ema_gold_cross2'] = ema_gold_cross2
    df['ema_gold_cross3'] = ema_gold_cross3
    df['ema_gold_cross4'] = ema_gold_cross4

    df['ma_glue'] = ma_glue
    df['ema_glue'] = ema_glue
    df['ma_out_sea'] = ma_out_sea
    df['ema_out_sea'] = ema_out_sea
    df['ma_hold_moon'] = ma_hold_moon
    df['ema_hold_moon'] = ema_hold_moon
    df['ma_over_gate'] = ma_over_gate
    df['ema_over_gate'] = ema_over_gate
    df['ma_up_group'] = ma_up_group
    df['ema_up_group'] = ema_up_group

    df['td8'] = td8
    df['td9'] = td9

    df['bias6'] = bias6
    df['bias12'] = bias12
    df['bias24'] = bias24
    df['bias60'] = bias60
    df['bias72'] = bias72
    df['bias120'] = bias120

    set_ma_silver_valley(df)
    set_ema_silver_valley(df)
    set_ma_gold_valley(df)
    set_ema_gold_valley(df)

    # MA金蜘蛛(5/10/20)
    set_ma_spider(df)
    # MA金蜘蛛(5/10/20/30)
    set_ma_spider2(df)
    # EMA金蜘蛛(5/10/20)
    set_ema_spider(df)
    # EMA金蜘蛛(5/10/20/30)
    set_ema_spider2(df)

    # print(math.max(df['td8']))
    # print(df['ma_silver_valley'][50:100].max())
    # print('silver valley')
    # print(df['ma_silver_valley'].to_numpy())
    # print('gold valley')
    # print(df['ma_gold_valley'].to_numpy())


def is_ma_glue(df, row, index):
    # 最近9个交易日 0 <= ma20_slope <= 1
    # 最近9个交易日 -1.5 < ma10_slope < 1.5
    # 最近9个交易日 -1.5 < ma5_slope < 1.5
    if df.ma20_slope[index - 8: index + 1].min() >= 0 and df.ma20_slope[index - 8: index + 1].max() <= 1 and \
            df.ma5_slope[index - 8: index + 1].min() > -1.5 and df.ma5_slope[index - 8: index + 1].max() < 1.5 and \
            df.ma10_slope[index - 8: index + 1].min() > -1.5 and df.ma10_slope[index - 8: index + 1].max() < 1.5:
        return True
    else:
        return False


def is_ema_glue(df, row, index):
    # 最近9个交易日 0 <= ema20_slope <= 1
    # 最近9个交易日 -1.5 < ema10_slope < 1.5
    # 最近9个交易日 -1.5 < ema5_slope < 1.5
    if df.ema20_slope[index - 8: index + 1].min() >= 0 and df.ema20_slope[index - 8: index + 1].max() <= 1 and \
            df.ema5_slope[index - 8: index + 1].min() > -1.5 and df.ema5_slope[index - 8: index + 1].max() < 1.5 and \
            df.ema10_slope[index - 8: index + 1].min() > -1.5 and df.ema10_slope[index - 8: index + 1].max() < 1.5:
        return True
    else:
        return False


def is_ma_up_group(df, row, index):
    # 大阳线
    # 跳空阳线
    # K线站上ma5/ma10/ma20
    # 昨日K线未站上ma5/ma10/ma20
    if row.pct_chg and row.pct_chg >= 4 and \
            row.low > df.iloc[index - 1].high and \
            row.close > row.ma5 and row.close > row.ma10 and row.close > row.ma20 and \
            (df.iloc[index - 1].low < df.iloc[index - 1].ma5 or
             df.iloc[index - 1].low < df.iloc[index - 1].ma10 or
             df.iloc[index - 1].low < df.iloc[index - 1].ma20) and \
            (df.iloc[index - 1].open < df.iloc[index - 1].ma20 or
             df.iloc[index - 1].close < df.iloc[index - 1].ma20):
        return True
    else:
        return False


def is_ema_up_group(df, row, index):
    # 大阳线
    # 跳空阳线
    # K线站上ema5/ema10/ema20
    # 昨日K线未站上ema5/ema10/ema20
    if row.pct_chg and row.pct_chg >= 4 and \
            row.close > row.ema5 and row.close > row.ema10 and row.close > row.ema20 and \
            row.low > df.iloc[index - 1].high and \
            df.iloc[index - 1].low < df.iloc[index - 1].ema20 and \
            (df.iloc[index - 1].low < df.iloc[index - 1].ema5 or
             df.iloc[index - 1].low < df.iloc[index - 1].ema10 or
             df.iloc[index - 1].low < df.iloc[index - 1].ema20) and \
            (df.iloc[index - 1].open < df.iloc[index - 1].ema20 or
             df.iloc[index - 1].close < df.iloc[index - 1].ema20):
        return True
    else:
        return False


def is_ma_over_gate(df, row, index):
    pre_row = df.iloc[index - 1]

    # 大阳线
    # K线站上ma5/ma10/ma20
    # 昨日K线未站上ma5/ma10/ma20
    # 昨日出现均线粘合
    if row.pct_chg and row.pct_chg >= 4 and \
            row.close > row.ma5 and row.close > row.ma10 and row.close > row.ma20 and \
            (pre_row.low < pre_row.ma5 or pre_row.low < pre_row.ma10 or pre_row.low < pre_row.ma20) and \
            pre_row.ma20_slope > 0 and pre_row.ma5 > pre_row.ma20 and pre_row.ma10 > pre_row.ma20:
        return True
    else:
        return False


def is_ema_over_gate(df, row, index):
    pre_row = df.iloc[index - 1]
    # 大阳线
    # K线站上ema5/ema10/ema20
    # 昨日K线未站上ema5/ema10/ema20
    # 昨日出现均线粘合
    if row.pct_chg and row.pct_chg >= 4 and \
            row.close > row.ema5 and row.close > row.ema10 and row.close > row.ema20 and \
            (pre_row.low < pre_row.ema5 or pre_row.low < pre_row.ema10 or pre_row.low < pre_row.ema20) and \
            pre_row.ema20_slope > 0 and pre_row.ema5 > pre_row.ema20 and pre_row.ema10 > pre_row.ema20:
        return True
    else:
        return False


def is_ma_hold_moon(df, row, index):
    # ma20 下方支撑
    def ma_hold(item):
        if item.ma5 > item.ma20 and item.ma10 > item.ma20 and item.ma5_slope < 5 and item.ma10_slope < 5:
            return True
        return False

    # 过滤掉前20根K线
    # 最近9个交易日不能有波动大于3%
    # 最近9个交易日 ma20向上
    # 最近9个交易日 ma5/ma10 在ma20之上
    # ma5/ma10/ma20 某种程度上粘合
    if index > 20 and df.pct_chg[index - 8: index + 1].min() >= -3 and df.pct_chg[index - 8: index + 1].max() <= 3 \
            and df.ma20_slope[index - 8: index + 1].min() > 0 \
            and df.ma20_slope[index - 8: index + 1].max() <= 3 and \
            ma_hold(row) and ma_hold(df.iloc[index - 1]) and ma_hold(df.iloc[index - 2]) \
            and ma_hold(df.iloc[index - 3]) and ma_hold(df.iloc[index - 4]) \
            and ma_hold(df.iloc[index - 5]) and ma_hold(df.iloc[index - 6]) \
            and ma_hold(df.iloc[index - 7]) and ma_hold(df.iloc[index - 8]):
        return True
    else:
        return False


def is_ema_hold_moon(df, row, index):
    # ema20 下方支撑
    def ma_hold(item):
        if item.ema5 > item.ema20 and item.ema10 > item.ema20 and item.ema5_slope < 5 and item.ema10_slope < 5:
            return True
        return False

    # 过滤掉前20根K线
    # 最近9个交易日不能有波动大于3%
    # 最近9个交易日 ema20向上
    # 最近9个交易日 ema5/ema10 在ema20之上
    # ema5/ema10/ema20 某种程度上粘合
    if index > 20 and df.pct_chg[index - 8: index + 1].min() >= -3 and df.pct_chg[index - 8: index + 1].max() <= 3 \
            and df.ema20_slope[index - 8: index + 1].min() > 0 \
            and df.ema20_slope[index - 8: index + 1].max() <= 3 and \
            ma_hold(row) and ma_hold(df.iloc[index - 1]) and ma_hold(df.iloc[index - 2]) \
            and ma_hold(df.iloc[index - 3]) and ma_hold(df.iloc[index - 4]) \
            and ma_hold(df.iloc[index - 5]) and ma_hold(df.iloc[index - 6]) \
            and ma_hold(df.iloc[index - 7]) and ma_hold(df.iloc[index - 8]):
        return True
    else:
        return False


def is_ma_out_sea(row):
    # 大阳线 贯穿ma5/ma10/ma20
    # ma20 上行
    if row.pct_chg and row.pct_chg >= 4 and \
            row.open < row.ma5 and row.open < row.ma10 and row.open < row.ma20 and \
            row.close > row.ma5 and row.close > row.ma10 and row.close > row.ma20 and \
            row.ma60_slope > 0:
        return True
    else:
        return False


def is_ema_out_sea(row):
    # 大阳线 贯穿ema5/ema10/ema20
    # ema20/ema60 上行
    if row.pct_chg and row.pct_chg >= 4 and \
            row.open < row.ema5 and row.open < row.ema10 and row.open < row.ema20 and \
            row.close > row.ema5 and row.close > row.ema10 and row.close > row.ema20 and \
            row.ema60_slope > 0:
        return True
    else:
        return False


def is_ma_gold_cross1(df, row, index):
    # ma5上穿ma10
    # ma5/ma10上行
    if row.ma5 > row.ma10 and df.iloc[index - 1].ma5 < df.iloc[index - 1].ma10 and \
            row.ma5_slope > 0 and row.ma10_slope > 0:
        return True
    else:
        return False


def is_ma_gold_cross2(df, row, index):
    # ma5上穿ma20
    # ma5/ma20上行
    if row.ma5 > row.ma20 and df.iloc[index - 1].ma5 < df.iloc[index - 1].ma20 and \
            row.ma5_slope > 0 and row.ma20_slope > 0:
        return True
    else:
        return False


def is_ma_gold_cross3(df, row, index):
    # ma10上穿ma20
    # ma10/ma20上行
    if row.ma10 > row.ma20 and df.iloc[index - 1].ma10 < df.iloc[index - 1].ma20 and \
            row.ma10_slope > 0 and row.ma20_slope > 0:
        return True
    else:
        return False


def is_ma_gold_cross4(df, row, index):
    # ma10上穿ma30
    # ma10/ma30上行
    if row.ma10 > row.ma30 and df.iloc[index - 1].ma10 < df.iloc[index - 1].ma30 and \
            row.ma10_slope > 0 and row.ma30_slope > 0:
        return True
    else:
        return False


def is_ema_gold_cross1(df, row, index):
    # ema5上穿ema10
    # ema5/ema10上行
    if row.ema5 > row.ema10 and df.iloc[index - 1].ema5 < df.iloc[index - 1].ema10 and \
            row.ema5_slope > 0 and row.ema10_slope > 0:
        return True
    else:
        return False


def is_ema_gold_cross2(df, row, index):
    # ema5上穿ema20
    # ema5/ema20上行
    if row.ema5 > row.ema20 and df.iloc[index - 1].ema5 < df.iloc[index - 1].ema20 and \
            row.ema5_slope > 0 and row.ema20_slope > 0:
        return True
    else:
        return False


def is_ema_gold_cross3(df, row, index):
    # ema10上穿ema20
    # ema10/ema20上行
    if row.ema10 > row.ema20 and df.iloc[index - 1].ema10 < df.iloc[index - 1].ema20 and \
            row.ema10_slope > 0 and row.ema20_slope > 0:
        return True
    else:
        return False


def is_ema_gold_cross4(df, row, index):
    # ema10上穿ema30
    # ema10/ema30上行
    if row.ema10 > row.ema30 and df.iloc[index - 1].ema10 < df.iloc[index - 1].ema30 and \
            row.ema10_slope > 0 and row.ema30_slope > 0:
        return True
    else:
        return False


def set_ma_silver_valley(df):
    ma_silver_valley = []

    for index, row in df.iterrows():
        if index >= 10 and (row.ma_gold_cross2 == 1 or row.ma_gold_cross3 == 1):
            gold_cross_cnt = 0
            if df['ma_gold_cross1'][index - 9: index + 1].max() == 1:
                gold_cross_cnt += 1
            if df['ma_gold_cross2'][index - 9: index + 1].max() == 1:
                gold_cross_cnt += 1
            if df['ma_gold_cross3'][index - 9: index + 1].max() == 1:
                gold_cross_cnt += 1

            if gold_cross_cnt >= 2:
                ma_silver_valley.insert(index, 1)
            else:
                ma_silver_valley.insert(index, 0)
        else:
            ma_silver_valley.insert(index, 0)

    df['ma_silver_valley'] = ma_silver_valley


def set_ema_silver_valley(df):
    ema_silver_valley = []

    for index, row in df.iterrows():
        if index >= 10 and (row.ema_gold_cross2 == 1 or row.ema_gold_cross3 == 1):
            gold_cross_cnt = 0
            if df['ema_gold_cross1'][index - 9: index + 1].max() == 1:
                gold_cross_cnt += 1
            if df['ema_gold_cross2'][index - 9: index + 1].max() == 1:
                gold_cross_cnt += 1
            if df['ema_gold_cross3'][index - 9: index + 1].max() == 1:
                gold_cross_cnt += 1

            if gold_cross_cnt >= 2:
                ema_silver_valley.insert(index, 1)
            else:
                ema_silver_valley.insert(index, 0)
        else:
            ema_silver_valley.insert(index, 0)

    df['ema_silver_valley'] = ema_silver_valley


def set_ma_gold_valley(df):
    ma_gold_valley = []

    for index, row in df.iterrows():
        # 最近30个交易日内形成两次银山谷 视为 金山谷
        if index >= 30 and df['ma_silver_valley'][index - 29: index - 1].max() == 1 and \
                row.ma_silver_valley == 1 and df.iloc[index - 30].ma20 < row.ma20 and row.ma20_slope > 0:
            ma_gold_valley.insert(index, 1)
        else:
            ma_gold_valley.insert(index, 0)

    df['ma_gold_valley'] = ma_gold_valley


def set_ema_gold_valley(df):
    ema_gold_valley = []

    for index, row in df.iterrows():
        # 最近30个交易日内形成两次银山谷 视为 金山谷
        if index >= 30 and df['ema_silver_valley'][index - 29: index - 1].max() == 1 and \
                row.ema_silver_valley == 1 and df.iloc[index - 30].ema20 < row.ema20 and row.ema20_slope > 0:
            ema_gold_valley.insert(index, 1)
        else:
            ema_gold_valley.insert(index, 0)

    df['ema_gold_valley'] = ema_gold_valley


def set_ma_spider(df):
    ma_spider = []

    for index, row in df.iterrows():
        # 最近3个交易日ma5/ma10/ma20交叉于一点 (即出现至少2个金叉)
        # 今日ma5/ma10/ma20多头发散
        gold_cross_cnt = 0
        if df['ma_gold_cross1'][index - 2: index + 1].max() == 1:
            gold_cross_cnt += 1
        if df['ma_gold_cross2'][index - 2: index + 1].max() == 1:
            gold_cross_cnt += 1
        if df['ma_gold_cross3'][index - 2: index + 1].max() == 1:
            gold_cross_cnt += 1

        if gold_cross_cnt > 1 and row.ma5 > row.ma10 > row.ma20:
            ma_spider.insert(index, 1)
        else:
            ma_spider.insert(index, 0)

    df['ma_spider'] = ma_spider


def set_ma_spider2(df):
    ma_spider2 = []

    for index, row in df.iterrows():
        # 最近3个交易日 ma5/ma10/ma20/ma30 交叉于一点 (即出现至少3个金叉)
        # 今日 ma5/ma10/ma20/ma30 多头发散
        gold_cross_cnt = 0
        if df['ma_gold_cross1'][index - 2: index + 1].max() == 1:
            gold_cross_cnt += 1
        if df['ma_gold_cross2'][index - 2: index + 1].max() == 1:
            gold_cross_cnt += 1
        if df['ma_gold_cross3'][index - 2: index + 1].max() == 1:
            gold_cross_cnt += 1
        if df['ma_gold_cross4'][index - 2: index + 1].max() == 1:
            gold_cross_cnt += 1

        if gold_cross_cnt > 2 and row.ma5 > row.ma10 > row.ma20 > row.ma30:
            ma_spider2.insert(index, 1)
        else:
            ma_spider2.insert(index, 0)

    df['ma_spider2'] = ma_spider2


def set_ema_spider(df):
    ema_spider = []

    for index, row in df.iterrows():
        # 最近3个交易日ema5/ema10/ema20交叉于一点 (即出现至少2个金叉)
        # 今日ema5/ema10/ema20多头发散
        gold_cross_cnt = 0
        if df['ema_gold_cross1'][index - 2: index + 1].max() == 1:
            gold_cross_cnt += 1
        if df['ema_gold_cross2'][index - 2: index + 1].max() == 1:
            gold_cross_cnt += 1
        if df['ema_gold_cross3'][index - 2: index + 1].max() == 1:
            gold_cross_cnt += 1

        if gold_cross_cnt > 1 and row.ema5 > row.ema10 > row.ema20:
            ema_spider.insert(index, 1)
        else:
            ema_spider.insert(index, 0)

    df['ema_spider'] = ema_spider


def set_ema_spider2(df):
    ema_spider2 = []

    for index, row in df.iterrows():
        # 最近3个交易日 ema5/ema10/ema20/ema30 交叉于一点 (即出现至少3个金叉)
        # 今日 ema5/ema10/ema20/ema30 多头发散
        gold_cross_cnt = 0
        if df['ema_gold_cross1'][index - 2: index + 1].max() == 1:
            gold_cross_cnt += 1
        if df['ema_gold_cross2'][index - 2: index + 1].max() == 1:
            gold_cross_cnt += 1
        if df['ema_gold_cross3'][index - 2: index + 1].max() == 1:
            gold_cross_cnt += 1
        if df['ema_gold_cross4'][index - 2: index + 1].max() == 1:
            gold_cross_cnt += 1

        if gold_cross_cnt > 2 and row.ema5 > row.ema10 > row.ema20 > row.ema30:
            ema_spider2.insert(index, 1)
        else:
            ema_spider2.insert(index, 0)

    df['ema_spider2'] = ema_spider2
