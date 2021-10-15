import os.path as path
import pandas as pd
import datetime
import talib
import numpy as np
import math as math


def assert_msg(condition, msg):
    if not condition:
        raise Exception(msg)


def read_file(filename):
    # 获得文件绝对路径
    filepath = path.join(path.dirname(__file__), filename)

    # 判定文件是否存在
    assert_msg(path.exists(filepath), "文件不存在")

    # 读取CSV文件并返回
    return pd.read_csv(
        filepath, index_col=0, parse_dates=True, infer_datetime_format=True
    )


def convert_date(date):
    if isinstance(date, (datetime.date, datetime.datetime)):
        beijing = datetime.timezone(datetime.timedelta(hours=8))
        return date.astimezone(beijing).strftime("%Y-%m-%d %H:%M:%S")


def SMA(values, n):
    """
    返回简单滑动平均
    """
    return pd.Series(values).rolling(n).mean()


def crossover(series1, series2) -> bool:
    """
    检查两个序列是否在结尾交叉
    :param series1:  序列1
    :param series2:  序列2
    :return:         如果交叉返回True，反之False
    """
    return series1[-2] < series2[-2] and series1[-1] > series2[-1]


def MACDCrossover(series1, series2, tick) -> bool:
    """
    检查两个序列是否在结尾交叉,是否存在看多
    :param series1:  序列1
    :param series2:  序列2
    :return:         如果交叉返回True，反之False
    """
    return series1[tick - 1] < series2[tick - 1] and series1[tick] > series2[tick]


# the right algorithm for StochRSI.
def StochRSI(close):
    RSI = talib.RSI(np.array(close), timeperiod=14)
    LLV = pd.Series(RSI).rolling(window=14).min()
    HHV = pd.Series(RSI).rolling(window=14).max()
    stochRSI = (RSI - LLV) / (HHV - LLV) * 100
    stochRSI = talib.MA(np.array(stochRSI), 3)
    stochRSI = np.around(stochRSI, decimals=4, out=None)
    fastk = talib.MA(np.array(stochRSI), 3)
    fastk = np.around(fastk, decimals=4, out=None)
    return stochRSI, fastk


def LLV(array, period):
    min = array[len(array) - period]
    for index, val in enumerate(array[len(array) - period :]):
        if val < min:
            min = val
    return min


def HHV(array, period):
    max = array[len(array) - period]
    for index, val in enumerate(array[len(array) - period :]):
        if val > max:
            max = val
    return max


def go_short(candle, deviation_percent=0.01):
    open = candle["open"]
    close = candle["close"]
    high = candle["high"]
    low = candle["low"]

    # 偏差
    deviation = round((high - low) * deviation_percent, 2)

    """
    判断K线是否为流星线形态 (长上影线)
    """
    k_len = high - low
    bar_len = math.fabs(open - close)
    down_shadow_len = math.fabs(open - low if open < close else close - low)
    down_one_third = low + (k_len / 3)
    down_half = low + (k_len / 2)

    # 流星线判读标准：（上升行情中的看空信号）
    # 开盘价和收盘价都位于k线下方1/3处 (即：上影线长度占k线长度的2/3以上）
    # 下影线长度需小于柱体长度的1/2
    if (
        open - deviation <= down_one_third + deviation
        and close - deviation <= down_one_third + deviation
        # and down_shadow_len < bar_len
    ):
        return True

    # 流星线判读标准：（上升行情中的看空信号）
    # 开盘价和收盘价都位于k线下方1/3处 (即：上影线长度占k线长度的2/3以上）
    # 下影线长度需小于柱体长度的1/2
    if (
        open + deviation >= down_half - deviation
        and close + deviation >= down_half - deviation
        and down_shadow_len < bar_len / 5
    ):
        return True

    return False


def go_long(candle, deviation_percent=0.01):
    open = candle["open"]
    close = candle["close"]
    high = candle["high"]
    low = candle["low"]

    # 偏差
    deviation = round((high - low) * deviation_percent, 2)

    """
    判断K线是否为锤子线形态 (长下影线)
    """
    k_len = high - low
    bar_len = math.fabs(open - close)
    up_shadow_len = math.fabs(open - low if open < close else close - low)
    up_one_third = high - (k_len / 3)
    up_half = high - (k_len / 2)

    # 锤子线判读标准1：（下跌行情中的看多信号）
    # 开盘价和收盘价都位于k线上方1/3处 (即：下影线长度占k线长度的2/3以上）
    # 上影线长度需小于柱体长度的1/2
    if (
        open + deviation >= up_one_third - deviation
        and close + deviation >= up_one_third - deviation
        # and up_shadow_len < bar_len
    ):
        return True

    # 锤子线判读标准2：（下跌行情中的看多信号）
    # 开盘价和收盘价都位于k线上方1/2处 (即：下影线长度占k线长度的1/2以上）
    # 上影线长度需小于柱体长度的1/5
    if (
        open + deviation >= up_half - deviation
        and close + deviation >= up_half - deviation
        and up_shadow_len < bar_len / 5
    ):
        return True

    return False


# 根据流星线 获取开仓价位
def get_short_open_price(candle):
    open = candle["open"]
    close = candle["close"]
    high = candle["high"]
    low = candle["low"]

    return math.floor((high - low) / 2)


# 获取开仓价位
def get_open_price(candle):
    high = candle["high"]
    low = candle["low"]

    return math.floor((high - low) / 2 + low)


# 设置标准差(deviation)为 K线长度 1%
def is_pin_bar(candle):
    high = candle["high"]
    low = candle["low"]

    if go_short(candle) or go_long(candle):
        return True

    return False


def get_candle_dict(data, i):
    return {
        "open": data.open[i],
        "close": data.close[i],
        "high": data.high[i],
        "low": data.low[i],
    }


# 有效标准：
# 若是针向上pinbar最高价高于过去7根K线；
# 若是针向下pinbar最低价低于过去7根K线
# pinbar的柱体端必须没有影线或者影线长度小于柱体长度的1/2
def is_valid_pin_bar(i, data):
    open = data.open[i]
    close = data.close[i]
    high = data.high[i]
    low = data.low[i]

    bar_len = high - low

    # 需要比较的K线数量
    count = 7

    # 剔除十字星
    if -1 < open - close < 1:
        return False, 0

    # 看空
    if go_short(get_candle_dict(data, i)):
        total_bar_len = 0
        for num in range(count):
            total_bar_len += data.high[i - num] - data.low[i - num]
            if (i + num) < len(data) and data.high[i - num] > high:
                return False, 0

        if bar_len < math.floor(total_bar_len / 7):
            return False, 0

        return True, -1

    # 看涨
    if go_long(get_candle_dict(data, i)):
        for num in range(count):
            if (i + num) < len(data) and data.low[i - num] < low:
                return False, 0
        return True, 1

    return False, 0


"""
description: 看涨吞没形态
有效标准：
1.市场处于清晰的下降趋势
2.第二根K线必须吞没第一根
3.第二根实体必须与第一个实体颜色相反
4.之前的趋势超长，或非常剧烈的震荡

param {*} i 当前时间tick
param {*} data 行情数据dataFrame
return {*} Flag:boolean 是否看涨吞没
return {*} Unit:number  开仓单位
"""


def is_swallow_up(i, data):
    open = data.open[i]
    close = data.close[i]
    high = data.high[i]
    low = data.low[i]

    # 获取前一根K线 OHLC
    pre_open = data.open[i - 1]
    pre_close = data.close[i - 1]
    pre_high = data.high[i - 1]
    pre_low = data.low[i - 1]

    k_len = high - low
    bar_len = close - open if open < close else open - close
    pre_bar_len = pre_close - pre_open if pre_close < pre_open else pre_open - pre_close

    # 标准形态 2个单位 （1个单位对应 1% 仓位）
    # 强势形态 2个单位
    # *长期趋势形态 2个单位
    # 有效成交量 2个单位

    position_unit = 0
    is_long = False

    # 满足基本定义
    if (
        is_short_tendency(i, data)
        and open < close
        # and bar_len > k_len // 2
        and pre_open > pre_close
        and open - 1 <= pre_close
        and close > pre_open
        and high >= pre_high
        and low <= pre_low
    ):
        position_unit += 2

        if bar_len > pre_bar_len * 1.5:
            position_unit += 2

        if data.volume[i] > data.volume[i - 1]:
            position_unit += 2

    if position_unit > 0:
        is_long = True

    return is_long, position_unit


"""
description: 看跌吞没形态
有效标准：
1.市场处于清晰的下降趋势
2.第二根K线必须吞没第一根
3.第二根实体必须与第一个实体颜色相反
4.之前的趋势超长，或非常剧烈的震荡

param {*} i 当前时间tick
param {*} data 行情数据dataFrame
return {*} Flag:boolean 是否看跌吞没
return {*} Unit:number  开仓单位
"""


def is_swallow_down(i, data):
    open = data.open[i]
    close = data.close[i]
    high = data.high[i]
    low = data.low[i]

    # 获取前一根K线 OHLC
    pre_open = data.open[i - 1]
    pre_close = data.close[i - 1]
    pre_high = data.high[i - 1]
    pre_low = data.low[i - 1]

    k_len = high - low
    bar_len = close - open if open < close else open - close
    pre_bar_len = pre_close - pre_open if pre_close < pre_open else pre_open - pre_close

    # 标准形态 2个单位 （1个单位对应 1% 仓位）
    # 强势形态 2个单位
    # *长期趋势形态 2个单位
    # 有效成交量 2个单位

    position_unit = 0
    is_short = False

    # 满足基本
    if (
        is_long_tendency(i, data)
        and open > close
        # and bar_len > k_len // 2
        and pre_open < pre_close
        and close < pre_open
        and open + 1 >= pre_close
        and high >= pre_high
        and low <= pre_low
    ):
        position_unit += 2

        if bar_len > pre_bar_len * 1.5:
            position_unit += 2

        if data.volume[i] > data.volume[i - 1]:
            position_unit += 2

    if position_unit > 0:
        is_short = True

    return is_short, position_unit


"""
description: 判断当前形态是否属于长期上涨趋势
param {*} i 当前时间tick
param {*} data 行情数据dataFrame
return {*} isLong:boolean 
"""


def is_long_tendency(i, data):
    high = data.high[i]
    pre_high = data.high[i - 1]

    for num in range(1, 8):
        if high < data.high[i - num - 1] and pre_high < data.high[i - num - 1]:
            return False

    return True


"""
description: 判断当前形态是否属于长期下跌趋势
param {*} i
param {*} data
return {*}
"""


def is_short_tendency(i, data):
    low = data.low[i]
    pre_low = data.low[i - 1]

    for num in range(1, 8):
        if low > data.low[i - num - 1] and pre_low > data.low[i - num - 1]:
            return False

    return True


def heikin_ashi(df):
    heikin_ashi_df = pd.DataFrame(
        index=df.index.values,
        columns=[
            "open",
            "high",
            "low",
            "close",
            "HAopen",
            "HAhigh",
            "HAlow",
            "HAclose",
            "volume",
        ],
    )

    df_len = len(df)
    heikin_ashi_df["open"] = df["open"]
    heikin_ashi_df["high"] = df["high"]
    heikin_ashi_df["low"] = df["low"]
    heikin_ashi_df["close"] = df["close"]
    heikin_ashi_df["volume"] = df["volume"]

    heikin_ashi_df["HAclose"] = round(
        (df["open"] + df["high"] + df["low"] + df["close"]) / 4, 1
    )

    for i in range(df_len):
        if i == 0:
            heikin_ashi_df.at[df.index[df_len - 1], "HAopen"] = df["open"].iloc[
                df_len - 1
            ]
        else:
            heikin_ashi_df.at[df.index[df_len - 1 - i], "HAopen"] = round(
                (
                    heikin_ashi_df.at[df.index[df_len - i], "HAopen"]
                    + heikin_ashi_df.at[df.index[df_len - i], "HAclose"]
                )
                / 2,
                1,
            )

    heikin_ashi_df["HAhigh"] = round(
        heikin_ashi_df.loc[:, ["HAopen", "HAclose"]].join(df["high"]).max(axis=1), 1
    )

    heikin_ashi_df["HAlow"] = round(
        heikin_ashi_df.loc[:, ["HAopen", "HAclose"]].join(df["low"]).min(axis=1), 1
    )

    print(heikin_ashi_df)

    return heikin_ashi_df

