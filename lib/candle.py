import math as math


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


def is_hammer(i, open, high, low, close, pct_chg):
    if i < 21:
        return False

    _open = open[i]
    _high = high[i]
    _low = low[i]
    _close = close[i]
    k_len = _high - _low
    bar_len = math.fabs(_open - _close)
    up_shadow_len = math.fabs(_high - _close if _open < _close else _high - _open)
    up_one_third = _high - (k_len / 3)

    # 最近21日最低价
    lowest_low = min(low[i - 20: i + 1])

    # 开盘价和收盘价都位于k线上方1/3处 (即：下影线长度占k线长度的2/3以上）
    # 上影线长度需小于柱体长度的1/5
    if lowest_low == _low and _open > up_one_third and _close > up_one_third \
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


def is_pour_hammer(i, open, high, low, close, pct_chg):
    if i < 20:
        return False

    _open = open[i]
    _high = high[i]
    _low = low[i]
    _close = close[i]
    k_len = _high - _low
    bar_len = math.fabs(_open - _close)
    bottom_shadow_len = math.fabs(_open - _low if _open < _close else _close - _low)
    bottom_one_third = _low + (k_len / 3)

    # 最近21日最低价
    lowest_low = min(low[i - 20: i + 1])

    # 开盘价和收盘价都位于k线下方1/3处 (即：上影线长度占k线长度的2/3以上）
    # 下影线长度需小于柱体长度的1/5
    if lowest_low == _low and _open < bottom_one_third and _close < bottom_one_third \
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


def is_hang_neck(i, open, high, low, close, pct_chg):
    if i < 20:
        return False

    _open = open[i]
    _high = high[i]
    _low = low[i]
    _close = close[i]
    k_len = _high - _low
    bar_len = math.fabs(_open - _close)
    up_shadow_len = math.fabs(_high - _close if _open < _close else _high - _open)
    up_one_third = _high - (k_len / 3)

    # 最近21日最高价
    highest_high = min(high[i - 20: i + 1])

    # 开盘价和收盘价都位于k线上方1/3处 (即：下影线长度占k线长度的2/3以上）
    # 上影线长度需小于柱体长度的1/5
    if highest_high == _high and _open > up_one_third and _close > up_one_third \
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


def is_shooting(i, open, high, low, close, pct_chg):
    if i < 20:
        return False

    _open = open[i]
    _high = high[i]
    _low = low[i]
    _close = close[i]
    k_len = _high - _low
    bar_len = math.fabs(_open - _close)
    bottom_shadow_len = math.fabs(open - low if open < close else close - low)
    bottom_one_third = low + (k_len / 3)

    # 最近21日最高价
    highest_high = min(high[i - 20: i + 1])

    # 开盘价和收盘价都位于k线下方1/3处 (即：上影线长度占k线长度的2/3以上）
    # 下影线长度需小于柱体长度的1/5
    if highest_high == _high and _open < bottom_one_third and _close < bottom_one_third \
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


def is_short_end(i, open, high, low, close, pct_chg):
    if i < 20:
        return False

    _open = open[i]
    _high = high[i]
    _low = low[i]
    _close = close[i]
    k_len = _high - _low
    bar_len = math.fabs(_open - _close)

    bottom_shadow_len = math.fabs(_open - _low if _open < _close else _close - _low)
    pre_bottom_shadow_high = (open[i - 1] if open[i - 1] < close[i - 1] else close[i - 1])
    pre_bottom_shadow_low = low[i - 1]

    # 最近21日最低价
    lowest_low = min(low[i - 20: i + 1])

    # 下跌趋势中 前一根K线为中阴线或大阴线
    # 开盘价和收盘价都位于前一K线下影线内
    # 前一根K线下影线长度需小于K线长度的1/2
    # K线实体长度大于K线长度的2/5
    if (lowest_low == low[i - 1] or lowest_low == _low) and \
            pre_bottom_shadow_high > _open > pre_bottom_shadow_low and \
            pre_bottom_shadow_high > _close > pre_bottom_shadow_low \
            and bottom_shadow_len < k_len / 2 and bar_len > (k_len * 2) / 5 \
            and open[i - 1] > close[i - 1] and pct_chg[i - 1] < -3:
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


def is_long_end(i, open, high, low, close, pct_chg):
    if i < 20:
        return False

    _open = open[i]
    _high = high[i]
    _low = low[i]
    _close = close[i]
    k_len = _high - _low
    bar_len = math.fabs(_open - _close)

    up_shadow_len = math.fabs(_high - _open if _open > _close else _high - _close)
    pre_up_shadow_high = high[i - 1]
    pre_up_shadow_low = (close[i - 1] if open[i - 1] < close[i-1] else open[i-1])

    # 最近21日最高价
    highest_high = min(high[i - 20: i + 1])

    # 上涨趋势中 前一根K线为中阳线或大阳线
    # 开盘价和收盘价都位于前一K线下影线内
    # 前一根K线下影线长度需小于K线长度的1/2
    # K线实体长度大于K线长度的2/5
    if (highest_high == high[i-1] or lowest_low == high[i-1]) and \
            pre_up_shadow_high > _open > pre_up_shadow_low and \
            pre_up_shadow_high > _close > pre_up_shadow_low \
            and up_shadow_len < k_len / 2 and bar_len > (k_len * 2) / 5 \
            and open[i-1] < close[i-1] and pct_chg[i-1] > 3:
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


def is_attack_short(i, open, high, low, close, pct_chg):
    if i < 20:
        return False

    _open = open[i]
    _high = high[i]
    _low = low[i]
    _close = close[i]
    k_len = _high - _low
    bar_len = math.fabs(_open - _close)

    # 最近21日最低价
    lowest_low = min(low[i - 20: i + 1])

    # 下跌趋势中 前一根K线为中阴线或大阴线 当日K线为跳空低开的中阳线或大阳线
    # 当日K线跳空低开
    # 当日K线收盘价与前日K线收盘价相近
    if pct_chg[i-1] < -3 and pct_chg[i] > 3 and lowest_low == _low and \
            low[i-1] > _open and (bar_len / 5 + close[i-1]) > _close > close[i-1]:
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


def is_first_light(i, open, high, low, close, pct_chg):
    if i < 20:
        return False

    _open = open[i]
    _high = high[i]
    _low = low[i]
    _close = close[i]
    k_len = _high - _low
    bar_len = math.fabs(_open - _close)

    # 最近21日最低价
    lowest_low = min(low[i - 20: i + 1])

    # 下跌趋势中 前一根K线为中阴线或大阴线 当日K线为跳空低开的中阳线或大阳线
    # 当日K线跳空低开
    # 当日K线收盘价插入前日K线实体的1/2 但没有超过前日K线的开盘价
    if pct_chg[i-1] < -3 and pct_chg[i] > 3 and lowest_low == _low and \
            low[i-1] > _open and (bar_len / 2 + close[i-1]) < _close < open[i-1]:
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


def is_sunrise(i, open, high, low, close, pct_chg):
    if i < 20:
        return False

    _open = open[i]
    _high = high[i]
    _low = low[i]
    _close = close[i]
    k_len = _high - _low
    bar_len = math.fabs(_open - _close)

    # 最近21日最低价
    lowest_low = min(low[i - 20: i + 1])

    # 下跌趋势中 前一根K线为中阴线或大阴线 当日K线为高开的中阳线或大阳线
    # 当日K线收盘价插入前日K线实体的1/2 但没有超过前日K线的开盘价
    if pct_chg[i-1] < -3 and pct_chg[i] > 3 and lowest_low == low[i-1] and \
            _close > open[i-1] > _open > close[i-1]:
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


def is_flat_base(i, open, high, low, close, pct_chg):
    if i < 14:
        return False

    pre_low = low[i - 1]
    before_pre_low = low[i - 2]
    # 比较最低价的偏差
    deviation = low[i]*5 / 1000

    # 最近21日最低价
    lowest_low = min(low[i - 20: i + 1])

    # 下跌趋势中 最近两根K线最低价位于同一水平 / 最近三根K线最低价位于同一水平
    if (lowest_low == low[i] or lowest_low == pre_low or lowest_low == before_pre_low) \
            and math.fabs(low[i] - pre_low) < deviation \
            and math.fabs(low[i] - before_pre_low) < deviation:
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


def is_swallow_up(i, open, high, low, close, pct_chg):
    if i < 20:
        return False

    _open = open[i]
    _high = high[i]
    _low = low[i]
    _close = close[i]
    k_len = _high - _low
    bar_len = math.fabs(_open - _close)

    pre_open = open[i - 1]
    pre_close = close[i - 1]
    pre_low = low[i - 1]

    # 最近20日最低价
    lowest_low = min(low[i - 20: i + 1])

    # 今昨两日最低价为最近21日最低价 (最近20日呈下跌趋势)
    if (lowest_low == pre_low or lowest_low == _low) \
            and _open < pre_close < pre_open < _close:
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


def is_swallow_down(i, open, high, low, close, pct_chg):
    if i < 20:
        return False

    _open = open[i]
    _high = high[i]
    _low = low[i]
    _close = close[i]
    k_len = _high - _low
    bar_len = math.fabs(_open - _close)

    pre_open = open[i - 1]
    pre_close = close[i - 1]
    pre_high = high[i - 1]

    # 最近20日最高价
    highest_high = min(high[i - 20: i + 1])

    # 今昨两日最高价为最近21日最高价 (最近21日呈上涨趋势)
    if (highest_high == pre_high or highest_high == _high) \
            and _open > pre_close > pre_open > _close:
        return True

    return False
