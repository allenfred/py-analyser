# -- coding: utf-8 -
from lib.signal.common.ma import is_ma20_rise, is_ma30_rise, is_ma60_rise, is_ma120_rise, is_up_ma_arrange, \
    is_up_short_ma_arrange1, is_up_short_ma_arrange2, is_ma60_support, is_ma120_support, is_ma_glue


def long_analyze(org_df):
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

    up_ma_arrange = []
    up_ema_arrange = []

    up_short_ma_arrange1 = []
    up_short_ma_arrange2 = []
    up_short_ema_arrange1 = []
    up_short_ema_arrange2 = []

    up_middle_ma_arrange1 = []
    up_middle_ma_arrange2 = []
    up_middle_ema_arrange1 = []
    up_middle_ema_arrange2 = []

    up_long_ma_arrange1 = []
    up_long_ma_arrange2 = []
    up_long_ema_arrange1 = []
    up_long_ema_arrange2 = []

    ma_gold_cross1 = []
    ma_gold_cross2 = []
    ma_gold_cross3 = []
    ma_gold_cross4 = []

    ma_silver_valley = []
    ma_gold_valley = []

    up_ma_spider = []

    ma_out_sea = []
    ma_hold_moon = []
    ma_over_gate = []
    ma_up_ground = []
    ma_glue = []

    down_td8 = []
    down_td9 = []

    down_bias6 = []
    down_bias12 = []
    down_bias24 = []
    down_bias60 = []
    down_bias72 = []
    down_bias120 = []

    ma60_support = []
    ma120_support = []

    stand_up_ma60 = []
    stand_up_ma120 = []

    ma_up_arrange51020 = []
    ma_up_arrange5102030 = []
    ma_up_arrange510203060 = []
    ma_up_arrange203060 = []
    ma_up_arrange2060120 = []

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
        if is_ma20_rise(index, ma):
            ma20_up.insert(index, 1)
        else:
            ma20_up.insert(index, 0)

        # EMA20上行
        if is_ma20_rise(index, ema):
            ema20_up.insert(index, 1)
        else:
            ema20_up.insert(index, 0)

        # MA30上行
        if is_ma30_rise(index, ma):
            ma30_up.insert(index, 1)
        else:
            ma30_up.insert(index, 0)

        # EMA30上行
        if is_ma30_rise(index, ema):
            ema30_up.insert(index, 1)
        else:
            ema30_up.insert(index, 0)

        # MA60上行
        if is_ma60_rise(index, ma):
            ma60_up.insert(index, 1)
        else:
            ma60_up.insert(index, 0)

        # EMA60上行
        if is_ma60_rise(index, ema):
            ema60_up.insert(index, 1)
        else:
            ema60_up.insert(index, 0)

        # MA120上行
        if is_ma120_rise(index, ma):
            ma120_up.insert(index, 1)
        else:
            ma120_up.insert(index, 0)

        # EMA120上行
        if is_ma120_rise(index, ema):
            ema120_up.insert(index, 1)
        else:
            ema120_up.insert(index, 0)

        # MA多头排列（5/10/20/60）
        if is_up_ma_arrange(index, ma):
            up_ma_arrange.insert(index, 1)
        else:
            up_ma_arrange.insert(index, 0)

        # EMA多头排列（5/10/20/60）
        if is_up_ma_arrange(index, ema):
            up_ema_arrange.insert(index, 1)
        else:
            up_ema_arrange.insert(index, 0)

        # MA短期组合多头排列（5/10/20）
        if is_up_short_ma_arrange1(index, ma):
            up_short_ma_arrange1.insert(index, 1)
        else:
            up_short_ma_arrange1.insert(index, 0)

        # MA短期组合多头排列（5/10/30）
        if is_up_short_ma_arrange2(index, ma):
            up_short_ma_arrange2.insert(index, 1)
        else:
            up_short_ma_arrange2.insert(index, 0)

        # EMA短期组合多头排列（5/10/20）
        if is_up_short_ma_arrange1(index, ema):
            up_short_ema_arrange1.insert(index, 1)
        else:
            up_short_ema_arrange1.insert(index, 0)

        # EMA短期组合多头排列（5/10/30）
        if is_up_short_ma_arrange2(index, ema):
            up_short_ema_arrange2.insert(index, 1)
        else:
            up_short_ema_arrange2.insert(index, 0)

        # MA中期组合多头排列（10/20/60）
        if _ma10_slope > 0 and _ma20_slope > 0 and _ma60_slope > 0 \
                and _ma10 > _ma20 > _ma60:
            up_middle_ma_arrange1.insert(index, 1)
        else:
            up_middle_ma_arrange1.insert(index, 0)

        # MA中期组合多头排列（10/20/55）
        if _ma10_slope > 0 and _ma20_slope > 0 and _ma55_slope > 0 \
                and _ma10 > _ma20 > _ma55:
            up_middle_ma_arrange2.insert(index, 1)
        else:
            up_middle_ma_arrange2.insert(index, 0)

        # EMA中期组合多头排列（10/20/60）
        if _ema10_slope > 0 and _ema20_slope > 0 and _ema60_slope > 0 \
                and _ema10 > _ema20 > _ema60:
            up_middle_ema_arrange1.insert(index, 1)
        else:
            up_middle_ema_arrange1.insert(index, 0)

        # EMA中期组合多头排列（10/20/55）
        if _ema10_slope > 0 and _ema20_slope > 0 and _ema55_slope > 0 \
                and _ema10 > _ema20 > _ema55:
            up_middle_ema_arrange2.insert(index, 1)
        else:
            up_middle_ema_arrange2.insert(index, 0)

        # MA长期组合多头排列（20/55/120）
        if _ma20_slope > 0 and _ma55_slope > 0 and _ma120_slope > 0 \
                and _ma20 > _ma55 > _ma120:
            up_long_ma_arrange1.insert(index, 1)
        else:
            up_long_ma_arrange1.insert(index, 0)

        # MA长期组合多头排列（30/60/120）
        if _ma30_slope > 0 and _ma60_slope > 0 and _ma120_slope > 0 \
                and _ma30 > _ma60 > _ma120:
            up_long_ma_arrange2.insert(index, 1)
        else:
            up_long_ma_arrange2.insert(index, 0)

        # EMA长期组合多头排列（20/55/120）
        if _ema20_slope > 0 and _ema55_slope > 0 and _ema120_slope > 0 \
                and _ema20 > _ema55 > _ema120:
            up_long_ema_arrange1.insert(index, 1)
        else:
            up_long_ema_arrange1.insert(index, 0)

        # EMA长期组合多头排列（30/60/120）
        if _ema30_slope > 0 and _ema60_slope > 0 and _ema120_slope > 0 \
                and _ema30 > _ema60 > _ema120:
            up_long_ema_arrange2.insert(index, 1)
        else:
            up_long_ema_arrange2.insert(index, 0)

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

        # MA银山谷
        if is_ma_silver_valley(index, ma_gold_cross1, ma_gold_cross2, ma_gold_cross3):
            ma_silver_valley.insert(index, 1)
        else:
            ma_silver_valley.insert(index, 0)

        # MA金山谷
        if is_ma_gold_valley(index, ma, ma_slope, ma_silver_valley):
            ma_gold_valley.insert(index, 1)
        else:
            ma_gold_valley.insert(index, 0)

        # MA金蜘蛛
        if is_ma_spider(index, ma, ma_gold_cross1, ma_gold_cross2, ma_gold_cross3, ma_gold_cross4):
            up_ma_spider.insert(index, 1)
        else:
            up_ma_spider.insert(index, 0)

        # MA蛟龙出海(5/10/20)
        # 大阳线 贯穿ma5/ma10/ma20
        # ma20 上行
        if _pct_chg >= 4 and _open < _ma5 and _open < _ma10 and _open < _ma20 and \
                _close > _ma5 and _close > _ma10 and _close > _ma20 and _ma60_slope > 0:
            ma_out_sea.insert(index, 1)
        else:
            ma_out_sea.insert(index, 0)

        # MA均线粘合(5/10/20)
        if is_ma_glue(index, ma, org_df):
            ma_glue.insert(index, 1)
        else:
            ma_glue.insert(index, 0)

        # MA烘云托月(5/10/20)
        if is_ma_hold_moon(index, ma, org_df):
            ma_hold_moon.insert(index, 1)
        else:
            ma_hold_moon.insert(index, 0)

        # MA鱼跃龙门(5/10/20)
        if is_ma_over_gate(index, _close, _pct_chg, candle, ma, _ma5, _ma10, _ma20, ma_slope):
            ma_over_gate.insert(index, 1)
        else:
            ma_over_gate.insert(index, 0)

        # MA旱地拔葱(5/10/20)
        if is_ma_up_ground(index, _pct_chg, open, high, low, close, ma5, ma10, ma20):
            ma_up_ground.insert(index, 1)
        else:
            ma_up_ground.insert(index, 0)

        # TD_8
        if td[index][1] == 8:
            down_td8.insert(index, 1)
        else:
            down_td8.insert(index, 0)

        # TD_9
        if td[index][1] == 9:
            down_td9.insert(index, 1)
        else:
            down_td9.insert(index, 0)

        # bias6
        if bias[index][0] < -3:
            down_bias6.insert(index, 1)
        else:
            down_bias6.insert(index, 0)

        # bias12
        if bias[index][1] < -4.5:
            down_bias12.insert(index, 1)
        else:
            down_bias12.insert(index, 0)

        # bias24
        if bias[index][2] < -7:
            down_bias24.insert(index, 1)
        else:
            down_bias24.insert(index, 0)

        # bias72
        if bias[index][4] < -11:
            down_bias72.insert(index, 1)
        else:
            down_bias72.insert(index, 0)

        # bias60 不作为单独信号 需结合趋势判断上涨回踩形态
        if 1.5 >= bias[index][3] >= -1.5:
            down_bias60.insert(index, 1)
        else:
            down_bias60.insert(index, 0)

        # bias120 不作为单独信号 需结合趋势判断上涨回踩形态
        if 1 >= bias[index][5] >= -1:
            down_bias120.insert(index, 1)
        else:
            down_bias120.insert(index, 0)

        # 最近3个交易日站上 ma60/ma120 ema60/ema120
        if is_stand_up_ma60(index, open, close, ma60, ma60_slope):
            stand_up_ma60.insert(index, 1)
        else:
            stand_up_ma60.insert(index, 0)

        if is_stand_up_ma120(index, open, close, ma120, ma120_slope):
            stand_up_ma120.insert(index, 1)
        else:
            stand_up_ma120.insert(index, 0)

        # 连续两日K线在ma60上方收出下影线 / 或遇支撑
        if is_ma60_support(index, candle, ma, ma_slope, org_df):
            ma60_support.insert(index, 1)
        else:
            ma60_support.insert(index, 0)

        # 连续两日K线在ma120上方收出下影线 / 或遇支撑
        if is_ma120_support(index, candle, ma, ma_slope, org_df):
            ma120_support.insert(index, 1)
        else:
            ma120_support.insert(index, 0)

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

    org_df['up_ma_arrange'] = up_ma_arrange
    org_df['up_ema_arrange'] = up_ema_arrange

    org_df['up_short_ma_arrange1'] = up_short_ma_arrange1
    org_df['up_short_ma_arrange2'] = up_short_ma_arrange2
    org_df['up_short_ema_arrange1'] = up_short_ema_arrange1
    org_df['up_short_ema_arrange2'] = up_short_ema_arrange2

    org_df['up_middle_ma_arrange1'] = up_middle_ma_arrange1
    org_df['up_middle_ma_arrange2'] = up_middle_ma_arrange2
    org_df['up_middle_ema_arrange1'] = up_middle_ema_arrange1
    org_df['up_middle_ema_arrange2'] = up_middle_ema_arrange2

    org_df['up_long_ma_arrange1'] = up_long_ma_arrange1
    org_df['up_long_ma_arrange2'] = up_long_ma_arrange2
    org_df['up_long_ema_arrange1'] = up_long_ema_arrange1
    org_df['up_long_ema_arrange2'] = up_long_ema_arrange2

    org_df['ma_gold_cross1'] = ma_gold_cross1
    org_df['ma_gold_cross2'] = ma_gold_cross2
    org_df['ma_gold_cross3'] = ma_gold_cross3
    org_df['ma_gold_cross4'] = ma_gold_cross4

    org_df['ma_silver_valley'] = ma_silver_valley
    org_df['ma_gold_valley'] = ma_gold_valley
    org_df['up_ma_spider'] = up_ma_spider
    org_df['ma_glue'] = ma_glue
    org_df['ma_out_sea'] = ma_out_sea
    org_df['ma_hold_moon'] = ma_hold_moon
    org_df['ma_over_gate'] = ma_over_gate
    org_df['ma_up_ground'] = ma_up_ground

    org_df['down_td8'] = down_td8
    org_df['down_td9'] = down_td9

    org_df['down_bias6'] = down_bias6
    org_df['down_bias12'] = down_bias12
    org_df['down_bias24'] = down_bias24
    org_df['down_bias60'] = down_bias60
    org_df['down_bias72'] = down_bias72
    org_df['down_bias120'] = down_bias120

    org_df['stand_up_ma60'] = stand_up_ma60
    org_df['stand_up_ma120'] = stand_up_ma120

    org_df['ma60_support'] = ma60_support
    org_df['ma120_support'] = ma120_support

    return org_df


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


def ma_hold(ma5, ma10, ma20, ma5_slope, ma10_slope):
    if ma5 > ma20 and ma10 > ma20 and ma5_slope < 5 and ma10_slope < 5:
        return True
    return False


def is_stand_up_ma60(index, open, close, ma60, ma60_slope):
    if index < 90:
        return False

    # 前55个交易日(除最近3个交易日外) ma60向下运行
    ma60_down_still = True
    close_down_still = True
    ma60_up_recently = False

    if max(ma60_slope[index - 55: index - 2]) >= 0:
        ma60_down_still = False

    # 最近3个交易日收盘价高于 ma60
    # 最近3个交易日 ma60 开始向上
    if close[index] > ma60[index] and close[index - 1] > ma60[index - 1] and \
            close[index - 2] > ma60[index - 2] and \
            ma60[index] > ma60[index - 1] > ma60[index - 2]:
        ma60_up_recently = True

    if close_down_still and ma60_down_still and ma60_up_recently:
        return True
    else:
        return False


def is_stand_up_ma120(index, open, close, ma120, ma120_slope):
    if index < 160:
        return 0

    # 前89个交易日(除最近3个交易日外) ma120向下运行
    ma120_down_still = True
    close_down_still = True
    ma120_up_recently = False

    if max(ma120_slope[index - 89: index - 2]) >= 0:
        ma120_down_still = False

    # 最近3个交易日收盘价高于 ma120
    # 最近3个交易日 ma120 开始向上
    if close[index] > ma120[index] and close[index - 1] > ma120[index - 1] and \
            close[index - 2] > ma120[index - 2] and \
            ma120_slope[index] > 0 and ma120_slope[index - 1] > 0 and \
            ma120[index] > ma120[index - 1] > ma120[index - 2] > ma120[index - 3]:
        ma120_up_recently = True

    if close_down_still and ma120_down_still and ma120_up_recently:
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


def is_ma_spider(index, ma, ma_gold_cross1, ma_gold_cross2, ma_gold_cross3, ma_gold_cross4):
    # MA金蜘蛛
    # 最近3个交易日ma5/ma10/ma20交叉于一点 (即出现至少1个金叉)
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

    flag = False

    # MA金蜘蛛
    if index > 20 and gold_cross_cnt > 0 and \
     (ma[index - 1][0] == ma[index - 1][1] == ma[index - 1][2] or
            ma[index - 1][0] == ma[index - 1][1] == ma[index - 1][3]) :
        flag = True

    return flag


def is_ma_hold_moon(index, ma, df):
    """
    MA烘云托月 (5/10/20) / (5/10/30)
    最近 7 个交易日
    均线粘合
    ma20向上 / ma30向上

    :param index:
    :param ma:
    :param df:
    :return:
    """

    _count = 8 - 1
    ma20 = ma[:, 2]
    ma30 = ma[:, 3]

    def ma20_rise_steady():
        flag = True
        for i in range(_count):
            # 如果 当前 MA20 < 前值
            if ma20[index - i] < ma20[index - i - 1]:
                flag = False
        return flag

    def ma30_rise_steady():
        flag = True
        for i in range(_count):
            # 如果 当前 MA30 < 前值
            if ma30[index - i] < ma30[index - i - 1]:
                flag = False
        return flag

    if index > 60 and (ma20_rise_steady() or ma30_rise_steady()) and is_ma_glue(index, ma, df):
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


def is_ma_gold_valley(index, ma, ma_slope, ma_silver_valley):
    # MA金山谷
    # 最近30个交易日内形成两次银山谷视为金山谷
    if index >= 30 and max(ma_silver_valley[index - 29: index - 1]) == 1 and \
            ma_silver_valley[index] == 1 and ma[index - 30][2] < ma[index][2] and \
            ma_slope[index][2] > 0:
        return True
    else:
        return False