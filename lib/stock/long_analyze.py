# -- coding: utf-8 -
from lib.signal.common.ma import is_ma20_rise, is_ma30_rise, is_ma60_rise, is_ma120_rise, \
    is_up_hill, is_up_ma_arrange, is_up_short_ma_arrange, is_up_middle_ma_arrange, is_up_long_ma_arrange, \
    is_gold_cross, \
    is_ma60_support, is_ma120_support, is_stand_up_ma60, is_stand_up_ma120, \
    is_ma_glue, is_ma_out_sea, is_ma_hold_moon, is_ma_over_gate, is_ma_up_ground, \
    is_ma_gold_valley, is_ma_silver_valley, is_ma_spider


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

    ema5 = ema[:, 0]
    ema10 = ema[:, 1]
    ema20 = ema[:, 2]
    ema30 = ema[:, 3]
    ema55 = ema[:, 4]
    ema60 = ema[:, 5]
    ema120 = ema[:, 6]

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

    up_hill = []

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

    for index in range(len(candle)):
        # set_yearly_price_position
        high_price = max(high[index - 259: index + 1]) if index >= 260 else max(high)
        low_price = min(low[index - 259: index + 1]) if index >= 260 else min(low)

        price_range = high_price - low_price
        price_pct_position = round((close[index] - low_price) * 100 / price_range, 1)
        yearly_price_position.insert(index, price_pct_position)

        # yearly_price_position
        yearly_price_position10.insert(index, 1 if 10 >= yearly_price_position[index] else 0)
        yearly_price_position20.insert(index, 1 if 20 >= yearly_price_position[index] else 0)
        yearly_price_position30.insert(index, 1 if 30 >= yearly_price_position[index] else 0)
        yearly_price_position50.insert(index, 1 if 50 >= yearly_price_position[index] else 0)
        yearly_price_position70.insert(index, 1 if 70 >= yearly_price_position[index] else 0)

        # MA上行
        ma20_up.insert(index, 1 if is_ma20_rise(index, ma) else 0)
        ema20_up.insert(index, 1 if is_ma20_rise(index, ema) else 0)
        ma30_up.insert(index, 1 if is_ma30_rise(index, ma) else 0)
        ema30_up.insert(index, 1 if is_ma30_rise(index, ema) else 0)
        ma60_up.insert(index, 1 if is_ma60_rise(index, ma) else 0)
        ema60_up.insert(index, 1 if is_ma60_rise(index, ema) else 0)
        ma120_up.insert(index, 1 if is_ma120_rise(index, ma) else 0)
        ema120_up.insert(index, 1 if is_ma120_rise(index, ema) else 0)

        # 上山爬坡
        up_hill.insert(index, 1 if is_up_hill(index, org_df) else 0)
        # MA多头排列（5/10/20/60）
        up_ma_arrange.insert(index, 1 if is_up_ma_arrange(index, ma) else 0)
        # EMA多头排列（5/10/20/60）
        up_ema_arrange.insert(index, 1 if is_up_ma_arrange(index, ema) else 0)
        # MA短期组合多头排列（5/10/20）
        up_short_ma_arrange1.insert(index, 1 if is_up_short_ma_arrange(index, ma5, ma10, ma20) else 0)
        # MA短期组合多头排列（5/10/30）
        up_short_ma_arrange2.insert(index, 1 if is_up_short_ma_arrange(index, ma5, ma10, ma30) else 0)
        # EMA短期组合多头排列（5/10/20）
        up_short_ema_arrange1.insert(index, 1 if is_up_short_ma_arrange(index, ema5, ema10, ema20) else 0)
        # EMA短期组合多头排列（5/10/30）
        up_short_ema_arrange2.insert(index, 1 if is_up_short_ma_arrange(index, ema5, ema10, ema30) else 0)
        # MA中期组合多头排列（10/20/60）
        up_middle_ma_arrange1.insert(index, 1 if is_up_middle_ma_arrange(index, ma10, ma20, ma60) else 0)
        # MA中期组合多头排列（10/20/55）
        up_middle_ma_arrange2.insert(index, 1 if is_up_middle_ma_arrange(index, ma10, ma20, ma55) else 0)
        # EMA中期组合多头排列（10/20/60）
        up_middle_ema_arrange1.insert(index, 1 if is_up_middle_ma_arrange(index, ema10, ema20, ema60) else 0)
        # EMA中期组合多头排列（10/20/55）
        up_middle_ema_arrange2.insert(index, 1 if is_up_middle_ma_arrange(index, ema10, ema20, ema55) else 0)
        # MA长期组合多头排列（20/55/120）
        up_long_ma_arrange1.insert(index, 1 if is_up_long_ma_arrange(index, ma20, ma55, ma120) else 0)
        # MA长期组合多头排列（30/60/120）
        up_long_ma_arrange2.insert(index, 1 if is_up_long_ma_arrange(index, ma30, ma60, ma120) else 0)
        # EMA长期组合多头排列（20/55/120）
        up_long_ema_arrange1.insert(index, 1 if is_up_long_ma_arrange(index, ema20, ema55, ema120) else 0)
        # EMA长期组合多头排列（30/60/120）
        up_long_ema_arrange2.insert(index, 1 if is_up_long_ma_arrange(index, ema30, ema60, ema120) else 0)

        # MA黄金交叉（5/10）
        ma_gold_cross1.insert(index, 1 if is_gold_cross(index, ma5, ma10) else 0)
        # MA黄金交叉（5/20）
        ma_gold_cross2.insert(index, 1 if is_gold_cross(index, ma5, ma20) else 0)
        # MA黄金交叉（10/20）
        ma_gold_cross3.insert(index, 1 if is_gold_cross(index, ma10, ma20) else 0)
        # MA黄金交叉（10/30）
        ma_gold_cross4.insert(index, 1 if is_gold_cross(index, ma10, ma30) else 0)

        # MA银山谷
        ma_silver_valley.insert(index, 1 if is_ma_silver_valley(index,
                                                                ma_gold_cross1, ma_gold_cross2, ma_gold_cross3) else 0)
        # MA金山谷
        ma_gold_valley.insert(index, 1 if is_ma_gold_valley(index, ma, ma_slope, ma_silver_valley) else 0)
        # MA金蜘蛛
        up_ma_spider.insert(index, 1 if is_ma_spider(index, ma, ma_gold_cross1,
                                                     ma_gold_cross2, ma_gold_cross3, ma_gold_cross4) else 0)

        # MA蛟龙出海(5/10/20)
        ma_out_sea.insert(index, 1 if is_ma_out_sea(index, org_df) else 0)
        # MA均线粘合(5/10/20)
        ma_glue.insert(index, 1 if is_ma_glue(index, org_df) else 0)
        # MA烘云托月(5/10/20)
        ma_hold_moon.insert(index, 1 if is_ma_hold_moon(index, org_df) else 0)
        # MA鱼跃龙门(5/10/20)
        ma_over_gate.insert(index, 1 if is_ma_over_gate(index, org_df) else 0)
        # MA旱地拔葱(5/10/20)
        ma_up_ground.insert(index, 1 if is_ma_up_ground(index, org_df) else 0)

        # TD_8
        down_td8.insert(index, 1 if td[index][1] == 8 else 0)
        # TD_9
        down_td9.insert(index, 1 if td[index][1] == 9 else 0)
        # bias6
        down_bias6.insert(index, 1 if bias[index][0] < -3 else 0)
        # bias12
        down_bias12.insert(index, 1 if bias[index][1] < -4.5 else 0)
        # bias24
        down_bias24.insert(index, 1 if bias[index][2] < -7 else 0)
        # bias72
        down_bias72.insert(index, 1 if bias[index][4] < -11 else 0)
        # bias60 不作为单独信号 需结合趋势判断上涨回踩形态
        down_bias60.insert(index, 1 if 1.5 >= bias[index][3] >= -1.5 else 0)
        # bias120 不作为单独信号 需结合趋势判断上涨回踩形态
        down_bias120.insert(index, 1 if 1 >= bias[index][5] >= -1 else 0)

        stand_up_ma60.insert(index, 1 if is_stand_up_ma60(index, org_df) else 0)
        stand_up_ma120.insert(index, 1 if is_stand_up_ma120(index, org_df) else 0)

        ma60_support.insert(index, 1 if is_ma60_support(index, org_df) else 0)
        ma120_support.insert(index, 1 if is_ma120_support(index, org_df) else 0)

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

    org_df['up_hill'] = up_hill

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
