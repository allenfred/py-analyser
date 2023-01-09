"""
fractal candlestick pattern

https://towardsdatascience.com/detection-of-price-support-and-resistance-levels-in-python-baedc44c34c9

https://medium.datadriveninvestor.com/how-to-detect-support-resistance-levels-and-breakout-using-python-f8b5dac42f21
"""
import numpy as np
from .util import has_support_patterns, has_bottom_patterns

_start_at = 100


# determine bullish fractal
def is_support(df, i):
    cond1 = df['low'][i] < df['low'][i - 1]
    cond2 = df['low'][i] < df['low'][i + 1]
    cond3 = df['low'][i + 1] < df['low'][i + 2]
    cond4 = df['low'][i - 1] < df['low'][i - 2]

    return cond1 and cond2 and cond3 and cond4


# determine bearish fractal
def is_resistance(df, i):
    cond1 = df['high'][i] > df['high'][i - 1]
    cond2 = df['high'][i] > df['high'][i + 1]
    cond3 = df['high'][i + 1] > df['high'][i + 2]
    cond4 = df['high'][i - 1] > df['high'][i - 2]

    return cond1 and cond2 and cond3 and cond4


# to make sure the new level area does not exist already
def is_far_from_level(value, levels, df):
    ave = np.mean(df['high'] - df['low'])
    return np.sum([abs(value - level) < ave for _, level in levels]) == 0


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

    # a list to store resistance and support levels
    levels = []
    hlines = []

    for i in range(2, df.shape[0] - 2):
        if is_support(df, i):
            low = df['low'][i]
            if is_far_from_level(low, levels, df):
                levels.append((i, low))
                hlines.append(low)

        elif is_resistance(df, i):
            high = df['high'][i]
            if is_far_from_level(high, levels, df):
                levels.append((i, high))
                hlines.append(high)

    return hlines
