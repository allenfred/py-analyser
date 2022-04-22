def is_ma60_first_rule(index, candles, bias, ma, ma_slope):
    """
    葛南维第一大法则 (均线扭转)
    MA60 开始拐头 (ma60_slope 连续3日 > 0)
    收盘价位于MA60之上
    最近21个交易日中前18个交易日 ma60_slope < 0

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param ma_slope:
    :return:
    """

    # 反转看涨增强信号
    # ma60_slope 连续9日增大

    candle = candles[index]
    _close = candle[3]
    ma60_slope = ma_slope[:, 5]
    _ma60 = ma[:, 5][index]
    bias60 = bias[:, 3]

    if index > 90 and _close > _ma60 and max(ma60_slope[index - 21: index - 2]) <= 0 and \
            0 < ma60_slope[index - 2] < ma60_slope[index - 1] < ma60_slope[index] and bias60 < 8:
        return True
    else:
        return False


def is_ma60_second_rule(index, candles, bias, ma, ma_slope):
    """
    葛南维第二大法则 (均线服从)
    MA60 上行 (ma60_slope 连续9日 > 2)
    收盘价连续9日在MA60之上
    价格回落 未跌破MA60

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
    ma60_slope = ma_slope[:, 5]
    _ma60 = ma[:, 5][index]
    bias60 = bias[:, 3]

    if index > 90 and _ma60 > 0:
        _low_bias60 = (_low - _ma60) * 100 / _ma60

    def steady_on_ma():
        flag = True
        for i in range(13):
            if candles[index - i][3] < ma[:, 5][index - i]:
                flag = False
        return flag

    if index > 90 and steady_on_ma() and min(ma60_slope[index - 8: index]) > 2 and \
            min(bias60[index - 8: index]) > 0 and _low_bias60 < 2:
        return True
    else:
        return False


def is_ma60_third_rule(index, candles, bias, ma, ma_slope):
    """
    葛南维第三大法则 (均线服从和黄金交叉)
    MA60 上行 (ma60_slope 连续9日 > 0)
    跌破MA60之后收盘又站上MA60
    随后出现黄金交叉 (5/10 5/20 10/20 5/60 10/60)

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
    ma60_slope = ma_slope[:, 5]
    _ma60 = ma[:, 5][index]
    bias60 = bias[:, 3]

    if index > 90 and _ma60 > 0:
        _low_bias60 = (_low - _ma60) * 100 / _ma60

    def steady_on_ma():
        flag = 0
        for i in range(13):
            if candles[index - i][3] < ma[:, 5][index - i]:
                flag += 1
        return 0 < flag < 3

    if index > 90 and _close > _ma60 and steady_on_ma() and min(ma60_slope[index - 8: index]) > 2 and \
            candles[index - 1][3] < ma[:, 5][index - 1] and bias60[index] < 8 and _low_bias60 < 0:
        return True
    else:
        return False


def is_ma60_fourth_rule(index, candles, bias, ma, ma_slope):
    """
    葛南维第四大法则 (均线修复)
    MA60 下行 (ma60_slope 连续13日 < 0)
    超卖 bias60 < -11%

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
    ma60_slope = ma_slope[:, 5]
    _ma60 = ma[:, 5][index]
    bias60 = bias[:, 3]

    if index > 90 and _ma60 > 0:
        _low_bias60 = (_low - _ma60) * 100 / _ma60

    def steady_under_ma():
        flag = True
        for i in range(13):
            if candles[index - i][3] > ma[:, 5][index - i]:
                flag = False
        return flag

    if index > 90 and bias60[index] < -16 and steady_under_ma() and \
            max(ma60_slope[index - 12: index]) < 0:
        return True
    else:
        return False


def is_ma60_fifth_rule(index, candles, bias, ma, ma_slope):
    """
    葛南维第五大法则 (均线修复)
    MA60上行 (ma60_slope 连续13日 > 2)
    超买 bias60 > 11%

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
    ma60_slope = ma_slope[:, 5]
    _ma60 = ma[:, 5][index]
    bias60 = bias[:, 3]

    if index > 90 and _ma60 > 0:
        _low_bias60 = (_low - _ma60) * 100 / _ma60

    if index > 90 and bias60[index] > 11 and min(ma60_slope[index - 12: index]) > 2:
        return True
    else:
        return False


def is_ma60_sixth_rule(index, candles, bias, ma, ma_slope):
    """
    葛南维第六大法则 (均线扭转)
    MA60开始由上行逐渐走平 (ma60_slope 连续13日 > 2 最近3日 < 1)
    bias60 正常

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
    ma60_slope = ma_slope[:, 5]
    _ma60 = ma[:, 5][index]
    bias60 = bias[:, 3]

    if index > 90 and _ma60 > 0:
        _low_bias60 = (_low - _ma60) * 100 / _ma60

    if index > 90 and bias60[index] > 11 and min(ma60_slope[index - 12: index]) > 2:
        return True
    else:
        return False


def is_ma60_seventh_rule(index, candles, bias, ma, ma_slope):
    """
    葛南维第七大法则 (均线服从)
    MA60 下行 (ma60_slope 连续13日 < 0)
    反弹时未站上MA60之后 继续下行

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
    ma60_slope = ma_slope[:, 5]
    _ma60 = ma[:, 5][index]
    bias60 = bias[:, 3]

    if index > 90 and _ma60 > 0:
        _low_bias60 = (_low - _ma60) * 100 / _ma60

    def steady_under_ma():
        flag = True
        for i in range(13):
            if candles[index - i][3] > ma[:, 5][index - i]:
                flag = False
        return flag

    if index > 90 and bias60[index] > -1 and steady_under_ma() and \
            max(ma60_slope[index - 12: index]) < 0:
        return True
    else:
        return False


def is_ma60_eighth_rule(index, candles, bias, ma, ma_slope):
    """
    葛南维第八大法则 (均线服从和死亡交叉)
    MA60 下行 (ma60_slope 连续13日 < 0)
    反弹站上MA60之后 徘徊数日 继续下行
    随后出现死亡交叉 (5/10 5/20 10/20 5/60 10/60)

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
    ma60_slope = ma_slope[:, 5]
    _ma60 = ma[:, 5][index]
    bias60 = bias[:, 3]

    if index > 90 and _ma60 > 0:
        _low_bias60 = (_low - _ma60) * 100 / _ma60

    def stand_on_ma_temp():
        tag = 0
        for i in range(13):
            if candles[index - i - 1][3] > ma[:, 5][index - i - 1]:
                tag += 1
        return tag <= 3

    if index > 90 and -2 < bias60[index] < 0 and stand_on_ma_temp() and \
            max(ma60_slope[index - 12: index]) < 0:
        return True
    else:
        return False
