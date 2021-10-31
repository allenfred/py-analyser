from talib import SMA
import numpy as np
import math


def long_signals(df):
    ma30_up = []
    ema30_up = []
    ma60_up = []
    ema60_up = []
    ma120_up = []
    ema120_up = []

    ma_arrange = []
    ema_arrange = []

    short_ma_arrange_1 = []
    short_ma_arrange_2 = []
    short_ema_arrange_1 = []
    short_ema_arrange_2 = []

    middle_ma_arrange_1 = []
    middle_ma_arrange_2 = []
    middle_ema_arrange_1 = []
    middle_ema_arrange_2 = []

    long_ma_arrange_1 = []
    long_ma_arrange_2 = []
    long_ema_arrange_1 = []
    long_ema_arrange_2 = []

    ma_gold_cross_1 = []
    ma_gold_cross_2 = []
    ma_gold_cross_3 = []
    ema_gold_cross_1 = []
    ema_gold_cross_2 = []
    ema_gold_cross_3 = []

    ma_out_sea = []
    ema_out_sea = []

    ma_hold_moon = []
    ema_hold_moon = []

    ma_over_gate = []
    ema_over_gate = []

    ma_up_group = []
    ema_up_group = []

    ma_spider = []
    ma_spider_2 = []
    ema_spider = []
    ema_spider_2 = []

    td8 = []
    td9 = []

    for index, row in df.iterrows():
        # MA30上行
        if row.ma30_slope > 0:
            ma30_up.insert(len(df) - index - 1, 1)
        else:
            ma30_up.insert(len(df) - index - 1, 0)

        # EMA30上行
        if row.ema30_slope > 0:
            ema30_up.insert(len(df) - index - 1, 1)
        else:
            ema30_up.insert(len(df) - index - 1, 0)

        # MA60上行
        if row.ma60_slope > 0:
            ma60_up.insert(len(df) - index - 1, 1)
        else:
            ma60_up.insert(len(df) - index - 1, 0)

        # EMA60上行
        if row.ema60_slope > 0:
            ema60_up.insert(len(df) - index - 1, 1)
        else:
            ema60_up.insert(len(df) - index - 1, 0)

        # MA120上行
        if row.ma120_slope > 0:
            ma120_up.insert(len(df) - index - 1, 1)
        else:
            ma120_up.insert(len(df) - index - 1, 0)

        # EMA120上行
        if row.ema120_slope > 0:
            ema120_up.insert(len(df) - index - 1, 1)
        else:
            ema120_up.insert(len(df) - index - 1, 0)

        # MA多头排列（5/10/20/60）
        if row.ma5_slope > 0 and row.ma10_slope > 0 and row.ma20_slope > 0 and row.ma60_slope > 0 \
                and row.ma5 > row.ma10 > row.ma20 > row.ma60:
            ma_arrange.insert(len(df) - index - 1, 1)
        else:
            ma_arrange.insert(len(df) - index - 1, 0)

        # EMA多头排列（5/10/20/60）
        if row.ema5_slope > 0 and row.ema10_slope > 0 and row.ema20_slope > 0 and row.ema60_slope > 0 \
                and row.ema5 > row.ema10 > row.ema20 > row.ema60:
            ema_arrange.insert(len(df) - index - 1, 1)
        else:
            ema_arrange.insert(len(df) - index - 1, 0)

        # MA短期组合多头排列（5/10/20）
        if row.ma5_slope > 0 and row.ma10_slope > 0 and row.ma20_slope > 0 \
                and row.ma5 > row.ma10 > row.ma20:
            short_ma_arrange_1.insert(len(df) - index - 1, 1)
        else:
            short_ma_arrange_1.insert(len(df) - index - 1, 0)

        # MA短期组合多头排列（5/10/30）
        if row.ma5_slope > 0 and row.ma10_slope > 0 and row.ma30_slope > 0 \
                and row.ma5 > row.ma10 > row.ma30:
            short_ma_arrange_2.insert(len(df) - index - 1, 1)
        else:
            short_ma_arrange_2.insert(len(df) - index - 1, 0)

        # EMA短期组合多头排列（5/10/20）
        if row.ema5_slope > 0 and row.ema10_slope > 0 and row.ema20_slope > 0 \
                and row.ema5 > row.ema10 > row.ema20:
            short_ema_arrange_1.insert(len(df) - index - 1, 1)
        else:
            short_ema_arrange_1.insert(len(df) - index - 1, 0)

        # EMA短期组合多头排列（5/10/30）
        if row.ema5_slope > 0 and row.ema10_slope > 0 and row.ema30_slope > 0 \
                and row.ema5 > row.ema10 > row.ema30:
            short_ema_arrange_2.insert(len(df) - index - 1, 1)
        else:
            short_ema_arrange_2.insert(len(df) - index - 1, 0)

        # MA中期组合多头排列（10/20/60）
        if row.ma10_slope > 0 and row.ma20_slope > 0 and row.ma60_slope > 0 \
                and row.ma10 > row.ma20 > row.ma60:
            middle_ma_arrange_1.insert(len(df) - index - 1, 1)
        else:
            middle_ma_arrange_1.insert(len(df) - index - 1, 0)

        # MA中期组合多头排列（10/20/55）
        if row.ma10_slope > 0 and row.ma20_slope > 0 and row.ma55_slope > 0 \
                and row.ma10 > row.ma20 > row.ma55:
            middle_ma_arrange_2.insert(len(df) - index - 1, 1)
        else:
            middle_ma_arrange_2.insert(len(df) - index - 1, 0)

        # EMA中期组合多头排列（10/20/60）
        if row.ema10_slope > 0 and row.ema20_slope > 0 and row.ema60_slope > 0 \
                and row.ema10 > row.ema20 > row.ema60:
            middle_ema_arrange_1.insert(len(df) - index - 1, 1)
        else:
            middle_ema_arrange_1.insert(len(df) - index - 1, 0)

        # EMA中期组合多头排列（10/20/55）
        if row.ema10_slope > 0 and row.ema20_slope > 0 and row.ema55_slope > 0 \
                and row.ema10 > row.ema20 > row.ema55:
            middle_ema_arrange_2.insert(len(df) - index - 1, 1)
        else:
            middle_ema_arrange_2.insert(len(df) - index - 1, 0)

        # MA长期组合多头排列（20/55/120）
        if row.ma20_slope > 0 and row.ma55_slope > 0 and row.ma120_slope > 0 \
                and row.ma20 > row.ma55 > row.ma120:
            long_ma_arrange_1.insert(len(df) - index - 1, 1)
        else:
            long_ma_arrange_1.insert(len(df) - index - 1, 0)

        # MA长期组合多头排列（30/60/120）
        if row.ma30_slope > 0 and row.ma60_slope > 0 and row.ma120_slope > 0 \
                and row.ma30 > row.ma60 > row.ma120:
            long_ma_arrange_2.insert(len(df) - index - 1, 1)
        else:
            long_ma_arrange_2.insert(len(df) - index - 1, 0)

        # EMA长期组合多头排列（20/55/120）
        if row.ema20_slope > 0 and row.ema55_slope > 0 and row.ema120_slope > 0 \
                and row.ema20 > row.ema55 > row.ema120:
            long_ema_arrange_1.insert(len(df) - index - 1, 1)
        else:
            long_ema_arrange_1.insert(len(df) - index - 1, 0)

        # EMA长期组合多头排列（30/60/120）
        if row.ema30_slope > 0 and row.ema60_slope > 0 and row.ema120_slope > 0 \
                and row.ema30 > row.ema60 > row.ema120:
            long_ema_arrange_2.insert(len(df) - index - 1, 1)
        else:
            long_ema_arrange_2.insert(len(df) - index - 1, 0)

        # MA黄金交叉（5/10）
        if is_ma_gold_cross_1(df, row, index):
            ma_gold_cross_1.insert(len(df) - index - 1, 1)
        else:
            ma_gold_cross_1.insert(len(df) - index - 1, 0)

        # MA黄金交叉（10/20）
        if is_ma_gold_cross_2(df, row, index):
            ma_gold_cross_2.insert(len(df) - index - 1, 1)
        else:
            ma_gold_cross_2.insert(len(df) - index - 1, 0)

        # MA黄金交叉（10/30）
        if is_ma_gold_cross_3(df, row, index):
            ma_gold_cross_3.insert(len(df) - index - 1, 1)
        else:
            ma_gold_cross_3.insert(len(df) - index - 1, 0)

        # EMA黄金交叉（5/10）
        if is_ema_gold_cross_1(df, row, index):
            ema_gold_cross_1.insert(len(df) - index - 1, 1)
        else:
            ema_gold_cross_1.insert(len(df) - index - 1, 0)

        # EMA黄金交叉（10/20）
        if is_ema_gold_cross_2(df, row, index):
            ema_gold_cross_2.insert(len(df) - index - 1, 1)
        else:
            ema_gold_cross_2.insert(len(df) - index - 1, 0)

        # EMA黄金交叉（10/30）
        if is_ema_gold_cross_3(df, row, index):
            ema_gold_cross_3.insert(len(df) - index - 1, 1)
        else:
            ema_gold_cross_3.insert(len(df) - index - 1, 0)

        # MA蛟龙出海(5/10/20)
        if is_ma_out_sea(row):
            ma_out_sea.insert(len(df) - index - 1, 1)
        else:
            ma_out_sea.insert(len(df) - index - 1, 0)

        # EMA蛟龙出海(5/10/20)
        if is_ema_out_sea(row):
            ema_out_sea.insert(len(df) - index - 1, 1)
        else:
            ema_out_sea.insert(len(df) - index - 1, 0)

        # MA烘云托月(5/10/20)
        if is_ma_hold_moon(df, row, index):
            ma_hold_moon.insert(len(df) - index - 1, 1)
        else:
            ma_hold_moon.insert(len(df) - index - 1, 0)

        # EMA烘云托月(5/10/20)
        if is_ema_hold_moon(df, row, index):
            ema_hold_moon.insert(len(df) - index - 1, 1)
        else:
            ema_hold_moon.insert(len(df) - index - 1, 0)

        # MA鱼跃龙门(5/10/20)
        if is_ma_over_gate(df, row, index):
            ma_over_gate.insert(len(df) - index - 1, 1)
        else:
            ma_over_gate.insert(len(df) - index - 1, 0)

        # EMA鱼跃龙门(5/10/20)
        if is_ema_over_gate(df, row, index):
            ema_over_gate.insert(len(df) - index - 1, 1)
        else:
            ema_over_gate.insert(len(df) - index - 1, 0)

        # MA旱地拔葱(5/10/20)
        if is_ma_up_group(df, row, index):
            ma_up_group.insert(len(df) - index - 1, 1)
        else:
            ma_up_group.insert(len(df) - index - 1, 0)

        # EMA旱地拔葱(5/10/20)
        if is_ema_up_group(df, row, index):
            ema_up_group.insert(len(df) - index - 1, 1)
        else:
            ema_up_group.insert(len(df) - index - 1, 0)

        # MA金蜘蛛(5/10/20)
        if is_ma_spider(df, row, index):
            ma_spider.insert(len(df) - index - 1, 1)
        else:
            ma_spider.insert(len(df) - index - 1, 0)

        # MA金蜘蛛(5/10/20/30)
        if is_ma_spider2(df, row, index):
            ma_spider_2.insert(len(df) - index - 1, 1)
        else:
            ma_spider_2.insert(len(df) - index - 1, 0)

        # EMA金蜘蛛(5/10/20)
        if is_ema_spider(df, row, index):
            ema_spider.insert(len(df) - index - 1, 1)
        else:
            ema_spider.insert(len(df) - index - 1, 0)

        # EMA金蜘蛛(5/10/20/30)
        if is_ema_spider2(df, row, index):
            ema_spider_2.insert(len(df) - index - 1, 1)
        else:
            ema_spider_2.insert(len(df) - index - 1, 0)

        # TD_8
        if row.low_td == 8:
            td8.insert(len(df) - index - 1, 1)
        else:
            td8.insert(len(df) - index - 1, 0)

        # TD_9
        if row.low_td == 9:
            td9.insert(len(df) - index - 1, 1)
        else:
            td9.insert(len(df) - index - 1, 0)

    df['ma30_up'] = ma30_up
    df['ema30_up'] = ema30_up
    df['ma60_up'] = ma60_up
    df['ema60_up'] = ema60_up
    df['ma120_up'] = ma120_up
    df['ema120_up'] = ema120_up
    df['ma_arrange'] = ma_arrange
    df['ema_arrange'] = ema_arrange

    df['short_ma_arrange_1'] = short_ma_arrange_1
    df['short_ma_arrange_2'] = short_ma_arrange_2
    df['short_ema_arrange_1'] = short_ema_arrange_1
    df['short_ema_arrange_2'] = short_ema_arrange_2

    df['middle_ma_arrange_1'] = middle_ma_arrange_1
    df['middle_ma_arrange_2'] = middle_ma_arrange_2
    df['middle_ema_arrange_1'] = middle_ema_arrange_1
    df['middle_ema_arrange_2'] = middle_ema_arrange_2

    df['long_ma_arrange_1'] = long_ma_arrange_1
    df['long_ma_arrange_2'] = long_ma_arrange_2
    df['long_ema_arrange_1'] = long_ema_arrange_1
    df['long_ema_arrange_2'] = long_ema_arrange_2

    df['ma_gold_cross_1'] = ma_gold_cross_1
    df['ma_gold_cross_2'] = ma_gold_cross_2
    df['ma_gold_cross_3'] = ma_gold_cross_3
    df['ema_gold_cross_1'] = ema_gold_cross_1
    df['ema_gold_cross_2'] = ema_gold_cross_2
    df['ema_gold_cross_3'] = ema_gold_cross_3

    df['ma_out_sea'] = ma_out_sea
    df['ema_out_sea'] = ema_out_sea
    df['ma_hold_moon'] = ma_hold_moon
    df['ema_hold_moon'] = ema_hold_moon
    df['ma_over_gate'] = ma_over_gate
    df['ema_over_gate'] = ema_over_gate
    df['ma_up_group'] = ma_up_group
    df['ema_up_group'] = ema_up_group
    df['ma_spider'] = ma_spider
    df['ma_spider_2'] = ma_spider_2
    df['ema_spider'] = ema_spider
    df['ema_spider_2'] = ema_spider_2
    df['td8'] = td8
    df['td9'] = td9

    set_ma_silver_valley(df)
    set_ema_silver_valley(df)
    set_ma_gold_valley(df)
    set_ema_gold_valley(df)

    # print(short_ma_arrange_1)
    # print(math.max(df['td8']))
    # print(df['ma_silver_valley'][50:100].max())
    # print('silver valley')
    # print(df['ma_silver_valley'].to_numpy())
    # print('gold valley')
    # print(df['ma_gold_valley'].to_numpy())


def is_ma_spider(df, row, index):
    # 昨日ma5/ma10/ma20交叉于一点
    # 今日ma5/ma10/ma20多头发散
    if df.iloc[len(df) - index - 1 - 1].ma5 == df.iloc[len(df) - index - 1 - 1].ma10 == \
            df.iloc[len(df) - index - 1 - 1].ma20 and row.ma5 > row.ma10 > row.ma20:
        return True
    else:
        return False


def is_ma_spider2(df, row, index):
    # 昨日ma5/ma10/ma20/ma30交叉于一点
    # 今日ma5/ma10/ma20/ma30多头发散
    if df.iloc[len(df) - index - 1 - 1].ma5 == df.iloc[len(df) - index - 1 - 1].ma10 == \
            df.iloc[len(df) - index - 1 - 1].ma20 == df.iloc[len(df) - index - 1 - 1].ma30 and \
            row.ma5 > row.ma10 > row.ma20 > row.ma30:
        return True
    else:
        return False


def is_ema_spider(df, row, index):
    # 昨日ema5/ema10/ema20交叉于一点
    # 今日ema5/ema10/ema20多头发散
    if df.iloc[len(df) - index - 1 - 1].ema5 == df.iloc[len(df) - index - 1 - 1].ema10 \
            == df.iloc[len(df) - index - 1 - 1].ema20 and \
            row.ema5 > row.ema10 > row.ema20:
        return True
    else:
        return False


def is_ema_spider2(df, row, index):
    # 昨日ema5/ema10/ema20/ema30交叉于一点
    # 今日ema5/ema10/ema20/ema30多头发散
    if df.iloc[len(df) - index - 1 - 1].ema5 == df.iloc[len(df) - index - 1 - 1].ema10 == \
            df.iloc[len(df) - index - 1 - 1].ema20 == df.iloc[len(df) - index - 1 - 1].ema30 and \
            row.ema5 > row.ema10 > row.ema20 > row.ema30:
        return True
    else:
        return False


def is_ma_up_group(df, row, index):
    # 大阳线
    # 跳空阳线
    # K线站上ma5/ma10/ma20
    # 昨日K线未站上ma5/ma10/ma20
    if row.pct_chg >= 4 and \
            row.low > df.iloc[len(df) - index - 1 - 1].high and \
            row.close > row.ma5 and row.close > row.ma10 and row.close > row.ma20 and \
            (df.iloc[len(df) - index - 1 - 1].low < df.iloc[len(df) - index - 1 - 1].ma5 or
             df.iloc[len(df) - index - 1 - 1].low < df.iloc[len(df) - index - 1 - 1].ma10 or
             df.iloc[len(df) - index - 1 - 1].low < df.iloc[len(df) - index - 1 - 1].ma20) and \
            (df.iloc[len(df) - index - 1 - 1].open < df.iloc[len(df) - index - 1 - 1].ma20 or
             df.iloc[len(df) - index - 1 - 1].close < df.iloc[len(df) - index - 1 - 1].ma20):
        return True
    else:
        return False


def is_ema_up_group(df, row, index):
    # 大阳线
    # 跳空阳线
    # K线站上ema5/ema10/ema20
    # 昨日K线未站上ema5/ema10/ema20
    if row.pct_chg >= 4 and \
            row.close > row.ema5 and row.close > row.ema10 and row.close > row.ema20 and \
            row.low > df.iloc[len(df) - index - 1 - 1].high and \
            df.iloc[len(df) - index - 1 - 1].low < df.iloc[len(df) - index - 1 - 1].ema20 and \
            (df.iloc[len(df) - index - 1 - 1].low < df.iloc[len(df) - index - 1 - 1].ema5 or
             df.iloc[len(df) - index - 1 - 1].low < df.iloc[len(df) - index - 1 - 1].ema10 or
             df.iloc[len(df) - index - 1 - 1].low < df.iloc[len(df) - index - 1 - 1].ema20) and \
            (df.iloc[len(df) - index - 1 - 1].open < df.iloc[len(df) - index - 1 - 1].ema20 or
             df.iloc[len(df) - index - 1 - 1].close < df.iloc[len(df) - index - 1 - 1].ema20):
        return True
    else:
        return False


def is_ma_over_gate(df, row, index):
    # 大阳线
    # K线站上ma5/ma10/ma20
    # 昨日K线未站上ma5/ma10/ma20
    # 昨日出现均线粘合
    if row.pct_chg >= 4 and \
            row.close > row.ma5 and row.close > row.ma10 and row.close > row.ma20 and \
            (df.iloc[len(df) - index - 1 - 1].low < df.iloc[len(df) - index - 1 - 1].ma5 or
             df.iloc[len(df) - index - 1 - 1].low < df.iloc[len(df) - index - 1 - 1].ma10 or
             df.iloc[len(df) - index - 1 - 1].low < df.iloc[len(df) - index - 1 - 1].ma20) and \
            df.iloc[len(df) - index - 1 - 1].ma20_slope > 0 and \
            df.iloc[len(df) - index - 1 - 1].ma5 > df.iloc[len(df) - index - 1 - 1].ma20 and \
            df.iloc[len(df) - index - 1 - 1].ma10 > df.iloc[len(df) - index - 1 - 1].ma20:
        return True
    else:
        return False


def is_ema_over_gate(df, row, index):
    # 大阳线
    # K线站上ema5/ema10/ema20
    # 昨日K线未站上ema5/ema10/ema20
    # 昨日出现均线粘合
    if row.pct_chg >= 4 and \
            row.close > row.ema5 and row.close > row.ema10 and row.close > row.ema20 and \
            (df.iloc[len(df) - index - 1 - 1].low < df.iloc[len(df) - index - 1 - 1].ema5 or
             df.iloc[len(df) - index - 1 - 1].low < df.iloc[len(df) - index - 1 - 1].ema10 or
             df.iloc[len(df) - index - 1 - 1].low < df.iloc[len(df) - index - 1 - 1].ema20) and \
            df.iloc[len(df) - index - 1 - 1].ema20_slope > 0 and \
            df.iloc[len(df) - index - 1 - 1].ema5 > df.iloc[len(df) - index - 1 - 1].ema20 and \
            df.iloc[len(df) - index - 1 - 1].ema10 > df.iloc[len(df) - index - 1 - 1].ema20:
        return True
    else:
        return False


def is_ma_hold_moon(df, row, index):
    # 今昨两日K线未站上ma5/ma10/ma20
    # 今昨两日出现均线粘合
    # ma20/ma60 上行
    if (row.low < row.ma5 or row.low < row.ma10 or row.low < row.ma20) and row.ma5 > row.ma20 and \
            row.ma10 > row.ma20 and \
            (df.iloc[len(df) - index - 1 - 1].low < df.iloc[len(df) - index - 1 - 1].ma5 or
             df.iloc[len(df) - index - 1 - 1].low < df.iloc[len(df) - index - 1 - 1].ma10 or
             df.iloc[len(df) - index - 1 - 1].low < df.iloc[len(df) - index - 1 - 1].ma20) and \
            df.iloc[len(df) - index - 1 - 1].ma20_slope > 0 and \
            df.iloc[len(df) - index - 1 - 1].ma5 > df.iloc[len(df) - index - 1 - 1].ma20 and \
            df.iloc[len(df) - index - 1 - 1].ma10 > df.iloc[len(df) - index - 1 - 1].ma20 and \
            row.ma20_slope > 0 and row.ma60_slope > 0:
        return True
    else:
        return False


def is_ema_hold_moon(df, row, index):
    # 今昨两日K线未站上ema5/ema10/ema20
    # 今昨两日出现均线粘合
    # ema20/ema60 上行
    if (row.low < row.ema5 or row.low < row.ema10 or row.low < row.ema20) and row.ema5 > row.ema20 and \
            row.ema10 > row.ema20 and \
            (df.iloc[len(df) - index - 1 - 1].low < df.iloc[len(df) - index - 1 - 1].ema5 or
             df.iloc[len(df) - index - 1 - 1].low < df.iloc[len(df) - index - 1 - 1].ema10 or
             df.iloc[len(df) - index - 1 - 1].low < df.iloc[len(df) - index - 1 - 1].ema20) and \
            df.iloc[len(df) - index - 1 - 1].ema20_slope > 0 and \
            df.iloc[len(df) - index - 1 - 1].ema5 > df.iloc[len(df) - index - 1 - 1].ema20 and \
            df.iloc[len(df) - index - 1 - 1].ema10 > df.iloc[len(df) - index - 1 - 1].ema20 and \
            row.ema20_slope > 0 and row.ema60_slope > 0:
        return True
    else:
        return False


def is_ma_out_sea(row):
    # 大阳线 贯穿ma5/ma10/ma20
    # ma20 上行
    if row.pct_chg >= 4 and \
            row.open < row.ma5 and row.open < row.ma10 and row.open < row.ma20 and \
            row.close > row.ma5 and row.close > row.ma10 and row.close > row.ma20 and \
            row.ma60_slope > 0:
        return True
    else:
        return False


def is_ema_out_sea(row):
    # 大阳线 贯穿ema5/ema10/ema20
    # ema20/ema60 上行
    if row.pct_chg >= 4 and \
            row.open < row.ema5 and row.open < row.ema10 and row.open < row.ema20 and \
            row.close > row.ema5 and row.close > row.ema10 and row.close > row.ema20 and \
            row.ema60_slope > 0:
        return True
    else:
        return False


def is_ma_gold_cross_1(df, row, index):
    # ma5上穿ma10
    # ma5/ma10上行
    if row.ma5 > row.ma10 and df.iloc[len(df) - index - 1 - 1].ma5 < df.iloc[len(df) - index - 1 - 1].ma10 and \
            row.ma5_slope > 0 and row.ma10_slope > 0:
        return True
    else:
        return False


def is_ma_gold_cross_2(df, row, index):
    # ma10上穿ma20
    # ma10/ma20上行
    if row.ma10 > row.ma20 and df.iloc[len(df) - index - 1 - 1].ma10 < df.iloc[len(df) - index - 1 - 1].ma20 and \
            row.ma10_slope > 0 and row.ma20_slope > 0:
        return True
    else:
        return False


def is_ma_gold_cross_3(df, row, index):
    # ma10上穿ma30
    # ma10/ma30上行
    if row.ma10 > row.ma30 and df.iloc[len(df) - index - 1 - 1].ma10 < df.iloc[len(df) - index - 1 - 1].ma30 and \
            row.ma10_slope > 0 and row.ma30_slope > 0:
        return True
    else:
        return False


def is_ema_gold_cross_1(df, row, index):
    # ema5上穿ema10
    # ema5/ema10上行
    if row.ema5 > row.ema10 and df.iloc[len(df) - index - 1 - 1].ema5 < df.iloc[len(df) - index - 1 - 1].ema10 and \
            row.ema5_slope > 0 and row.ema10_slope > 0:
        return True
    else:
        return False


def is_ema_gold_cross_2(df, row, index):
    # ema10上穿ema20
    # ema10/ema20上行
    if row.ema10 > row.ema20 and df.iloc[len(df) - index - 1 - 1].ema10 < df.iloc[len(df) - index - 1 - 1].ema20 and \
            row.ema10_slope > 0 and row.ema20_slope > 0:
        return True
    else:
        return False


def is_ema_gold_cross_3(df, row, index):
    # ema10上穿ema30
    # ema10/ema30上行
    if row.ema10 > row.ema30 and df.iloc[len(df) - index - 1 - 1].ema10 < df.iloc[len(df) - index - 1 - 1].ema30 and \
            row.ema30_slope > 0 and row.ema30_slope > 0:
        return True
    else:
        return False


def set_ma_silver_valley(df):
    ma_silver_valley = []

    for index, row in df.iterrows():
        if len(df) - index - 1 >= 10:
            gold_cross_cnt = 0
            if df['ma_gold_cross_1'][len(df) - index - 1 - 10: len(df) - index - 1].max() == 1:
                gold_cross_cnt += 1
            if df['ma_gold_cross_2'][len(df) - index - 1 - 10: len(df) - index - 1].max() == 1:
                gold_cross_cnt += 1
            if df['ma_gold_cross_3'][len(df) - index - 1 - 10: len(df) - index - 1].max() == 1:
                gold_cross_cnt += 1

            if gold_cross_cnt >= 2:
                ma_silver_valley.insert(len(df) - index - 1, 1)
            else:
                ma_silver_valley.insert(len(df) - index - 1, 0)
        else:
            ma_silver_valley.insert(len(df) - index - 1, 0)

    df['ma_silver_valley'] = ma_silver_valley


def set_ema_silver_valley(df):
    ema_silver_valley = []

    for index, row in df.iterrows():
        if len(df) - index - 1 >= 10:
            gold_cross_cnt = 0
            if df['ema_gold_cross_1'][len(df) - index - 1 - 10: len(df) - index - 1].max() == 1:
                gold_cross_cnt += 1
            if df['ema_gold_cross_2'][len(df) - index - 1 - 10: len(df) - index - 1].max() == 1:
                gold_cross_cnt += 1
            if df['ema_gold_cross_3'][len(df) - index - 1 - 10: len(df) - index - 1].max() == 1:
                gold_cross_cnt += 1

            if gold_cross_cnt >= 2:
                ema_silver_valley.insert(len(df) - index - 1, 1)
            else:
                ema_silver_valley.insert(len(df) - index - 1, 0)
        else:
            ema_silver_valley.insert(len(df) - index - 1, 0)

    df['ema_silver_valley'] = ema_silver_valley


def set_ma_gold_valley(df):
    ma_gold_valley = []

    for index, row in df.iterrows():
        if len(df) - index - 1 >= 30:
            gold_cross_cnt = 0
            if df['ma_gold_cross_1'][len(df) - index - 1 - 10: len(df) - index - 1].max() == 1:
                gold_cross_cnt += 1
            if df['ma_gold_cross_2'][len(df) - index - 1 - 10: len(df) - index - 1].max() == 1:
                gold_cross_cnt += 1
            if df['ma_gold_cross_3'][len(df) - index - 1 - 10: len(df) - index - 1].max() == 1:
                gold_cross_cnt += 1

            if df['ma_silver_valley'][len(df) - index - 1 - 30: len(df) - index - 1].max() == 1 and \
                    gold_cross_cnt >= 2 and \
                    df.iloc[len(df) - index - 1 - 30].ma20 < row.ma20 and row.ma20_slope > 0:
                ma_gold_valley.insert(len(df) - index - 1, 1)
            else:
                ma_gold_valley.insert(len(df) - index - 1, 0)
        else:
            ma_gold_valley.insert(len(df) - index - 1, 0)

    df['ma_gold_valley'] = ma_gold_valley


def set_ema_gold_valley(df):
    ema_gold_valley = []

    for index, row in df.iterrows():
        if len(df) - index - 1 >= 30:
            gold_cross_cnt = 0
            if df['ema_gold_cross_1'][len(df) - index - 1 - 10: len(df) - index - 1].max() == 1:
                gold_cross_cnt += 1
            if df['ema_gold_cross_2'][len(df) - index - 1 - 10: len(df) - index - 1].max() == 1:
                gold_cross_cnt += 1
            if df['ema_gold_cross_3'][len(df) - index - 1 - 10: len(df) - index - 1].max() == 1:
                gold_cross_cnt += 1

            if df['ema_silver_valley'][len(df) - index - 1 - 30: len(df) - index - 1].max() == 1 and \
                    gold_cross_cnt >= 2 and \
                    df.iloc[len(df) - index - 1 - 30].ema20 < row.ema20 and row.ema20_slope > 0:
                ema_gold_valley.insert(len(df) - index - 1, 1)
            else:
                ema_gold_valley.insert(len(df) - index - 1, 0)
        else:
            ema_gold_valley.insert(len(df) - index - 1, 0)

    df['ema_gold_valley'] = ema_gold_valley
