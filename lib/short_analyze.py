# -- coding: utf-8 -

from .signal.stock.candle import is_long_end, is_swallow_down, \
    is_hang_neck, is_shooting, is_jump_line, is_up_screw
from .signal.stock.ma60 import is_ma60_fifth, is_ma60_sixth, is_ma60_seventh, is_ma60_eighth
from .signal.stock.ma55 import is_ma55_fifth, is_ma55_sixth, is_ma55_seventh, is_ma55_eighth
from .signal.stock.ema60 import is_ema60_fifth, is_ema60_sixth, is_ema60_seventh, is_ema60_eighth
from .signal.stock.ema55 import is_ema55_fifth, is_ema55_sixth, is_ema55_seventh, is_ema55_eighth


# def short_analyze(candle, ma, ema, ma_slope, ema_slope, bias, td):
def short_analyze(org_df):
    """
    计算空头信号

    :return: df
    """

    candle = org_df[['open', 'high', 'low', 'close', 'pct_chg', 'trade_date']].to_numpy()
    ma = org_df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    ema = org_df[['ema5', 'ema10', 'ema20', 'ema30', 'ema55', 'ema60', 'ema120']].to_numpy()
    ma_slope = org_df[['ma5_slope', 'ma10_slope', 'ma20_slope', 'ma30_slope', 'ma55_slope',
                       'ma60_slope', 'ma120_slope']].to_numpy()
    ema_slope = org_df[['ema5_slope', 'ema10_slope', 'ema20_slope', 'ema30_slope', 'ema55_slope',
                        'ema60_slope', 'ema120_slope']].to_numpy()
    bias = org_df[['bias6', 'bias12', 'bias24', 'bias55', 'bias60', 'bias72', 'bias120']].to_numpy()
    td = org_df[['high_td', 'low_td']].to_numpy()

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

    down_ma_arrange = []
    down_ema_arrange = []

    ma_down_arrange51020 = []
    ma_down_arrange5102030 = []
    ma_down_arrange510203060 = []
    ma_down_arrange203060 = []
    ma_down_arrange2060120 = []
    ema_down_arrange51020 = []
    ema_down_arrange5102030 = []
    ema_down_arrange510203060 = []
    ema_down_arrange203060 = []
    ema_down_arrange2055120 = []

    down_short_ma_arrange1 = []
    down_short_ma_arrange2 = []
    down_short_ema_arrange1 = []
    down_short_ema_arrange2 = []

    down_middle_ma_arrange1 = []
    down_middle_ma_arrange2 = []
    down_middle_ema_arrange1 = []
    down_middle_ema_arrange2 = []

    down_long_ma_arrange1 = []
    down_long_ma_arrange2 = []
    down_long_ema_arrange1 = []
    down_long_ema_arrange2 = []

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

    # 断头铡刀
    ma_knife = []
    ema_knife = []

    # 乌云密布
    ma_dark_cloud = []
    ema_dark_cloud = []

    # 战机起航
    ma_set_sail = []
    ema_set_sail = []

    # 气贯长虹
    ma_supreme = []
    ema_supreme = []

    # 绝命跳
    ma_dead_jump = []
    ema_dead_jump = []

    down_ma_spider = []
    down_ema_spider = []

    up_td8 = []
    up_td9 = []

    up_bias6 = []
    up_bias12 = []
    up_bias24 = []
    up_bias60 = []
    up_bias72 = []
    up_bias120 = []

    long_end = []
    swallow_down = []
    hang_neck = []
    shooting = []
    jump_line = []
    up_screw = []

    ma55_fifth = []
    ma55_sixth = []
    ma55_seventh = []
    ma55_eighth = []

    ma60_fifth = []
    ma60_sixth = []
    ma60_seventh = []
    ma60_eighth = []

    ema55_fifth = []
    ema55_sixth = []
    ema55_seventh = []
    ema55_eighth = []

    ema60_fifth = []
    ema60_sixth = []
    ema60_seventh = []
    ema60_eighth = []

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
        if index > 60 and max(ma20_slope[index - 4: index]) < 0:
            ma20_down.insert(index, 1)
        else:
            ma20_down.insert(index, 0)

        # EMA20下行
        if index > 60 and max(ema20_slope[index - 4: index]) < 0:
            ema20_down.insert(index, 1)
        else:
            ema20_down.insert(index, 0)

        # MA30下行
        if index > 60 and max(ma30_slope[index - 4: index]) < 0:
            ma30_down.insert(index, 1)
        else:
            ma30_down.insert(index, 0)

        # EMA30下行
        if index > 60 and max(ema30_slope[index - 4: index]) < 0:
            ema30_down.insert(index, 1)
        else:
            ema30_down.insert(index, 0)

        # MA60下行
        if index > 90 and max(ma60_slope[index - 6: index]) < 0:
            ma60_down.insert(index, 1)
        else:
            ma60_down.insert(index, 0)

        # EMA60下行
        if index > 90 and max(ema60_slope[index - 6: index]) < 0:
            ema60_down.insert(index, 1)
        else:
            ema60_down.insert(index, 0)

        # MA120下行
        if index > 150 and max(ma120_slope[index - 13: index]) < 0:
            ma120_down.insert(index, 1)
        else:
            ma120_down.insert(index, 0)

        # EMA120下行
        if index > 150 and max(ema120_slope[index - 13: index]) < 0:
            ema120_down.insert(index, 1)
        else:
            ema120_down.insert(index, 0)

        # MA空头排列（5/10/20/60）
        if _ma5_slope < 0 and _ma10_slope < 0 and _ma20_slope < 0 and _ma60_slope < 0 \
                and _ma5 < _ma10 < _ma20 < _ma60:
            down_ma_arrange.insert(index, 1)
        else:
            down_ma_arrange.insert(index, 0)

        # EMA空头排列（5/10/20/60）
        if _ema5_slope < 0 and _ema10_slope < 0 and _ema20_slope < 0 and _ema60_slope < 0 \
                and _ema5 < _ema10 < _ema20 < _ema60:
            down_ema_arrange.insert(index, 1)
        else:
            down_ema_arrange.insert(index, 0)

        # MA短期组合空头排列（5/10/20）
        if _ma5_slope < 0 and _ma10_slope < 0 and _ma20_slope < 0 \
                and _ma5 < _ma10 < _ma20:
            down_short_ma_arrange1.insert(index, 1)
        else:
            down_short_ma_arrange1.insert(index, 0)

        # MA短期组合空头排列（5/10/30）
        if _ma5_slope < 0 and _ma10_slope < 0 and _ma30_slope < 0 \
                and _ma5 < _ma10 < _ma30:
            down_short_ma_arrange2.insert(index, 1)
        else:
            down_short_ma_arrange2.insert(index, 0)

        # EMA短期组合空头排列（5/10/20）
        if _ema5_slope < 0 and _ema10_slope < 0 and _ema20_slope < 0 \
                and _ema5 < _ema10 < _ema20:
            down_short_ema_arrange1.insert(index, 1)
        else:
            down_short_ema_arrange1.insert(index, 0)

        # EMA短期组合空头排列（5/10/30）
        if _ema5_slope < 0 and _ema10_slope < 0 and _ema30_slope < 0 \
                and _ema5 < _ema10 < _ema30:
            down_short_ema_arrange2.insert(index, 1)
        else:
            down_short_ema_arrange2.insert(index, 0)

        # MA中期组合空头排列（10/20/60）
        if _ma10_slope < 0 and _ma20_slope < 0 and _ma60_slope < 0 \
                and _ma10 < _ma20 < _ma60:
            down_middle_ma_arrange1.insert(index, 1)
        else:
            down_middle_ma_arrange1.insert(index, 0)

        # MA中期组合空头排列（10/20/55）
        if _ma10_slope < 0 and _ma20_slope < 0 and _ma55_slope < 0 \
                and _ma10 < _ma20 < _ma55:
            down_middle_ma_arrange2.insert(index, 1)
        else:
            down_middle_ma_arrange2.insert(index, 0)

        # EMA中期组合空头排列（10/20/60）
        if _ema10_slope < 0 and _ema20_slope < 0 and _ema60_slope < 0 \
                and _ema10 < _ema20 < _ema60:
            down_middle_ema_arrange1.insert(index, 1)
        else:
            down_middle_ema_arrange1.insert(index, 0)

        # EMA中期组合空头排列（10/20/55）
        if _ema10_slope < 0 and _ema20_slope < 0 and _ema55_slope < 0 \
                and _ema10 < _ema20 < _ema55:
            down_middle_ema_arrange2.insert(index, 1)
        else:
            down_middle_ema_arrange2.insert(index, 0)

        # MA长期组合空头排列（20/55/120）
        if _ma20_slope < 0 and _ma55_slope < 0 and _ma120_slope < 0 \
                and _ma20 < _ma55 < _ma120:
            down_long_ma_arrange1.insert(index, 1)
        else:
            down_long_ma_arrange1.insert(index, 0)

        # MA长期组合空头排列（30/60/120）
        if _ma30_slope < 0 and _ma60_slope < 0 and _ma120_slope < 0 \
                and _ma30 < _ma60 < _ma120:
            down_long_ma_arrange2.insert(index, 1)
        else:
            down_long_ma_arrange2.insert(index, 0)

        # EMA长期组合空头排列（20/55/120）
        if _ema20_slope < 0 and _ema55_slope < 0 and _ema120_slope < 0 \
                and _ema20 < _ema55 < _ema120:
            down_long_ema_arrange1.insert(index, 1)
        else:
            down_long_ema_arrange1.insert(index, 0)

        # EMA长期组合空头排列（30/60/120）
        if _ema30_slope < 0 and _ema60_slope < 0 and _ema120_slope < 0 \
                and _ema30 < _ema60 < _ema120:
            down_long_ema_arrange2.insert(index, 1)
        else:
            down_long_ema_arrange2.insert(index, 0)

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

        # MA死亡谷
        if is_ma_dead_valley(index, ma_dead_cross1, ma_dead_cross2, ma_dead_cross3):
            ma_dead_valley.insert(index, 1)
        else:
            ma_dead_valley.insert(index, 0)

        # EMA死亡谷
        if is_ema_dead_valley(index, ema_dead_cross1, ema_dead_cross2, ema_dead_cross3):
            ema_dead_valley.insert(index, 1)
        else:
            ema_dead_valley.insert(index, 0)

        # MA毒蜘蛛
        if is_ma_spider(index, ma, ma_dead_cross1, ma_dead_cross2, ma_dead_cross3, ma_dead_cross4):
            down_ma_spider.insert(index, 1)
        else:
            down_ma_spider.insert(index, 0)

        # EMA毒蜘蛛
        if is_ema_spider(index, ema, ema_dead_cross1, ema_dead_cross2, ema_dead_cross3, ema_dead_cross4):
            down_ema_spider.insert(index, 1)
        else:
            down_ema_spider.insert(index, 0)

        # MA断头铡刀
        if is_ma_knife(index, candle, ma, ma_slope):
            ma_knife.insert(index, 1)
        else:
            ma_knife.insert(index, 0)

        # EMA断头铡刀
        if is_ema_knife(index, candle, ema, ema_slope):
            ema_knife.insert(index, 1)
        else:
            ema_knife.insert(index, 0)

        # MA乌云密布
        if is_ma_dark_cloud(index, ma_slope):
            ma_dark_cloud.insert(index, 1)
        else:
            ma_dark_cloud.insert(index, 0)

        # EMA乌云密布
        if is_ema_dark_cloud(index, ema_slope):
            ema_dark_cloud.insert(index, 1)
        else:
            ema_dark_cloud.insert(index, 0)

        # TD_8
        if td[index][0] == 8:
            up_td8.insert(index, 1)
        else:
            up_td8.insert(index, 0)

        # TD_9
        if td[index][0] == 9:
            up_td9.insert(index, 1)
        else:
            up_td9.insert(index, 0)

        # bias6
        if bias[index][0] < -3:
            up_bias6.insert(index, 1)
        else:
            up_bias6.insert(index, 0)

        # bias12
        if bias[index][1] < -4.5:
            up_bias12.insert(index, 1)
        else:
            up_bias12.insert(index, 0)

        # bias24
        if bias[index][2] < -7:
            up_bias24.insert(index, 1)
        else:
            up_bias24.insert(index, 0)

        # bias72
        if bias[index][4] < -11:
            up_bias72.insert(index, 1)
        else:
            up_bias72.insert(index, 0)

        # bias60 不作为单独信号 需结合趋势判断上涨回踩形态
        if 1.5 >= bias[index][3] >= -1.5:
            up_bias60.insert(index, 1)
        else:
            up_bias60.insert(index, 0)

        # bias120 不作为单独信号 需结合趋势判断上涨回踩形态
        if 1 >= bias[index][5] >= -1:
            up_bias120.insert(index, 1)
        else:
            up_bias120.insert(index, 0)

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

        # 看跌尽头线
        if is_long_end(index, candle):
            long_end.insert(index, 1)
        else:
            long_end.insert(index, 0)

        # 看跌吞没
        if is_swallow_down(index, candle):
            swallow_down.insert(index, 1)
        else:
            swallow_down.insert(index, 0)

        # 吊颈线
        if is_hang_neck(index, candle):
            hang_neck.insert(index, 1)
        else:
            hang_neck.insert(index, 0)

        # 射击之星
        if is_shooting(index, candle):
            shooting.insert(index, 1)
        else:
            shooting.insert(index, 0)

        # 跌停一字板
        if is_jump_line(index, candle):
            jump_line.insert(index, 1)
        else:
            jump_line.insert(index, 0)

        # 看跌螺旋桨
        if is_up_screw(index, candle, ma_slope):
            up_screw.insert(index, 1)
        else:
            up_screw.insert(index, 0)

        # MA55 葛南维第5大法则
        if is_ma55_fifth(index, candle, bias, ma, ma_slope):
            ma55_fifth.insert(index, 1)
        else:
            ma55_fifth.insert(index, 0)

        # MA55 葛南维第6大法则
        if is_ma55_sixth(index, candle, bias, ma, ma_slope):
            ma55_sixth.insert(index, 1)
        else:
            ma55_sixth.insert(index, 0)

        # MA55 葛南维第7大法则
        if is_ma55_seventh(index, candle, bias, ma, ma_slope):
            ma55_seventh.insert(index, 1)
        else:
            ma55_seventh.insert(index, 0)

        # MA55 葛南维第8大法则
        if is_ma55_eighth(index, candle, bias, ma, ma_slope):
            ma55_eighth.insert(index, 1)
        else:
            ma55_eighth.insert(index, 0)

        # MA60 葛南维第5大法则
        if is_ma60_fifth(index, candle, bias, ma, ma_slope):
            ma60_fifth.insert(index, 1)
        else:
            ma60_fifth.insert(index, 0)

        # MA60 葛南维第6大法则
        if is_ma60_sixth(index, candle, bias, ma, ma_slope):
            ma60_sixth.insert(index, 1)
        else:
            ma60_sixth.insert(index, 0)

        # MA60 葛南维第7大法则
        if is_ma60_seventh(index, candle, bias, ma, ma_slope):
            ma60_seventh.insert(index, 1)
        else:
            ma60_seventh.insert(index, 0)

        # MA60 葛南维第8大法则
        if is_ma60_eighth(index, candle, bias, ma, ma_slope):
            ma60_eighth.insert(index, 1)
        else:
            ma60_eighth.insert(index, 0)

        # EMA55 葛南维第5大法则
        if is_ema55_fifth(index, candle, bias, ema, ema_slope):
            ema55_fifth.insert(index, 1)
        else:
            ema55_fifth.insert(index, 0)

        # EMA55 葛南维第6大法则
        if is_ema55_sixth(index, candle, bias, ema, ema_slope):
            ema55_sixth.insert(index, 1)
        else:
            ema55_sixth.insert(index, 0)

        # EMA55 葛南维第7大法则
        if is_ema55_seventh(index, candle, bias, ema, ema_slope):
            ema55_seventh.insert(index, 1)
        else:
            ema55_seventh.insert(index, 0)

        # EMA55 葛南维第8大法则
        if is_ema55_eighth(index, candle, bias, ema, ema_slope):
            ema55_eighth.insert(index, 1)
        else:
            ema55_eighth.insert(index, 0)

        # EMA60 葛南维第5大法则
        if is_ema60_fifth(index, candle, bias, ema, ema_slope):
            ema60_fifth.insert(index, 1)
        else:
            ema60_fifth.insert(index, 0)

        # EMA60 葛南维第6大法则
        if is_ema60_sixth(index, candle, bias, ema, ema_slope):
            ema60_sixth.insert(index, 1)
        else:
            ema60_sixth.insert(index, 0)

        # EMA60 葛南维第7大法则
        if is_ema60_seventh(index, candle, bias, ema, ema_slope):
            ema60_seventh.insert(index, 1)
        else:
            ema60_seventh.insert(index, 0)

        # EMA60 葛南维第8大法则
        if is_ema60_eighth(index, candle, bias, ema, ema_slope):
            ema60_eighth.insert(index, 1)
        else:
            ema60_eighth.insert(index, 0)

    org_df['ma20_down'] = ma20_down
    org_df['ema20_down'] = ema20_down
    org_df['ma30_down'] = ma30_down
    org_df['ema30_down'] = ema30_down
    org_df['ma60_down'] = ma60_down
    org_df['ema60_down'] = ema60_down
    org_df['ma120_down'] = ma120_down
    org_df['ema120_down'] = ema120_down

    org_df['down_ma_arrange'] = down_ma_arrange
    org_df['down_ema_arrange'] = down_ema_arrange

    org_df['down_short_ma_arrange1'] = down_short_ma_arrange1
    org_df['down_short_ma_arrange2'] = down_short_ma_arrange2
    org_df['down_short_ema_arrange1'] = down_short_ema_arrange1
    org_df['down_short_ema_arrange2'] = down_short_ema_arrange2

    org_df['down_middle_ma_arrange1'] = down_middle_ma_arrange1
    org_df['down_middle_ma_arrange2'] = down_middle_ma_arrange2
    org_df['down_middle_ema_arrange1'] = down_middle_ema_arrange1
    org_df['down_middle_ema_arrange2'] = down_middle_ema_arrange2

    org_df['down_short_ma_arrange1'] = down_short_ma_arrange1
    org_df['down_short_ma_arrange2'] = down_short_ma_arrange2
    org_df['down_short_ema_arrange1'] = down_short_ema_arrange1
    org_df['down_short_ema_arrange2'] = down_short_ema_arrange2

    org_df['down_middle_ma_arrange1'] = down_middle_ma_arrange1
    org_df['down_middle_ma_arrange2'] = down_middle_ma_arrange2
    org_df['down_middle_ema_arrange1'] = down_middle_ema_arrange1
    org_df['down_middle_ema_arrange2'] = down_middle_ema_arrange2

    org_df['down_long_ma_arrange1'] = down_long_ma_arrange1
    org_df['down_long_ma_arrange2'] = down_long_ma_arrange2
    org_df['down_long_ema_arrange1'] = down_long_ema_arrange1
    org_df['down_long_ema_arrange2'] = down_long_ema_arrange2

    org_df['ma_dead_cross1'] = ma_dead_cross1
    org_df['ma_dead_cross2'] = ma_dead_cross2
    org_df['ma_dead_cross3'] = ma_dead_cross3
    org_df['ma_dead_cross4'] = ma_dead_cross4

    org_df['ema_dead_cross1'] = ema_dead_cross1
    org_df['ema_dead_cross2'] = ema_dead_cross2
    org_df['ema_dead_cross3'] = ema_dead_cross3
    org_df['ema_dead_cross4'] = ema_dead_cross4

    org_df['ma_dead_valley'] = ma_dead_valley
    org_df['ema_dead_valley'] = ema_dead_valley

    org_df['down_ma_spider'] = down_ma_spider
    org_df['down_ema_spider'] = down_ema_spider

    org_df['ma_knife'] = ma_knife
    org_df['ema_knife'] = ema_knife
    org_df['ma_dark_cloud'] = ma_dark_cloud
    org_df['ema_dark_cloud'] = ema_dark_cloud

    # org_df['ma_set_sail'] = ma_set_sail
    # org_df['ema_set_sail'] = ema_set_sail
    # org_df['ma_supreme'] = ma_supreme
    # org_df['ema_supreme'] = ema_supreme
    # org_df['ma_dead_jump'] = ma_dead_jump
    # org_df['ema_dead_jump'] = ema_dead_jump

    org_df['up_td8'] = up_td8
    org_df['up_td9'] = up_td9

    org_df['up_bias6'] = up_bias6
    org_df['up_bias12'] = up_bias12
    org_df['up_bias24'] = up_bias24
    org_df['up_bias60'] = up_bias60
    org_df['up_bias72'] = up_bias72
    org_df['up_bias120'] = up_bias120

    org_df['ma_down_arrange51020'] = ma_down_arrange51020
    org_df['ma_down_arrange5102030'] = ma_down_arrange5102030
    org_df['ma_down_arrange510203060'] = ma_down_arrange510203060
    org_df['ma_down_arrange203060'] = ma_down_arrange203060
    org_df['ma_down_arrange2060120'] = ma_down_arrange2060120

    org_df['ema_down_arrange51020'] = ema_down_arrange51020
    org_df['ema_down_arrange5102030'] = ema_down_arrange5102030
    org_df['ema_down_arrange510203060'] = ema_down_arrange510203060
    org_df['ema_down_arrange203060'] = ema_down_arrange203060
    org_df['ema_down_arrange2055120'] = ema_down_arrange2055120

    org_df['ma55_fifth'] = ma55_fifth
    org_df['ma55_sixth'] = ma55_sixth
    org_df['ma55_seventh'] = ma55_seventh
    org_df['ma55_eighth'] = ma55_eighth

    org_df['ma60_fifth'] = ma60_fifth
    org_df['ma60_sixth'] = ma60_sixth
    org_df['ma60_seventh'] = ma60_seventh
    org_df['ma60_eighth'] = ma60_eighth

    org_df['ema55_fifth'] = ema55_fifth
    org_df['ema55_sixth'] = ema55_sixth
    org_df['ema55_seventh'] = ema55_seventh
    org_df['ema55_eighth'] = ema55_eighth

    org_df['ema60_fifth'] = ema60_fifth
    org_df['ema60_sixth'] = ema60_sixth
    org_df['ema60_seventh'] = ema60_seventh
    org_df['ema60_eighth'] = ema60_eighth

    org_df['long_end'] = long_end
    org_df['swallow_down'] = swallow_down
    org_df['hang_neck'] = hang_neck
    org_df['shooting'] = shooting
    org_df['jump_line'] = jump_line
    org_df['up_screw'] = up_screw

    return org_df


def is_ma_down_arrange51020(index, ma5, ma10, ma20, ma5_slope, ma10_slope, ma20_slope):
    # ma5/ma10/ma20 出现空头排列
    if index < 1:
        return False

    pre_index = index - 1
    # 前一交易日 未形成空头排列
    # 当前交易日 形成空头排列
    if (not (ma5[pre_index] > ma10[pre_index] > ma20[pre_index] and
             ma5_slope[pre_index] > 0 and ma10_slope[pre_index] > 0 and
             ma20_slope[pre_index] > 0)) \
            and ma5[index] > ma10[index] > ma20[index] \
            and ma5_slope[index] > 0 and ma10_slope[index] > 0 and ma20_slope[index] > 0:
        return True
    else:
        return False


def is_ma_down_arrange5102030(index, ma5, ma10, ma20, ma30, ma5_slope, ma10_slope, ma20_slope, ma30_slope):
    # ma5/ma10/ma20/ma30 出现空头排列
    if index < 1:
        return False

    pre_index = index - 1
    # 前一交易日 未形成空头排列
    # 当前交易日 形成空头排列
    if (not (ma5[pre_index] > ma10[pre_index] > ma20[pre_index] > ma30[pre_index] and
             ma5_slope[pre_index] > 0 and ma10_slope[pre_index] > 0 and
             ma20_slope[pre_index] > 0 and ma30_slope[pre_index] > 0)) \
            and ma5[index] > ma10[index] > ma20[index] > ma30[index] \
            and ma5_slope[index] > 0 and ma10_slope[index] > 0 and ma20_slope[index] > 0 \
            and ma30_slope[index] > 0:
        return True
    else:
        return False


def is_ma_down_arrange510203060(index, ma5, ma10, ma20, ma30, ma60, ma5_slope, ma10_slope, ma20_slope,
                                ma30_slope, ma60_slope):
    # ma5/ma10/ma20/ma30/ma60 出现空头排列
    if index < 1:
        return False

    pre_index = index - 1
    # 前一交易日 未形成空头排列
    # 当前交易日 形成空头排列
    if (not (ma5[pre_index] > ma10[pre_index] > ma20[pre_index] > ma30[pre_index] > ma60[pre_index] and
             ma5_slope[pre_index] > 0 and ma10_slope[pre_index] > 0 and
             ma20_slope[pre_index] > 0 and ma30_slope[pre_index] > 0 and ma60_slope[pre_index] > 0)) \
            and ma5[index] > ma10[index] > ma20[index] > ma30[index] > ma60[index] \
            and ma5_slope[index] > 0 and ma10_slope[index] > 0 and ma20_slope[index] > 0 \
            and ma30_slope[index] > 0 and ma60_slope[index] > 0:
        return True
    else:
        return False


def is_ma_down_arrange203060(index, ma20, ma30, ma60, ma20_slope, ma30_slope, ma60_slope):
    # ma20/ma30/ma60 出现空头排列
    if index == 0:
        return False

    pre_index = index - 1
    # 前一交易日 未形成空头排列
    # 当前交易日 形成空头排列
    if (not (ma20[pre_index] > ma30[pre_index] > ma60[pre_index] and
             ma20_slope[pre_index] > 0 and ma30_slope[pre_index] > 0 and ma60_slope[pre_index] > 0)) \
            and ma20[index] > ma30[index] > ma60[index] \
            and ma20_slope[index] > 0 and ma30_slope[index] > 0 and ma60_slope[index] > 0:
        return True
    else:
        return False


def is_ma_down_arrange2060120(index, ma20, ma60, ma120, ma20_slope, ma60_slope, ma120_slope):
    # ma20/ma60/ma120 出现空头排列
    if index < 1:
        return False

    pre_index = index - 1
    # 前一交易日 未形成空头排列
    # 当前交易日 形成空头排列
    if (not (ma20[pre_index] > ma60[pre_index] > ma120[pre_index] and
             ma20_slope[pre_index] > 0 and ma60_slope[pre_index] > 0 and ma120_slope[pre_index] > 0)) \
            and ma20[index] > ma60[index] > ma120[index] \
            and ma20_slope[index] > 0 and ma60_slope[index] > 0 and ma120_slope[index] > 0:
        return True
    else:
        return False


def is_ema_down_arrange51020(index, ema5, ema10, ema20, ema5_slope, ema10_slope, ema20_slope):
    # ema5/ema10/ema20 出现空头排列
    if index < 1:
        return False

    pre_index = index - 1
    # 前一交易日 未形成空头排列
    # 当前交易日 形成空头排列
    if (not (ema5[pre_index] > ema10[pre_index] > ema20[pre_index] and
             ema5_slope[pre_index] > 0 and ema10_slope[pre_index] > 0 and ema20_slope[pre_index] > 0)) \
            and ema5[index] > ema10[index] > ema20[index] \
            and ema5_slope[index] > 0 and ema10_slope[index] > 0 and ema20_slope[index] > 0:
        return True
    else:
        return False


def is_ema_down_arrange5102030(index, ema5, ema10, ema20, ema30, ema5_slope, ema10_slope, ema20_slope, ema30_slope):
    # ema5/ema10/ema20/ema30 出现空头排列
    if index < 1:
        return False

    pre_index = index - 1

    # 前一交易日 未形成空头排列
    # 当前交易日 形成空头排列
    if (not (ema5[pre_index] > ema10[pre_index] > ema20[pre_index] > ema30[pre_index] and
             (ema5_slope[pre_index] > 0 and ema10_slope[pre_index] > 0 and
              ema20_slope[pre_index] > 0 and ema30_slope[pre_index] > 0))) \
            and ema5[index] > ema10[index] > ema20[index] > ema30[index] and \
            ema5_slope[index] > 0 and ema10_slope[index] > 0 and ema20_slope[index] > 0 and ema30_slope[index] > 0:
        return True
    else:
        return False


def is_ema_down_arrange510203060(index, ema5, ema10, ema20, ema30, ema60, ema5_slope, ema10_slope, ema20_slope,
                                 ema30_slope, ema60_slope):
    # ema5/ema10/ema20/ema30/ema60 出现空头排列
    if index < 1:
        return False

    pre_index = index - 1

    # 前一交易日 未形成空头排列
    # 当前交易日 形成空头排列
    if (not (ema5[pre_index] > ema10[pre_index] > ema20[pre_index] > ema30[pre_index] > ema60[pre_index] and
             ema5_slope[pre_index] > 0 and ema10_slope[pre_index] > 0 and
             ema20_slope[pre_index] > 0 and ema30_slope[pre_index] > 0 and ema60_slope[pre_index] > 0)) \
            and ema5[index] > ema10[index] > ema20[index] > ema30[index] > ema60[index] \
            and ema5_slope[index] > 0 and ema10_slope[index] > 0 and ema20_slope[index] > 0 \
            and ema30_slope[index] > 0 and ema60_slope[index] > 0:
        return True
    else:
        return False


def is_ema_down_arrange203060(index, ema20, ema30, ema60, ema20_slope, ema30_slope, ema60_slope):
    # ema20/ema30/ema60 出现空头排列
    if index < 1:
        return False

    # 前一交易日 未形成空头排列
    # 当前交易日 形成空头排列
    if (not (ema20[index - 1] > ema30[index - 1] > ema60[index - 1] and
             ema20_slope[index - 1] > 0 and ema30_slope[index - 1] > 0 and ema60_slope[index - 1] > 0)) \
            and ema20[index] > ema30[index] > ema60[index] \
            and ema20_slope[index] > 0 and ema30_slope[index] > 0 and ema60_slope[index] > 0:
        return True
    else:
        return False


def is_ema_down_arrange2055120(index, ema20, ema55, ema120, ema20_slope, ema55_slope, ema120_slope):
    # ema20/ema55/ema120 出现空头排列
    if index < 1:
        return False

    # 前一交易日 未形成空头排列
    # 当前交易日 形成空头排列
    if (not (ema20[index - 1] > ema55[index - 1] > ema120[index - 1] and
             ema20_slope[index - 1] > 0 and ema55_slope[index - 1] > 0 and ema120_slope[index - 1] > 0)) \
            and ema20[index] > ema55[index] > ema120[index] \
            and ema20_slope[index] > 0 and ema55_slope[index] > 0 and ema120_slope[index] > 0:
        return True
    else:
        return False


def is_ma_spider(index, ma, ma_gold_cross1, ma_gold_cross2, ma_gold_cross3, ma_gold_cross4):
    # MA毒蜘蛛
    # 最近3个交易日ma5/ma10/ma20交叉于一点 (即出现至少2个死叉)
    # 今日ma5/ma10/ma20空头发散
    gold_cross_cnt = 0
    if max(ma_gold_cross1[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1
    if max(ma_gold_cross2[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1
    if max(ma_gold_cross3[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1
    if max(ma_gold_cross4[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1

    is_spider1 = False
    is_spider2 = False

    if gold_cross_cnt > 1 and ma[index][0] > ma[index][1] > ma[index][2]:
        is_spider1 = True

    # MA金蜘蛛2
    if gold_cross_cnt > 2 and ma[index][0] > ma[index][1] > ma[index][2] > ma[index][3]:
        is_spider2 = True

    return is_spider1, is_spider2


def is_ema_spider(index, ema, ema_gold_cross1, ema_gold_cross2, ema_gold_cross3, ema_gold_cross4):
    # EMA毒蜘蛛
    # 最近3个交易日ema5/ema10/ema20交叉于一点 (即出现至少2个死叉)
    # 今日ema5/ema10/ema20空头发散
    ema_gold_cross_cnt = 0
    if max(ema_gold_cross1[index - 2: index + 1]) == 1:
        ema_gold_cross_cnt += 1
    if max(ema_gold_cross2[index - 2: index + 1]) == 1:
        ema_gold_cross_cnt += 1
    if max(ema_gold_cross3[index - 2: index + 1]) == 1:
        ema_gold_cross_cnt += 1
    if max(ema_gold_cross4[index - 2: index + 1]) == 1:
        ema_gold_cross_cnt += 1

    is_spider1 = False
    is_spider2 = False

    # EMA金蜘蛛
    if ema_gold_cross_cnt > 1 and ema[index][0] > ema[index][1] > ema[index][2]:
        is_spider1 = True

    # EMA金蜘蛛2
    if ema_gold_cross_cnt > 2 and ema[index][0] > ema[index][1] > ema[index][2] > ema[index][3]:
        is_spider2 = True

    return is_spider1, is_spider2


def is_ma_dead_valley(index, ma_dead_cross1, ma_dead_cross2, ma_dead_cross3):
    # MA死亡谷
    if index >= 10 and (ma_dead_cross2[index] == 1 or ma_dead_cross3[index] == 1):
        cross_cnt = 0
        if max(ma_dead_cross1[index - 9: index + 1]) == 1:
            cross_cnt += 1
        if max(ma_dead_cross2[index - 9: index + 1]) == 1:
            cross_cnt += 1
        if max(ma_dead_cross3[index - 9: index + 1]) == 1:
            cross_cnt += 1

        if cross_cnt >= 2:
            return True

    return False


def is_ema_dead_valley(index, ema_dead_cross1, ema_dead_cross2, ema_dead_cross3):
    if index >= 10 and (ema_dead_cross2[index] == 1 or ema_dead_cross3[index] == 1):
        cross_cnt = 0
        if max(ema_dead_cross1[index - 9: index + 1]) == 1:
            cross_cnt += 1
        if max(ema_dead_cross2[index - 9: index + 1]) == 1:
            cross_cnt += 1
        if max(ema_dead_cross3[index - 9: index + 1]) == 1:
            cross_cnt += 1

        if cross_cnt >= 2:
            return True

    return False


def is_ma_knife(index, candles, ma, ma_slope):
    # MA断头铡刀(5/10/20)
    # 大阴线/中阴线
    # K线跌破ma5/ma10/ma20
    # 昨日K线未跌破ma5/ma10/ma20
    # 昨日出现均线粘合
    # 过去13个交易日MA20上行

    # 股票 要求涨跌幅不小于 4%
    pre_close = candles[index - 1][3]
    _close = candles[index][3]
    ma5 = ma[:, 0]
    ma10 = ma[:, 1]
    ma20 = ma[:, 2]

    # 股票 要求涨跌幅不小于 4%
    if type == 1 and candles[index][4] < 4:
        return False

    if _close < ma5[index] and _close < ma10[index] and _close < ma20[index] and \
            (pre_close > ma[index - 1][0] or pre_close > ma[index - 1][1] or pre_close > ma[index - 1][2]) and \
            ma_slope[index - 1][2] > 0 and ma[index - 1][0] > ma[index - 1][2] \
            and ma[index - 1][1] > ma[index - 1][2]:
        return True
    else:
        return False


def is_ema_knife(index, candles, ema, ema_slope):
    """
    MA断头铡刀(5/10/20)
    大阴线/中阴线
    K线跌破ema5/ema10/ema20
    昨日K线未跌破ema5/ema10/ema20
    昨日出现均线粘合
    过去13个交易日EMA20上行
    """

    pre_close = candles[index - 1][3]
    _close = candles[index][3]
    ema5 = ema[:, 0]
    ema10 = ema[:, 1]
    ema20 = ema[:, 2]

    # 股票 要求涨跌幅不小于 4%
    if type == 1 and candles[index][4] < 4:
        return False

    if _close < ema5[index] and _close < ema10[index] and _close < ema20[index] and \
            (pre_close > ema[index - 1][0] or pre_close > ema[index - 1][1] or pre_close > ema[index - 1][2]) and \
            ema_slope[index - 1][2] > 0 and ema[index - 1][0] > ema[index - 1][2] \
            and ema[index - 1][1] > ema[index - 1][2]:
        return True
    else:
        return False


def is_ma_dark_cloud(index, ma_slope):
    # MA乌云密布
    # MA20持续下行 压制价格
    # 最近7个交易日 0 > ma20_slope > -0.6
    # 最近7个交易日 -0.5 < ma10_slope < 0.8
    # 最近7个交易日 -0.5 < ma5_slope < 1

    ma5_slope = ma_slope[:, 0]
    ma10_slope = ma_slope[:, 1]
    ma20_slope = ma_slope[:, 2]

    if index > 10 and min(ma20_slope[index - 6: index + 1]) < 0 and max(ma20_slope[index - 6: index + 1]) > -0.6 and \
            min(ma10_slope[index - 6: index + 1]) > -0.5 and max(ma10_slope[index - 6: index + 1]) < 0.8 and \
            min(ma5_slope[index - 6: index + 1]) > -0.5 and max(ma5_slope[index - 6: index + 1]) < 1:
        return True
    else:
        return False


def is_ema_dark_cloud(index, ema_slope):
    # EMA乌云密布
    # EMA20持续下行 压制价格
    # 最近7个交易日 0 > ema20_slope > -0.6
    # 最近7个交易日 -0.5 < ema10_slope < 0.8
    # 最近7个交易日 -0.5 < ema5_slope < 1

    ema5_slope = ema_slope[:, 0]
    ema10_slope = ema_slope[:, 1]
    ema20_slope = ema_slope[:, 2]

    if index > 10 and min(ema20_slope[index - 6: index + 1]) < 0 and max(ema20_slope[index - 6: index + 1]) > -0.6 and \
            min(ema10_slope[index - 6: index + 1]) > -0.5 and max(ema10_slope[index - 6: index + 1]) < 0.8 and \
            min(ema5_slope[index - 6: index + 1]) > -0.5 and max(ema5_slope[index - 6: index + 1]) < 1:
        return True
    else:
        return False


# MA战机起航
def is_ma_set_sail():
    # slope > 75
    return True


def is_ema_set_sail():
    return True


# MA气贯长虹
def is_ma_supreme():
    # slope > 75
    return True


def is_ema_supreme():
    return True


# MA绝命跳
def is_ma_dead_jump():
    return True


def is_ema_dead_jump():
    return True
