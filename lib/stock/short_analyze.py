# -- coding: utf-8 -
from config.common import START_INDEX
from lib.signal.common.ma import is_ma20_down, is_ma30_down, is_ma60_down, is_ma120_down, \
    is_ema20_down, is_ema30_down, is_ema60_down, is_ema120_down


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

    ma20_down = [0 for _ in range(len(org_df))]
    ema20_down = [0 for _ in range(len(org_df))]
    ma30_down = [0 for _ in range(len(org_df))]
    ema30_down = [0 for _ in range(len(org_df))]
    ma60_down = [0 for _ in range(len(org_df))]
    ema60_down = [0 for _ in range(len(org_df))]
    ma120_down = [0 for _ in range(len(org_df))]
    ema120_down = [0 for _ in range(len(org_df))]

    down_ma_arrange = [0 for _ in range(len(org_df))]
    down_ema_arrange = [0 for _ in range(len(org_df))]

    down_short_ma_arrange1 = [0 for _ in range(len(org_df))]
    down_short_ma_arrange2 = [0 for _ in range(len(org_df))]
    down_short_ema_arrange1 = [0 for _ in range(len(org_df))]
    down_short_ema_arrange2 = [0 for _ in range(len(org_df))]

    down_middle_ma_arrange1 = [0 for _ in range(len(org_df))]
    down_middle_ma_arrange2 = [0 for _ in range(len(org_df))]
    down_middle_ema_arrange1 = [0 for _ in range(len(org_df))]
    down_middle_ema_arrange2 = [0 for _ in range(len(org_df))]

    down_long_ma_arrange1 = [0 for _ in range(len(org_df))]
    down_long_ma_arrange2 = [0 for _ in range(len(org_df))]
    down_long_ema_arrange1 = [0 for _ in range(len(org_df))]
    down_long_ema_arrange2 = [0 for _ in range(len(org_df))]

    ma_dead_cross1 = [0 for _ in range(len(org_df))]
    ma_dead_cross2 = [0 for _ in range(len(org_df))]
    ma_dead_cross3 = [0 for _ in range(len(org_df))]
    ma_dead_cross4 = [0 for _ in range(len(org_df))]

    ma_dead_valley = [0 for _ in range(len(org_df))]

    # 断头铡刀
    ma_knife = [0 for _ in range(len(org_df))]
    # 乌云密布
    ma_dark_cloud = [0 for _ in range(len(org_df))]
    # 战机起航
    ma_set_sail = [0 for _ in range(len(org_df))]
    # 气贯长虹
    ma_supreme = [0 for _ in range(len(org_df))]
    # 绝命跳
    ma_dead_jump = [0 for _ in range(len(org_df))]

    down_ma_spider = [0 for _ in range(len(org_df))]

    up_td8 = [0 for _ in range(len(org_df))]
    up_td9 = [0 for _ in range(len(org_df))]

    up_bias6 = [0 for _ in range(len(org_df))]
    up_bias12 = [0 for _ in range(len(org_df))]
    up_bias24 = [0 for _ in range(len(org_df))]
    up_bias60 = [0 for _ in range(len(org_df))]
    up_bias72 = [0 for _ in range(len(org_df))]
    up_bias120 = [0 for _ in range(len(org_df))]

    _start_at = START_INDEX

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

        if index > _start_at:
            # MA20下行
            ma20_down[index] = is_ma20_down(index, ma)

            # EMA20下行
            ema20_down[index] = is_ema20_down(index, ma)

            # MA30下行
            ma30_down[index] = is_ma30_down(index, ma)

            # EMA30下行
            ema30_down[index] = is_ema30_down(index, ma)

            # MA60下行
            ma60_down[index] = is_ma60_down(index, ma)

            # EMA60下行
            ema60_down[index] = is_ema60_down(index, ma)

            # MA120下行
            ma120_down[index] = is_ma120_down(index, ma)

            # EMA120下行
            ema120_down[index] = is_ema120_down(index, ma)

            # MA空头排列（5/10/20/60）

            if _ma5_slope < 0 and _ma10_slope < 0 and _ma20_slope < 0 and _ma60_slope < 0 \
                    and _ma5 < _ma10 < _ma20 < _ma60:
                down_ma_arrange[index] = 1

            # EMA空头排列（5/10/20/60）
            if _ema5_slope < 0 and _ema10_slope < 0 and _ema20_slope < 0 and _ema60_slope < 0 \
                    and _ema5 < _ema10 < _ema20 < _ema60:
                down_ema_arrange[index] = 1

            # MA短期组合空头排列（5/10/20）
            if _ma5_slope < 0 and _ma10_slope < 0 and _ma20_slope < 0 \
                    and _ma5 < _ma10 < _ma20:
                down_short_ma_arrange1[index] = 1

            # MA短期组合空头排列（5/10/30）
            if _ma5_slope < 0 and _ma10_slope < 0 and _ma30_slope < 0 \
                    and _ma5 < _ma10 < _ma30:
                down_short_ma_arrange2[index] = 1

            # EMA短期组合空头排列（5/10/20）
            if _ema5_slope < 0 and _ema10_slope < 0 and _ema20_slope < 0 \
                    and _ema5 < _ema10 < _ema20:
                down_short_ema_arrange1[index] = 1

            # EMA短期组合空头排列（5/10/30）
            if _ema5_slope < 0 and _ema10_slope < 0 and _ema30_slope < 0 \
                    and _ema5 < _ema10 < _ema30:
                down_short_ema_arrange2[index] = 1

            # MA中期组合空头排列（10/20/60）
            if _ma10_slope < 0 and _ma20_slope < 0 and _ma60_slope < 0 \
                    and _ma10 < _ma20 < _ma60:
                down_middle_ma_arrange1[index] = 1

            # MA中期组合空头排列（10/20/55）
            if _ma10_slope < 0 and _ma20_slope < 0 and _ma55_slope < 0 \
                    and _ma10 < _ma20 < _ma55:
                down_middle_ma_arrange2[index] = 1

            # EMA中期组合空头排列（10/20/60）
            if _ema10_slope < 0 and _ema20_slope < 0 and _ema60_slope < 0 \
                    and _ema10 < _ema20 < _ema60:
                down_middle_ema_arrange1[index] = 1

            # EMA中期组合空头排列（10/20/55）
            if _ema10_slope < 0 and _ema20_slope < 0 and _ema55_slope < 0 \
                    and _ema10 < _ema20 < _ema55:
                down_middle_ema_arrange2[index] = 1

            # MA长期组合空头排列（20/55/120）
            if _ma20_slope < 0 and _ma55_slope < 0 and _ma120_slope < 0 \
                    and _ma20 < _ma55 < _ma120:
                down_long_ma_arrange1[index] = 1

            # MA长期组合空头排列（30/60/120）
            if _ma30_slope < 0 and _ma60_slope < 0 and _ma120_slope < 0 \
                    and _ma30 < _ma60 < _ma120:
                down_long_ma_arrange2[index] = 1

            # EMA长期组合空头排列（20/55/120）
            if _ema20_slope < 0 and _ema55_slope < 0 and _ema120_slope < 0 \
                    and _ema20 < _ema55 < _ema120:
                down_long_ema_arrange1[index] = 1

            # EMA长期组合空头排列（30/60/120）
            if _ema30_slope < 0 and _ema60_slope < 0 and _ema120_slope < 0 \
                    and _ema30 < _ema60 < _ema120:
                down_long_ema_arrange2[index] = 1

            # MA死亡交叉（5/10）
            if ma[index][0] < ma[index][1] and ma[index - 1][0] > ma[index - 1][1] and \
                    ma_slope[index][0] < 0 and ma_slope[index][1] < 0:
                ma_dead_cross1[index] = 1

            # MA死亡交叉（5/20）
            if ma[index][0] < ma[index][2] and ma[index - 1][0] > ma[index - 1][2] and \
                    ma_slope[index][0] < 0 and ma_slope[index][2] < 0:
                ma_dead_cross2[index] = 1

            # MA死亡交叉（10/20）
            if ma[index][1] < ma[index][2] and ma[index - 1][1] > ma[index - 1][2] and \
                    ma_slope[index][1] < 0 and ma_slope[index][2] < 0:
                ma_dead_cross3[index] = 1

            # MA死亡交叉（10/30）
            if ma[index][1] < ma[index][3] and ma[index - 1][1] > ma[index - 1][3] and \
                    ma_slope[index][1] < 0 and ma_slope[index][3] < 0:
                ma_dead_cross4[index] = 1

            # MA死亡谷
            if is_ma_dead_valley(index, ma_dead_cross1, ma_dead_cross2, ma_dead_cross3):
                ma_dead_valley[index] = 1

            # MA毒蜘蛛
            if is_ma_spider(index, ma, ma_dead_cross1, ma_dead_cross2, ma_dead_cross3, ma_dead_cross4):
                down_ma_spider[index] = 1

            # MA断头铡刀
            if is_ma_knife(index, candle, ma, ma_slope):
                ma_knife[index] = 1

            # MA乌云密布
            if is_ma_dark_cloud(index, ma_slope):
                ma_dark_cloud[index] = 1

            # TD_8
            if td[index][0] == 8:
                up_td8[index] = 1

            # TD_9
            if td[index][0] == 9:
                up_td9[index] = 1

            # bias6
            if bias[index][0] < -3:
                up_bias6[index] = 1

            # bias12
            if bias[index][1] < -4.5:
                up_bias12[index] = 1

            # bias24
            if bias[index][2] < -7:
                up_bias24[index] = 1

            # bias72
            if bias[index][4] < -11:
                up_bias72[index] = 1

            # bias60 不作为单独信号 需结合趋势判断上涨回踩形态
            if 1.5 >= bias[index][3] >= -1.5:
                up_bias60[index] = 1

            # bias120 不作为单独信号 需结合趋势判断上涨回踩形态
            if 1 >= bias[index][5] >= -1:
                up_bias120[index] = 1

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

    org_df['ma_dead_valley'] = ma_dead_valley
    org_df['down_ma_spider'] = down_ma_spider
    org_df['ma_knife'] = ma_knife
    org_df['ma_dark_cloud'] = ma_dark_cloud

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

    return org_df


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
