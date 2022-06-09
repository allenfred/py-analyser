import numpy as np
from .patterns import has_long_patterns, has_short_patterns, \
    has_bottom_patterns, has_top_patterns, \
    has_long_break_patterns, has_short_break_patterns

"""
MA60 葛南维买卖八大法则
"""


def first(index, candles, bias, ma, df):
    """
    葛南维第一大法则 (均线扭转)
    1.收盘价位于MA60之上
    3.最近55个交易日中前21个交易日下行
    4.最近几个交易日上行且出现放量

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param df: patterns df
    :return:
    """

    candle = candles[index]
    _close = candle[3]
    ma60 = ma[:, 5]
    _ma60 = ma60[index]
    bias60 = bias[:, 4]
    _bias60 = bias60[index]
    print(df['gran'][0])

    def ma60_down_steady():
        flag = True
        for i in range(55):
            # 如果 当前MA60 > 前值
            if ma60[index - i - 9] > ma60[index - i - 1 - 9]:
                flag = False
        return flag

    def start_up_ma():
        flag = True
        for i in range(7):
            if candles[index - i][3] < ma60[index - i] or \
                    ma60[index - i] < ma60[index - i - 1]:
                flag = False
        return flag

    def has_vol(i):
        if df.iloc[i]['max_vol'] > 0 or df.iloc[i]['huge_vol'] > 0 or \
                df.iloc[i]['large_vol'] > 0 or df.iloc[i]['high_vol'] > 0 or \
                df.iloc[i]['increasingly_vol'] > 0:
            return True
        return False

    if index > 90 and _close > _ma60 and ma60_down_steady() and start_up_ma() and \
            (has_vol(index) or has_vol(index - 1) or has_vol(index - 2)):
        # print(index, candle[5], '1')
        return 1

    return 0


def second(index, candles, bias, ma, df):
    """
    葛南维第二大法则 (均线服从)
    1. 连续13个交易日 收盘价在MA60之上 / MA60上行
    2. 价格回落 未跌破MA60 且 K线出现止跌支撑信号 (看涨吞没/看涨锤头线/探水竿/看涨螺旋桨/看涨孕线/下探上涨)
    3. 价格回落未出现强势空头K线 （大阴线/倒锤头线）

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param df: patterns df
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma5 = ma[:, 0]
    ma10 = ma[:, 1]
    ma20 = ma[:, 2]
    ma60 = ma[:, 5]
    _ma60 = ma60[index]
    bias60 = bias[:, 4]
    _bias60 = bias60[index]

    if index > 90 and _ma60 > 0:
        _low_bias60 = (_low - _ma60) * 100 / _ma60

    def steady_on_ma():
        flag = True
        for i in range(13):
            if candles[index - i][3] < ma60[index - i] or ma60[index - i] < ma60[index - i - 1]:
                flag = False

        return flag

    # MA10/MA20 空头排列
    def ma_down():
        flag = True
        for i in range(5):
            if ma10[index - i] > ma10[index - i - 1] \
                    or ma20[index - i] > ma20[index - i - 1] \
                    or ma10[index - i] > ma20[index - i]:
                flag = False
        return flag

    if index > 90 and _low_bias60 < 1 and steady_on_ma() and not ma_down() and \
            (has_long_break_patterns(index, df) or has_long_patterns(index, df)):
        if index > 290:
            print(index, candle[5], '2')
        return 1

    return 0


def third(index, candles, bias, ma, df):
    """
    葛南维第三大法则 (均线服从和黄金交叉)
    1. 连续13个交易日 MA60上行 当日收盘价在MA60之上
    2. 价格回落 短暂跌破MA60之后 收盘又站上MA60 K线出现止跌支撑信号 (看涨吞没/看涨锤头线/看涨螺旋桨/看涨孕线)
    3. 随后出现黄金交叉 (5/10 5/20 10/20 5/60 10/60)

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param df: patterns df
    :return:
    """
    if index < 90:
        return 0

    gran = df['gran'][0]
    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma60 = ma[:, 5]
    _ma60 = ma60[index]
    bias60 = bias[:, 4]
    _bias60 = bias60[index]

    if _ma60 > 0:
        _low_bias60 = (_low - _ma60) * 100 / _ma60

    def ma_rise_steady():
        flag = True
        for i in range(21):
            # 如果 当前MA60 < 前值
            if ma60[index - i] < ma60[index - i - 1]:
                flag = False
        return flag

    def fall_down_ma_temp():
        tag1 = 0
        tag2 = 0
        for i in range(13):
            if candles[index - i - 1][3] < ma60[index - i - 1]:
                tag1 += 1
            if i < 6 and candles[index - i - 1][3] < ma60[index - i - 1]:
                tag2 += 1
        return 4 > tag1 > 0 and 4 > tag2 > 0

    if _close > _ma60 > _low and _bias60 < 8 and \
            ma_rise_steady() and fall_down_ma_temp() and \
            (has_long_break_patterns(index, df) or has_long_patterns(index, df)):
        # print(index, candle[5], '3')
        return 1

    return 0


def fourth(index, candles, bias, ma, df):
    """
    葛南维第四大法则 (均线修复)
    1. 均线持续下行 - 连续13个交易日 收盘价在MA60之下 / MA60下行
    2. 乖离率出现超卖 bias60 < -16
    3. K线出现止跌支撑信号 (看涨吞没/看涨锤头线/看涨螺旋桨/看涨孕线)

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param df: patterns df
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma60 = ma[:, 5]
    _ma60 = ma60[index]
    bias60 = bias[:, 5]
    _bias60 = bias60[index]

    if index > 90 and _ma60 > 0:
        _low_bias60 = (_low - _ma60) * 100 / _ma60

    def steady_under_ma():
        flag = True
        for i in range(21):
            if candles[index - i][3] > ma60[index - i]:
                flag = False
        return flag

    def ma_down_steady():
        flag = True
        for i in range(21):
            # 如果 当前MA60 > 前值
            if ma60[index - i] > ma60[index - i - 1]:
                flag = False
        return flag

    def has_bottom_patterns_recently():
        if has_bottom_patterns(index, df) or has_bottom_patterns(index - 1, df) or \
                has_bottom_patterns(index - 2, df) or has_bottom_patterns(index - 3, df) or \
                has_bottom_patterns(index - 4, df):
            return True

    if index > 90 and _bias60 < -16 and ma_down_steady() and \
            steady_under_ma() and has_bottom_patterns_recently():
        # print(index, candle[5], '4')
        return 1

    return 0


def fifth(index, candles, bias, ma, df):
    """
    葛南维第五大法则 (均线修复)
    1. 连续13个交易日 MA60上行
    2. 乖离率出现超买 bias60 > 11%
    3. K线出现短期见顶信号 (看跌吞没/看跌锤头线/看跌螺旋桨/看跌孕线/看跌尽头线)

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param df: patterns df
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma60 = ma[:, 5]
    _ma60 = ma60[index]
    bias60 = bias[:, 4]
    _bias60 = bias60[index]

    if index > 90 and _ma60 > 0:
        _low_bias60 = (_low - _ma60) * 100 / _ma60

    def steady_on_ma():
        flag = True
        for i in range(9):
            if candles[index - i][3] < ma60[index - i] or ma60[index - i] < ma60[index - i - 1]:
                flag = False
        return flag

    if index > 90 and steady_on_ma() and _bias60 > 16 and \
            has_top_patterns(index, df):
        # print(index, candle[5], '5')
        return 1

    return 0


def sixth(index, candles, bias, ma, df):
    """
    葛南维第六大法则 (均线扭转)
    1. 趋势异态 - MA60开始由上行逐渐走平: 连续18个交易日 MA60上行
    2. 最近3日 MA60开始拐头向下
    2. bias60 正常
    3. K线出现短期见顶信号 >= 2 (看跌吞没/看跌锤头线/看跌螺旋桨/看跌孕线/看跌尽头线)

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param df: patterns df
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma60 = ma[:, 5]
    _ma60 = ma60[index]
    bias60 = bias[:, 4]
    _bias60 = bias60[index]

    if index > 90 and _ma60 > 0:
        _low_bias60 = (_low - _ma60) * 100 / _ma60

    def ma_rise_before():
        flag = True
        for i in range(21):
            # 如果 当前MA60 < 前值
            if ma60[index - i - 3] < ma60[index - i - 4]:
                flag = False
        return flag

    def ma_down_recently():
        flag = True
        for i in range(3):
            # 如果 当前MA60 > 前值
            if ma60[index - i] > ma60[index - i - 1]:
                flag = False
        return flag

    if index > 90 and _close < _ma60 and ma_rise_before() and ma_down_recently() and \
            has_short_patterns(index, df) and \
            8 > _bias60 > -7:
        # print(index, candle[5], '6')
        return 1

    return 0


def seventh(index, candles, bias, ma, df):
    """
    葛南维第七大法则 (均线服从)
    1. 均线持续下行 - 连续21个交易日: MA60下行
    2. 反弹时未站上MA60之后 继续下行
    3. 出现 看跌K线形态 / 死亡交叉 (5/10 5/20 10/20 5/60 10/60)

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param df: patterns df
    :return:
    """
    if index < 90:
        return 0

    gran = df['gran'][0]
    candle = candles[index]
    _high = candle[1]
    _low = candle[2]
    _close = candle[3]
    ma60 = ma[:, 5]
    _ma60 = ma60[index]
    bias60 = bias[:, 4]
    _bias60 = bias60[index]

    if index > 90 and _ma60 > 0:
        _high_bias60 = (_high - _ma60) * 100 / _ma60

    def steady_under_ma():
        flag = True
        for i in range(21):
            if candles[index - i][3] > ma60[index - i] or ma60[index - i] > ma60[index - i - 1]:
                flag = False
        return flag

    def has_resistance():
        if _high < _ma60:
            if has_top_patterns(index, df) and has_top_patterns(index - 1, df):
                return True
        elif _high_bias60 > -1 and has_top_patterns(index, df):
            return True
        return False

    if _bias60 > -1 and has_resistance() and steady_under_ma():
        # print(index, candle[5], '7')
        return 1

    return 0


def eighth(index, candles, bias, ma, df):
    """
    葛南维第八大法则 (均线服从和死亡交叉)
    1. 均线持续下行 - 连续18个交易日 MA60下行
    2. 反弹短暂站上MA60之后 又继续下行
       1h 站上MA60周期小于3
       15min  站上MA60周期小于9
    3. 出现 看跌K线形态 / 死亡交叉 (5/10 5/20 10/20 5/60 10/60)

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param df: patterns df
    :return:
    """
    if index < 90:
        return 0

    gran = df['gran'][0]
    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma60 = ma[:, 5]
    _ma60 = ma60[index]
    bias60 = bias[:, 4]
    _bias60 = bias60[index]

    if index > 90 and _ma60 > 0:
        _low_bias60 = (_low - _ma60) * 100 / _ma60

    def ma_down_steady():
        flag = True
        for i in range(18):
            # 如果 当前MA60 > 前值
            if ma60[index - i] > ma60[index - i - 1]:
                flag = False
        return flag

    def stand_on_ma_temp():
        tag = 0
        for i in range(13):
            if candles[index - i - 1][3] > ma60[index - i - 1]:
                tag += 1
        if gran == 900:
            return 7 > tag > 1
        else:
            return 4 > tag > 0

    def fall_down_continually():
        return candles[index - 1][1] > ma60[index - 1] and -1 < _bias60 < 0

    def has_short_signals():
        return has_top_patterns(index, df) or has_short_break_patterns(index, df)

    if ma_down_steady() and \
            stand_on_ma_temp() and \
            fall_down_continually() and \
            has_short_signals():
        # print(index, candle[5], '8')
        return 1

    return 0
