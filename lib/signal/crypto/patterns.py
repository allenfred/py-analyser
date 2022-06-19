import numpy as np

"""
K线形态

强势看涨形态
强势看跌形态
底部看涨形态
顶部看跌形态
"""


def has_long_patterns(index, df):
    """
    当前Ticker 存在看涨K线形态
    看涨吞没
    下探上涨
    下跌螺旋桨
    锤头线
    T字线
    刺透形态
    梯底

    :param index:
    :param df:
    :return:
    """
    if df.iloc[index]['swallow_up'] > 0 or \
            df.iloc[index]['down_rise'] > 0 or \
            df.iloc[index]['down_screw'] > 0 or \
            df.iloc[index]['hammer'] > 0 or \
            df.iloc[index]['t_line'] > 0 or \
            df.iloc[index]['CDLPIERCING'] > 0 or \
            df.iloc[index]['CDLLADDERBOTTOM'] > 0:
        return True

    return False


def has_short_patterns(index, df):
    """
    判断当前是否存在看跌K线形态

    黄昏之星(黄昏十字星)
    看跌吞没
    看跌螺旋桨
    射击之星
    倾盆大雨
    刺透形态

    :param index: 当前时间
    :param df:
    :return:
    """

    if df.iloc[index]['CDLEVENINGSTAR'] < 0 or \
            df.iloc[index]['CDLEVENINGDOJISTAR'] < 0 or \
            df.iloc[index]['swallow_down'] < 0 or \
            df.iloc[index]['up_screw'] < 0 or \
            df.iloc[index]['shooting'] < 0 or \
            df.iloc[index]['CDLPIERCING'] < 0:
        return True

    return False


def has_bottom_patterns(index, df):
    """
    判断当前是否存在底部看涨K线形态
    看涨吞没
    刺透心态 (旭日东升 / 曙光初现 / 好友反攻)
    看涨螺旋桨
    锤头
    早晨之星(早晨十字星)

    :param index: 当前时间
    :param df:
    :return:
    """

    if df.iloc[index]['swallow_up'] > 0 or \
            df.iloc[index]['sunrise'] > 0 or \
            df.iloc[index]['down_screw'] > 0 or \
            df.iloc[index]['hammer'] > 0 or \
            df.iloc[index]['t_line'] > 0 or \
            df.iloc[index]['CDLMORNINGSTAR'] > 0 or \
            df.iloc[index]['CDLMORNINGDOJISTAR'] > 0:
        return True

    return False


def has_top_patterns(index, df):
    """
    判断当前是否存在顶部看跌K线形态
    看跌吞没
    看跌螺旋桨
    射击之星
    射击十字星
    倾盆大雨
    阻力线(上影线占K线长度1/2)
    刺透形态
    黄昏之星(黄昏十字星)

    :param index:
    :param df:
    :return:
    """

    if df.iloc[index]['swallow_down'] < 0 or \
            df.iloc[index]['up_screw'] < 0 or \
            df.iloc[index]['shooting'] < 0 or \
            df.iloc[index]['shooting_doji'] < 0 or \
            df.iloc[index]['down_pour'] < 0 or \
            df.iloc[index]['resistance_shadow'] < 0 or \
            df.iloc[index]['CDLPIERCING'] < 0 or \
            df.iloc[index]['CDLEVENINGSTAR'] < 0 or \
            df.iloc[index]['CDLEVENINGDOJISTAR'] < 0:
        return True

    return False


def has_long_break_patterns(index, df):
    """
    判断当前是否存在看涨K线形态
    大阳线
    光头光脚
    一阳穿三线
    一阳穿四线

    :param index: 当前时间
    :param df:
    :return:
    """
    _cnt = 0

    if df.iloc[index]['long_line'] > 0 or \
            df.iloc[index]['marubozu'] > 0 or \
            df.iloc[index]['up_cross3ma'] > 0 or \
            df.iloc[index]['up_cross4ma'] > 0:
        return True

    return _cnt > 1


def has_short_break_patterns(index, df):
    """
    判断当前是否存在看跌突破K线形态
    大阴线
    光头光脚
    一阴穿三线
    一阴穿四线

    :param index: 当前时间
    :param df:
    :return:
    """
    _cnt = 0

    if df.iloc[index]['long_line'] < 0 or \
            df.iloc[index]['marubozu'] < 0 or \
            df.iloc[index]['drop_cross3ma'] < 0 or \
            df.iloc[index]['drop_cross4ma'] < 0:
        return True

    return _cnt > 1


