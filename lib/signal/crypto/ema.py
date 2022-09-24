import numpy as np
import math as math


# MA 信号


def is_ema20_rise(index, ema):
    ema20 = ema[:, 2]

    def ma_rise():
        flag = True
        for i in range(7):
            # 如果 当前EMA20 <= 前值
            if ema20[index - i] <= ema20[index - i - 1]:
                flag = False
        return flag

    if index > 60 and ma_rise():
        return True
    else:
        return False


def is_ema30_rise(index, ema):
    ema30 = ema[:, 3]

    def ma_rise():
        flag = True
        for i in range(7):
            # 如果 当前EMA30 <= 前值
            if ema30[index - i] <= ema30[index - i - 1]:
                flag = False
        return flag

    if index > 60 and ma_rise():
        return True
    else:
        return False


def is_ema60_rise(index, ema):
    ema60 = ema[:, 5]

    def ma_rise():
        flag = True
        for i in range(13):
            # 如果 当前EMA60 <= 前值
            if ema60[index - i] <= ema60[index - i - 1]:
                flag = False
        return flag

    if index > 90 and ma_rise():
        return True
    else:
        return False


def is_ema120_rise(index, ema):
    ema120 = ema[:, 6]

    def ma_rise():
        flag = True
        for i in range(13):
            # 如果 当前EMA120 <= 前值
            if ema120[index - i] <= ema120[index - i - 1]:
                flag = False
        return flag

    if index > 150 and ma_rise():
        return True
    else:
        return False


def is_ema20_down(index, ema):
    ema20 = ema[:, 2]

    def ma_down():
        flag = True
        for i in range(7):
            # 如果 当前EMA20 >= 前值
            if ema20[index - i] >= ema20[index - i - 1]:
                flag = False
        return flag

    if index > 60 and ma_down():
        return True
    else:
        return False


def is_ema30_down(index, ema):
    ema30 = ema[:, 3]

    def ma_down():
        flag = True
        for i in range(9):
            # 如果 当前EMA30 >= 前值
            if ema30[index - i] >= ema30[index - i - 1]:
                flag = False
        return flag

    if index > 60 and ma_down():
        return True
    else:
        return False


def is_ema60_down(index, ema):
    ema60 = ema[:, 5]

    def ma_down():
        flag = True
        for i in range(13):
            # 如果 当前EMA60 >= 前值
            if ema60[index - i] >= ema60[index - i - 1]:
                flag = False
        return flag

    if index > 90 and ma_down():
        return True
    else:
        return False


def is_ema120_down(index, ema):
    ema120 = ema[:, 6]

    def ma_down():
        flag = True
        for i in range(13):
            # 如果 当前EMA120 >= 前值
            if ema120[index - i] >= ema120[index - i - 1]:
                flag = False
        return flag

    if index > 150 and ma_down():
        return True
    else:
        return False
