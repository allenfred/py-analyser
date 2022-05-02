# EMA60 葛南维买卖八大法则

def is_ema60_first(index, candles, bias, ema, ema_slope):
    """
    葛南维第一大法则 (均线扭转)
    1.收盘价位于EMA55之上
    2.EMA55 开始拐头 (ema55_slope 连续5日 > 0)
    3.最近21个交易日中前18个交易日 ema55_slope < 0
    4.最近3个交易日 slope 呈上升趋势
    5.乖离率 不存在超买

    :param index:
    :param candles:
    :param bias:
    :param ema:
    :param ema_slope:
    :return:
    """

    # 反转看涨增强信号
    # ema60_slope 连续9日增大

    candle = candles[index]
    _close = candle[3]
    ema60_slope = ema_slope[:, 5]
    ema60 = ema[:, 5]
    _ema60 = ema60[index]
    bias60 = bias[:, 4]
    _bias60 = bias60[index]

    # EMA60 开始拐头向上
    def start_up_ema():
        flag = True
        for i in range(5):
            if candles[index - i][3] < ema60[index - i] or \
                    ema60[index - i] < ema60[index - i - 1]:
                flag = False
        return flag

    if index > 90 and _close > _ema60 and start_up_ema() and \
            max(ema60_slope[index - 21: index - 2]) <= 0 and \
            0 < ema60_slope[index - 2] < ema60_slope[index - 1] < ema60_slope[index] and \
            _bias60 < 8:
        return True
    else:
        return False


def is_ema60_second(index, candles, bias, ema, ema_slope):
    """
    葛南维第二大法则 (均线服从)
    1. 连续13个交易日 收盘价在EMA60之上
    2. 连续13个交易日 EMA60上行
    3. 连续13个交易日 ema60_slope >= 2
    4. 价格回落 未跌破MA55 且 K线出现止跌支撑信号 (看涨吞没/看涨锤头线/看涨螺旋桨/看涨孕线)
    5. 价格回落未出现强势空头K线 （大阴线/倒锤头线）

    :param index:
    :param candles:
    :param bias:
    :param ema:
    :param ema_slope:
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ema60_slope = ema_slope[:, 5]
    ema60 = ema[:, 5]
    _ema60 = ema60[index]
    bias60 = bias[:, 4]
    _bias60 = bias60[index]

    if index > 90 and _ema60 > 0:
        _low_bias60 = (_low - _ema60) * 100 / _ema60

    def steady_on_ema():
        flag = True
        for i in range(13):
            if candles[index - i][3] < ema60[index - i] or ema60[index] < ema60[index - 1]:
                flag = False
        return flag

    if index > 90 and steady_on_ema() and min(ema60_slope[index - 8: index]) > 2 and _low_bias60 < 2:
        return True
    else:
        return False


def is_ema60_third(index, candles, bias, ema, ema_slope):
    """
    葛南维第三大法则 (均线服从和黄金交叉)
    1. 连续13个交易日 收盘价在EMA60之上
    2. 连续13个交易日 EMA60上行
    3. 连续13个交易日 ema60_slope >= 2
    4. 价格回落 跌破EMA60之后收盘又站上EMA60 K线出现止跌支撑信号 (看涨吞没/看涨锤头线/看涨螺旋桨/看涨孕线)
    5. 随后出现黄金交叉 (5/10 5/20 10/20 5/60 10/60)

    :param index:
    :param candles:
    :param bias:
    :param ema:
    :param ema_slope:
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ema60_slope = ema_slope[:, 5]
    ema60 = ema[:, 5]
    _ema60 = ema60[index]
    bias60 = bias[:, 4]
    _bias60 = bias60[index]

    if index > 90 and _ema60 > 0:
        _low_bias60 = (_low - _ema60) * 100 / _ema60

    def steady_on_ema():
        flag = 0
        for i in range(13):
            if candles[index - i][3] < ema60[index - i]:
                flag += 1
        return 0 < flag < 3

    def ema_rise_steady():
        flag = True
        for i in range(13):
            # 如果 当前MA60 < 前值
            if ema60[index - i] < ema60[index - i - 1]:
                flag = False
        return flag

    if index > 90 and _close > _ema60 and steady_on_ema() and ema_rise_steady() and \
            min(ema60_slope[index - 12: index]) > 2 and \
            candles[index - 1][3] < ema60[index - 1] and _bias60 < 8 and \
            _low_bias60 < 0:
        return True
    else:
        return False


def is_ema60_fourth(index, candles, bias, ema, ema_slope):
    """
    葛南维第四大法则 (均线修复)
    1. 连续13个交易日 收盘价在EMA60之下 / EMA60下行 / ema60_slope < 0
    2. 乖离率出现超卖 bias60 < -16
    3. K线出现止跌支撑信号 (看涨吞没/看涨锤头线/看涨螺旋桨/看涨孕线)

    :param index:
    :param candles:
    :param bias:
    :param ema:
    :param ema_slope:
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ema60_slope = ema_slope[:, 5]
    ema60 = ema[:, 5]
    _ema60 = ema60[index]
    bias60 = bias[:, 4]
    _bias60 = bias60[index]

    if index > 90 and _ema60 > 0:
        _low_bias60 = (_low - _ema60) * 100 / _ema60

    def steady_under_ema():
        flag = True
        for i in range(13):
            if candles[index - i][3] > ema60[index - i]:
                flag = False
        return flag

    def ema_down_steady():
        flag = True
        for i in range(13):
            # 如果 当前EMA60 > 前值
            if ema60[index - i] > ema60[index - i - 1]:
                flag = False
        return flag

    if index > 90 and steady_under_ema() and ema_down_steady() and \
            max(ema60_slope[index - 12: index]) < 0 and _bias60 < -16:
        return True
    else:
        return False


def is_ema60_fifth(index, candles, bias, ema, ema_slope):
    """
    葛南维第五大法则 (均线修复)
    1. 连续13个交易日 EMA60上行 / ema60_slope > 1
    2. 乖离率出现超买 bias60 > 11
    3. K线出现短期见顶信号 (看跌吞没/看跌锤头线/看跌螺旋桨/看跌孕线/看跌尽头线)

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param ema_slope:
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ema60_slope = ema_slope[:, 5]
    ema60 = ema[:, 5]
    _ema60 = ema60[index]
    bias60 = bias[:, 4]
    _bias60 = bias60[index]

    if index > 90 and _ema60 > 0:
        _low_bias60 = (_low - _ema60) * 100 / _ema60

    def steady_on_ema():
        flag = True
        for i in range(13):
            if candles[index - i][3] < ema60[index - i] or ema60[index - i] < ema60[index - i - 1]:
                flag = False
        return flag

    if index > 90 and steady_on_ema() and _bias60 > 11 and \
            min(ema60_slope[index - 12: index]) > 1:
        return True
    else:
        return False


def is_ema60_sixth(index, candles, bias, ema, ema_slope):
    """
    葛南维第六大法则 (均线扭转)
    1. EMA60开始由上行逐渐走平: 连续18个交易日 EMA60上行
    2. 最近3日 MA60开始拐头向下 ema60_slope < 1
    2. bias60 正常
    3. K线出现短期见顶信号 (看跌吞没/看跌锤头线/看跌螺旋桨/看跌孕线/看跌尽头线)

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param ema_slope:
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ema60_slope = ema_slope[:, 5]
    ema60 = ema[:, 5]
    _ema60 = ema60[index]
    bias60 = bias[:, 4]
    _bias60 = bias60[index]

    if index > 90 and _ema60 > 0:
        _low_bias60 = (_low - _ema60) * 100 / _ema60

    def ema_rise_before():
        flag = True
        for i in range(21):
            # 如果 当前MA60 < 前值
            if ema60[index - i - 3] < ema60[index - i - 4]:
                flag = False
        return flag

    def ema_down_recently():
        flag = True
        for i in range(3):
            # 如果 当前MA60 > 前值
            if ema60[index - i] > ema60[index - i - 1]:
                flag = False
        return flag

    if index > 90 and ema_rise_before() and ema_down_recently() and _bias60 > 11:
        return True
    else:
        return False


def is_ema60_seventh(index, candles, bias, ema, ema_slope):
    """
    葛南维第七大法则 (均线服从)
    1. 连续13个交易日: EMA60下行 (ema60_slope < 0)
    2. 反弹时未站上EMA60之后 继续下行

    :param index:
    :param candles:
    :param bias:
    :param ema:
    :param ema_slope:
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ema60_slope = ema_slope[:, 5]
    ema60 = ema[:, 5]
    _ema60 = ema60[index]
    bias60 = bias[:, 4]
    _bias60 = bias60[index]

    if index > 90 and _ema60 > 0:
        _low_bias60 = (_low - _ema60) * 100 / _ema60

    def steady_under_ema():
        flag = True
        for i in range(13):
            if candles[index - i][3] > ema60[index - i] or ema60[index - i] > ema60[index - i - 1]:
                flag = False
        return flag

    if index > 90 and _bias60 > -1 and steady_under_ema():
        return True
    else:
        return False


def is_ema60_eighth(index, candles, bias, ema, ema_slope):
    """
    葛南维第八大法则 (均线服从和死亡交叉)
    1. 连续21个交易日 EMA60下行 (ema60_slope < 0)
    2. 前几个交易日反弹站上EMA60之后 又继续下行
    3. 出现死亡交叉 (5/10 5/20 10/20 5/60 10/60)

    :param index:
    :param candles:
    :param bias:
    :param ema:
    :param ema_slope:
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ema60_slope = ema_slope[:, 5]
    ema60 = ema[:, 5]
    _ema60 = ema60[index]
    bias60 = bias[:, 4]
    _bias60 = bias60[index]

    if index > 90 and _ema60 > 0:
        _low_bias60 = (_low - _ema60) * 100 / _ema60

    def stand_on_ema_temp():
        tag = 0
        for i in range(13):
            if candles[index - i - 1][3] > ema60[index - i - 1]:
                tag += 1
        return tag <= 3

    def ema_down_steady():
        flag = True
        for i in range(21):
            # 如果 当前EMA60 > 前值
            if ema60[index - i] > ema60[index - i - 1]:
                flag = False
        return flag

    if index > 90 and -2 < _bias60 < 0 and stand_on_ema_temp() and ema_down_steady():
        return True
    else:
        return False
