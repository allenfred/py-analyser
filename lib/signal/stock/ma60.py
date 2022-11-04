import numpy as np


# MA60 葛南维买卖八大法则

def is_ma60_first(index, candles, bias, ma, ma_slope, df):
    """
    葛南维第一大法则 (均线扭转)
    1.收盘价位于MA60之上
    2.MA20 连续7个交易日上行
    5.乖离率正常 不存在超买

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param ma_slope:
    :param df: patterns df
    :return:
    """

    candle = candles[index]
    _close = candle[3]
    ma20 = ma[:, 2]
    ma60 = ma[:, 5]
    _ma60 = ma60[index]
    bias60 = bias[:, 4]
    _bias60 = bias60[index]

    def ma60_down_before():
        flag = True
        for i in range(55):
            # 如果 当前MA60 > 前值
            if ma60[index - i - 5] > ma60[index - i - 6]:
                flag = False
        return flag

    def start_up_ma60():
        flag = True
        for i in range(3):
            if candles[index - i][3] < ma60[index - i]:
                flag = False
        return flag

    def ma20_rise_steady():
        flag = True
        for i in range(7):
            # 如果 当前MA60 < 前值
            if ma20[index - i] < ma20[index - i - 1]:
                flag = False
        return flag

    if index > 90 and ma60_down_before() and start_up_ma60() and ma20_rise_steady() and _bias60 < 8:
        return True
    else:
        return False


def is_ma60_second(index, candles, bias, ma, ma_slope, df):
    """
    葛南维第二大法则 (均线服从)
    1. 连续21个交易日 收盘价在MA60之上 / MA60上行
    2. 价格回落 未跌破MA60 且 K线出现止跌支撑信号 (看涨吞没/看涨锤头线/探水竿/看涨螺旋桨/看涨孕线/下探上涨)
    3. 价格回落未出现强势空头K线 （大阴线/倒锤头线）

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param ma_slope:
    :param df: patterns df
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma60_slope = ma_slope[:, 5]
    ma60 = ma[:, 5]
    _ma60 = ma60[index]
    bias60 = bias[:, 4]
    _bias60 = bias60[index]

    if index > 90 and _ma60 > 0:
        _low_bias60 = (_low - _ma60) * 100 / _ma60

    def steady_on_ma():
        flag = True
        for i in range(21):
            if candles[index - i][3] < ma60[index - i] or ma60[index - i] < ma60[index - i - 1]:
                flag = False
        return flag

    if index > 90 and steady_on_ma() and \
            has_support_patterns(index, df) and _low_bias60 < 2:
        return True
    else:
        return False


def is_ma60_third(index, candles, bias, ma, ma_slope, df):
    """
    葛南维第三大法则 (均线服从和黄金交叉)
    1. 连续21个交易日 收盘价在MA60之上 / MA60上行 / ma60_slope > 0
    2. 价格回落 短暂跌破MA60之后 收盘又站上MA60 K线出现止跌支撑信号 (看涨吞没/看涨锤头线/看涨螺旋桨/看涨孕线)
    3. 随后出现黄金交叉 (5/10 5/20 10/20 5/60 10/60)

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param ma_slope:
    :param df: patterns df
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    close = candles[:, 3]
    _close = candle[3]
    ma60_slope = ma_slope[:, 5]
    ma60 = ma[:, 5]
    _ma60 = ma60[index]
    bias60 = bias[:, 4]
    _bias60 = bias60[index]

    if index > 90 and _ma60 > 0:
        _low_bias60 = (_low - _ma60) * 100 / _ma60

    def rise_steady():
        flag = True
        beneath_ma60_cnt = 0
        for i in range(21):
            # 如果 当前MA60 < 前值
            if ma60[index - i] < ma60[index - i - 1]:
                flag = False

            if close[index - 1] < ma60[index - i]:
                beneath_ma60_cnt += 1

        return flag and 1 < beneath_ma60_cnt <= 5

    if index > 90 and _close > _ma60 > _low and _bias60 < 8 and \
            rise_steady() and candles[index - 1][2] < ma60[index - 1]:
        return True
    else:
        return False


def is_ma60_fourth(index, candles, bias, ma, ma_slope, df):
    """
    葛南维第四大法则 (均线修复)
    1. 均线持续下行 - 连续13个交易日 收盘价在MA60之下 / MA60下行
    2. 乖离率出现超卖 bias60 < -16
    3. K线出现止跌支撑信号 (看涨吞没/看涨锤头线/看涨螺旋桨/看涨孕线)

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param ma_slope:
    :param df: patterns df
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma60_slope = ma_slope[:, 5]
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
        return True
    else:
        return False


def is_ma60_fifth(index, candles, bias, ma, ma_slope, df):
    """
    葛南维第五大法则 (均线修复)
    1. 连续13个交易日 MA60上行 / ma60_slope > 1
    2. 乖离率出现超买 bias60 > 11%
    3. K线出现短期见顶信号 (看跌吞没/看跌锤头线/看跌螺旋桨/看跌孕线/看跌尽头线)

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param ma_slope:
    :param df: patterns df
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma60_slope = ma_slope[:, 5]
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

    if index > 90 and steady_on_ma() and _bias60 > 11 and \
            has_short_patterns(index, df) and \
            min(ma60_slope[index - 12: index]) > 1:
        return True
    else:
        return False


def is_ma60_sixth(index, candles, bias, ma, ma_slope, df):
    """
    葛南维第六大法则 (均线扭转)
    1. 趋势异态 - MA60开始由上行逐渐走平: 连续18个交易日 MA60上行
    2. 最近3日 MA60开始拐头向下 ma60_slope < 1
    2. bias60 正常
    3. K线出现短期见顶信号 >= 2 (看跌吞没/看跌锤头线/看跌螺旋桨/看跌孕线/看跌尽头线)

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param ma_slope:
    :param df: patterns df
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma60_slope = ma_slope[:, 5]
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
        return True
    else:
        return False


def is_ma60_seventh(index, candles, bias, ma, ma_slope, df):
    """
    葛南维第七大法则 (均线服从)
    1. 均线持续下行 - 连续13个交易日: MA60下行 (ma60_slope < 0)
    2. 反弹时未站上MA60之后 继续下行

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param ma_slope:
    :param df: patterns df
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma60_slope = ma_slope[:, 5]
    ma60 = ma[:, 5]
    _ma60 = ma60[index]
    bias60 = bias[:, 4]
    _bias60 = bias60[index]

    if index > 90 and _ma60 > 0:
        _low_bias60 = (_low - _ma60) * 100 / _ma60

    def steady_under_ma():
        flag = True
        for i in range(13):
            if candles[index - i][3] > ma60[index - i] or ma60[index - i] > ma60[index - i - 1]:
                flag = False
        return flag

    if index > 90 and _bias60 > -1 and steady_under_ma() and \
            has_short_patterns(index, df):
        return True
    else:
        return False


def is_ma60_eighth(index, candles, bias, ma, ma_slope, df):
    """
    葛南维第八大法则 (均线服从和死亡交叉)
    1. 均线持续下行 - 连续21个交易日 MA60下行 (ma60_slope < 0)
    2. 反弹短暂站上MA60之后 又继续下行
    3. 出现死亡交叉 (5/10 5/20 10/20 5/60 10/60)

    :param index:
    :param candles:
    :param bias:
    :param ma:
    :param ma_slope:
    :param df: patterns df
    :return:
    """

    candle = candles[index]
    _low = candle[2]
    _close = candle[3]
    ma60_slope = ma_slope[:, 5]
    ma60 = ma[:, 5]
    _ma60 = ma60[index]
    bias60 = bias[:, 4]
    _bias60 = bias60[index]

    if index > 90 and _ma60 > 0:
        _low_bias60 = (_low - _ma60) * 100 / _ma60

    def stand_on_ma_temp():
        tag = 0
        for i in range(7):
            if candles[index - i - 1][3] > ma60[index - i - 1]:
                tag += 1
        return tag >= 2

    def ma_down_steady():
        flag = True
        for i in range(21):
            # 如果 当前MA60 > 前值
            if ma60[index - i] > ma60[index - i - 1]:
                flag = False
        return flag

    if index > 90 and -2 < _bias60 < 0 and stand_on_ma_temp() and \
            ma_down_steady() and has_short_patterns(index, df):
        return True
    else:
        return False


def has_support_patterns(index, df):
    """
    当前Ticker 存在看涨K线形态
    看涨吞没
    下探上涨
    锤头线
    墓碑十字线
    蜻蜓十字线
    探水竿
    孕线
    十字孕线
    刺透形态
    梯底

    :param index:
    :param df:
    :return:
    """
    if df.iloc[index]['swallow_up'] > 0 or df.iloc[index]['down_rise'] > 0 \
            or df.iloc[index]['CDLHAMMER'] > 0 or df.iloc[index]['CDLGRAVESTONEDOJI'] > 0 \
            or df.iloc[index]['CDLDRAGONFLYDOJI'] > 0 or df.iloc[index]['CDLTAKURI'] > 0 \
            or df.iloc[index]['CDLHARAMI'] > 0 or df.iloc[index]['CDLHARAMICROSS'] > 0 \
            or df.iloc[index]['CDLPIERCING'] > 0 or df.iloc[index]['CDLLADDERBOTTOM'] > 0:
        return True

    return False


def has_bottom_patterns(index, df):
    """
    判断当前是否存在底部看涨K线形态
    看涨吞没
    旭日东升
    看涨螺旋桨
    锤头 (探水竿)
    倒锤头
    墓碑十字/倒T十字 CDLGRAVESTONEDOJI
    晨星 CDLMORNINGSTAR
    十字晨星 CDLMORNINGDOJISTAR
    刺透心态 CDLPIERCING

    :param index: 当前时间
    :param df:
    :return:
    """

    if df.iloc[index]['swallow_up'] > 0 or \
            df.iloc[index]['sunrise'] > 0 or \
            df.iloc[index]['down_screw'] > 0 or \
            df.iloc[index]['hammer'] > 0 or \
            df.iloc[index]['pour_hammer'] > 0 or \
            df.iloc[index]['CDLGRAVESTONEDOJI'] > 0 or \
            df.iloc[index]['CDLMORNINGSTAR'] > 0 or \
            df.iloc[index]['CDLMORNINGDOJISTAR'] > 0 or \
            df.iloc[index]['CDLPIERCING'] > 0:
        return True

    return False


def has_short_patterns(index, df):
    """
    判断当前是否存在看跌K线形态信号个数 > 1

    :param index: 当前时间
    :param df:
    :return:
    """
    patterns = get_patterns(df)
    arr = patterns[index]
    arr2 = np.argwhere(arr < 0)

    return len(arr2) > 1


def get_patterns(df):
    patterns = df[['CDLCLOSINGMARUBOZU', 'CDLDOJI', 'CDLDOJISTAR', 'CDLDRAGONFLYDOJI',
                   'CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLHANGINGMAN',
                   'CDLINVERTEDHAMMER', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE',
                   'CDLMARUBOZU', 'CDLRICKSHAWMAN', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE',
                   'CDLTAKURI',
                   'CDLCOUNTERATTACK', 'CDLDARKCLOUDCOVER', 'CDLGAPSIDESIDEWHITE',
                   'CDLHARAMI', 'CDLHARAMICROSS', 'CDLHOMINGPIGEON', 'CDLINNECK',
                   'CDLKICKING', 'CDLKICKINGBYLENGTH', 'CDLMATCHINGLOW', 'CDLONNECK',
                   'CDLSEPARATINGLINES', 'CDLTHRUSTING', 'CDLBELTHOLD', 'CDLENGULFING',
                   'CDLPIERCING',
                   'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE', 'CDL3OUTSIDE', 'CDL3STARSINSOUTH',
                   'CDLABANDONEDBABY', 'CDLUNIQUE3RIVER', 'CDLMORNINGSTAR', 'CDLMORNINGDOJISTAR',
                   'CDLEVENINGSTAR', 'CDLEVENINGDOJISTAR', 'CDL3WHITESOLDIERS', 'CDLADVANCEBLOCK',
                   'CDLHIGHWAVE', 'CDLHIKKAKE', 'CDLHIKKAKEMOD', 'CDLIDENTICAL3CROWS',
                   'CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH', 'CDLTASUKIGAP',
                   'CDLTRISTAR', 'CDLUPSIDEGAP2CROWS',
                   'CDL3LINESTRIKE', 'CDLCONCEALBABYSWALL',
                   'CDLBREAKAWAY', 'CDLLADDERBOTTOM', 'CDLMATHOLD', 'CDLRISEFALL3METHODS', 'CDLXSIDEGAP3METHODS'
                   ]].to_numpy()

    return patterns
