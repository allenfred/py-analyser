import numpy as np
from .util import has_support_patterns, has_bottom_patterns, has_top_patterns, is_strong_bull, is_strong_bear

_start_at = 100


def is_up_trend(index, df):
    """
    趋势上涨

    :param index:
    :param df:
    :return:
    """

    return df.iloc[index]['steady_on_ma120'] == 1


def is_down_trend(index, df):
    """
    趋势下跌

    :param index:
    :param df:
    :return:
    """

    return df.iloc[index]['steady_below_ma120'] == 1


def is_strong_decline(index, df):
    """
    强势下跌:

    1.ma120 连续13日下行
    2.ma60  连续13日下行
    3.ma60  连续13日在ma120之下运行
    3.收盘价 连续13日位于ma60之下
    :param index:
    :param df:
    :return:
    """
    ma = df[['ma20', 'ma30', 'ma60', 'ma120']].to_numpy()
    close = df['close'].to_numpy()
    ma60 = ma[:, 2]
    ma120 = ma[:, 3]

    close_below_ma60_13days = True
    ma60_decline_13days = True
    ma60_below_ma120_13days = True

    for i in range(13):
        # 如果当前 MA60 > 前值
        if ma60[index - i] > ma60[index - i - 1]:
            ma60_decline_13days = False

        # 如果当前 close > 前值
        if close[index - i] > ma60[index - i]:
            close_below_ma60_13days = False

        # 如果当前 MA60 > MA120
        if ma60[index - i] > ma120[index - i]:
            ma60_below_ma120_13days = False

    return \
        ma60_decline_13days and close_below_ma60_13days and ma60_below_ma120_13days and \
        df.iloc[index]['steady_below_ma60'] == 1 and df.iloc[index]['steady_below_ma120'] == 1


def is_strong_rise(index, df):
    """
    强势上涨:
    120日 ma60/ma120 呈微笑曲线

    1.ma120 连续13日上行
    2.ma60  连续13日上行
    3.ma60  连续13日在ma120之上运行
    4.收盘价 连续13日位于ma60之上
    :param index:
    :param df:
    :return:
    """
    ma = df[['ma20', 'ma30', 'ma60', 'ma120']].to_numpy()
    close = df['close'].to_numpy()
    ma60 = ma[:, 2]
    ma120 = ma[:, 3]

    close_on_ma60_13days = True
    ma60_steady_13days = True
    ma60_on_ma120_13days = True

    for i in range(13):
        # 如果当前 MA60 <= 前值
        if ma60[index - i] < ma60[index - i - 1]:
            ma60_steady_13days = False

        # 如果当前 close <= 前值
        if close[index - i] < ma60[index - i]:
            close_on_ma60_13days = False

        # 如果当前 MA60 < MA120
        if ma60[index - i] < ma120[index - i]:
            ma60_on_ma120_13days = False

    # if \
    #         ma60_steady_13days and close_on_ma60_13days and ma60_on_ma120_13days and \
    #                 steady_on_ma120(index, df):
    #     print(df.iloc[index]['trade_date'], 'is_strong_rise')

    return \
        ma60_steady_13days and close_on_ma60_13days and ma60_on_ma120_13days and \
        df.iloc[index]['steady_on_ma120'] == 1


def up_pullback(df, i):
    """
    上涨回调

    1.is_up_trend  (steady_on_ma120)
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

    1.is_down_trend (MA60/MA120 下行)
    2.反弹至MA60/MA120附近（-5 < bias60/bias120 < 0）
    3.出现空头阻力K线形态

    :param df:
    :param i:
    :return:
    """

    _close = df.iloc[i]['close']
    _low = df.iloc[i]['low']

    # if df.iloc[i]['up_trend'] == 1 and \
    #         (has_support_patterns(df, i) or has_bottom_patterns(df, i)
    #          or has_support_patterns(df, i - 1) or has_bottom_patterns(df, i - 1)
    #          or has_support_patterns(df, i - 2) or has_bottom_patterns(df, i - 2)):
    if df.iloc[i]['down_trend'] == 1 and \
            (-5 <= df.iloc[i]['bias60'] <= 0 or -5 < df.iloc[i]['bias120'] <= 0):
        return 1

    return 0


def up_break(df, i, isStock=True):
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

    # 收盘价站上所有均线
    def stand_on_ma():
        return df.iloc[i]['ma5'] < _close and df.iloc[i]['ma10'] < _close and \
               df.iloc[i]['ma20'] < _close and df.iloc[i]['ma60'] < _close and \
               df.iloc[i]['ma120'] < _close

    if stand_on_hline() and is_strong_bull(df, i) and stand_on_ma():
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
