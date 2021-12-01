import math as math


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


"""
description: 锤头线 (看涨)
有效标准：
1.市场处于清晰的下降趋势
2.当前K线收出锤头线形态
3.当前K线最低价为近期最低价

param {*} df 行情数据dataFrame
param {*} i 当前时间tick
return {*} Flag:boolean 是否符合
"""


def is_hammer(df, row):
    i = row.name
    if i < 13:
        return False

    open = row.open
    high = row.high
    low = row.low
    close = row.close
    k_len = high - low
    bar_len = math.fabs(open - close)
    up_shadow_len = math.fabs(high - close if open < close else high - open)
    up_one_third = high - (k_len / 3)

    # 最近13日最低价
    lowest_low = df['low'][i - 12: i + 1].min()

    # 开盘价和收盘价都位于k线上方1/3处 (即：下影线长度占k线长度的2/3以上）
    # 上影线长度需小于柱体长度的1/5
    if lowest_low == low and open > up_one_third and close > up_one_third \
            and up_shadow_len < bar_len / 5:
        return True

    return False


"""
description: 倒锤头线 (看涨)
有效标准：
1.市场处于清晰的下降趋势
2.当前K线收出倒锤头线形态
3.当前K线最低价为近期最低价

param {*} df 行情数据dataFrame
param {*} i 当前时间tick
return {*} Flag:boolean 是否符合
"""


def is_pour_hammer(df, row):
    i = row.name
    if i < 13:
        return False

    open = row.open
    high = row.high
    low = row.low
    close = row.close
    k_len = high - low
    bar_len = math.fabs(open - close)
    bottom_shadow_len = math.fabs(open - low if open < close else close - low)
    bottom_one_third = low + (k_len / 3)

    # 最近13日最低价
    lowest_low = df['low'][i - 12: i + 1].min()

    # 开盘价和收盘价都位于k线下方1/3处 (即：上影线长度占k线长度的2/3以上）
    # 下影线长度需小于柱体长度的1/5
    if lowest_low == low and open < bottom_one_third and close < bottom_one_third \
            and bottom_shadow_len < bar_len / 5:
        return True

    return False


"""
description: 吊颈线 (看跌)
有效标准：
1.市场处于清晰的上涨趋势 
2.当前K线收出吊颈线形态
3.当前K线最高价为近期最高价

param {*} df 行情数据dataFrame
param {*} i 当前时间tick
return {*} Flag:boolean 是否符合
"""


def is_hang_neck(df, row):
    i = row.name
    if i < 13:
        return False

    open = row.open
    high = row.high
    low = row.low
    close = row.close
    k_len = high - low
    bar_len = math.fabs(open - close)
    up_shadow_len = math.fabs(high - close if open < close else high - open)
    up_one_third = high - (k_len / 3)

    # 最近13日最高价
    highest_high = df['high'][i - 12: i + 1].min()

    # 开盘价和收盘价都位于k线上方1/3处 (即：下影线长度占k线长度的2/3以上）
    # 上影线长度需小于柱体长度的1/5
    if highest_high == high and open > up_one_third and close > up_one_third \
            and up_shadow_len < bar_len / 5:
        return True

    return False


"""
description: 射击之星 (看跌)
有效标准：
1.市场处于清晰的上涨趋势 
2.当前K线收出射击之星形态
3.当前K线最高价为近期最高价

param {*} df 行情数据dataFrame
param {*} i 当前时间tick
return {*} Flag:boolean 是否符合
"""


def is_shooting(df, row):
    i = row.name
    if i < 13:
        return False

    open = row.open
    high = row.high
    low = row.low
    close = row.close
    bar_len = math.fabs(open - close)
    bottom_shadow_len = math.fabs(open - low if open < close else close - low)
    bottom_one_third = low + (k_len / 3)

    # 最近13日最高价
    highest_high = df['high'][i - 12: i + 1].min()

    # 开盘价和收盘价都位于k线下方1/3处 (即：上影线长度占k线长度的2/3以上）
    # 下影线长度需小于柱体长度的1/5
    if highest_high == high and open < bottom_one_third and close < bottom_one_third \
            and bottom_shadow_len < bar_len / 5:
        return True

    return False


"""
description: 尽头线 (看涨)
有效标准：
1.市场处于清晰的上涨趋势 
2.当前K线收出射击之星形态
3.当前K线最高价为近期最高价

param {*} df 行情数据dataFrame
param {*} i 当前时间tick
return {*} Flag:boolean 是否符合
"""


def is_short_end(df, row):
    i = row.name
    if i < 13:
        return False

    pre_row = df.iloc[i - 1]
    open = row.open
    high = row.high
    low = row.low
    close = row.close
    k_len = high - low
    bar_len = math.fabs(open - close)

    bottom_shadow_len = math.fabs(open - low if open < close else close - low)
    pre_bottom_shadow_high = (open if open < close else close)
    pre_bottom_shadow_low = low

    # 最近13日最低价
    lowest_low = df['low'][i - 12: i + 1].min()

    # 下跌趋势中 前一根K线为中阴线或大阴线
    # 开盘价和收盘价都位于前一K线下影线内
    # 前一根K线下影线长度需小于K线长度的1/2
    # K线实体长度大于K线长度的2/5
    if (lowest_low == pre_row.low or lowest_low == low) and \
            pre_bottom_shadow_high > open > pre_bottom_shadow_low and \
            pre_bottom_shadow_high > close > pre_bottom_shadow_low \
            and bottom_shadow_len < k_len / 2 and bar_len > (k_len * 2) / 5 \
            and pre_row.open > pre_row.close and pre_row.pct_chg < -3:
        return True

    return False


"""
description: 尽头线 (看跌)
有效标准：
1.市场处于清晰的上涨趋势 
2.当前K线收出射击之星形态
3.当前K线最高价为近期最高价

param {*} df 行情数据dataFrame
param {*} i 当前时间tick
return {*} Flag:boolean 是否符合
"""


def is_long_end(df, row):
    i = row.name
    if i < 13:
        return False

    pre_row = df.iloc[i - 1]
    open = row.open
    high = row.high
    low = row.low
    close = row.close
    k_len = high - low
    bar_len = math.fabs(open - close)

    up_shadow_len = math.fabs(high - open if open > close else high - close)
    pre_up_shadow_high = high
    pre_up_shadow_low = (close if open < close else open)

    # 最近13日最高价
    highest_high = df['high'][i - 12: i + 1].min()

    # 上涨趋势中 前一根K线为中阳线或大阳线
    # 开盘价和收盘价都位于前一K线下影线内
    # 前一根K线下影线长度需小于K线长度的1/2
    # K线实体长度大于K线长度的2/5
    if (highest_high == pre_row.high or lowest_low == high) and \
            pre_up_shadow_high > open > pre_up_shadow_low and \
            pre_up_shadow_high > close > pre_up_shadow_low \
            and up_shadow_len < k_len / 2 and bar_len > (k_len * 2) / 5 \
            and pre_row.open < pre_row.close and pre_row.pct_chg > 3:
        return True

    return False


"""
description: 好友反攻 (看涨)
有效标准：
1.市场处于清晰的下跌趋势 
2.当前K线收出好友反攻形态
3.当前K线最低价为近期最低价

param {*} df 行情数据dataFrame
param {*} i 当前时间tick
return {*} Flag:boolean 是否符合
"""


def is_attack_short(df, row):
    i = row.name
    if i < 13:
        return False

    pre_row = df.iloc[i - 1]
    open = row.open
    low = row.low
    close = row.close
    bar_len = math.fabs(open - close)

    # 最近13日最低价
    lowest_low = df['low'][i - 12: i + 1].min()

    # 下跌趋势中 前一根K线为中阴线或大阴线 当日K线为跳空低开的中阳线或大阳线
    # 当日K线跳空低开
    # 当日K线收盘价与前日K线收盘价相近
    if pre_row.pct_chg < -3 and row.pct_chg > 3 and lowest_low == low and \
            pre_row.low > open and (bar_len / 5 + pre_row.close) > close > pre_row.close:
        return True

    return False


"""
description: 曙光初现 (看涨)
有效标准：
1.市场处于清晰的下跌趋势 
2.当前K线收出曙光初现形态
3.当前K线最低价为近期最低价

param {*} df 行情数据dataFrame
param {*} i 当前时间tick
return {*} Flag:boolean 是否符合
"""


def is_first_light(df, row):
    i = row.name
    if i < 13:
        return False

    pre_row = df.iloc[i - 1]
    open = row.open
    low = row.low
    close = row.close
    bar_len = math.fabs(open - close)

    # 最近13日最低价
    lowest_low = df['low'][i - 12: i + 1].min()

    # 下跌趋势中 前一根K线为中阴线或大阴线 当日K线为跳空低开的中阳线或大阳线
    # 当日K线跳空低开
    # 当日K线收盘价插入前日K线实体的1/2 但没有超过前日K线的开盘价
    if pre_row.pct_chg < -3 and row.pct_chg > 3 and lowest_low == low and \
            pre_row.low > open and (bar_len / 2 + pre_row.close) < close < pre_row.open:
        return True

    return False


"""
description: 旭日东升 (看涨)
有效标准：
1.市场处于清晰的下降趋势 
2.当前K线收出旭日东升形态
3.当前K线最低价为近期最低价

param {*} df 行情数据dataFrame
param {*} i 当前时间tick
return {*} Flag:boolean 是否符合
"""


def is_sunrise(df, row):
    i = row.name
    if i < 13:
        return False

    pre_row = df.iloc[i - 1]
    open = row.open
    close = row.close

    # 最近13日最低价
    lowest_low = df['low'][i - 12: i + 1].min()

    # 下跌趋势中 前一根K线为中阴线或大阴线 当日K线为高开的中阳线或大阳线
    # 当日K线收盘价插入前日K线实体的1/2 但没有超过前日K线的开盘价
    if pre_row.pct_chg < -3 and row.pct_chg > 3 and lowest_low == pre_row.low and \
            close > pre_row.open > open > pre_row.close:
        return True

    return False


"""
description: 平底 (看涨)
有效标准：
1.市场处于清晰的下降趋势 
2.当前K线收出平底形态
3.当前K线最低价为近期最低价

param {*} df 行情数据dataFrame
param {*} i 当前时间tick
return {*} Flag:boolean 是否符合
"""


def is_flat_base(df, row):
    i = row.name
    if i < 14:
        return False

    pre_row = df.iloc[i - 1]
    before_pre_row = df.iloc[i - 2]
    # 比较最低价的偏差
    deviation = row.low / 100

    # 最近15日最低价
    lowest_low = df['low'][i - 14: i + 1].min()

    # 下跌趋势中 最近两根K线最低价位于同一水平 / 最近三根K线最低价位于同一水平
    if (lowest_low == row.low or lowest_low == pre_row.low or lowest_low == before_pre_row.low) \
            and math.fabs(row.low - pre_row.low) < deviation \
            and math.fabs(row.low - before_pre_row.low) < deviation:
        return True

    return False


"""
description: 看涨吞没
有效标准：
1.市场处于清晰的下降趋势
2.第二根K线必须吞没第一根
3.第二根实体必须与第一个实体颜色相反
4.之前的趋势超长，或非常剧烈的震荡

param {*} df 行情数据dataFrame
param {*} row 当前时间tick
return {*} Flag:boolean 是否符合
"""


def is_swallow_up(df, row):
    i = row.name
    if i < 13:
        return False

    open = row.open
    close = row.close
    low = row.low

    pre_open = df.open[i - 1]
    pre_close = df.close[i - 1]
    pre_low = df.low[i - 1]

    # 最近13日最低价
    lowest_low = df['low'][i - 12: i + 1].min()

    # 今昨两日最低价为最近13日最低价 (最近13日呈下跌趋势)
    if (lowest_low == pre_low or lowest_low == low) \
            and open < pre_close < pre_open < close:
        return True

    return False


"""
description: 看跌吞没
有效标准：
1.市场处于清晰的下降趋势
2.第二根K线必须吞没第一根
3.第二根实体必须与第一个实体颜色相反
4.之前的趋势超长，或非常剧烈的震荡

param {*} i 当前时间tick
param {*} data 行情数据dataFrame
return {*} Flag:boolean 是否看跌吞没
"""


def is_swallow_down(df, row):
    i = row.name
    if i < 13:
        return False

    open = df.open[i]
    close = df.close[i]
    high = df.high[i]

    pre_open = df.open[i - 1]
    pre_close = df.close[i - 1]
    pre_high = df.high[i - 1]

    # 最近13日最高价
    highest_high = df['high'][i - 12: i + 1].min()

    # 今昨两日最高价为最近13日最高价 (最近13日呈上涨趋势)
    if (highest_high == pre_high or highest_high == high) \
            and open > pre_close > pre_open > close:
        return True

    return False
