# EMA55 葛南维买卖八大法则

def is_ema55_first(index, candles, bias, ma, ema_slope):
    """
    葛南维第一大法则 (均线扭转)
    MA55 开始拐头 (ma55_slope 连续3日 > 0)
    收盘价位于MA55之上
    最近21个交易日中前18个交易日 ma55_slope < 0

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param ema_slope:
    :return:
    """

    # 反转看涨增强信号
    # ma55_slope 连续9日增大

    candle = candles[index]
    _close = candle[3]
    ma55_slope = ema_slope[:, 4]
    _ema55 = ma[:, 4][index]
    _bias55 = bias[:, 3][index]

    if index > 90 and _close > _ema55 and max(ma55_slope[index - 21: index - 2]) <= 0 and \
            0 < ma55_slope[index - 2] < ma55_slope[index - 1] < ma55_slope[index] and \
            _bias55 < 8:
        return True
    else:
        return False


def is_ema55_second(index, candles, bias, ma, ema_slope):
    """
    葛南维第二大法则 (均线服从)
    MA55 上行 (ma55_slope 连续9日 > 2)
    收盘价连续9日在MA55之上
    价格回落 未跌破MA55

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
    ma55_slope = ema_slope[:, 4]
    _ema55 = ma[:, 4][index]
    bias55 = bias[:, 3]

    if index > 90 and _ema55 > 0:
        _low_bias55 = (_low - _ema55) * 100 / _ema55

    def steady_on_ma():
        flag = True
        for i in range(13):
            if candles[index - i][3] < ma[:, 4][index - i]:
                flag = False
        return flag

    if index > 90 and steady_on_ma() and min(ma55_slope[index - 8: index]) > 2 and \
            min(bias55[index - 8: index]) > 0 and _low_bias55 < 2:
        return True
    else:
        return False


def is_ema55_third(index, candles, bias, ma, ema_slope):
    """
    葛南维第三大法则 (均线服从和黄金交叉)
    MA55 上行 (ma55_slope 连续9日 > 0)
    跌破MA55之后收盘又站上MA55
    随后出现黄金交叉 (5/10 5/20 10/20 5/55 10/55)

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
    ma55_slope = ema_slope[:, 4]
    _ema55 = ma[:, 4][index]
    bias55 = bias[:, 3]

    if index > 90 and _ema55 > 0:
        _low_bias55 = (_low - _ema55) * 100 / _ema55

    def steady_on_ma():
        flag = 0
        for i in range(13):
            if candles[index - i][3] < ma[:, 4][index - i]:
                flag += 1
        return 0 < flag < 3

    if index > 90 and _close > _ema55 and steady_on_ma() and min(ma55_slope[index - 8: index]) > 2 and \
            candles[index - 1][3] < ma[:, 4][index - 1] and bias55[index] < 8 and \
            _low_bias55 < 0:
        return True
    else:
        return False


def is_ema55_fourth(index, candles, bias, ma, ema_slope):
    """
    葛南维第四大法则 (均线修复)
    MA55 下行 (ma55_slope 连续13日 < 0)
    超卖 bias55 < -11%

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
    ma55_slope = ema_slope[:, 4]
    _ema55 = ma[:, 4][index]
    _bias55 = bias[:, 3][index]

    if index > 90 and _ema55 > 0:
        _low_bias55 = (_low - _ema55) * 100 / _ema55

    def steady_under_ma():
        flag = True
        for i in range(13):
            if candles[index - i][3] > ma[:, 4][index - i]:
                flag = False
        return flag

    if index > 90 and _bias55 < -16 and steady_under_ma() and \
            max(ma55_slope[index - 12: index]) < 0:
        return True
    else:
        return False


def is_ema55_fifth(index, candles, bias, ma, ema_slope):
    """
    葛南维第五大法则 (均线修复)
    MA55上行 (ma55_slope 连续13日 > 2)
    超买 bias55 > 11%

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
    ma55_slope = ema_slope[:, 4]
    _ema55 = ma[:, 4][index]
    _bias55 = bias[:, 3][index]

    if index > 90 and _ema55 > 0:
        _low_bias55 = (_low - _ema55) * 100 / _ema55

    if index > 90 and _bias55 > 11 and min(ma55_slope[index - 12: index]) > 2:
        return True
    else:
        return False


def is_ema55_sixth(index, candles, bias, ma, ema_slope):
    """
    葛南维第六大法则 (均线扭转)
    MA55开始由上行逐渐走平 (ma55_slope 连续13日 > 2 最近3日 < 1)
    bias55 正常

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
    ma55_slope = ema_slope[:, 4]
    _ema55 = ma[:, 4][index]
    _bias55 = bias[:, 3][index]

    if index > 90 and _ema55 > 0:
        _low_bias55 = (_low - _ema55) * 100 / _ema55

    if index > 90 and _bias55 > 11 and min(ma55_slope[index - 12: index]) > 2:
        return True
    else:
        return False


def is_ema55_seventh(index, candles, bias, ma, ema_slope):
    """
    葛南维第七大法则 (均线服从)
    MA55 下行 (ma55_slope 连续13日 < 0)
    反弹时未站上MA55之后 继续下行

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
    ma55_slope = ema_slope[:, 4]
    _ema55 = ma[:, 4][index]
    _bias55 = bias[:, 3][index]

    if index > 90 and _ema55 > 0:
        _low_bias55 = (_low - _ema55) * 100 / _ema55

    def steady_under_ma():
        flag = True
        for i in range(13):
            if candles[index - i][3] > ma[:, 4][index - i]:
                flag = False
        return flag

    if index > 90 and _bias55 > -1 and steady_under_ma() and \
            max(ma55_slope[index - 12: index]) < 0:
        return True
    else:
        return False


def is_ema55_eighth(index, candles, bias, ma, ema_slope):
    """
    葛南维第八大法则 (均线服从和死亡交叉)
    MA55 下行 (ma55_slope 连续13日 < 0)
    反弹站上MA55之后 徘徊数日 继续下行
    随后出现死亡交叉 (5/10 5/20 10/20 5/55 10/55)

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
    ma55_slope = ema_slope[:, 4]
    _ema55 = ma[:, 4][index]
    _bias55 = bias[:, 3][index]

    if index > 90 and _ema55 > 0:
        _low_bias55 = (_low - _ema55) * 100 / _ema55

    def stand_on_ma_temp():
        tag = 0
        for i in range(13):
            if candles[index - i - 1][3] > ma[:, 4][index - i - 1]:
                tag += 1
        return tag <= 3

    if index > 90 and -2 < _bias55 < 0 and stand_on_ma_temp() and \
            max(ma55_slope[index - 12: index]) < 0:
        return True
    else:
        return False
