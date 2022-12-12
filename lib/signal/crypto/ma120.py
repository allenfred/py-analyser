import numpy as np
from .patterns import has_long_patterns, has_short_patterns, \
    has_bottom_patterns, has_top_patterns, \
    has_long_break_patterns, has_short_break_patterns


def steady_on_ma120(index, df):
    ma = df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    close = df['close'].to_numpy()
    ma20 = ma[:, 2]
    ma60 = ma[:, 5]
    ma120 = ma[:, 6]

    ma120_steady_33days = True
    ma60_on_ma120_33days = True
    close_steady_33days = True

    ma60_steady_55days = True
    ma20_on_ma60_55days = True
    close_steady_55days = True

    for i in range(21):
        # 如果当前 MA120 <= 前值
        if ma60[index - i] < ma120[index - i - 1]:
            ma60_steady_22days = False

        # 如果当前 MA60 < MA120
        if ma60[index - i] < ma120[index - i]:
            ma20_on_ma60_22days = False

        # 如果收盘价低于 MA120
        if close[index - i] < ma120[index - i]:
            close_steady_22days = False

    for i in range(33):
        # 如果当前 MA60 <= 前值
        if ma120[index - i] < ma120[index - i - 1]:
            ma60_steady_33days = False

        # 如果当前 MA60 < MA120
        if ma60[index - i] < ma120[index - i]:
            ma20_on_ma60_33days = False

        # 如果收盘价低于 MA120
        if close[index - i] < ma120[index - i]:
            close_steady_33days = False

    for i in range(55):
        # 如果当前 MA120 <= 前值
        if ma120[index - i] < ma120[index - i - 1]:
            ma60_steady_55days = False

        # 如果当前 MA20 < MA120
        if ma60[index - i] < ma120[index - i]:
            ma20_on_ma60_55days = False

        # 如果收盘价低于 MA120
        if close[index - i] < ma120[index - i]:
            close_steady_55days = False

    # 当MA60持续上行 收盘价和MA20必须稳定在MA60之上
    if ma60_steady_55days:
        if close_steady_55days and ma20_on_ma60_55days:
            return True
        else:
            return False

    if ma60_steady_33days:
        if close_steady_33days and ma20_on_ma60_33days:
            return True
        else:
            return False

    if ma60_steady_22days:
        if close_steady_22days and ma20_on_ma60_22days:
            return True
        else:
            return False

    return False


"""
MA120 葛南维买卖八大法则
"""


def first(index, candles, bias, ma, df):
    """
    葛南维第一大法则 (均线扭转)
    1.收盘价位于MA120之上
    3.最近30个交易日中前21个交易日下行
    4.最近9个交易日上行

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param df: patterns df
    :return:
    """

    candle = candles[index]
    _close = candle[3]
    ma20 = ma[:, 2]
    ma60 = ma[:, 5]
    ma120 = ma[:, 6]
    _ma120 = ma120[index]
    bias120 = bias[:, 6]
    _bias120 = bias120[index]

    def ma120_down_steady():
        flag = True
        for i in range(55):
            # 如果 当前MA120 > 前值
            if ma120[index - i - 9] > ma120[index - i - 1 - 9]:
                flag = False
        return flag

    def start_up_ma():
        flag = True
        for i in range(13):
            if candles[index - i][3] < ma120[index - i] or \
                    ma120[index - i] < ma120[index - i - 1]:
                flag = False
        return flag

    def ma20_rise_steady():
        flag = True
        for i in range(9):
            # 如果 当前MA20 < 前值
            if ma20[index - i] <= ma20[index - i - 1]:
                flag = False
        return flag

    def ma60_rise_steady():
        flag = True
        for i in range(9):
            # 如果 当前MA60 < 前值
            if ma60[index - i] <= ma60[index - i - 1]:
                flag = False
        return flag

    def has_vol(i):
        if df.iloc[i]['max_vol'] > 0 or df.iloc[i]['huge_vol'] > 0 or \
                df.iloc[i]['large_vol'] > 0 or df.iloc[i]['high_vol'] > 0 or \
                df.iloc[i]['increasingly_vol'] > 0:
            return True
        return False

    if index > 150 and _close > _ma120 and _bias120 < 8 and ma120_down_steady() and start_up_ma() and \
            (ma20_rise_steady() or ma60_rise_steady()):
        # print(index, candle[5], '1', 'ma120')
        return 1

    return 0


def second(index, candles, bias, ma, df):
    """
    葛南维第二大法则 (均线服从)
    1. 连续21个交易日 收盘价在MA120之上 / MA120上行
    2. 价格回落 未跌破MA120 且 K线出现止跌支撑信号 (看涨吞没/看涨锤头线/探水竿/看涨螺旋桨/看涨孕线/下探上涨)
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
    ma120 = ma[:, 6]
    _ma120 = ma120[index]
    bias120 = bias[:, 6]
    _bias120 = bias120[index]

    if index > 150 and _ma120 > 0:
        _low_bias120 = (_low - _ma120) * 100 / _ma120

    def steady_on_ma():
        flag = True
        for i in range(21):
            if candles[index - i][3] < ma120[index - i] or ma120[index - i] < ma120[index - i - 1]:
                flag = False

        return flag

    if index > 150 and _low_bias120 < 1 and steady_on_ma() and \
            (has_long_break_patterns(index, df) or has_long_patterns(index, df)):
        # print(index, candle[5], '2', 'ma120')
        return 1

    return 0


def third(index, candles, bias, ma, df):
    """
    葛南维第三大法则 (均线服从和黄金交叉)
    1. 连续21个交易日 收盘价在MA120之上 / MA120上行 / ma120_slope > 0
    2. 价格回落 跌破MA120之后 收盘又站上MA120 K线出现止跌支撑信号 (看涨吞没/看涨锤头线/看涨螺旋桨/看涨孕线)
    3. 随后出现黄金交叉 (5/10 5/20 10/20 5/60 10/60)

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
    ma10 = ma[:, 1]
    ma20 = ma[:, 2]
    ma120 = ma[:, 6]
    _ma120 = ma120[index]
    bias120 = bias[:, 6]
    _bias120 = bias120[index]

    if index > 150 and _ma120 > 0:
        _low_bias120 = (_low - _ma120) * 100 / _ma120

    def ma_rise_steady():
        flag = True
        for i in range(21):
            # 如果 当前MA120 < 前值
            if ma120[index - i] < ma120[index - i - 1]:
                flag = False
        return flag

    if index > 150 and _close > _ma120 > _low and _bias120 < 8 and \
            ma_rise_steady() and candles[index - 1][2] < ma120[index - 1] and \
            (has_long_break_patterns(index, df) or has_long_patterns(index, df)):
        # print(index, candle[5], '3', 'ma120')
        return 1

    return 0


def fourth(index, candles, bias, ma, df):
    """
    葛南维第四大法则 (均线修复)
    1. 均线持续下行 - 连续21个交易日 收盘价在MA120之下 / MA120下行
    2. 乖离率出现超卖 bias120 < -16
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
    ma120 = ma[:, 6]
    _ma120 = ma120[index]
    bias120 = bias[:, 6]
    _bias120 = bias120[index]

    if index > 150 and _ma120 > 0:
        _low_bias120 = (_low - _ma120) * 100 / _ma120

    def steady_under_ma():
        flag = True
        for i in range(21):
            if candles[index - i][3] > ma120[index - i]:
                flag = False
        return flag

    def ma_down_steady():
        flag = True
        for i in range(21):
            # 如果 当前MA120 > 前值
            if ma120[index - i] > ma120[index - i - 1]:
                flag = False
        return flag

    def has_bottom_patterns_recently():
        if has_bottom_patterns(index, df) or has_bottom_patterns(index - 1, df) or \
                has_bottom_patterns(index - 2, df) or has_bottom_patterns(index - 3, df) or \
                has_bottom_patterns(index - 4, df):
            return True

    if index > 150 and _bias120 < -16 and ma_down_steady() and \
            steady_under_ma() and has_bottom_patterns_recently():
        # print(index, candle[5], '4', 'ma120')
        return 1

    return 0


def fifth(index, candles, bias, ma, df):
    """
    葛南维第五大法则 (均线修复)
    1. 连续21个交易日 MA120上行
    2. 乖离率出现超买 bias120 > 11%
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
    ma120 = ma[:, 6]
    _ma120 = ma120[index]
    bias120 = bias[:, 6]
    _bias120 = bias120[index]

    if index > 150 and _ma120 > 0:
        _low_bias120 = (_low - _ma120) * 100 / _ma120

    def steady_on_ma():
        flag = True
        for i in range(21):
            if candles[index - i][3] < ma120[index - i] or ma120[index - i] < ma120[index - i - 1]:
                flag = False
        return flag

    if index > 150 and steady_on_ma() and _bias120 > 11 and \
            (has_top_patterns(index, df) or has_short_break_patterns(index, df)):
        # print(index, candle[5], '5', 'ma120')
        return 1

    return 0


def sixth(index, candles, bias, ma, df):
    """
    葛南维第六大法则 (均线扭转)
    1. 趋势异态 - MA120开始由上行逐渐走平: 连续18个交易日 MA120上行
    2. 最近3日 MA120开始拐头向下
    2. bias120 正常
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
    ma120 = ma[:, 6]
    _ma120 = ma120[index]
    bias120 = bias[:, 6]
    _bias120 = bias120[index]

    if index > 150 and _ma120 > 0:
        _low_bias120 = (_low - _ma120) * 100 / _ma120

    def ma_rise_before():
        flag = True
        for i in range(21):
            # 如果 当前MA120 < 前值
            if ma120[index - i - 3] < ma120[index - i - 4]:
                flag = False
        return flag

    def ma_down_recently():
        flag = True
        for i in range(3):
            # 如果 当前MA120 > 前值
            if ma120[index - i] > ma120[index - i - 1]:
                flag = False
        return flag

    if index > 150 and 8 > _bias120 > -7 and _close < _ma120 and \
            ma_rise_before() and ma_down_recently() and \
            (has_short_patterns(index, df) or has_short_break_patterns(index, df)):
        # print(index, candle[5], '6', 'ma120')
        return 1

    return 0


def seventh(index, candles, bias, ma, df):
    """
    葛南维第七大法则 (均线服从)
    1. 均线持续下行 - 连续21个交易日: MA120下行
    2. 反弹时未站上MA120之后 继续下行

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param df: patterns df
    :return:
    """

    candle = candles[index]
    _high = candle[1]
    _low = candle[2]
    _close = candle[3]
    ma120 = ma[:, 6]
    _ma120 = ma120[index]
    bias120 = bias[:, 6]
    _bias120 = bias120[index]

    if index > 150 and _ma120 > 0:
        _high_bias120 = (_high - _ma120) * 100 / _ma120

    def steady_under_ma():
        flag = True
        for i in range(21):
            if candles[index - i][3] > ma120[index - i] or ma120[index - i] > ma120[index - i - 1]:
                flag = False
        return flag

    def has_resistance():
        if _high < _ma120:
            if has_top_patterns(index, df) and has_top_patterns(index - 1, df):
                return True
        elif _high_bias120 > -1 and has_top_patterns(index, df):
            return True
        return False

    if index > 150 and has_resistance() and steady_under_ma():
        # print(index, candle[5], '7', 'ma120')
        return 1

    return 0


def eighth(index, candles, bias, ma, df):
    """
    葛南维第八大法则 (均线服从和死亡交叉)
    1. 均线持续下行 - 连续21个交易日 MA120下行
    2. 反弹短暂站上MA120之后 又继续下行
    3. 出现死亡交叉 (5/10 5/20 10/20 5/60 10/60)

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
    ma120 = ma[:, 6]
    _ma120 = ma120[index]
    bias120 = bias[:, 6]
    _bias120 = bias120[index]

    if index > 150 and _ma120 > 0:
        _low_bias120 = (_low - _ma120) * 100 / _ma120

    def stand_on_ma_temp():
        tag = 0
        for i in range(7):
            if candles[index - i - 1][3] > ma120[index - i - 1]:
                tag += 1
        return tag >= 2

    def ma_down_steady():
        flag = True
        for i in range(21):
            # 如果 当前MA120 > 前值
            if ma120[index - i] > ma120[index - i - 1]:
                flag = False
        return flag

    if index > 150 and candles[index - 1][3] > ma120[index - 1] and _close < _ma120 and \
            ma_down_steady() and stand_on_ma_temp() and \
            (has_top_patterns(index, df) or has_short_break_patterns(index, df)):
        # print(index, candle[5], '8', 'ma120')
        return 1

    return 0
