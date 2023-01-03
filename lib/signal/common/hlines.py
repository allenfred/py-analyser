import numpy as np


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


def limit_pullback(df, index):
    return False
