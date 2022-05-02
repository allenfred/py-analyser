from talib import SMA, EMA
import numpy as np
import math


def slope(close, ma_type, ima):
    """
    description:

    :param close:
    :param ma_type:
    :param ima:
    :return:
    """

    rad2degree = 180 / 3.14159265359  # pi
    i_bars_back = 5

    ma = []
    if ma_type == 'SMA':
        ma = SMA(close, ima)
    else:
        ma = EMA(close, ima)
    ma = np.nan_to_num(ma, nan=0)
    slope_arr = []

    for index, value in enumerate(ma):
        val = round(rad2degree * math.atan((value - ma[index - i_bars_back]) / i_bars_back), 2)
        slope_arr.insert(index, val)

    return slope_arr
