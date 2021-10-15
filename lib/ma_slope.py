from talib import SMA
import numpy as np
import math

rad2degree = 180 / 3.14159265359  # pi
i_bars_back = 10


def slope(close, isma):
    sma_x = SMA(close, isma)
    sma_x = np.nan_to_num(sma_x, nan=0)
    slope_arr = []

    for index, value in enumerate(sma_x):
        val = round(rad2degree * math.atan((value - sma_x[index - i_bars_back]) / i_bars_back), 2)
        slope_arr.insert(index, val)

    return slope_arr
