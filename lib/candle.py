def stand_on_ma(df, row, range):
    # K线收出下影线
    # K线收盘站稳ma

    # 下影线的最高处
    bottom_shadow_line_high = 0
    # 下影线的最低处
    bottom_shadow_line_low = row.low

    if row.close >= row.open > row.low:
        bottom_shadow_line_high = row.open

    if row.open >= row.close > row.low:
        bottom_shadow_line_high = row.close

    ma = 0
    ma_slope = 0

    if range == 20:
        ma = row.ma20
        ma_slope = row.ma20_slope

    if range == 30:
        ma = row.ma30
        ma_slope = row.ma30_slope

    if range == 60:
        ma = row.ma60
        ma_slope = row.ma60_slope

    if range == 120:
        ma = row.ma120
        ma_slope = row.ma120_slope

    # ma上行
    # 收盘价高于ma
    # ma位于下影线之间
    if ma_slope > 0 and row.close > ma and \
            bottom_shadow_line_high > ma > bottom_shadow_line_low:
        return True
    else:
        return False


def stand_on_ema(df, row, range):
    # K线收出下影线
    # K线收盘站稳ema

    # 下影线的最高处
    bottom_shadow_line_high = 0
    # 下影线的最低处
    bottom_shadow_line_low = row.low

    if row.close >= row.open > row.low:
        bottom_shadow_line_high = row.open

    if row.open >= row.close > row.low:
        bottom_shadow_line_high = row.close

    ema = 0
    ema_slope = 0

    if range == 20:
        ema = row.ema20
        ema_slope = row.ema20_slope

    if range == 30:
        ema = row.ma30
        ema_slope = row.ema30_slope

    if range == 60:
        ema = row.ema60
        ema_slope = row.ema60_slope

    if range == 120:
        ema = row.ema120
        ema_slope = row.ema120_slope

    # ema上行
    # 收盘价高于ema
    # ma位于下影线之间
    if ema_slope > 0 and row.close > ema and \
            bottom_shadow_line_high > ema > bottom_shadow_line_low:
        return True
    else:
        return False

