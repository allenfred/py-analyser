# MA120 葛南维买卖八大法则

def is_ma120_first(index, candles, bias, ma, ma_slope):
    """
    葛南维第一大法则 (均线扭转)
    1.收盘价位于MA120之上
    2.MA120 开始拐头 (ma120_slope 连续3日 > 0)
    3.最近21个交易日中前18个交易日 ma120_slope < 0
    4.最近3个交易日 slope 呈上升趋势
    5.乖离率正常 不存在超买

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param ma_slope:
    :return:
    """

    candle = candles[index]
    _close = candle[3]
    ma120_slope = ma_slope[:, 5]
    ma120 = ma[:, 5]
    _ma120 = ma120[index]
    bias120 = bias[:, 4]
    _bias120 = bias120[index]

    # MA120 开始拐头向上
    def start_up_ma():
        flag = True
        for i in range(3):
            if candles[index - i][3] < ma120[index - i] or \
                    ma120[index - i] < ma120[index - i - 1]:
                flag = False
        return flag

    if index > 90 and _close > _ma120 and start_up_ma() and \
            max(ma120_slope[index - 21: index - 2]) <= 0 and \
            0 < ma120_slope[index - 2] < ma120_slope[index - 1] < ma120_slope[index] and \
            _bias120 < 8:
        return True
    else:
        return False


def is_ma120_second(index, candles, bias, ma, ma_slope):
    """
    葛南维第二大法则 (均线服从)
    1. 连续13个交易日 收盘价在MA120之上 / MA120上行 / ma120_slope > 0
    2. 价格回落 未跌破MA120 且 K线出现止跌支撑信号 (看涨吞没/看涨锤头线/看涨螺旋桨/看涨孕线)
    3. 价格回落未出现强势空头K线 （大阴线/倒锤头线）

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param ma_slope:
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma120_slope = ma_slope[:, 5]
    ma120 = ma[:, 5]
    _ma120 = ma120[index]
    bias120 = bias[:, 4]
    _bias120 = bias120[index]

    if index > 90 and _ma120 > 0:
        _low_bias120 = (_low - _ma120) * 100 / _ma120

    def steady_on_ma():
        flag = True
        for i in range(13):
            if candles[index - i][3] < ma120[index - i] or ma120[index] < ma120[index - 1]:
                flag = False
        return flag

    if index > 90 and steady_on_ma() and min(ma120_slope[index - 12: index]) > 0 and _low_bias120 < 2:
        return True
    else:
        return False


def is_ma120_third(index, candles, bias, ma, ma_slope):
    """
    葛南维第三大法则 (均线服从和黄金交叉)
    1. 连续13个交易日 收盘价在MA120之上 / MA120上行 / ma120_slope > 0
    2. 价格回落 跌破MA120之后 收盘又站上MA120 K线出现止跌支撑信号 (看涨吞没/看涨锤头线/看涨螺旋桨/看涨孕线)
    3. 随后出现黄金交叉 (5/10 5/20 10/20 5/120 10/120)

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param ma_slope:
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma120_slope = ma_slope[:, 5]
    ma120 = ma[:, 5]
    _ma120 = ma120[index]
    bias120 = bias[:, 4]
    _bias120 = bias120[index]

    if index > 90 and _ma120 > 0:
        _low_bias120 = (_low - _ma120) * 100 / _ma120

    def steady_on_ma():
        flag = 0
        for i in range(13):
            if candles[index - i][3] < ma120[index - i]:
                flag += 1
        return 0 < flag < 3

    def ma_rise_steady():
        flag = True
        for i in range(13):
            # 如果 当前MA120 < 前值
            if ma120[index - i] < ma120[index - i - 1]:
                flag = False
        return flag

    if index > 90 and _close > _ma120 and steady_on_ma() and ma_rise_steady() and \
            min(ma120_slope[index - 12: index]) > 0 and \
            candles[index - 1][3] < ma120[index - 1] and \
            _bias120 < 8 and _low_bias120 < 0:
        return True
    else:
        return False


def is_ma120_fourth(index, candles, bias, ma, ma_slope):
    """
    葛南维第四大法则 (均线修复)
    1. 连续13个交易日 收盘价在MA120之下 / MA120下行 / ma120_slope < 0
    2. 乖离率出现超卖 bias120 < -16
    3. K线出现止跌支撑信号 (看涨吞没/看涨锤头线/看涨螺旋桨/看涨孕线)

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param ma_slope:
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma120_slope = ma_slope[:, 5]
    ma120 = ma[:, 5]
    _ma120 = ma120[index]
    bias120 = bias[:, 4]
    _bias120 = bias120[index]

    if index > 90 and _ma120 > 0:
        _low_bias120 = (_low - _ma120) * 100 / _ma120

    def steady_under_ma():
        flag = True
        for i in range(13):
            if candles[index - i][3] > ma120[index - i]:
                flag = False
        return flag

    def ma_down_steady():
        flag = True
        for i in range(13):
            # 如果 当前MA120 > 前值
            if ma120[index - i] > ma120[index - i - 1]:
                flag = False
        return flag

    if index > 90 and ma_down_steady() and steady_under_ma() and _bias120 < -16 and \
            max(ma120_slope[index - 12: index]) < 0:
        return True
    else:
        return False


def is_ma120_fifth(index, candles, bias, ma, ma_slope):
    """
    葛南维第五大法则 (均线修复)
    1. 连续13个交易日 MA120上行 / ma120_slope > 1
    2. 乖离率出现超买 bias120 > 11%
    3. K线出现短期见顶信号 (看跌吞没/看跌锤头线/看跌螺旋桨/看跌孕线/看跌尽头线)

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param ma_slope:
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma120_slope = ma_slope[:, 5]
    ma120 = ma[:, 5]
    _ma120 = ma120[index]
    bias120 = bias[:, 4]
    _bias120 = bias120[index]

    if index > 90 and _ma120 > 0:
        _low_bias120 = (_low - _ma120) * 100 / _ma120

    def steady_on_ma():
        flag = True
        for i in range(13):
            if candles[index - i][3] < ma120[index - i] or ma120[index - i] < ma120[index - i - 1]:
                flag = False
        return flag

    if index > 90 and steady_on_ma() and _bias120 > 11 and \
            min(ma120_slope[index - 12: index]) > 1:
        return True
    else:
        return False


def is_ma120_sixth(index, candles, bias, ma, ma_slope):
    """
    葛南维第六大法则 (均线扭转)
    1. MA120开始由上行逐渐走平: 连续18个交易日 MA120上行
    2. 最近3日 MA120开始拐头向下 ma120_slope < 1
    2. bias120 正常
    3. K线出现短期见顶信号 (看跌吞没/看跌锤头线/看跌螺旋桨/看跌孕线/看跌尽头线)

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param ma_slope:
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma120_slope = ma_slope[:, 5]
    ma120 = ma[:, 5]
    _ma120 = ma120[index]
    bias120 = bias[:, 4]
    _bias120 = bias120[index]

    if index > 90 and _ma120 > 0:
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

    if index > 90 and ma_rise_before() and ma_down_recently() and 11 > _bias120 > -11:
        return True
    else:
        return False


def is_ma120_seventh(index, candles, bias, ma, ma_slope):
    """
    葛南维第七大法则 (均线服从)
    1. 连续13个交易日: MA120下行 (ma120_slope < 0)
    2. 反弹时未站上MA120之后 继续下行

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param ma_slope:
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma120_slope = ma_slope[:, 5]
    ma120 = ma[:, 5]
    _ma120 = ma120[index]
    bias120 = bias[:, 4]
    _bias120 = bias120[index]

    if index > 90 and _ma120 > 0:
        _low_bias120 = (_low - _ma120) * 100 / _ma120

    def steady_under_ma():
        flag = True
        for i in range(13):
            if candles[index - i][3] > ma120[index - i] or ma120[index - i] > ma120[index - i - 1]:
                flag = False
        return flag

    if index > 90 and _bias120 > -1 and steady_under_ma():
        return True
    else:
        return False


def is_ma120_eighth(index, candles, bias, ma, ma_slope):
    """
    葛南维第八大法则 (均线服从和死亡交叉)
    1. 连续21个交易日 MA120下行 (ma120_slope < 0)
    2. 前几个交易日反弹站上MA120之后 又继续下行
    3. 出现死亡交叉 (5/10 5/20 10/20 5/120 10/120)

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param ma_slope:
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma120_slope = ma_slope[:, 5]
    ma120 = ma[:, 5]
    _ma120 = ma120[index]
    bias120 = bias[:, 4]
    _bias120 = bias120[index]

    if index > 90 and _ma120 > 0:
        _low_bias120 = (_low - _ma120) * 100 / _ma120

    def stand_on_ma_temp():
        tag = 0
        for i in range(13):
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

    if index > 90 and -2 < _bias120 < 0 and stand_on_ma_temp() and ma_down_steady():
        return True
    else:
        return False
