import numpy as np
from .util import has_support_patterns, has_bottom_patterns, has_top_patterns, is_strong_bull, is_strong_bear
from .ma import is_up_trend

_start_at = 100


def up_pullback(df, i):
    """
    上涨回调

    1.is_up_trend
    2.回撤至MA60/MA120附近（0 < bias60/bias120 < 5）
    3.出现看涨K线形态

    :param df:
    :param i:
    :return:
    """
    if df.iloc[i]['up_trend'] == 1 and \
            (0 <= df.iloc[i]['bias60'] <= 5 or 0 <= df.iloc[i]['bias120'] <= 5):
        return 1

    return 0


def down_pullback(df, i):
    """
    下跌反弹

    1.短中期处于下跌趋势 (MA20/MA30/MA60 下行)
    2.反弹至关键水平位附近
    3.关键水平位附近出现空头阻力K线形态

    :param df:
    :param i:
    :return:
    """

    _close = df.iloc[i]['close']
    _low = df.iloc[i]['low']
    hlines = df.iloc[i]['hlines']

    def down_trend():
        return df.iloc[i]['ma20_down'] == 1 or df.iloc[i]['ma30_down'] == 1 or df.iloc[i]['ma60_down'] == 1

    def back_key_level():
        valid_level = False
        down_recently = True
        bad_kline_cnt = 0

        for j in range(len(hlines)):
            if df.iloc[i]['high'] > hlines[j] > df.iloc[i]['close']:
                key_hline = hlines[j]

                if key_hline > 0:
                    for k in range(30):
                        # 如果收盘价高于水平位 视为 bad kline
                        if df.iloc[i - k]['high'] > key_hline > df.iloc[i - k]['low'] \
                                and df.iloc[i - k]['close'] > key_hline:
                            bad_kline_cnt += 1

                    for j in range(1, 8):
                        if df.iloc[i - j]['close'] > key_hline:
                            down_recently = False

                    if bad_kline_cnt <= 3:
                        valid_level = True

        return valid_level and down_recently

    if down_trend() and back_key_level() and \
            (has_support_patterns(df, i) or has_bottom_patterns(df, i)
             or has_support_patterns(df, i - 1) or has_bottom_patterns(df, i - 1)
             or has_support_patterns(df, i - 2) or has_bottom_patterns(df, i - 2)):
        # print(df.iloc[i]['trade_date'], 'up_pullback')
        return 1

    return 0


def up_break(df, i):
    """
    向上突破/水平突破

    1.最近20个交易日收盘价位于该关键水平位之下
    2.最新收盘价位于水平位之上
    3.向上突破K线为 涨停/大阳线/放量

    :param df:
    :param i:
    :return:
    """

    _close = df.iloc[i]['close']
    _low = df.iloc[i]['low']
    hlines = df.iloc[i]['hlines']

    # 收盘价站上关键水平位
    def stand_on_hline():
        valid_level = True
        hline = 0

        for j in range(len(hlines)):
            if df.iloc[i]['close'] > hlines[j] > df.iloc[i - 1]['close']:
                hline = hlines[j]

        if hline > 0:
            for j in range(1, 30):
                if df.iloc[i - j]['close'] > hline:
                    valid_level = False

        return hline > 0 and valid_level

    if stand_on_hline() and is_strong_bull(df, i) and \
            (df.iloc[i]['ma20_up'] == 1 or df.iloc[i]['ma30_up'] == 1):
        # print(df.iloc[i]['trade_date'], 'up_break')
        return 1

    return 0


def down_break(df, i):
    """
    向下突破/水平跌破

    1.最近20个交易日收盘价位于该关键水平位之上
    2.最新收盘价位于水平位之下
    3.向下突破K线为 跌停/大阴线/放量

    :param df:
    :param i:
    :return:
    """

    _close = df.iloc[i]['close']
    _low = df.iloc[i]['low']
    hlines = df.iloc[i]['hlines']

    # 收盘价站上关键水平位
    def stand_on_hline():
        valid_level = True
        hline = 0

        for j in range(len(hlines)):
            if df.iloc[i]['close'] > hlines[j] > df.iloc[i - 1]['close']:
                hline = hlines[j]

        if hline > 0:
            for j in range(1, 30):
                if df.iloc[i - j]['close'] > hline:
                    valid_level = False

        return hline > 0 and valid_level

    if stand_on_hline() and is_strong_bear(df, i) and \
            (df.iloc[i]['ma20_down'] == 1 or df.iloc[i]['ma30_down'] == 1):
        # print(df.iloc[i]['trade_date'], 'up_break')
        return 1

    return 0


def hline_support(df, i):
    """
    水平支撑

    1.长期下跌趋势(ma20_down / ma60_down)
    2.价格在关键水平位出现底部支撑形态

    :param df:
    :param i:
    :return:
    """

    _close = df.iloc[i]['close']
    _low = df.iloc[i]['low']
    hlines = df.iloc[i]['hlines']

    def back_key_level():
        valid_level = False
        up_recently = True
        bad_kline_cnt = 0

        for j in range(len(hlines)):
            if df.iloc[i]['close'] > hlines[j] > df.iloc[i]['low']:
                key_hline = hlines[j]

                if key_hline > 0:
                    for k in range(30):
                        if df.iloc[i - k]['high'] > key_hline > df.iloc[i - k]['low'] \
                                and df.iloc[i - k]['close'] < key_hline:
                            bad_kline_cnt += 1

                    for j in range(1, 8):
                        if df.iloc[i - j]['close'] < key_hline:
                            up_recently = False

                    if bad_kline_cnt <= 3:
                        valid_level = True

        return valid_level and up_recently

    if back_key_level() and \
            (has_support_patterns(df, i) or has_bottom_patterns(df, i)
             or has_support_patterns(df, i - 1) or has_bottom_patterns(df, i - 1)
             or has_support_patterns(df, i - 2) or has_bottom_patterns(df, i - 2)):
        # print(df.iloc[i]['trade_date'], 'up_pullback')
        return 1

    return 0


def hline_resistance(df, i):
    """
    水平阻力

    1.短期下跌趋势(ma20_down / ma60_down)
    2.价格在关键水平位出现底部支撑形态

    :param df:
    :param i:
    :return:
    """

    _close = df.iloc[i]['close']
    _low = df.iloc[i]['low']
    hlines = df.iloc[i]['hlines']

    def back_key_level():
        valid_level = False
        up_recently = True
        bad_kline_cnt = 0

        for j in range(len(hlines)):
            if df.iloc[i]['close'] > hlines[j] > df.iloc[i]['low']:
                key_hline = hlines[j]

                if key_hline > 0:
                    for k in range(30):
                        if df.iloc[i - k]['high'] > key_hline > df.iloc[i - k]['low'] \
                                and df.iloc[i - k]['close'] < key_hline:
                            bad_kline_cnt += 1

                    for j in range(1, 8):
                        if df.iloc[i - j]['close'] < key_hline:
                            up_recently = False

                    if bad_kline_cnt <= 3:
                        valid_level = True

        return valid_level and up_recently

    if back_key_level() and \
            (has_top_patterns(df, i) or has_top_patterns(df, i - 1) or has_top_patterns(df, i - 2)):
        # print(df.iloc[i]['trade_date'], 'up_pullback')
        return 1

    return 0
