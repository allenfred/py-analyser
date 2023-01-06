import numpy as np

_start_at = 100


def is_support(df, i):
    support = df['low'][i] < df['low'][i - 1] < df['low'][i - 2] and \
              df['low'][i] < df['low'][i + 1] < df['low'][i + 2]

    return support


def is_resistance(df, i):
    resistance = df['high'][i] > df['high'][i - 1] > df['high'][i - 2] and \
                 df['high'][i] > df['high'][i + 1] > df['high'][i + 2]

    return resistance


def calc_hlines(df, index):
    """
    计算水平位
    :param df:
    :param index:
    :return:
    """

    if index < 20:
        return []

    # volatility 波动率
    s = np.mean(df['high'] - df['low'])

    def is_far_from_level(l):
        return np.sum([abs(l - x) < s for x in levels]) == 0

    levels = []
    hlines = []

    for i in range(2, index - 2):
        if is_support(df, i):
            l = df['low'][i]

            if is_far_from_level(l):
                levels.append((i, l))
                hlines.append(l)

        elif is_resistance(df, i):
            l = df['high'][i]

            if is_far_from_level(l):
                levels.append((i, l))
                hlines.append(l)

    return hlines


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
        return False

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
def limit_pullback(df, index):
    """
    涨停回调
    1.
    :param df:
    :param index:
    :return:
    """

    return False


def up_pullback(df, index):
    """
    上涨回调

    :param df:
    :param index:
    :return:
    """
    return False


def down_pullback(df, index):
    """
    下跌回调

    :param df:
    :param index:
    :return:
    """
    return False


def hline_support(df, index):
    """
    水平支撑

    :param df:
    :param index:
    :return:
    """
    return False


def hline_resistance(df, index):
    """
    水平阻力

    :param df:
    :param index:
    :return:
    """
    return False
