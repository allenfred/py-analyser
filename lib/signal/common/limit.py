import numpy as np
from .util import has_support_patterns, has_bottom_patterns

_start_at = 100


def limit_up_gene(i, candles, df):
    """
    description: 涨停基因(看涨)
    标准 1:
    最近22个交易日有涨停
    价格 回调至上个涨停区间 0.5

    标准 2:
    最近20个交易日有涨停
    价格 回调至上个涨停区间
    回调至 MA20/MA60 附近

    :param i: 当前tick
    :param candles:
    :param df:
    :return: boolean
    """

    if i < _start_at:
        return 0

    if 'limit' not in df.columns:
        return 0

    ma = df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()

    _open = candles[:, 0][i]
    _low = candles[:, 2][i]
    _close = candles[:, 3][i]
    ma20 = ma[:, 2]
    ma60 = ma[:, 5]

    def steady_on_ma():
        if _close > ma60[i] and (df.iloc[i]['ma60_up'] == 1 or df.iloc[i]['ma30_up'] == 1):
            return True

        return False

    # 回调至涨停区间
    def back_limit_zone():
        flag = False

        for j in range(1, 21):
            if df.iloc[i - j]['limit'] == 'U' and \
                    (df.iloc[i - j]['close'] > _close or df.iloc[i - j]['close'] * 0.95 > _low) and \
                    (df.iloc[i]['bias24'] < 10 and df.iloc[i]['bias60'] < 10):
                flag = True

        return flag

    # 最近22个交易日内无连续上涨行情
    def has_no_crazy_up():
        flag = True
        for j in range(0, 21):
            if df.iloc[i - j]['bias24'] > 30:
                flag = False
        return flag

    # if steady_on_ma() and back_limit_zone() and has_no_crazy_up():
    if steady_on_ma() and back_limit_zone():
        # print('limit_up_gene', df.iloc[i]['trade_date'], i)
        return 1

    return 0


# 参看 西安饮食 西安旅游 拟合
def limit_pullback(df, i):
    """
    涨停回调

    1.最近30个交易日有涨停
    2.回撤至涨停区间或起涨点附近
    3.回撤至某一水平位（且最近3个交易日触及关键水平 或 接近水平位出现下影线）
    4.该水平位具有强支撑阻力(过去30日交易日 触及且收盘低于该水平K线数量 <= 3)
    5.最近3个交易日具有 多头K线信号

    :param df:
    :param i:
    :return:
    """

    if 'limit' not in df.columns:
        return 0

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

    def back_limit_zone():
        flag = False

        for j in range(1, 30):
            if df.iloc[i - j]['limit'] == 'U' and \
                    (df.iloc[i - j]['close'] > _close or df.iloc[i - j]['close'] > _low):
                flag = True

        return flag

    if back_key_level() and back_limit_zone() and \
            (has_support_patterns(df, i) or has_bottom_patterns(df, i)
             or has_support_patterns(df, i - 1) or has_bottom_patterns(df, i - 1)
             or has_support_patterns(df, i - 2) or has_bottom_patterns(df, i - 2)):
        # print(df.iloc[i]['trade_date'], 'limit_pullback')
        return 1

    return 0
