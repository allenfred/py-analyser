import numpy as np

_start_at = 100


def is_strong_bull(df, i):
    """
    量价配合
    1.强势K线形态
    2.成交量

    :param df:
    :param i:
    :return:
    """
    if (df.iloc[i]['long_line'] > 0 or df.iloc[i]['marubozu'] > 0 or df.iloc[i]['limit'] == 'U') and \
            (df.iloc[i]['high_vol'] > 0 or df.iloc[i]['large_vol'] > 0 or df.iloc[i]['huge_vol'] > 0
             or df.iloc[i]['max_vol'] > 0 or df.iloc[i]['increasingly_vol'] > 0):
        return True

    return False


def has_support_patterns(df, index):
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
    吞噬形态
    梯底

    :param df:
    :param index:
    :return:
    """
    if df.iloc[index]['swallow_up'] > 0 or \
            df.iloc[index]['down_rise'] > 0 or \
            df.iloc[index]['CDLHAMMER'] > 0 or \
            df.iloc[index]['CDLGRAVESTONEDOJI'] > 0 \
            or df.iloc[index]['CDLDRAGONFLYDOJI'] > 0 \
            or df.iloc[index]['CDLTAKURI'] > 0 \
            or df.iloc[index]['CDLHARAMI'] > 0 \
            or df.iloc[index]['CDLHARAMICROSS'] > 0 \
            or df.iloc[index]['CDLPIERCING'] > 0 \
            or df.iloc[index]['CDLENGULFING'] > 0 \
            or df.iloc[index]['flat_base'] > 0:
        return True

    return False


def has_bottom_patterns(df, index):
    """
    判断当前是否存在底部看涨K线形态
    看涨吞没
    吞噬模式 CDLENGULFING
    旭日东升
    看涨螺旋桨
    锤头 (探水竿)
    倒锤头
    墓碑十字/倒T十字 CDLGRAVESTONEDOJI
    晨星 CDLMORNINGSTAR
    十字晨星 CDLMORNINGDOJISTAR
    刺透形态 CDLPIERCING
    反击线 CDLCOUNTERATTACK
    梯底

    :param df:
    :param index:
    :return:
    """

    if df.iloc[index]['swallow_up'] > 0 or \
            df.iloc[index]['CDLENGULFING'] > 0 or \
            df.iloc[index]['sunrise'] > 0 or \
            df.iloc[index]['down_screw'] > 0 or \
            df.iloc[index]['hammer'] > 0 or \
            df.iloc[index]['pour_hammer'] > 0 or \
            df.iloc[index]['CDLGRAVESTONEDOJI'] > 0 or \
            df.iloc[index]['CDLMORNINGSTAR'] > 0 or \
            df.iloc[index]['CDLMORNINGDOJISTAR'] > 0 or \
            df.iloc[index]['CDLPIERCING'] > 0 or \
            df.iloc[index]['CDLCOUNTERATTACK'] > 0 or \
            df.iloc[index]['flat_base'] > 0:
        return True

    return False
