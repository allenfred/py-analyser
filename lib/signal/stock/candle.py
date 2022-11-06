import math as math
import os
import sys

# path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(path)
_start_at = 100


def long_line(i, candles):
    """
    description: 大阳线/大阴线
    有效标准：
    1.市场处于清晰的上涨/下跌趋势
    2.实体长度占比小于90%
    3.K线涨跌幅大于 5

    :param i:
    :param candles:
    :return:
    """
    if i < _start_at:
        return 0

    open = candles[:, 0]
    high = candles[:, 1]
    low = candles[:, 2]
    close = candles[:, 3]
    pct_chg = candles[:, 4]
    pct_range = candles[:, 5]
    _open = open[i]
    _high = high[i]
    _low = low[i]
    _close = close[i]
    _per = 0.05

    k_len = _high - _low
    bar_len = math.fabs(_open - _close)
    up_shadow_len = math.fabs(_high - _close if _open < _close else _high - _open)
    bottom_shadow_len = math.fabs(_open - _low if _open < _close else _close - _low)

    pct_chg_base = 5

    if up_shadow_len + bottom_shadow_len < k_len * _per * 2 and \
            (up_shadow_len > k_len * _per or bottom_shadow_len > k_len * _per) and \
            math.fabs(pct_chg[i]) > pct_chg_base:
        if _open < _close:
            return 1
        else:
            return -1

    return 0


def marubozu(i, candles):
    """
    description: 光头光脚 (看涨/看跌)
    有效标准：
    1.市场处于清晰的上涨/下降趋势
    2.上下影线占K线长度比例小于5%
    3.K线涨跌幅大于 5

    :param i: 当前tick
    :param candles:
    :return: boolean
    """

    if i < _start_at:
        return 0

    open = candles[:, 0]
    high = candles[:, 1]
    low = candles[:, 2]
    close = candles[:, 3]
    pct_chg = candles[:, 4]
    pct_range = candles[:, 5]
    _open = open[i]
    _high = high[i]
    _low = low[i]
    _close = close[i]
    _per = 0.05

    k_len = _high - _low
    bar_len = math.fabs(_open - _close)
    up_shadow_len = math.fabs(_high - _close if _open < _close else _high - _open)
    bottom_shadow_len = math.fabs(_open - _low if _open < _close else _close - _low)

    pct_chg_base = 5

    if up_shadow_len < k_len * _per and bottom_shadow_len < k_len * _per and \
            math.fabs(pct_chg[i]) > pct_chg_base:
        if _open < _close:
            return 1
        else:
            return -1

    return 0


def hammer(i, candles):
    """
    description: 锤头线 (看涨)
    有效标准：
    1.市场处于清晰的下降趋势
    2.当前K线收出锤头线形态
    3.当前K线最低价为近期最低价
    4..K线震幅大于5%

    :param i: 当前tick
    :param candles:
    :return: boolean
    """
    if i < _start_at:
        return 0

    open = candles[:, 0]
    high = candles[:, 1]
    low = candles[:, 2]
    close = candles[:, 3]
    pct_chg = candles[:, 4]
    _open = open[i]
    _high = high[i]
    _low = low[i]
    _close = close[i]
    pre_close = close[i - 1]

    k_len = _high - _low
    bar_len = math.fabs(_open - _close)
    up_shadow_len = math.fabs(_high - _close if _open < _close else _high - _open)
    up_one_third = _high - (k_len / 3)

    # 最近21日最低价
    lowest_low = min(low[i - 20: i + 1])

    # 开盘价和收盘价都位于k线上方1/3处 (即：下影线长度占k线长度的2/3以上）
    # 上影线长度需小于柱体长度的1/5
    if lowest_low == _low and _open > up_one_third and _close > up_one_third \
            and up_shadow_len < bar_len / 5 \
            and pre_close * 0.05 <= k_len:
        return 1

    return 0


def pour_hammer(i, candles):
    """
    description: 倒锤头线 (看涨)
    有效标准：
    1.市场处于清晰的下降趋势
    2.当前K线收出倒锤头线形态
    3.当前K线最低价为近期最低价
    4..K线震幅大于5%

    :param i: 当前tick
    :param candles:
    :return: boolean
    """
    if i < _start_at:
        return 0

    open = candles[:, 0]
    high = candles[:, 1]
    low = candles[:, 2]
    close = candles[:, 3]
    pct_chg = candles[:, 4]
    _open = open[i]
    _high = high[i]
    _low = low[i]
    _close = close[i]
    pre_close = close[i - 1]

    k_len = _high - _low
    bar_len = math.fabs(_open - _close)

    bottom_shadow_len = math.fabs(_open - _low if _open < _close else _close - _low)
    bottom_one_third = _low + (k_len / 3)

    # 最近21日最低价
    lowest_low = min(low[i - 20: i + 1])

    # 开盘价和收盘价都位于k线下方1/3处 (即：上影线长度占k线长度的2/3以上）
    # 下影线长度需小于柱体长度的1/5
    if lowest_low == _low and _open < bottom_one_third and _close < bottom_one_third \
            and bottom_shadow_len < bar_len / 5 \
            and pre_close * 0.05 <= k_len:
        return 1

    return 0


def hang_neck(i, candles):
    """
    description: 吊颈线 (看跌)
    有效标准：
    1.市场处于清晰的上涨趋势
    2.当前K线收出吊颈线形态
    3.当前K线最高价为近期最高价

    :param i: 当前tick
    :param candles:
    :return: boolean
    """
    if i < _start_at:
        return 0

    open = candles[:, 0]
    high = candles[:, 1]
    low = candles[:, 2]
    close = candles[:, 3]
    pct_chg = candles[:, 4]
    _open = open[i]
    _high = high[i]
    _low = low[i]
    _close = close[i]

    k_len = _high - _low
    bar_len = math.fabs(_open - _close)
    up_shadow_len = math.fabs(_high - _close if _open < _close else _high - _open)
    up_one_third = _high - (k_len / 3)

    # 最近21日最高价
    highest_high = max(high[i - 20: i + 1])

    # 开盘价和收盘价都位于k线上方1/3处 (即：下影线长度占k线长度的2/3以上）
    # 上影线长度需小于柱体长度的1/5
    if highest_high == _high and _open > up_one_third and _close > up_one_third \
            and up_shadow_len < bar_len / 5:
        return 1

    return 0


def shooting(i, candles):
    """
    description: 射击之星 (看跌)
    有效标准：
    1.市场处于清晰的上涨趋势
    2.当前K线收出射击之星形态
    3.当前K线最高价为近期最高价

    :param i: 当前tick
    :param candles:
    :return: boolean
    """
    if i < _start_at:
        return 0

    open = candles[:, 0]
    high = candles[:, 1]
    low = candles[:, 2]
    close = candles[:, 3]
    pct_chg = candles[:, 4]
    _open = open[i]
    _high = high[i]
    _low = low[i]
    _close = close[i]

    k_len = _high - _low
    bar_len = math.fabs(_open - _close)

    bottom_shadow_len = math.fabs(_open - _low if _open < _close else _close - _low)
    bottom_one_third = _low + (k_len / 3)

    # 最近21日最高价
    highest_high = min(high[i - 20: i + 1])

    # 开盘价和收盘价都位于k线下方1/3处 (即：上影线长度占k线长度的2/3以上）
    # 下影线长度需小于柱体长度的1/5
    if highest_high == _high and _open < bottom_one_third and _close < bottom_one_third \
            and bottom_shadow_len < bar_len / 5:
        return 1

    return 0


def short_end(i, candles):
    """
    description: 尽头线 (看涨)
    有效标准：
    1.市场处于清晰的上涨趋势
    2.当前K线收出射击之星形态
    3.当前K线最高价为近期最高价

    :param i: 当前tick
    :param candles:
    :return: boolean
    """
    if i < _start_at:
        return 0

    open = candles[:, 0]
    high = candles[:, 1]
    low = candles[:, 2]
    close = candles[:, 3]
    pct_chg = candles[:, 4]
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
        return 1

    return 0


def long_end(i, candles):
    """
    description: 尽头线 (看跌)
    有效标准：
    1.市场处于清晰的上涨趋势
    2.当前K线收出射击之星形态
    3.当前K线最高价为近期最高价

    param {*} i 当前时间tick
    param {*} candles
    return {*} Flag:boolean 是否符合
    """
    if i < _start_at:
        return 0

    open = candles[:, 0]
    high = candles[:, 1]
    low = candles[:, 2]
    close = candles[:, 3]
    pct_chg = candles[:, 4]
    _open = open[i]
    _high = high[i]
    _low = low[i]
    _close = close[i]

    k_len = _high - _low
    bar_len = math.fabs(_open - _close)

    up_shadow_len = math.fabs(_high - _open if _open > _close else _high - _close)
    pre_up_shadow_high = high[i - 1]
    pre_up_shadow_low = (close[i - 1] if open[i - 1] < close[i - 1] else open[i - 1])

    # 最近21日最高价
    highest_high = min(high[i - 20: i + 1])
    # 最近21日最低价
    lowest_low = min(low[i - 20: i + 1])

    # 上涨趋势中 前一根K线为中阳线或大阳线
    # 开盘价和收盘价都位于前一K线下影线内
    # 前一根K线下影线长度需小于K线长度的1/2
    # K线实体长度大于K线长度的2/5
    if (highest_high == high[i - 1] or lowest_low == high[i - 1]) and \
            pre_up_shadow_high > _open > pre_up_shadow_low and \
            pre_up_shadow_high > _close > pre_up_shadow_low \
            and up_shadow_len < k_len / 2 and bar_len > (k_len * 2) / 5 \
            and open[i - 1] < close[i - 1] and pct_chg[i - 1] > 3:
        return 1

    return 0


def attack_short(i, candles):
    """
    description: 好友反攻 (看涨)
    有效标准：
    1.市场处于清晰的下跌趋势
    2.当前K线收出好友反攻形态
    3.当前K线最低价为近期最低价

    param {*} i 当前时间tick
    param {*} candles
    return {*} Flag:boolean 是否符合
    """
    if i < _start_at:
        return 0

    open = candles[:, 0]
    high = candles[:, 1]
    low = candles[:, 2]
    close = candles[:, 3]
    pct_chg = candles[:, 4]
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
    if pct_chg[i - 1] < -3 and pct_chg[i] > 3 and lowest_low == _low and \
            low[i - 1] > _open and (bar_len / 5 + close[i - 1]) > _close > close[i - 1]:
        return 1

    return 0


def first_light(i, candles):
    """
    description: 曙光初现 (看涨)
    有效标准：
    1.市场处于清晰的下跌趋势
    2.当前K线收出曙光初现形态
    3.当前K线最低价为近期最低价

    param {*} i 当前时间tick
    param {*} candles
    return {*} Flag:boolean 是否符合
    """
    if i < _start_at:
        return 0

    open = candles[:, 0]
    high = candles[:, 1]
    low = candles[:, 2]
    close = candles[:, 3]
    pct_chg = candles[:, 4]
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
    if pct_chg[i - 1] < -3 and pct_chg[i] > 3 and lowest_low == _low and \
            low[i - 1] > _open and (bar_len / 2 + close[i - 1]) < _close < open[i - 1]:
        return 1

    return 0


def sunrise(i, candles):
    """
    description: 旭日东升 (看涨)
    有效标准：
    1.市场处于清晰的下降趋势
    2.当前K线开盘价高于前日收盘价
    3.当前K线收盘价高于前日开盘价
    4.K线波动幅度大于3%

    param {*} i 当前时间tick
    param {*} candles
    return {*} Flag:boolean 是否符合
    """
    if i < _start_at:
        return 0

    open = candles[:, 0]
    high = candles[:, 1]
    low = candles[:, 2]
    close = candles[:, 3]
    pct_chg = candles[:, 4]
    _open = open[i]
    _high = high[i]
    _low = low[i]
    _close = close[i]

    k_len = _high - _low
    bar_len = math.fabs(_open - _close)

    # 最近21日最低价
    lowest_low = min(low[i - 20: i + 1])

    if pct_chg[i - 1] < -3 and pct_chg[i] > 3 and lowest_low == low[i - 1] and \
            _close > open[i - 1] > _open > close[i - 1]:
        return 1

    return 0


def flat_base(i, candles):
    """
    description: 平底 (看涨)
    有效标准：
    1.市场处于清晰的下降趋势
    2.当前K线收出平底形态
    3.当前K线最低价为近期最低价

    param {*} i 当前时间tick
    param {*} candles
    return {*} Flag:boolean 是否符合
    """
    if i < _start_at:
        return 0

    low = candles[:, 2]
    _open = candles[:, 0][i]
    _high = candles[:, 1][i]
    _low = candles[:, 2][i]
    _close = candles[:, 3][i]

    pre_low = candles[:, 2][i - 1]
    before_pre_low = candles[:, 2][i - 2]
    # 比较最低价的偏差
    deviation = _low * 5 / 1000

    # 最近21日最低价
    lowest_low = min(low[i - 20: i + 1])

    # 下跌趋势中 最近两根K线最低价位于同一水平 / 最近三根K线最低价位于同一水平
    if (lowest_low == low[i] or lowest_low == pre_low or lowest_low == before_pre_low) \
            and math.fabs(low[i] - pre_low) < deviation \
            and math.fabs(low[i] - before_pre_low) < deviation:
        return 1

    return 0


def down_rise(i, candles):
    """
    description: 下探上涨
    有效标准：
    1.市场处于短暂的下降趋势(回调)
    3.第二根K线必须吞没第一根
    4.第二根K线实体必须大于K线长度的 2/3
    5.第二根实体必须与第一个实体颜色相反
    6.第二根K线涨幅大于 3%

    :param i: 当前tick
    :param candles:
    :return: boolean
    """
    if i < _start_at:
        return 0

    _open = candles[:, 0][i]
    _high = candles[:, 1][i]
    _low = candles[:, 2][i]
    _close = candles[:, 3][i]
    k_len = _high - _low
    bar_len = math.fabs(_open - _close)

    pre_open = candles[:, 0][i - 1]
    pre_close = candles[:, 3][i - 1]

    if _open < pre_close < _close and _open < pre_open < _close and \
            bar_len > k_len / 2 and candles[:, 4][i] >= 3:
        return 1

    return 0


def swallow_up(i, candles):
    """
    description: 看涨吞没
    有效标准：
    1.市场处于清晰的下降趋势
    2.之前的趋势超长，或非常剧烈的震荡
    3.第二根K线必须吞没第一根
    4.第二根K线实体必须大于K线长度的 2/3
    5.第二根实体必须与第一个实体颜色相反
    6.第二根K线涨幅大于 3%

    :param i: 当前tick
    :param candles:
    :return: boolean
    """
    if i < _start_at:
        return 0

    _open = candles[:, 0][i]
    _high = candles[:, 1][i]
    _low = candles[:, 2][i]
    _close = candles[:, 3][i]
    k_len = _high - _low
    bar_len = math.fabs(_open - _close)

    pre_open = candles[:, 0][i - 1]
    pre_close = candles[:, 3][i - 1]
    pre_low = candles[:, 2][i - 1]

    # 最近20日最低价
    lowest_low = min(candles[:, 2][i - 20: i + 1])

    # 今昨两日最低价为最近21日最低价 (最近20日呈下跌趋势)
    if (lowest_low == pre_low or lowest_low == _low) \
            and _open < pre_close < pre_open < _close and \
            bar_len > k_len / 2 and candles[:, 4][i] >= 3:
        return 1

    return 0


def swallow_down(i, candles):
    """
    description: 看跌吞没
    有效标准：
    1.市场处于清晰的上涨趋势
    2.之前的趋势超长，或非常剧烈的震荡
    3.第二根K线必须吞没第一根
    4.第二根K线实体必须大于K线长度的 2/3
    5.第二根实体必须与第一个实体颜色相反
    6.第二根K线跌幅大于 3%

    :param i: 当前tick
    :param candles:
    :return: boolean
    """
    if i < _start_at:
        return 0

    _open = candles[:, 0][i]
    _high = candles[:, 1][i]
    _low = candles[:, 2][i]
    _close = candles[:, 3][i]
    k_len = _high - _low
    bar_len = math.fabs(_open - _close)

    pre_open = candles[:, 0][i - 1]
    pre_close = candles[:, 3][i - 1]
    pre_high = candles[:, 1][i - 1]

    # 最近20日最高价
    highest_high = max(candles[:, 1][i - 20: i + 1])

    # 今昨两日最高价为最近21日最高价 (最近21日呈上涨趋势)
    if (highest_high == pre_high or highest_high == _high) \
            and _open > pre_close > pre_open > _close \
            and bar_len > k_len / 2 and candles[:, 4][i] <= -3:
        return 1

    return 0


def rise_line(i, candles):
    """
    description: 涨停一字板
    有效标准：
    1.涨幅大于 9.99%

    :param i: 当前tick
    :param candles:
    :return: boolean
    """
    if i < _start_at:
        return 0

    _open = candles[:, 0][i]
    _high = candles[:, 1][i]
    _low = candles[:, 2][i]
    _close = candles[:, 3][i]
    _chg = candles[:, 4][i]

    if _open == _high == _low == _close and _chg > 9.5:
        return 1

    return 0


def drop_line(i, candles):
    """
    description: 跌停一字板
    1.跌幅大于 9.99%

    :param i: 当前tick
    :param candles:
    :return: boolean
    """
    if i < _start_at:
        return 0

    _open = candles[:, 0][i]
    _high = candles[:, 1][i]
    _low = candles[:, 2][i]
    _close = candles[:, 3][i]
    _chg = candles[:, 4][i]

    if _open == _high == _low == _close and _chg < -9.5:
        return 1

    return 0


def up_screw(i, candles):
    """
    description: 看跌螺旋桨 (看跌)
    有效标准：
    1.市场处于清晰的上涨趋势
    2.K线震幅大于6%
    3.上下影线长度大于K线长度的1/3

    :param i: 当前tick
    :param candles:
    :return: boolean
    """
    if i < _start_at:
        return 0

    _open = candles[:, 0][i]
    high = candles[:, 1]
    _high = high[i]
    _low = candles[:, 2][i]
    _close = candles[:, 3][i]

    k_len = _high - _low
    bar_len = math.fabs(_open - _close)

    up_shadow_len = math.fabs(_open - _high if _open < _close else _close - _high)
    bottom_shadow_len = math.fabs(_open - _low if _open < _close else _close - _low)

    if max(high[i - 9: i - 1]) < _high and \
            up_shadow_len > k_len / 3 and bottom_shadow_len > k_len / 3 and \
            _open * 1.03 < _high and _open * 0.93 > _low:
        return 1

    return 0


def down_screw(i, candles):
    """
    description: 看涨螺旋桨 (看涨)
    有效标准：
    1.市场处于清晰的下跌趋势 连续13日沿MA10下跌
    2.K线震幅大于6%
    3.上下影线长度大于K线长度的1/3

    :param i: 当前tick
    :param candles:
    :return: boolean
    """
    if i < _start_at:
        return 0

    _open = candles[:, 0][i]
    high = candles[:, 1]
    low = candles[:, 2]
    _high = high[i]
    _low = low[i]
    _close = candles[:, 3][i]

    k_len = _high - _low
    bar_len = math.fabs(_open - _close)

    up_shadow_len = math.fabs(_open - _high if _open < _close else _close - _high)
    bottom_shadow_len = math.fabs(_open - _low if _open < _close else _close - _low)

    if min(low[i - 9: i - 1]) > _low and \
            up_shadow_len > k_len / 3 and bottom_shadow_len > k_len / 3 and \
            _open * 1.03 < _high and _open * 0.93 > _low:
        return 1

    return 0


def upward_jump(i, candles):
    """
    description: 向上跳空
    有效标准：

    :param i: 当前tick
    :param candles:
    :return: boolean
    """
    if i < _start_at:
        return 0

    _open = candles[:, 0][i]
    _pre_high = candles[:, 1][i - 1]
    _low = candles[:, 2][i]
    _close = candles[:, 3][i]
    _chg = candles[:, 4][i]

    if _low > _pre_high:
        return 1

    return 0


def downward_jump(i, candles):
    """
    description: 向下跳空
    有效标准：

    :param i: 当前tick
    :param candles:
    :return: boolean
    """
    if i < _start_at:
        return 0

    _open = candles[:, 0][i]
    _high = candles[:, 1][i]
    _pre_low = candles[:, 2][i - 1]
    _close = candles[:, 3][i]
    _chg = candles[:, 4][i]

    if _high < _pre_low:
        return 1

    return 0


def up_cross3ma(i, candles, df):
    """
    description: 一阳穿三线 (看涨)
    有效标准：

    :param i: 当前tick
    :param candles:
    :param df:
    :return: boolean
    """
    if i < _start_at:
        return 0

    ma = df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    _open = candles[:, 0][i]
    _close = candles[:, 3][i]
    _ma5 = ma[:, 0][i]
    _ma10 = ma[:, 1][i]
    _ma20 = ma[:, 2][i]
    _ma30 = ma[:, 3][i]

    if ((_open < _ma5 and _open < _ma10 and _open < _ma20 and
         _close > _ma5 and _close > _ma10 and _close > _ma20) or
            (_open < _ma5 and _open < _ma10 and _open < _ma30 and
             _close > _ma5 and _close > _ma10 and _close > _ma30)):
        return 1

    return 0


def up_cross4ma(i, candles, df):
    """
    description: 一阳穿四线 (看涨)
    有效标准：

    :param i: 当前tick
    :param candles:
    :param df:
    :return: boolean
    """
    if i < _start_at:
        return 0

    ma = df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    _open = candles[:, 0][i]
    _close = candles[:, 3][i]
    _ma5 = ma[:, 0][i]
    _ma10 = ma[:, 1][i]
    _ma20 = ma[:, 2][i]
    _ma60 = ma[:, 5][i]

    if (_open < _ma5 and _open < _ma10 and _open < _ma20 and _open < _ma60 and
            _close > _ma5 and _close > _ma10 and _close > _ma20 and _close > _ma60):
        return 1

    return 0


def drop_cross3ma(i, candles, df):
    """
    description: 一阴穿三线 (看跌)
    有效标准：

    :param i: 当前tick
    :param candles:
    :param df:
    :return: boolean
    """
    if i < _start_at:
        return 0

    ma = df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    _open = candles[:, 0][i]
    _close = candles[:, 3][i]
    _ma5 = ma[:, 0][i]
    _ma10 = ma[:, 1][i]
    _ma20 = ma[:, 2][i]
    _ma30 = ma[:, 3][i]

    if ((_open > _ma5 and _open > _ma10 and _open > _ma20 and
         _close < _ma5 and _close < _ma10 and _close < _ma20) or
            (_open > _ma5 and _open > _ma10 and _open > _ma30 and
             _close < _ma5 and _close < _ma10 and _close < _ma30)):
        return 1

    return 0


def drop_cross4ma(i, candles, df):
    """
    description: 一阴穿四线 (看跌)
    有效标准：

    :param i: 当前tick
    :param candles:
    :param df:
    :return: boolean
    """
    if i < _start_at:
        return 0

    ma = df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    _open = candles[:, 0][i]
    _close = candles[:, 3][i]
    _ma5 = ma[:, 0][i]
    _ma10 = ma[:, 1][i]
    _ma20 = ma[:, 2][i]
    _ma60 = ma[:, 5][i]

    if (_open > _ma5 and _open > _ma10 and _open > _ma20 and _open > _ma60 and
            _close < _ma5 and _close < _ma10 and _close < _ma20 and _close < _ma60):
        return 1

    return 0


def limit_up_gene(i, candles, df):
    """
    description: 涨停基因(看涨)
    有效标准：
    最近20个交易日有涨停
    价格 回调至上个涨停区间 0.386

    :param i: 当前tick
    :param candles:
    :param df:
    :return: boolean
    """

    if i < _start_at:
        return 0

    ma = df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    _open = candles[:, 0][i]
    _close = candles[:, 3][i]
    _ma5 = ma[:, 0][i]
    _ma10 = ma[:, 1][i]
    _ma20 = ma[:, 2][i]
    _ma60 = ma[:, 5][i]

    if (_open > _ma5 and _open > _ma10 and _open > _ma20 and _open > _ma60 and
            _close < _ma5 and _close < _ma10 and _close < _ma20 and _close < _ma60):
        return 1

    return 0
