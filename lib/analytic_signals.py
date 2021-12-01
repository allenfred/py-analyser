from talib import SMA
import pandas as pd
import numpy as np
import math
from .candle import stand_on_ma, stand_on_ema, \
    is_hammer, is_pour_hammer, is_short_end, is_swallow_up, \
    is_sunrise, is_first_light, is_attack_short, is_flat_base
import time

"""
df: indicators with signals (long signals or short signals)
"""


def analytic_signals(org_df):
    def item_apply(df, row):
        index = row.name

        # set_yearly_price_position
        if index >= 260:
            high_price = df['high'][index - 259: index + 1].max()
            low_price = df['low'][index - 259: index + 1].min()
        else:
            high_price = df['high'].max()
            low_price = df['low'].min()

        price_range = high_price - low_price
        price_pct_position = round((row.close - low_price) * 100 / price_range, 1)
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
        if is_ma_gold_cross1(df, row):
            ma_gold_cross1.insert(index, 1)
        else:
            ma_gold_cross1.insert(index, 0)

        # MA黄金交叉（5/20）
        if is_ma_gold_cross2(df, row):
            ma_gold_cross2.insert(index, 1)
        else:
            ma_gold_cross2.insert(index, 0)

        # MA黄金交叉（10/20）
        if is_ma_gold_cross3(df, row):
            ma_gold_cross3.insert(index, 1)
        else:
            ma_gold_cross3.insert(index, 0)

        # MA黄金交叉（10/30）
        if is_ma_gold_cross4(df, row):
            ma_gold_cross4.insert(index, 1)
        else:
            ma_gold_cross4.insert(index, 0)

        # EMA黄金交叉（5/10）
        if is_ema_gold_cross1(df, row):
            ema_gold_cross1.insert(index, 1)
        else:
            ema_gold_cross1.insert(index, 0)

        # EMA黄金交叉（5/20）
        if is_ema_gold_cross2(df, row):
            ema_gold_cross2.insert(index, 1)
        else:
            ema_gold_cross2.insert(index, 0)

        # EMA黄金交叉（10/20）
        if is_ema_gold_cross3(df, row):
            ema_gold_cross3.insert(index, 1)
        else:
            ema_gold_cross3.insert(index, 0)

        # EMA黄金交叉（10/30）
        if is_ema_gold_cross4(df, row):
            ema_gold_cross4.insert(index, 1)
        else:
            ema_gold_cross4.insert(index, 0)

        # MA银山谷
        if is_ma_silver_valley(row, ma_gold_cross1, ma_gold_cross2, ma_gold_cross3):
            ma_silver_valley.insert(index, 1)
        else:
            ma_silver_valley.insert(index, 0)

        # EMA银山谷
        if is_ema_silver_valley(row, ema_gold_cross1, ema_gold_cross2, ema_gold_cross3):
            ema_silver_valley.insert(index, 1)
        else:
            ema_silver_valley.insert(index, 0)

        # MA金山谷
        if is_ma_gold_valley(df, row, ma_silver_valley):
            ma_gold_valley.insert(index, 1)
        else:
            ma_gold_valley.insert(index, 0)

        # EMA金山谷
        if is_ema_gold_valley(df, row, ema_silver_valley):
            ema_gold_valley.insert(index, 1)
        else:
            ema_gold_valley.insert(index, 0)

        # MA金蜘蛛
        if is_ma_spider(row, ma_gold_cross1, ma_gold_cross2, ma_gold_cross3):
            ma_spider.insert(index, 1)
        else:
            ma_spider.insert(index, 0)

        # MA金蜘蛛2
        if is_ma_spider2(row, ma_gold_cross1, ma_gold_cross2, ma_gold_cross3, ma_gold_cross4):
            ma_spider2.insert(index, 1)
        else:
            ma_spider2.insert(index, 0)

        # EMA金蜘蛛
        if is_ema_spider(row, ema_gold_cross1, ema_gold_cross2, ema_gold_cross3):
            ema_spider.insert(index, 1)
        else:
            ema_spider.insert(index, 0)

        # EMA金蜘蛛2
        if is_ema_spider2(row, ma_gold_cross1, ema_gold_cross2, ema_gold_cross3, ema_gold_cross4):
            ema_spider2.insert(index, 1)
        else:
            ema_spider2.insert(index, 0)

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
        if is_ma_hold_moon(df, row):
            ma_hold_moon.insert(index, 1)
        else:
            ma_hold_moon.insert(index, 0)

        # EMA烘云托月(5/10/20)
        if is_ema_hold_moon(df, row):
            ema_hold_moon.insert(index, 1)
        else:
            ema_hold_moon.insert(index, 0)

        # MA鱼跃龙门(5/10/20)
        if is_ma_over_gate(df, row):
            ma_over_gate.insert(index, 1)
        else:
            ma_over_gate.insert(index, 0)

        # EMA鱼跃龙门(5/10/20)
        if is_ema_over_gate(df, row):
            ema_over_gate.insert(index, 1)
        else:
            ema_over_gate.insert(index, 0)

        # MA旱地拔葱(5/10/20)
        if is_ma_up_group(df, row):
            ma_up_group.insert(index, 1)
        else:
            ma_up_group.insert(index, 0)

        # EMA旱地拔葱(5/10/20)
        if is_ema_up_group(df, row):
            ema_up_group.insert(index, 1)
        else:
            ema_up_group.insert(index, 0)

        # MA均线粘合(5/10/20)
        if is_ma_glue(df, row):
            ma_glue.insert(index, 1)
        else:
            ma_glue.insert(index, 0)

        # EMA均线粘合(5/10/20)
        if is_ema_glue(df, row):
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

        # 锤子线
        if is_hammer(df, row):
            hammer.insert(index, 1)
        else:
            hammer.insert(index, 0)

        # 倒锤子线
        if is_pour_hammer(df, row):
            pour_hammer.insert(index, 1)
        else:
            pour_hammer.insert(index, 0)

        # 看涨尽头线
        if is_short_end(df, row):
            short_end.insert(index, 1)
        else:
            short_end.insert(index, 0)

        # 看涨吞没
        if is_swallow_up(df, row):
            swallow_up.insert(index, 1)
        else:
            swallow_up.insert(index, 0)

        # 好友反攻
        if is_attack_short(df, row):
            attack_short.insert(index, 1)
        else:
            attack_short.insert(index, 0)

        # 曙光初现
        if is_first_light(df, row):
            first_light.insert(index, 1)
        else:
            first_light.insert(index, 0)

        # 旭日东升
        if is_sunrise(df, row):
            sunrise.insert(index, 1)
        else:
            sunrise.insert(index, 0)

        # 平底
        if is_flat_base(df, row):
            flat_base.insert(index, 1)
        else:
            flat_base.insert(index, 0)

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

    org_df.apply(lambda row: item_apply(org_df, row), axis=1)

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
    org_df['ma_up_group'] = ma_up_group
    org_df['ema_up_group'] = ema_up_group

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


def is_ma_glue(df, row):
    index = row.name

    # 最近9个交易日 0 < ma20_slope < 0.6
    # 最近9个交易日 -0.5 < ma10_slope < 0.8
    # 最近9个交易日 -0.5 < ma5_slope < 1
    if df.ma20_slope[index - 8: index + 1].min() > 0 and df.ma20_slope[index - 8: index + 1].max() < 0.6 and \
            df.ma10_slope[index - 8: index + 1].min() > -0.5 and df.ma10_slope[index - 8: index + 1].max() < 0.8 and \
            df.ma5_slope[index - 8: index + 1].min() > -0.5 and df.ma5_slope[index - 8: index + 1].max() < 1:
        return True
    else:
        return False


def is_ema_glue(df, row):
    index = row.name

    # 最近9个交易日 0 < ema20_slope < 0.6
    # 最近9个交易日 -0.5 < ema10_slope < 0.8
    # 最近9个交易日 -0.5 < ema5_slope < 1
    if df.ema20_slope[index - 8: index + 1].min() > 0 and df.ema20_slope[index - 8: index + 1].max() < 0.6 and \
            df.ema10_slope[index - 8: index + 1].min() > -0.5 and df.ema10_slope[index - 8: index + 1].max() < 0.8 and \
            df.ema5_slope[index - 8: index + 1].min() > -0.5 and df.ema5_slope[index - 8: index + 1].max() < 1:
        return True
    else:
        return False


def is_ma_up_group(df, row):
    index = row.name

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


def is_ema_up_group(df, row):
    index = row.name

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


def is_ma_over_gate(df, row):
    index = row.name
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


def is_ema_over_gate(df, row):
    index = row.name
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


def is_ma_hold_moon(df, row):
    index = row.name

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


def is_ema_hold_moon(df, row):
    index = row.name

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


def is_ma_gold_cross1(df, row):
    index = row.name

    # ma5上穿ma10
    # ma5/ma10上行
    if row.ma5 > row.ma10 and df.iloc[index - 1].ma5 < df.iloc[index - 1].ma10 and \
            row.ma5_slope > 0 and row.ma10_slope > 0:
        return True
    else:
        return False


def is_ma_gold_cross2(df, row):
    index = row.name

    # ma5上穿ma20
    # ma5/ma20上行
    if row.ma5 > row.ma20 and df.iloc[index - 1].ma5 < df.iloc[index - 1].ma20 and \
            row.ma5_slope > 0 and row.ma20_slope > 0:
        return True
    else:
        return False


def is_ma_gold_cross3(df, row):
    index = row.name

    # ma10上穿ma20
    # ma10/ma20上行
    if row.ma10 > row.ma20 and df.iloc[index - 1].ma10 < df.iloc[index - 1].ma20 and \
            row.ma10_slope > 0 and row.ma20_slope > 0:
        return True
    else:
        return False


def is_ma_gold_cross4(df, row):
    index = row.name

    # ma10上穿ma30
    # ma10/ma30上行
    if row.ma10 > row.ma30 and df.iloc[index - 1].ma10 < df.iloc[index - 1].ma30 and \
            row.ma10_slope > 0 and row.ma30_slope > 0:
        return True
    else:
        return False


def is_ema_gold_cross1(df, row):
    index = row.name

    # ema5上穿ema10
    # ema5/ema10上行
    if row.ema5 > row.ema10 and df.iloc[index - 1].ema5 < df.iloc[index - 1].ema10 and \
            row.ema5_slope > 0 and row.ema10_slope > 0:
        return True
    else:
        return False


def is_ema_gold_cross2(df, row):
    index = row.name

    # ema5上穿ema20
    # ema5/ema20上行
    if row.ema5 > row.ema20 and df.iloc[index - 1].ema5 < df.iloc[index - 1].ema20 and \
            row.ema5_slope > 0 and row.ema20_slope > 0:
        return True
    else:
        return False


def is_ema_gold_cross3(df, row):
    index = row.name

    # ema10上穿ema20
    # ema10/ema20上行
    if row.ema10 > row.ema20 and df.iloc[index - 1].ema10 < df.iloc[index - 1].ema20 and \
            row.ema10_slope > 0 and row.ema20_slope > 0:
        return True
    else:
        return False


def is_ema_gold_cross4(df, row):
    index = row.name

    # ema10上穿ema30
    # ema10/ema30上行
    if row.ema10 > row.ema30 and df.iloc[index - 1].ema10 < df.iloc[index - 1].ema30 and \
            row.ema10_slope > 0 and row.ema30_slope > 0:
        return True
    else:
        return False


def is_ma_silver_valley(row, cross1, cross2, cross3):
    index = row.name

    if index >= 10 and (cross2[index] == 1 or cross3[index] == 1):
        gold_cross_cnt = 0
        if max(cross1[index - 9: index + 1]) == 1:
            gold_cross_cnt += 1
        if max(cross2[index - 9: index + 1]) == 1:
            gold_cross_cnt += 1
        if max(cross3[index - 9: index + 1]) == 1:
            gold_cross_cnt += 1

        if gold_cross_cnt >= 2:
            return True
        else:
            return False
    else:
        return False


def is_ema_silver_valley(row, cross1, cross2, cross3):
    index = row.name

    if index >= 10 and (cross2[index] == 1 or cross3[index] == 1):
        gold_cross_cnt = 0
        if max(cross1[index - 9: index + 1]) == 1:
            gold_cross_cnt += 1
        if max(cross2[index - 9: index + 1]) == 1:
            gold_cross_cnt += 1
        if max(cross3[index - 9: index + 1]) == 1:
            gold_cross_cnt += 1

        if gold_cross_cnt >= 2:
            return True
        else:
            return False
    else:
        return False


def is_ma_gold_valley(df, row, ma_silver_valley):
    index = row.name
    # 最近30个交易日内形成两次银山谷视为金山谷
    # 最近30个交易日内形成两次银山谷视为金山谷
    if index >= 30 and max(ma_silver_valley[index - 29: index - 1]) == 1 and \
            ma_silver_valley[index] == 1 and df.iloc[index - 30].ma20 < row.ma20 and \
            row.ma20_slope > 0:
        return True
    else:
        return False


def is_ema_gold_valley(df, row, ema_silver_valley):
    index = row.name
    # 最近30个交易日内形成两次银山谷 视为 金山谷
    if index >= 30 and max(ema_silver_valley[index - 29: index - 1]) == 1 and \
            ema_silver_valley[index] == 1 and df.iloc[index - 30].ema20 < row.ema20 and \
            row.ema20_slope > 0:
        return True
    else:
        return False


def is_ma_spider(row, cross1, cross2, cross3):
    index = row.name
    # 最近3个交易日ma5/ma10/ma20交叉于一点 (即出现至少2个金叉)
    # 今日ma5/ma10/ma20多头发散
    gold_cross_cnt = 0
    if max(cross1[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1
    if max(cross2[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1
    if max(cross3[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1

    if gold_cross_cnt > 1 and row.ma5 > row.ma10 > row.ma20:
        return True
    else:
        return False


def is_ma_spider2(row, cross1, cross2, cross3, cross4):
    index = row.name
    # 最近3个交易日 ma5/ma10/ma20/ma30 交叉于一点 (即出现至少3个金叉)
    # 今日 ma5/ma10/ma20/ma30 多头发散
    gold_cross_cnt = 0
    if max(cross1[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1
    if max(cross2[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1
    if max(cross3[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1
    if max(cross4[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1

    if gold_cross_cnt > 2 and row.ma5 > row.ma10 > row.ma20 > row.ma30:
        return True
    else:
        return False


def is_ema_spider(row, cross1, cross2, cross3):
    index = row.name
    # 最近3个交易日ema5/ema10/ema20交叉于一点 (即出现至少2个金叉)
    # 今日ema5/ema10/ema20多头发散
    gold_cross_cnt = 0
    if max(cross1[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1
    if max(cross2[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1
    if max(cross3[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1

    if gold_cross_cnt > 1 and row.ema5 > row.ema10 > row.ema20:
        return True
    else:
        return False


def is_ema_spider2(row, cross1, cross2, cross3, cross4):
    index = row.name
    # 最近3个交易日 ema5/ema10/ema20/ema30 交叉于一点 (即出现至少3个金叉)
    # 今日 ema5/ema10/ema20/ema30 多头发散
    gold_cross_cnt = 0
    if max(cross1[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1
    if max(cross2[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1
    if max(cross3[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1
    if max(cross4[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1

    if gold_cross_cnt > 2 and row.ema5 > row.ema10 > row.ema20 > row.ema30:
        return True
    else:
        return False


def is_stand_up_ma60(df, row):
    if row.name < 60:
        return False

    # 前55个交易日(除最近2个交易日外) ma60向下运行
    index = row.name
    df1 = df.iloc[index - 55: index - 1]
    pre_row = df.iloc[index - 1]
    ma60_down_still = True
    close_down_still = True
    ma60_up_recently = False

    def close_judge(_row):
        if _row.close < _row.ma60:
            return 0
        else:
            return 1

    close_sets = df1.apply(lambda _: close_judge(_), axis=1)
    close_sets = close_sets.to_numpy()

    if close_sets.max() > 0:
        close_down_still = False

    if df1['ma60_slope'].max() >= 0:
        ma60_down_still = False

    # 最近2个交易日收盘价高于 ma60
    # 最近2个交易日 ma60 开始向上
    if row.close > row.ma60 and pre_row.close > pre_row.ma60 and row.ma60_slope > 0 and pre_row.ma60_slope > 0:
        ma60_up_recently = True

    if len(df) > 81 and close_down_still and ma60_down_still and ma60_up_recently:
        return True
    else:
        return False


def is_stand_up_ma120(df, row):
    if row.name < 130:
        return 0

    # 前89个交易日(除最近2个交易日外) ma120向下运行
    index = row.name
    df1 = df.iloc[index - 89: index - 1]
    pre_row = df.iloc[index - 1]
    ma120_down_still = True
    close_down_still = True
    ma120_up_recently = False

    def close_judge(_row):
        if _row.close < _row.ma120:
            return 0
        else:
            return 1

    close_sets = df1.apply(lambda _: close_judge(_), axis=1)
    close_sets = close_sets.to_numpy()

    if close_sets.max() > 0:
        close_down_still = False

    if df1['ma120_slope'].max() >= 0:
        ma120_down_still = False

    # 最近2个交易日收盘价高于 ma120
    # 最近2个交易日 ma120 开始向上
    if row.close > row.ma120 and pre_row.close > pre_row.ma120 and row.ma120_slope > 0 and pre_row.ma120_slope > 0:
        ma120_up_recently = True

    if len(df) > 154 and close_down_still and ma120_down_still and ma120_up_recently:
        return True
    else:
        return False


def is_stand_up_ema60(df, row):
    if row.name < 60:
        return 0

    # 前55个交易日(除最近3个交易日外) ema60 向下运行
    index = row.name
    df1 = df.iloc[index - 55: index - 1]
    pre_row = df.iloc[index - 1]
    ma60_down_still = True
    close_down_still = True
    ma60_up_recently = False

    def close_judge(_row):
        if _row.close < _row.ema60:
            return 0
        else:
            return 1

    close_sets = df1.apply(lambda _: close_judge(_), axis=1)
    close_sets = close_sets.to_numpy()

    if close_sets.max() > 0:
        close_down_still = False

    if df1['ema60_slope'].max() >= 0:
        ma60_down_still = False

    # 最近2个交易日收盘价高于 ema60
    # 最近2个交易日 ema60 开始向上
    if row.close > row.ema60 and pre_row.close > pre_row.ema60 and row.ema60_slope > 0 and pre_row.ema60_slope > 0:
        ma60_up_recently = True

    if len(df) > 81 and close_down_still and ma60_down_still and ma60_up_recently:
        return True
    else:
        return False


def is_stand_up_ema120(df, row):
    if row.name < 130:
        return 0

    # 前89个交易日(除最近2个交易日外) ma120向下运行
    index = row.name
    df1 = df.iloc[index - 89: index - 1]
    pre_row = df.iloc[index - 1]
    ma120_down_still = True
    close_down_still = True
    ma120_up_recently = False

    def close_judge(_row):
        if _row.close < _row.ema120:
            return 0
        else:
            return 1

    close_sets = df1.apply(lambda _: close_judge(_), axis=1)
    close_sets = close_sets.to_numpy()

    if close_sets.max() > 0:
        close_down_still = False

    if df1['ema120_slope'].max() >= 0:
        ma120_down_still = False

    # 最近2个交易日收盘价高于 ma120
    # 最近2个交易日 ma120 开始向上
    if row.close > row.ema120 and pre_row.close > pre_row.ema120 and row.ema120_slope > 0 and pre_row.ema120_slope > 0:
        ma120_up_recently = True

    if len(df) > 154 and close_down_still and ma120_down_still and ma120_up_recently:
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
