from talib import SMA
import pandas as pd
import numpy as np
import math
from .candle import is_hammer, is_pour_hammer, is_short_end, is_swallow_down, \
    is_sunrise, is_first_light, is_attack_short, is_flat_base


def short_analytic(candle, ma, ema, ma_slope, ema_slope, bias, td):
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

    ma20_down = []
    ema20_down = []
    ma30_down = []
    ema30_down = []
    ma60_down = []
    ema60_down = []
    ma120_down = []
    ema120_down = []

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

    ma_dead_cross1 = []
    ma_dead_cross2 = []
    ma_dead_cross3 = []
    ma_dead_cross4 = []
    ema_dead_cross1 = []
    ema_dead_cross2 = []
    ema_dead_cross3 = []
    ema_dead_cross4 = []

    ma_dead_valley = []
    ema_dead_valley = []

    ma_knife = []
    ema_knife = []

    ma_dark_cloud = []
    ema_dark_cloud = []

    ma_set_sail = []
    ema_set_sail = []

    ma_supreme = []
    ema_supreme = []

    ma_dead_jump = []
    ema_dead_jump = []

    ma_spider = []
    ma_spider2 = []
    ema_spider = []
    ema_spider2 = []

    td8 = []
    td9 = []

    bias6 = []
    bias12 = []
    bias24 = []
    bias60 = []
    bias72 = []
    bias120 = []

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

        # MA20下行
        if _ma20_slope < 0:
            ma20_down.insert(index, 1)
        else:
            ma20_down.insert(index, 0)

        # EMA20下行
        if _ema20_slope < 0:
            ema20_down.insert(index, 1)
        else:
            ema20_down.insert(index, 0)

        # MA30下行
        if _ma30_slope < 0:
            ma30_down.insert(index, 1)
        else:
            ma30_down.insert(index, 0)

        # EMA30下行
        if _ema30_slope < 0:
            ema30_down.insert(index, 1)
        else:
            ema30_down.insert(index, 0)

        # MA60下行
        if _ma60_slope < 0:
            ma60_down.insert(index, 1)
        else:
            ma60_down.insert(index, 0)

        # EMA60下行
        if _ema60_slope < 0:
            ema60_down.insert(index, 1)
        else:
            ema60_down.insert(index, 0)

        # MA120下行
        if _ma120_slope < 0:
            ma120_down.insert(index, 1)
        else:
            ma120_down.insert(index, 0)

        # EMA120下行
        if _ema120_slope < 0:
            ema120_down.insert(index, 1)
        else:
            ema120_down.insert(index, 0)

        # MA空头排列（5/10/20/60）
        if _ma5_slope < 0 and _ma10_slope < 0 and _ma20_slope < 0 and _ma60_slope < 0 \
                and _ma5 < _ma10 < _ma20 < _ma60:
            ma_arrange.insert(index, 1)
        else:
            ma_arrange.insert(index, 0)

        # EMA空头排列（5/10/20/60）
        if _ema5_slope < 0 and _ema10_slope < 0 and _ema20_slope < 0 and _ema60_slope < 0 \
                and _ema5 < _ema10 < _ema20 < _ema60:
            ema_arrange.insert(index, 1)
        else:
            ema_arrange.insert(index, 0)

        # MA短期组合空头排列（5/10/20）
        if _ma5_slope < 0 and _ma10_slope < 0 and _ma20_slope < 0 \
                and _ma5 < _ma10 < _ma20:
            short_ma_arrange1.insert(index, 1)
        else:
            short_ma_arrange1.insert(index, 0)

        # MA短期组合空头排列（5/10/30）
        if _ma5_slope < 0 and _ma10_slope < 0 and _ma30_slope < 0 \
                and _ma5 < _ma10 < _ma30:
            short_ma_arrange2.insert(index, 1)
        else:
            short_ma_arrange2.insert(index, 0)

        # EMA短期组合空头排列（5/10/20）
        if _ema5_slope < 0 and _ema10_slope < 0 and _ema20_slope < 0 \
                and _ema5 < _ema10 < _ema20:
            short_ema_arrange1.insert(index, 1)
        else:
            short_ema_arrange1.insert(index, 0)

        # EMA短期组合空头排列（5/10/30）
        if _ema5_slope < 0 and _ema10_slope < 0 and _ema30_slope < 0 \
                and _ema5 < _ema10 < _ema30:
            short_ema_arrange2.insert(index, 1)
        else:
            short_ema_arrange2.insert(index, 0)

        # MA中期组合空头排列（10/20/60）
        if _ma10_slope < 0 and _ma20_slope < 0 and _ma60_slope < 0 \
                and _ma10 < _ma20 < _ma60:
            middle_ma_arrange1.insert(index, 1)
        else:
            middle_ma_arrange1.insert(index, 0)

        # MA中期组合空头排列（10/20/55）
        if _ma10_slope < 0 and _ma20_slope < 0 and _ma55_slope < 0 \
                and _ma10 < _ma20 < _ma55:
            middle_ma_arrange2.insert(index, 1)
        else:
            middle_ma_arrange2.insert(index, 0)

        # EMA中期组合空头排列（10/20/60）
        if _ema10_slope < 0 and _ema20_slope < 0 and _ema60_slope < 0 \
                and _ema10 < _ema20 < _ema60:
            middle_ema_arrange1.insert(index, 1)
        else:
            middle_ema_arrange1.insert(index, 0)

        # EMA中期组合空头排列（10/20/55）
        if _ema10_slope < 0 and _ema20_slope < 0 and _ema55_slope < 0 \
                and _ema10 < _ema20 < _ema55:
            middle_ema_arrange2.insert(index, 1)
        else:
            middle_ema_arrange2.insert(index, 0)

        # MA长期组合空头排列（20/55/120）
        if _ma20_slope < 0 and _ma55_slope < 0 and _ma120_slope < 0 \
                and _ma20 < _ma55 < _ma120:
            long_ma_arrange1.insert(index, 1)
        else:
            long_ma_arrange1.insert(index, 0)

        # MA长期组合空头排列（30/60/120）
        if _ma30_slope < 0 and _ma60_slope < 0 and _ma120_slope < 0 \
                and _ma30 < _ma60 < _ma120:
            long_ma_arrange2.insert(index, 1)
        else:
            long_ma_arrange2.insert(index, 0)

        # EMA长期组合空头排列（20/55/120）
        if _ema20_slope < 0 and _ema55_slope < 0 and _ema120_slope < 0 \
                and _ema20 < _ema55 < _ema120:
            long_ema_arrange1.insert(index, 1)
        else:
            long_ema_arrange1.insert(index, 0)

        # EMA长期组合空头排列（30/60/120）
        if _ema30_slope < 0 and _ema60_slope < 0 and _ema120_slope < 0 \
                and _ema30 < _ema60 < _ema120:
            long_ema_arrange2.insert(index, 1)
        else:
            long_ema_arrange2.insert(index, 0)

        # MA死亡交叉（5/10）
        if ma[index][0] < ma[index][1] and ma[index - 1][0] > ma[index - 1][1] and \
                ma_slope[index][0] < 0 and ma_slope[index][1] < 0:
            ma_dead_cross1.insert(index, 1)
        else:
            ma_dead_cross1.insert(index, 0)

        # MA死亡交叉（5/20）
        if ma[index][0] < ma[index][2] and ma[index - 1][0] > ma[index - 1][2] and \
                ma_slope[index][0] < 0 and ma_slope[index][2] < 0:
            ma_dead_cross2.insert(index, 1)
        else:
            ma_dead_cross2.insert(index, 0)

        # MA死亡交叉（10/20）
        if ma[index][1] < ma[index][2] and ma[index - 1][1] > ma[index - 1][2] and \
                ma_slope[index][1] < 0 and ma_slope[index][2] < 0:
            ma_dead_cross3.insert(index, 1)
        else:
            ma_dead_cross3.insert(index, 0)

        # MA死亡交叉（10/30）
        if ma[index][1] < ma[index][3] and ma[index - 1][1] > ma[index - 1][3] and \
                ma_slope[index][1] < 0 and ma_slope[index][3] < 0:
            ma_dead_cross4.insert(index, 1)
        else:
            ma_dead_cross4.insert(index, 0)

        # EMA死亡交叉（5/10）
        if ema[index][0] < ema[index][1] and ema[index - 1][0] > ema[index - 1][1] and \
                ema_slope[index][0] < 0 and ema_slope[index][1] < 0:
            ema_dead_cross1.insert(index, 1)
        else:
            ema_dead_cross1.insert(index, 0)

        # EMA死亡交叉（5/20）
        if ema[index][0] < ema[index][2] and ema[index - 1][0] > ema[index - 1][2] and \
                ema_slope[index][0] < 0 and ema_slope[index][2] < 0:
            ema_dead_cross2.insert(index, 1)
        else:
            ema_dead_cross2.insert(index, 0)

        # EMA死亡交叉（10/20）
        if ema[index][1] < ma[index][2] and ema[index - 1][1] > ema[index - 1][2] and \
                ema_slope[index][1] < 0 and ema_slope[index][2] < 0:
            ema_dead_cross3.insert(index, 1)
        else:
            ema_dead_cross3.insert(index, 0)

        # EMA死亡交叉（10/30）
        if ema[index][1] < ma[index][3] and ema[index - 1][1] > ema[index - 1][3] and \
                ema_slope[index][1] < 0 and ema_slope[index][3] < 0:
            ema_dead_cross4.insert(index, 1)
        else:
            ema_dead_cross4.insert(index, 0)

        # MA银山谷
        if is_ma_dead_valley(index, ma_dead_cross1, ma_dead_cross2, ma_dead_cross3):
            ma_dead_valley.insert(index, 1)
        else:
            ma_dead_valley.insert(index, 0)

        # EMA银山谷
        if is_ema_dead_valley(index, ema_dead_cross1, ema_dead_cross2, ema_dead_cross3):
            ema_dead_valley.insert(index, 1)
        else:
            ema_dead_valley.insert(index, 0)

        # MA金山谷
        if is_ma_dead_valley(index, ma, ma_slope, ma_dead_valley):
            ma_dead_valley.insert(index, 1)
        else:
            ma_dead_valley.insert(index, 0)

        # EMA金山谷
        if is_ema_dead_valley(index, ema, ema_slope, ema_dead_valley):
            ema_dead_valley.insert(index, 1)
        else:
            ema_dead_valley.insert(index, 0)

        is_ma_spider1, is_ma_spider2 = is_ma_spider(index, ma, ma_dead_cross1, ma_dead_cross2,
                                                    ma_dead_cross3, ma_dead_cross4)

        # MA毒蜘蛛
        if is_ma_spider1:
            ma_spider.insert(index, 1)
        else:
            ma_spider.insert(index, 0)

        # MA毒蜘蛛2
        if is_ma_spider2:
            ma_spider2.insert(index, 1)
        else:
            ma_spider2.insert(index, 0)

        is_ema_spider1, is_ema_spider2 = is_ema_spider(index, ema, ema_dead_cross1, ema_dead_cross2,
                                                       ema_dead_cross3, ema_dead_cross4)

        # EMA毒蜘蛛
        if is_ema_spider1:
            ema_spider.insert(index, 1)
        else:
            ema_spider.insert(index, 0)

        # EMA毒蜘蛛2
        if is_ema_spider2:
            ema_spider2.insert(index, 1)
        else:
            ema_spider2.insert(index, 0)

        # TD_8
        if td[index][0] == 8:
            td8.insert(index, 1)
        else:
            td8.insert(index, 0)

        # TD_9
        if td[index][0] == 9:
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

        # ma5/ma10/ma20 出现空头排列
        if is_ma_down_arrange51020(index, ma5, ma10, ma20, ma5_slope, ma10_slope, ma20_slope):
            ma_down_arrange51020.insert(index, 1)
        else:
            ma_down_arrange51020.insert(index, 0)

        # ma5/ma10/ma20/ma30 出现空头排列
        if is_ma_down_arrange5102030(index, ma5, ma10, ma20, ma30, ma5_slope, ma10_slope, ma20_slope, ma30_slope):
            ma_down_arrange5102030.insert(index, 1)
        else:
            ma_down_arrange5102030.insert(index, 0)

        # ma5/ma10/ma20/ma30/ma60 出现空头排列
        if is_ma_down_arrange510203060(index, ma5, ma10, ma20, ma30, ma60, ma5_slope, ma10_slope, ma20_slope,
                                     ma30_slope,
                                     ma60_slope):
            ma_down_arrange510203060.insert(index, 1)
        else:
            ma_down_arrange510203060.insert(index, 0)

        # ma20/ma30/ma60 出现空头排列
        if is_ma_down_arrange203060(index, ma20, ma30, ma60, ma20_slope, ma30_slope, ma60_slope):
            ma_down_arrange203060.insert(index, 1)
        else:
            ma_down_arrange203060.insert(index, 0)

        # ma20/ma60/ma120 出现空头排列
        if is_ma_down_arrange2060120(index, ma20, ma60, ma120, ma20_slope, ma60_slope, ma120_slope):
            ma_down_arrange2060120.insert(index, 1)
        else:
            ma_down_arrange2060120.insert(index, 0)

        # ema5/ema10/ema20 出现空头排列
        if is_ema_down_arrange51020(index, ema5, ema10, ema20, ema5_slope, ema10_slope, ema20_slope):
            ema_down_arrange51020.insert(index, 1)
        else:
            ema_down_arrange51020.insert(index, 0)

        # ema5/ema10/ema20/ema30 出现空头排列
        if is_ema_down_arrange5102030(index, ema5, ema10, ema20, ema30, ema5_slope, ema10_slope, ema20_slope,
                                    ema30_slope):
            ema_down_arrange5102030.insert(index, 1)
        else:
            ema_down_arrange5102030.insert(index, 0)

        # ema5/ema10/ema20/ema30/ema60 出现空头排列
        if is_ema_down_arrange510203060(index, ema5, ema10, ema20, ema30, ema60, ema5_slope, ema10_slope, ema20_slope,
                                      ema30_slope, ema60_slope):
            ema_down_arrange510203060.insert(index, 1)
        else:
            ema_down_arrange510203060.insert(index, 0)

        # ema20/ema30/ema60 出现空头排列
        if is_ema_down_arrange203060(index, ema20, ema30, ema60, ema20_slope, ema30_slope, ema60_slope):
            ema_down_arrange203060.insert(index, 1)
        else:
            ema_down_arrange203060.insert(index, 0)

        # ema20/ema60/ema120 出现空头排列
        if is_ema_down_arrange2055120(index, ema20, ema55, ema120, ema20_slope, ema55_slope, ema120_slope):
            ema_down_arrange2055120.insert(index, 1)
        else:
            ema_down_arrange2055120.insert(index, 0)

    return ma20_down, ema20_down, ma30_down, ema30_down, ma60_down, ema60_down, ma120_down, ema120_down, \
           ma_arrange, ema_arrange, \
           short_ma_arrange1, short_ma_arrange2, short_ema_arrange1, short_ema_arrange2, \
           middle_ma_arrange1, middle_ma_arrange2, middle_ema_arrange1, middle_ema_arrange2, \
           long_ma_arrange1, long_ma_arrange2, long_ema_arrange1, long_ema_arrange2, \
           ma_dead_cross1, ma_dead_cross2, ma_dead_cross3, ma_dead_cross4, \
           ema_dead_cross1, ema_dead_cross2, ema_dead_cross3, ema_dead_cross4, \
           ma_dead_valley, ema_dead_valley, ma_dead_valley, ema_dead_valley, \
           ma_spider, ma_spider2, ema_spider, ema_spider2, \
           ma_glue, ema_glue, ma_out_sea, ema_out_sea, ma_hold_moon, ema_hold_moon, \
           ma_over_gate, ema_over_gate, ma_down_ground, ema_down_ground, td8, td9, \
           bias6, bias12, bias24, bias60, bias72, bias120, \
           stand_down_ma60, stand_down_ma120, stand_down_ema60, stand_down_ema120, \
           ma60_support, ema60_support, ma120_support, ema120_support, \
           ma_group_glue, ema_group_glue, \
           ma_down_arrange51020, ma_down_arrange5102030, ma_down_arrange510203060, \
           ma_down_arrange203060, ma_down_arrange2060120, \
           ema_down_arrange51020, ema_down_arrange5102030, ema_down_arrange510203060, \
           ema_down_arrange203060, ema_down_arrange2055120, \
           hammer, pour_hammer, short_end, swallow_down, attack_short, \
           first_light, sunrise, flat_base


