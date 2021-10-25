#!/usr/bin/python3
# -*- coding:utf-8 -*-
import os
import sys

path = os.path.dirname(os.path.abspath(__file__))

import math
import pandas as pd
import numpy as np


# close: ndarray
def td(close):
    high_td_series = []
    low_td_series = []

    for index, value in enumerate(close):
        if index < 4:
            high_td_series.insert(index, 0)
            low_td_series.insert(index, 0)
        else:
            # 低9 如果当前收盘价低于四天前收盘价
            if value < close[index - 4]:
                if not low_td_series[index - 1] == 9:
                    low_td_series.insert(index, low_td_series[index - 1] + 1)
                else:
                    low_td_series.insert(index, 1)
            else:
                low_td_series.insert(index, 0)

            # 高9 如果当前收盘价高于四天前收盘价
            if value > close[index - 4]:
                if not high_td_series[index - 1] == 9:
                    high_td_series.insert(index, high_td_series[index - 1] + 1)
                else:
                    high_td_series.insert(index, 1)
            else:
                high_td_series.insert(index, 0)

    return high_td_series, low_td_series
