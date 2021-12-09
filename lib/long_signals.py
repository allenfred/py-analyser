import math


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


def is_ma_hold_moon(index, candle, ma, ma_slope, _ma5, _ma10, _ma20, _ma5_slope, _ma10_slope):
    # MA烘云托月(5/10/20)
    # 过滤掉前20根K线
    # 最近9个交易日不能有波动大于3%
    # 最近9个交易日 ma20向上
    # 最近9个交易日 ma5/ma10 在ma20之上
    # ma5/ma10/ma20 某种程度上粘合
    if index > 20 and min(candle[:, 4][index - 8: index + 1]) >= -3 and \
            max(candle[:, 4][index - 8: index + 1]) <= 3 \
            and min(ma_slope[:, 2][index - 8: index + 1]) > 0 \
            and max(ma_slope[:, 2][index - 8: index + 1]) <= 3 \
            and ma_hold(_ma5, _ma10, _ma20, _ma5_slope, _ma10_slope) \
            and ma_hold(ma[index - 1][0], ma[index - 1][1], ma[index - 1][2],
                        ma_slope[index - 1][0], ma_slope[index - 1][1]) \
            and ma_hold(ma[index - 2][0], ma[index - 2][1], ma[index - 2][2],
                        ma_slope[index - 2][0], ma_slope[index - 2][1]) \
            and ma_hold(ma[index - 3][0], ma[index - 3][1], ma[index - 3][2],
                        ma_slope[index - 3][0], ma_slope[index - 3][1]) \
            and ma_hold(ma[index - 4][0], ma[index - 4][1], ma[index - 4][2],
                        ma_slope[index - 4][0], ma_slope[index - 4][1]) \
            and ma_hold(ma[index - 5][0], ma[index - 5][1], ma[index - 5][2],
                        ma_slope[index - 5][0], ma_slope[index - 5][1]) \
            and ma_hold(ma[index - 6][0], ma[index - 6][1], ma[index - 6][2],
                        ma_slope[index - 6][0], ma_slope[index - 6][1]) \
            and ma_hold(ma[index - 7][0], ma[index - 7][1], ma[index - 7][2],
                        ma_slope[index - 7][0], ma_slope[index - 7][1]) \
            and ma_hold(ma[index - 8][0], ma[index - 8][1], ma[index - 8][2],
                        ma_slope[index - 8][0], ma_slope[index - 8][1]):
        return True
    else:
        return False


def is_ema_hold_moon(index, candle, ema, ema_slope, _ema5, _ema10, _ema20, _ema5_slope, _ema10_slope):
    # MA烘云托月(5/10/20)
    # 过滤掉前20根K线
    # 最近9个交易日不能有波动大于3%
    # 最近9个交易日 ma20向上
    # 最近9个交易日 ma5/ma10 在ma20之上
    # ma5/ma10/ma20 某种程度上粘合
    if index > 20 and min(candle[:, 4][index - 8: index + 1]) >= -3 and \
            max(candle[:, 4][index - 8: index + 1]) <= 3 \
            and min(ema_slope[:, 2][index - 8: index + 1]) > 0 \
            and max(ema_slope[:, 2][index - 8: index + 1]) <= 3 \
            and ma_hold(_ema5, _ema10, _ema20, _ema5_slope, _ema10_slope) \
            and ma_hold(ema[index - 1][0], ema[index - 1][1], ema[index - 1][2],
                        ema_slope[index - 1][0], ema_slope[index - 1][1]) \
            and ma_hold(ema[index - 2][0], ema[index - 2][1], ema[index - 2][2],
                        ema_slope[index - 2][0], ema_slope[index - 2][1]) \
            and ma_hold(ema[index - 3][0], ema[index - 3][1], ema[index - 3][2],
                        ema_slope[index - 3][0], ema_slope[index - 3][1]) \
            and ma_hold(ema[index - 4][0], ema[index - 4][1], ema[index - 4][2],
                        ema_slope[index - 4][0], ema_slope[index - 4][1]) \
            and ma_hold(ema[index - 5][0], ema[index - 5][1], ema[index - 5][2],
                        ema_slope[index - 5][0], ema_slope[index - 5][1]) \
            and ma_hold(ema[index - 6][0], ema[index - 6][1], ema[index - 6][2],
                        ema_slope[index - 6][0], ema_slope[index - 6][1]) \
            and ma_hold(ema[index - 7][0], ema[index - 7][1], ema[index - 7][2],
                        ema_slope[index - 7][0], ema_slope[index - 7][1]) \
            and ma_hold(ema[index - 8][0], ema[index - 8][1], ema[index - 8][2],
                        ema_slope[index - 8][0], ema_slope[index - 8][1]):
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