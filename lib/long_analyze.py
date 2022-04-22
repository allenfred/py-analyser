# -- coding: utf-8 -

from .signal.stock.candle import is_hammer, is_pour_hammer, is_short_end, is_swallow_up, \
    is_sunrise, is_first_light, is_attack_short, is_flat_base, is_rise_line, is_down_screw
from .signal.stock.ma60 import is_ma60_first, is_ma60_second, is_ma60_third, is_ma60_fourth
from .signal.stock.ma55 import is_ma55_first, is_ma55_second, is_ma55_third, is_ma55_fourth
from .signal.stock.ema60 import is_ema60_first, is_ema60_second, is_ema60_third, is_ema60_fourth
from .signal.stock.ema55 import is_ema55_first, is_ema55_second, is_ema55_third, is_ema55_fourth


def long_analyze(candle, ma, ema, ma_slope, ema_slope, bias, td):
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
    rise_line = []
    down_screw = []

    ma55_first = []
    ma55_second = []
    ma55_third = []
    ma55_fourth = []

    ma60_first = []
    ma60_second = []
    ma60_third = []
    ma60_fourth = []

    ema55_first = []
    ema55_second = []
    ema55_third = []
    ema55_fourth = []

    ema60_first = []
    ema60_second = []
    ema60_third = []
    ema60_fourth = []

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
        if is_ma_hold_moon(index, candle, bias, ma_slope):
            ma_hold_moon.insert(index, 1)
        else:
            ma_hold_moon.insert(index, 0)

        # EMA烘云托月(5/10/20)
        if is_ema_hold_moon(index, candle, bias, ema_slope):
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
        if is_hammer(index, candle):
            hammer.insert(index, 1)
        else:
            hammer.insert(index, 0)

        # 倒锤子线
        if is_pour_hammer(index, candle):
            pour_hammer.insert(index, 1)
        else:
            pour_hammer.insert(index, 0)

        # 看涨尽头线
        if is_short_end(index, candle):
            short_end.insert(index, 1)
        else:
            short_end.insert(index, 0)

        # 看涨吞没
        if is_swallow_up(index, candle):
            swallow_up.insert(index, 1)
        else:
            swallow_up.insert(index, 0)

        # 好友反攻
        if is_attack_short(index, candle):
            attack_short.insert(index, 1)
        else:
            attack_short.insert(index, 0)

        # 曙光初现
        if is_first_light(index, candle):
            first_light.insert(index, 1)
        else:
            first_light.insert(index, 0)

        # 旭日东升
        if is_sunrise(index, candle):
            sunrise.insert(index, 1)
        else:
            sunrise.insert(index, 0)

        # 平底
        if is_flat_base(index, candle):
            flat_base.insert(index, 1)
        else:
            flat_base.insert(index, 0)

        # 涨停一字板
        if is_rise_line(index, candle):
            rise_line.insert(index, 1)
        else:
            rise_line.insert(index, 0)

        # 下跌螺旋桨
        if is_down_screw(index, candle, ma_slope):
            down_screw.insert(index, 1)
        else:
            down_screw.insert(index, 0)

        # MA55 葛南维第一大法则
        if is_ma55_first(index, candle, bias, ma, ma_slope):
            ma55_first.insert(index, 1)
        else:
            ma55_first.insert(index, 0)

        # MA55 葛南维第二大法则
        if is_ma55_second(index, candle, bias, ma, ma_slope):
            ma55_second.insert(index, 1)
        else:
            ma55_second.insert(index, 0)

        # MA55 葛南维第三大法则
        if is_ma55_third(index, candle, bias, ma, ma_slope):
            ma55_third.insert(index, 1)
        else:
            ma55_third.insert(index, 0)

        # MA55 葛南维第四大法则
        if is_ma55_fourth(index, candle, bias, ma, ma_slope):
            ma55_fourth.insert(index, 1)
        else:
            ma55_fourth.insert(index, 0)

        # MA60 葛南维第一大法则
        if is_ma60_first(index, candle, bias, ma, ma_slope):
            ma60_first.insert(index, 1)
        else:
            ma60_first.insert(index, 0)

        # MA60 葛南维第二大法则
        if is_ma60_second(index, candle, bias, ma, ma_slope):
            ma60_second.insert(index, 1)
        else:
            ma60_second.insert(index, 0)

        # MA60 葛南维第三大法则
        if is_ma60_third(index, candle, bias, ma, ma_slope):
            ma60_third.insert(index, 1)
        else:
            ma60_third.insert(index, 0)

        # MA60 葛南维第四大法则
        if is_ma60_fourth(index, candle, bias, ma, ma_slope):
            ma60_fourth.insert(index, 1)
        else:
            ma60_fourth.insert(index, 0)

        # EMA55 葛南维第一大法则
        if is_ema55_first(index, candle, bias, ema, ema_slope):
            ema55_first.insert(index, 1)
        else:
            ema55_first.insert(index, 0)

        # EMA55 葛南维第二大法则
        if is_ema55_second(index, candle, bias, ema, ema_slope):
            ema55_second.insert(index, 1)
        else:
            ema55_second.insert(index, 0)

        # EMA55 葛南维第三大法则
        if is_ema55_third(index, candle, bias, ema, ema_slope):
            ema55_third.insert(index, 1)
        else:
            ema55_third.insert(index, 0)

        # EMA55 葛南维第四大法则
        if is_ema55_fourth(index, candle, bias, ema, ema_slope):
            ema55_fourth.insert(index, 1)
        else:
            ema55_fourth.insert(index, 0)

        # EMA60 葛南维第一大法则
        if is_ema60_first(index, candle, bias, ema, ema_slope):
            ema60_first.insert(index, 1)
        else:
            ema60_first.insert(index, 0)

        # EMA60 葛南维第二大法则
        if is_ema60_second(index, candle, bias, ema, ema_slope):
            ema60_second.insert(index, 1)
        else:
            ema60_second.insert(index, 0)

        # EMA60 葛南维第三大法则
        if is_ema60_third(index, candle, bias, ema, ema_slope):
            ema60_third.insert(index, 1)
        else:
            ema60_third.insert(index, 0)

        # EMA60 葛南维第四大法则
        if is_ema60_fourth(index, candle, bias, ema, ema_slope):
            ema60_fourth.insert(index, 1)
        else:
            ema60_fourth.insert(index, 0)

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
           ma55_first, ma55_second, ma55_third, ma55_fourth, \
           ma60_first, ma60_second, ma60_third, ma60_fourth, \
           ema55_first, ema55_second, ema55_third, ema55_fourth, \
           ema60_first, ema60_second, ema60_third, ema60_fourth, \
           hammer, pour_hammer, short_end, swallow_up, attack_short, \
           first_light, sunrise, flat_base, rise_line, down_screw


def stand_on_ma(open, high, low, close, ma, ma_slope):
    # K线收出下影线
    # K线收盘站稳ma

    # 下影线的最高处
    bottom_shadow_line_high = 0
    # 下影线的最低处
    bottom_shadow_line_low = low

    if close >= open > low:
        bottom_shadow_line_high = open

    if open >= close > low:
        bottom_shadow_line_high = close

    # ma上行
    # 收盘价高于ma
    # ma位于下影线之间
    if ma_slope > 0 and close > ma and \
            bottom_shadow_line_high > ma > bottom_shadow_line_low:
        return True
    else:
        return False


def stand_on_ema(open, high, low, close, ema, ema_slope):
    # K线收出下影线
    # K线收盘站稳ema

    # 下影线的最高处
    bottom_shadow_line_high = 0
    # 下影线的最低处
    bottom_shadow_line_low = low

    if close >= open > low:
        bottom_shadow_line_high = open

    if open >= close > low:
        bottom_shadow_line_high = close

    # ema上行
    # 收盘价高于ema
    # ma位于下影线之间
    if ema_slope > 0 and close > ema and \
            bottom_shadow_line_high > ema > bottom_shadow_line_low:
        return True
    else:
        return False


def ma_hold(ma5, ma10, ma20, ma5_slope, ma10_slope):
    if ma5 > ma20 and ma10 > ma20 and ma5_slope < 5 and ma10_slope < 5:
        return True
    return False


def is_stand_up_ma60(index, open, close, ma60, ma60_slope):
    if index < 60:
        return False

    # 前55个交易日(除最近2个交易日外) ma60向下运行
    ma60_down_still = True
    close_down_still = True
    ma60_up_recently = False

    if max(ma60_slope[index - 55: index - 1]) >= 0:
        ma60_down_still = False

    # 最近2个交易日收盘价高于 ma60
    # 最近2个交易日 ma60 开始向上
    if close[index] > ma60[index] and close[index - 1] > ma60[index - 1] and \
            ma60_slope[index] > 0 and ma60_slope[index - 1] > 0:
        ma60_up_recently = True

    if len(open) > 81 and close_down_still and ma60_down_still and ma60_up_recently:
        return True
    else:
        return False


def is_stand_up_ma120(index, open, close, ma120, ma120_slope):
    if index < 130:
        return 0

    # 前89个交易日(除最近2个交易日外) ma120向下运行
    ma120_down_still = True
    close_down_still = True
    ma120_up_recently = False

    if max(ma120_slope[index - 89: index - 1]) >= 0:
        ma120_down_still = False

    # 最近2个交易日收盘价高于 ma120
    # 最近2个交易日 ma120 开始向上
    if close[index] > ma120[index] and close[index - 1] > ma120[index - 1] and \
            ma120_slope[index] > 0 and ma120_slope[index - 1] > 0:
        ma120_up_recently = True

    if len(open) > 154 and close_down_still and ma120_down_still and ma120_up_recently:
        return True
    else:
        return False


def is_stand_up_ema60(index, open, close, ema60, ema60_slope):
    if index < 60:
        return 0

    # 前55个交易日(除最近2个交易日外) ema60向下运行
    ema60_down_still = True
    close_down_still = True
    ema60_up_recently = False

    if max(ema60_slope[index - 55: index - 1]) >= 0:
        ema60_down_still = False

    # 最近2个交易日收盘价高于 ma60
    # 最近2个交易日 ma60 开始向上
    if close[index] > ema60[index] and close[index - 1] > ema60[index - 1] and \
            ema60_slope[index] > 0 and ema60_slope[index - 1] > 0:
        ema60_up_recently = True

    if len(open) > 81 and close_down_still and ema60_down_still and ema60_up_recently:
        return True
    else:
        return False


def is_stand_up_ema120(index, open, close, ema120, ema120_slope):
    if index < 130:
        return 0

    # 前89个交易日(除最近2个交易日外) ema120向下运行
    ema120_down_still = True
    close_down_still = True
    ema120_up_recently = False

    if max(ema120_slope[index - 89: index - 1]) >= 0:
        ema120_down_still = False

    # 最近2个交易日收盘价高于 ema120
    # 最近2个交易日 ema120 开始向上
    if close[index] > ema120[index] and close[index - 1] > ema120[index - 1] and \
            ema120_slope[index] > 0 and ema120_slope[index - 1] > 0:
        ema120_up_recently = True

    if len(open) > 154 and close_down_still and ema120_down_still and ema120_up_recently:
        return 1
    else:
        return 0


def is_ma60_steady_up(index, ma60_slope):
    # 最近21个交易日 ma60 稳步向上
    if len(ma60_slope) > 81 and min(ma60_slope[index - 20: index + 1]) > 0:
        return 1
    else:
        return 0


def is_ma120_steady_up(index, ma120_slope):
    # 最近34个交易日 ma120 稳步向上
    if len(ma120_slope) > 81 and min(ma120_slope[index - 33: index + 1]) > 0:
        return 1
    else:
        return 0


def is_ema60_steady_up(index, ema60_slope):
    # 最近21个交易日 ema60 稳步向上
    if len(ema60_slope) > 81 and min(ema60_slope[index - 20: index + 1]) > 0:
        return 1
    else:
        return 0


def is_ema120_steady_up(index, ema120_slope):
    # 最近34个交易日 ma120 稳步向上
    if len(ema120_slope) > 81 and min(ema120_slope[index - 33: index + 1]) > 0:
        return 1
    else:
        return 0


def is_ma60_support(index, _open, _high, _low, _close, ma60, ma60_slope):
    # 连续两日K线在ma60上方收出下影线 / 或遇支撑
    if stand_on_ma(_open, _high, _low, _close, ma60[index], ma60_slope[index]) \
            and is_ma60_steady_up(index, ma60_slope):
        return 1
    else:
        return 0


def is_ma120_support(index, _open, _high, _low, _close, ma120, ma120_slope):
    # 连续两日K线在ma120上方收出下影线 / 或遇支撑
    if stand_on_ma(_open, _high, _low, _close, ma120[index], ma120_slope[index]) \
            and is_ma120_steady_up(index, ma120_slope):
        return 1
    else:
        return 0


def is_ema60_support(index, _open, _high, _low, _close, ema60, ema60_slope):
    # 连续两日K线在ema60上方收出下影线 / 或遇支撑
    if stand_on_ema(_open, _high, _low, _close, ema60[index], ema60_slope[index]) \
            and is_ema60_steady_up(index, ema60_slope):
        return 1
    else:
        return 0


def is_ema120_support(index, _open, _high, _low, _close, ema120, ema120_slope):
    # 连续两日K线在ema120上方收出下影线 / 或遇支撑
    if stand_on_ema(_open, _high, _low, _close, ema120[index], ema120_slope[index]) \
            and is_ema120_steady_up(index, ema120_slope):
        return 1
    else:
        return 0


def is_ma_group_glue(index, ma10_slope, ma20_slope, ma30_slope, ma60_slope):
    if index < 10:
        return False

    # 最近9个交易日 0 <= ma60_slope < 0.6
    # 最近9个交易日 0 <= ma30_slope < 0.6
    # 最近9个交易日 0 <= ma20_slope < 0.6
    # 最近9个交易日 -1 < ma10_slope < 1.2
    if min(ma60_slope[index - 8: index + 1]) >= 0 \
            and max(ma60_slope[index - 8: index + 1]) < 0.6 \
            and min(ma30_slope[index - 8: index + 1]) >= 0 \
            and max(ma30_slope[index - 8: index + 1]) < 0.6 \
            and min(ma20_slope[index - 8: index + 1]) >= 0 \
            and max(ma20_slope[index - 8: index + 1]) < 0.6 \
            and min(ma10_slope[index - 8: index + 1]) > -1 \
            and max(ma10_slope[index - 8: index + 1]) < 1.2:
        return True
    else:
        return False


def is_ema_group_glue(index, ema10_slope, ema20_slope, ema30_slope, ema60_slope):
    if index < 10:
        return False

    # 最近9个交易日 0 <= ema60_slope < 0.6
    # 最近9个交易日 0 <= ema30_slope < 0.6
    # 最近9个交易日 0 <= ema20_slope < 0.6
    # 最近9个交易日 -1 < ema10_slope < 1.2
    if min(ema60_slope[index - 8: index + 1]) >= 0 \
            and max(ema60_slope[index - 8: index + 1]) < 0.6 \
            and min(ema30_slope[index - 8: index + 1]) >= 0 \
            and max(ema30_slope[index - 8: index + 1]) < 0.6 \
            and min(ema20_slope[index - 8: index + 1]) >= 0 \
            and max(ema20_slope[index - 8: index + 1]) < 0.6 \
            and min(ema10_slope[index - 8: index + 1]) > -1 \
            and max(ema10_slope[index - 8: index + 1]) < 1.2:
        return True
    else:
        return False


def is_ma_up_arrange51020(index, ma5, ma10, ma20, ma5_slope, ma10_slope, ma20_slope):
    # ma5/ma10/ma20 出现多头排列
    if index < 1:
        return False

    pre_index = index - 1
    # 前一交易日 未形成多头排列
    # 当前交易日 形成多头排列
    if (not (ma5[pre_index] > ma10[pre_index] > ma20[pre_index] and
             ma5_slope[pre_index] > 0 and ma10_slope[pre_index] > 0 and
             ma20_slope[pre_index] > 0)) \
            and ma5[index] > ma10[index] > ma20[index] \
            and ma5_slope[index] > 0 and ma10_slope[index] > 0 and ma20_slope[index] > 0:
        return True
    else:
        return False


def is_ma_up_arrange5102030(index, ma5, ma10, ma20, ma30, ma5_slope, ma10_slope, ma20_slope, ma30_slope):
    # ma5/ma10/ma20/ma30 出现多头排列
    if index < 1:
        return False

    pre_index = index - 1
    # 前一交易日 未形成多头排列
    # 当前交易日 形成多头排列
    if (not (ma5[pre_index] > ma10[pre_index] > ma20[pre_index] > ma30[pre_index] and
             ma5_slope[pre_index] > 0 and ma10_slope[pre_index] > 0 and
             ma20_slope[pre_index] > 0 and ma30_slope[pre_index] > 0)) \
            and ma5[index] > ma10[index] > ma20[index] > ma30[index] \
            and ma5_slope[index] > 0 and ma10_slope[index] > 0 and ma20_slope[index] > 0 \
            and ma30_slope[index] > 0:
        return True
    else:
        return False


def is_ma_up_arrange510203060(index, ma5, ma10, ma20, ma30, ma60, ma5_slope, ma10_slope, ma20_slope,
                              ma30_slope, ma60_slope):
    # ma5/ma10/ma20/ma30/ma60 出现多头排列
    if index < 1:
        return False

    pre_index = index - 1
    # 前一交易日 未形成多头排列
    # 当前交易日 形成多头排列
    if (not (ma5[pre_index] > ma10[pre_index] > ma20[pre_index] > ma30[pre_index] > ma60[pre_index] and
             ma5_slope[pre_index] > 0 and ma10_slope[pre_index] > 0 and
             ma20_slope[pre_index] > 0 and ma30_slope[pre_index] > 0 and ma60_slope[pre_index] > 0)) \
            and ma5[index] > ma10[index] > ma20[index] > ma30[index] > ma60[index] \
            and ma5_slope[index] > 0 and ma10_slope[index] > 0 and ma20_slope[index] > 0 \
            and ma30_slope[index] > 0 and ma60_slope[index] > 0:
        return True
    else:
        return False


def is_ma_up_arrange203060(index, ma20, ma30, ma60, ma20_slope, ma30_slope, ma60_slope):
    # ma20/ma30/ma60 出现多头排列
    if index == 0:
        return False

    pre_index = index - 1
    # 前一交易日 未形成多头排列
    # 当前交易日 形成多头排列
    if (not (ma20[pre_index] > ma30[pre_index] > ma60[pre_index] and
             ma20_slope[pre_index] > 0 and ma30_slope[pre_index] > 0 and ma60_slope[pre_index] > 0)) \
            and ma20[index] > ma30[index] > ma60[index] \
            and ma20_slope[index] > 0 and ma30_slope[index] > 0 and ma60_slope[index] > 0:
        return True
    else:
        return False


def is_ma_up_arrange2060120(index, ma20, ma60, ma120, ma20_slope, ma60_slope, ma120_slope):
    # ma20/ma60/ma120 出现多头排列
    if index < 1:
        return False

    pre_index = index - 1
    # 前一交易日 未形成多头排列
    # 当前交易日 形成多头排列
    if (not (ma20[pre_index] > ma60[pre_index] > ma120[pre_index] and
             ma20_slope[pre_index] > 0 and ma60_slope[pre_index] > 0 and ma120_slope[pre_index] > 0)) \
            and ma20[index] > ma60[index] > ma120[index] \
            and ma20_slope[index] > 0 and ma60_slope[index] > 0 and ma120_slope[index] > 0:
        return True
    else:
        return False


def is_ema_up_arrange51020(index, ema5, ema10, ema20, ema5_slope, ema10_slope, ema20_slope):
    # ema5/ema10/ema20 出现多头排列
    if index < 1:
        return False

    pre_index = index - 1
    # 前一交易日 未形成多头排列
    # 当前交易日 形成多头排列
    if (not (ema5[pre_index] > ema10[pre_index] > ema20[pre_index] and
             ema5_slope[pre_index] > 0 and ema10_slope[pre_index] > 0 and ema20_slope[pre_index] > 0)) \
            and ema5[index] > ema10[index] > ema20[index] \
            and ema5_slope[index] > 0 and ema10_slope[index] > 0 and ema20_slope[index] > 0:
        return True
    else:
        return False


def is_ema_up_arrange5102030(index, ema5, ema10, ema20, ema30, ema5_slope, ema10_slope, ema20_slope, ema30_slope):
    # ema5/ema10/ema20/ema30 出现多头排列
    if index < 1:
        return False

    pre_index = index - 1

    # 前一交易日 未形成多头排列
    # 当前交易日 形成多头排列
    if (not (ema5[pre_index] > ema10[pre_index] > ema20[pre_index] > ema30[pre_index] and
             (ema5_slope[pre_index] > 0 and ema10_slope[pre_index] > 0 and
              ema20_slope[pre_index] > 0 and ema30_slope[pre_index] > 0))) \
            and ema5[index] > ema10[index] > ema20[index] > ema30[index] and \
            ema5_slope[index] > 0 and ema10_slope[index] > 0 and ema20_slope[index] > 0 and ema30_slope[index] > 0:
        return True
    else:
        return False


def is_ema_up_arrange510203060(index, ema5, ema10, ema20, ema30, ema60, ema5_slope, ema10_slope, ema20_slope,
                               ema30_slope, ema60_slope):
    # ema5/ema10/ema20/ema30/ema60 出现多头排列
    if index < 1:
        return False

    pre_index = index - 1

    # 前一交易日 未形成多头排列
    # 当前交易日 形成多头排列
    if (not (ema5[pre_index] > ema10[pre_index] > ema20[pre_index] > ema30[pre_index] > ema60[pre_index] and
             ema5_slope[pre_index] > 0 and ema10_slope[pre_index] > 0 and
             ema20_slope[pre_index] > 0 and ema30_slope[pre_index] > 0 and ema60_slope[pre_index] > 0)) \
            and ema5[index] > ema10[index] > ema20[index] > ema30[index] > ema60[index] \
            and ema5_slope[index] > 0 and ema10_slope[index] > 0 and ema20_slope[index] > 0 \
            and ema30_slope[index] > 0 and ema60_slope[index] > 0:
        return True
    else:
        return False


def is_ema_up_arrange203060(index, ema20, ema30, ema60, ema20_slope, ema30_slope, ema60_slope):
    # ema20/ema30/ema60 出现多头排列
    if index < 1:
        return False

    # 前一交易日 未形成多头排列
    # 当前交易日 形成多头排列
    if (not (ema20[index - 1] > ema30[index - 1] > ema60[index - 1] and
             ema20_slope[index - 1] > 0 and ema30_slope[index - 1] > 0 and ema60_slope[index - 1] > 0)) \
            and ema20[index] > ema30[index] > ema60[index] \
            and ema20_slope[index] > 0 and ema30_slope[index] > 0 and ema60_slope[index] > 0:
        return True
    else:
        return False


def is_ema_up_arrange2055120(index, ema20, ema55, ema120, ema20_slope, ema55_slope, ema120_slope):
    # ema20/ema55/ema120 出现多头排列
    if index < 1:
        return False

    # 前一交易日 未形成多头排列
    # 当前交易日 形成多头排列
    if (not (ema20[index - 1] > ema55[index - 1] > ema120[index - 1] and
             ema20_slope[index - 1] > 0 and ema55_slope[index - 1] > 0 and ema120_slope[index - 1] > 0)) \
            and ema20[index] > ema55[index] > ema120[index] \
            and ema20_slope[index] > 0 and ema55_slope[index] > 0 and ema120_slope[index] > 0:
        return True
    else:
        return False


def is_ma_spider(index, ma, ma_gold_cross1, ma_gold_cross2, ma_gold_cross3, ma_gold_cross4):
    # MA金蜘蛛
    # 最近3个交易日ma5/ma10/ma20交叉于一点 (即出现至少2个金叉)
    # 今日ma5/ma10/ma20多头发散
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
    # EMA金蜘蛛
    # 最近3个交易日ema5/ema10/ema20交叉于一点 (即出现至少2个金叉)
    # 今日ema5/ema10/ema20多头发散
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


def is_ma_hold_moon(index, candles, bias, ma_slope):
    # MA烘云托月(5/10/20)

    # 最近 7 个交易日
    # 不能有波动大于4%
    # ma20向上 / ma30向上
    # ma5/ma10 在ma20之上
    # 乖离率正常区间 bias12 < 5 / bias24 < 8
    # 均线缓慢上行 ma10_slope < 1.5 / ma20_slope < 2 / ma30_slope < 2

    _count = 9 - 1

    if index > 50:
        min_bias6 = min(bias[:, 0][index - _count: index + 1])
        max_bias6 = max(bias[:, 0][index - _count: index + 1])
        min_bias12 = min(bias[:, 1][index - _count: index + 1])
        max_bias12 = max(bias[:, 1][index - _count: index + 1])
        min_bias24 = min(bias[:, 2][index - _count: index + 1])
        max_bias24 = max(bias[:, 2][index - _count: index + 1])

        min_ma10_slope = min(ma_slope[:, 1][index - _count: index + 1])
        max_ma10_slope = max(ma_slope[:, 1][index - _count: index + 1])
        min_ma20_slope = min(ma_slope[:, 2][index - _count: index + 1])
        max_ma20_slope = max(ma_slope[:, 2][index - _count: index + 1])
        min_ma30_slope = min(ma_slope[:, 3][index - _count: index + 1])
        max_ma30_slope = max(ma_slope[:, 3][index - _count: index + 1])

    if index > 50 and min(candles[:, 4][index - _count: index + 1]) >= -4 and \
            max(candles[:, 4][index - _count: index + 1]) <= 4 \
            and min_bias6 > -3 and max_bias6 < 3.5 \
            and min_bias12 > -4.5 and max_bias12 < 5 \
            and min_bias24 > -7 and max_bias24 < 8 \
            and min_ma10_slope >= -1 and max_ma10_slope <= 2 \
            and ((min_ma20_slope >= 0 and max_ma20_slope <= 2) or
                 (min_ma30_slope >= 0 and max_ma30_slope <= 2)):
        return True
    else:
        return False


def is_ema_hold_moon(index, candles, bias, ma_slope):
    # EMA烘云托月(5/10/20)

    # 最近 7 个交易日
    # 不能有波动大于4%
    # ema20向上 / ema30向上
    # ema5/ema10 在ema20之上
    # 乖离率正常区间 bias12 < 5 / bias24 < 8
    # 均线缓慢上行 ema10_slope < 1.5 / ema20_slope < 2 / ema30_slope < 2

    _count = 9 - 1

    if index > 50:
        min_bias6 = min(bias[:, 0][index - _count: index + 1])
        max_bias6 = max(bias[:, 0][index - _count: index + 1])
        min_bias12 = min(bias[:, 1][index - _count: index + 1])
        max_bias12 = max(bias[:, 1][index - _count: index + 1])
        min_bias24 = min(bias[:, 2][index - _count: index + 1])
        max_bias24 = max(bias[:, 2][index - _count: index + 1])

        min_ma10_slope = min(ma_slope[:, 1][index - _count: index + 1])
        max_ma10_slope = max(ma_slope[:, 1][index - _count: index + 1])
        min_ma20_slope = min(ma_slope[:, 2][index - _count: index + 1])
        max_ma20_slope = max(ma_slope[:, 2][index - _count: index + 1])
        min_ma30_slope = min(ma_slope[:, 3][index - _count: index + 1])
        max_ma30_slope = max(ma_slope[:, 3][index - _count: index + 1])

    if index > 50 and min(candles[:, 4][index - _count: index + 1]) >= -4 and \
            max(candles[:, 4][index - _count: index + 1]) <= 4 \
            and min_bias6 > -3 and max_bias6 < 3.5 \
            and min_bias12 > -4.5 and max_bias12 < 5 \
            and min_bias24 > -7 and max_bias24 < 8 \
            and min_ma10_slope >= -1 and max_ma10_slope <= 1.5 \
            and ((min_ma20_slope >= 0 and max_ma20_slope <= 2) or
                 (min_ma30_slope >= 0 and max_ma30_slope <= 2)):
        return True
    else:
        return False


def is_ma_over_gate(index, _close, _pct_chg, candle, ma, _ma5, _ma10, _ma20, ma_slope):
    # MA鱼跃龙门(5/10/20)
    # 大阳线
    # K线站上ma5/ma10/ma20
    # 昨日K线未站上ma5/ma10/ma20
    # 昨日出现均线粘合
    if _pct_chg >= 4 and _close > _ma5 and _close > _ma10 and _close > _ma20 and \
            (candle[index - 1][2] < ma[index - 1][0]
             or candle[index - 1][2] < ma[index - 1][1]
             or candle[index - 1][2] < ma[index - 1][2]) and \
            ma_slope[index - 1][2] > 0 and ma[index - 1][0] > ma[index - 1][2] \
            and ma[index - 1][1] > ma[index - 1][2]:
        return True
    else:
        return False


def is_ema_over_gate(index, _close, _pct_chg, candle, ema, _ema5, _ema10, _ema20, ema_slope):
    # MA鱼跃龙门(5/10/20)
    # 大阳线
    # K线站上ma5/ma10/ma20
    # 昨日K线未站上ma5/ma10/ma20
    # 昨日出现均线粘合
    if _pct_chg >= 4 and _close > _ema5 and _close > _ema10 and _close > _ema20 and \
            (candle[index - 1][2] < ema[index - 1][0]
             or candle[index - 1][2] < ema[index - 1][1]
             or candle[index - 1][2] < ema[index - 1][2]) and \
            ema_slope[index - 1][2] > 0 and ema[index - 1][0] > ema[index - 1][2] \
            and ema[index - 1][1] > ema[index - 1][2]:
        return True
    else:
        return False


def is_ma_up_ground(index, _pct_chg, open, high, low, close, ma5, ma10, ma20):
    # MA旱地拔葱(5/10/20)
    # 大阳线
    # 跳空阳线
    # K线站上ma5/ma10/ma20
    # 昨日K线未站上ma5/ma10/ma20
    if _pct_chg >= 4 and \
            low[index] > high[index - 1] and \
            close[index] > ma5[index] and close[index] > ma10[index] and close[index] > ma20[index] and \
            (low[index - 1] < ma5[index - 1] or
             low[index - 1] < ma10[index - 1] or
             low[index - 1] < ma20[index - 1]) and \
            (open[index - 1] < ma20[index - 1] or
             close[index - 1] < ma20[index - 1]):
        return True
    else:
        return False


def is_ema_up_ground(index, _pct_chg, open, high, low, close, ema5, ema10, ema20):
    # EMA旱地拔葱(5/10/20)
    # 大阳线
    # 跳空阳线
    # K线站上ema5/ema10/ema20
    # 昨日K线未站上ema5/ema10/ema20
    if _pct_chg >= 4 and \
            low[index] > high[index - 1] and \
            close[index] > ema5[index] and close[index] > ema10[index] and close[index] > ema20[index] and \
            (low[index - 1] < ema5[index - 1] or
             low[index - 1] < ema10[index - 1] or
             low[index - 1] < ema20[index - 1]) and \
            (open[index - 1] < ema20[index - 1] or
             close[index - 1] < ema20[index - 1]):
        return True
    else:
        return False


def is_ma_glue(index, ma5_slope, ma10_slope, ma20_slope):
    # MA均线粘合(5/10/20)
    # 最近9个交易日 0 < ma20_slope < 0.6
    # 最近9个交易日 -0.5 < ma10_slope < 0.8
    # 最近9个交易日 -0.5 < ma5_slope < 1
    if index > 10 and min(ma20_slope[index - 8: index + 1]) > 0 and max(ma20_slope[index - 8: index + 1]) < 0.6 and \
            min(ma10_slope[index - 8: index + 1]) > -0.5 and max(ma10_slope[index - 8: index + 1]) < 0.8 and \
            min(ma5_slope[index - 8: index + 1]) > -0.5 and max(ma5_slope[index - 8: index + 1]) < 1:
        return True
    else:
        return False


def is_ema_glue(index, ema5_slope, ema10_slope, ema20_slope):
    # EMA均线粘合(5/10/20)
    # 最近9个交易日 0 < ma20_slope < 0.6
    # 最近9个交易日 -0.5 < ma10_slope < 0.8
    # 最近9个交易日 -0.5 < ma5_slope < 1
    if index > 10 and min(ema20_slope[index - 8: index + 1]) > 0 and max(ema20_slope[index - 8: index + 1]) < 0.6 and \
            min(ema10_slope[index - 8: index + 1]) > -0.5 and max(ema10_slope[index - 8: index + 1]) < 0.8 and \
            min(ema5_slope[index - 8: index + 1]) > -0.5 and max(ema5_slope[index - 8: index + 1]) < 1:
        return True
    else:
        return False


def is_ma_silver_valley(index, ma_gold_cross1, ma_gold_cross2, ma_gold_cross3):
    # MA银山谷
    if index >= 10 and (ma_gold_cross2[index] == 1 or ma_gold_cross3[index] == 1):
        gold_cross_cnt = 0
        if max(ma_gold_cross1[index - 9: index + 1]) == 1:
            gold_cross_cnt += 1
        if max(ma_gold_cross2[index - 9: index + 1]) == 1:
            gold_cross_cnt += 1
        if max(ma_gold_cross3[index - 9: index + 1]) == 1:
            gold_cross_cnt += 1

        if gold_cross_cnt >= 2:
            return True

    return False


def is_ema_silver_valley(index, ema_gold_cross1, ema_gold_cross2, ema_gold_cross3):
    if index >= 10 and (ema_gold_cross2[index] == 1 or ema_gold_cross3[index] == 1):
        gold_cross_cnt = 0
        if max(ema_gold_cross1[index - 9: index + 1]) == 1:
            gold_cross_cnt += 1
        if max(ema_gold_cross2[index - 9: index + 1]) == 1:
            gold_cross_cnt += 1
        if max(ema_gold_cross3[index - 9: index + 1]) == 1:
            gold_cross_cnt += 1

        if gold_cross_cnt >= 2:
            return True

    return False


def is_ma_gold_valley(index, ma, ma_slope, ma_silver_valley):
    # MA金山谷
    # 最近30个交易日内形成两次银山谷视为金山谷
    if index >= 30 and max(ma_silver_valley[index - 29: index - 1]) == 1 and \
            ma_silver_valley[index] == 1 and ma[index - 30][2] < ma[index][2] and \
            ma_slope[index][2] > 0:
        return True
    else:
        return False


def is_ema_gold_valley(index, ema, ema_slope, ema_silver_valley):
    # MA金山谷
    # 最近30个交易日内形成两次银山谷视为金山谷
    if index >= 30 and max(ema_silver_valley[index - 29: index - 1]) == 1 and \
            ema_silver_valley[index] == 1 and ema[index - 30][2] < ema[index][2] and \
            ema_slope[index][2] > 0:
        return True
    else:
        return False


# 葛南维第一大法则
def is_ma_first(index, candles, ma, ma_slope):
    # MA60 开始拐头 (ma60_slope 连续3日 > 0)
    # 收盘价位于MA60之上
    # 最近21个交易日中前18个交易日 ma60_slope < 0

    # 趋势反转信号
    # ma60_slope 刚刚转正 / 连续3日转正

    # 反转看涨增强信号
    # ma60_slope 连续9日增大

    candle = candles[index]
    _close = candle[3]
    ma60_slope = ma_slope[:, 5]
    _ma60 = ma[:, 5][index]

    if index > 90 and _close > _ma60 and max(ma60_slope[index - 21: index - 2]) <= 0 and \
            0 < ma60_slope[index - 2] < ma60_slope[index - 1] < ma60_slope[index]:
        return True
    else:
        return False


# 葛南维第二大法则
def is_ma_second(index, candles, bias, ma, ma_slope):
    # MA60 向上 (ma60_slope 连续9日 > 0) slope > 1
    # 收盘价连续9日在MA60之上
    # 价格回落 未跌破MA60
    # 过去21个交易日未曾跌破 MA60

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma60_slope = ma_slope[:, 5]
    _ma60 = ma[:, 5][index]
    bias60 = bias[:, 3]

    if index > 90 and _ma60 > 0:
        _low_bias60 = (_low - _ma60) * 100 / _ma60

    def steady_on_ma():
        flag = True
        for i in range(13):
            if candles[index - i][3] < ma[:, 5][index - i]:
                flag = False
        return flag

    if index > 90 and steady_on_ma() and min(ma60_slope[index - 8: index]) > 2 and \
            min(bias60[index - 8: index]) > 0 and _low_bias60 < 2:
        return True
    else:
        return False


# 葛南维第三大法则
def is_ma_third(index, candles, bias, ma, ma_slope):
    # MA60 向上 (ma60_slope 连续9日 > 0)
    # 跌破MA60之后收盘又站上MA60

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma60_slope = ma_slope[:, 5]
    _ma60 = ma[:, 5][index]
    bias60 = bias[:, 3]

    if index > 90 and _ma60 > 0:
        _low_bias60 = (_low - _ma60) * 100 / _ma60

    def steady_on_ma():
        flag = 0
        for i in range(13):
            if candles[index - i][3] < ma[:, 5][index - i]:
                flag += 1
        return 0 < flag < 3

    if index > 90 and _close > _ma60 and steady_on_ma() and min(ma60_slope[index - 8: index]) > 2 and \
            candles[index - 1][3] < ma[:, 5][index - 1] and bias60[index] < 8 and _low_bias60 < 0:
        return True
    else:
        return False


# 葛南维第四大法则
def is_ma_fourth(index, candles, bias, ma, ma_slope):
    # MA60 下行 (ma60_slope 连续13日 < 0)
    # 超卖 bias60 < -11%

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma60_slope = ma_slope[:, 5]
    _ma60 = ma[:, 5][index]
    bias60 = bias[:, 3]

    if index > 90 and _ma60 > 0:
        _low_bias60 = (_low - _ma60) * 100 / _ma60

    def steady_under_ma():
        flag = True
        for i in range(13):
            if candles[index - i][3] > ma[:, 5][index - i]:
                flag = False
        return flag

    if index > 90 and bias60[index] < -16 and steady_under_ma() and max(ma60_slope[index - 12: index]) < 0:
        return True
    else:
        return False
