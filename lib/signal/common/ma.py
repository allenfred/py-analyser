import numpy as np
import math as math
import lib.signal.stock.candle as patterns


# MA 信号

def is_ma20_rise(index, ma):
    ma20 = ma[:, 2]

    def ma_rise():
        flag = True
        for i in range(5):
            # 如果 当前MA20 <= 前值
            if ma20[index - i] <= ma20[index - i - 1]:
                flag = False
        return flag

    if index > 60 and ma_rise():
        return True
    else:
        return False


def is_ema20_rise(index, ema):
    ema20 = ema[:, 2]

    def ma_rise():
        flag = True
        for i in range(5):
            # 如果 当前EMA20 <= 前值
            if ema20[index - i] <= ema20[index - i - 1]:
                flag = False
        return flag

    if index > 60 and ma_rise():
        return True
    else:
        return False


def is_ma30_rise(index, ma):
    ma30 = ma[:, 3]

    def ma_rise():
        flag = True
        for i in range(5):
            # 如果 当前MA30 <= 前值
            if ma30[index - i] <= ma30[index - i - 1]:
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
        for i in range(5):
            # 如果 当前EMA30 <= 前值
            if ema30[index - i] <= ema30[index - i - 1]:
                flag = False
        return flag

    if index > 60 and ma_rise():
        return True
    else:
        return False


def is_ma60_rise(index, ma):
    ma60 = ma[:, 5]

    def ma_rise():
        flag = True
        for i in range(7):
            # 如果 当前MA60 <= 前值
            if ma60[index - i] <= ma60[index - i - 1]:
                flag = False
        return flag

    if index > 90 and ma_rise():
        return True
    else:
        return False


def is_ema60_rise(index, ema):
    ema60 = ema[:, 5]

    def ma_rise():
        flag = True
        for i in range(7):
            # 如果 当前EMA60 <= 前值
            if ema60[index - i] <= ema60[index - i - 1]:
                flag = False
        return flag

    if index > 90 and ma_rise():
        return True
    else:
        return False


def is_ma120_rise(index, ma):
    ma120 = ma[:, 6]

    def ma_rise():
        flag = True
        for i in range(13):
            # 如果 当前MA120 <= 前值
            if ma120[index - i] <= ma120[index - i - 1]:
                flag = False
        return flag

    if index > 150 and ma_rise():
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


def steady_on_ma60(index, df):
    ma = df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    close = df['close'].to_numpy()
    ma20 = ma[:, 2]
    ma60 = ma[:, 5]

    ma60_steady_22days = True
    ma20_on_ma60_22days = True
    close_steady_22days = True

    ma60_steady_33days = True
    ma20_on_ma60_33days = True
    close_steady_33days = True

    ma60_steady_55days = True
    ma20_on_ma60_55days = True
    close_steady_55days = True

    for i in range(21):
        # 如果当前 MA60 <= 前值
        if ma60[index - i] < ma60[index - i - 1]:
            ma60_steady_22days = False

        # 如果当前 MA20 < MA60
        if ma20[index - i] < ma60[index - i]:
            ma20_on_ma60_22days = False

        # 如果收盘价低于 MA60
        if close[index - i] < ma60[index - i]:
            close_steady_22days = False

    for i in range(33):
        # 如果当前 MA60 <= 前值
        if ma60[index - i] < ma60[index - i - 1]:
            ma60_steady_33days = False

        # 如果当前 MA20 < MA60
        if ma20[index - i] < ma60[index - i]:
            ma20_on_ma60_33days = False

        # 如果收盘价低于 MA60
        if close[index - i] < ma60[index - i]:
            close_steady_33days = False

    for i in range(55):
        # 如果当前 MA60 <= 前值
        if ma60[index - i] < ma60[index - i - 1]:
            ma60_steady_55days = False

        # 如果当前 MA20 < MA60
        if ma20[index - i] < ma60[index - i]:
            ma20_on_ma60_55days = False

        # 如果收盘价低于 MA60
        if close[index - i] < ma60[index - i]:
            close_steady_55days = False

    # 当MA60持续上行 收盘价和MA20必须稳定在MA60之上
    if ma60_steady_22days:
        if close_steady_22days and ma20_on_ma60_22days:
            return True
        else:
            return False

    if ma60_steady_33days:
        if close_steady_33days and ma20_on_ma60_33days:
            return True
        else:
            return False

    if ma60_steady_55days:
        if close_steady_55days and ma20_on_ma60_55days:
            return True
        else:
            return False

    return True


def is_up_hill(index, df):
    """
    上山爬坡
    收盘价长期不跌破 MA60
    MA20/MA30/MA60 持续上行
    价格回落MA20 未有效跌破
    20个交易日内未出现涨停
    出现看涨形态

    :param index:
    :param df:
    :return:
    """

    ma = df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    close = df['close'].to_numpy()
    low = df['low'].to_numpy()
    ma5 = ma[:, 0]
    ma10 = ma[:, 1]
    ma20 = ma[:, 2]
    ma30 = ma[:, 3]
    ma60 = ma[:, 5]

    def ma60_rise_steady():
        flag = True
        for i in range(18):
            # 如果当前 MA <= 前值 / 收盘价低于 MA60
            if ma60[index - i] < ma60[index - i - 1] or close[index - i] < ma60[index - i]:
                flag = False
        return flag

    def ma20_rise_steady():
        flag = True
        for i in range(21):
            # 如果当前 MA <= 前值
            if ma20[index - i] < ma20[index - i - 1]:
                flag = False
        return flag

    def steady_on_ma30():
        flag = True
        for i in range(21):
            # 如果当前 MA <= 前值
            if ma30[index - i] < ma30[index - i - 1] or close[index - i] < ma30[index - i]:
                flag = False
        return flag

    # 在MA20/MA30 获得支撑
    def support_on_ma20():
        if (close[index] > ma20[index] or close[index] > ma30[index]) and \
                (low[index] < ma20[index] or low[index] < ma30[index]):
            return True

    def has_no_limit():
        flag = True
        for j in range(21):
            # 如果当前 MA <= 前值
            if df.iloc[index - j]['limit'] != 'N':
                flag = False
        return flag

    if index > 90 and steady_on_ma60(index, df) and ma60_rise_steady() and \
            steady_on_ma30() and has_no_limit():
        # print('is_up_hill', df.iloc[index]['trade_date'])
        return True

    return False


def is_up_wave(index, df):
    """
    逐浪上升
    MA120 长期持续上行
    价格回落跌破 MA120 后又站上 MA120
    MA120 附近出现看涨形态 (金叉/大阳线)

    :param index:
    :param df:
    :return:
    """

    ma = df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    close = df['close'].to_numpy()
    low = df['low'].to_numpy()
    ma5 = ma[:, 0]
    ma10 = ma[:, 1]
    ma20 = ma[:, 2]
    ma30 = ma[:, 3]
    ma60 = ma[:, 5]
    ma120 = ma[:, 6]

    def low_bias(sma, ind):
        return round(round((low[ind] - sma[ind]) / sma[ind], 5) * 100, 2)

    def ma120_rise_steady():
        flag = True
        _cnt = 0
        for i in range(44):
            # 如果当前 MA <= 前值
            if ma120[index - i] < ma120[index - i - 1]:
                flag = False

            # 如果当前 MA <= 前值
            if close[index - i] < ma120[index - i]:
                _cnt += 1

        return flag and _cnt < 2

    def has_bottom_patterns_recently():
        return has_bottom_patterns(index, df) or \
               has_bottom_patterns(index - 1, df) or \
               has_bottom_patterns(index - 2, df)

    def has_large_vol_recently():
        return df.iloc[index]['large_vol'] == 1 or \
               df.iloc[index - 1]['large_vol'] == 1 or \
               df.iloc[index - 2]['large_vol'] == 1

    def has_long_line_recently():
        return df.iloc[index]['long_line'] == 1 or \
               df.iloc[index - 1]['long_line'] == 1 or \
               df.iloc[index - 2]['long_line'] == 1 or \
               df.iloc[index]['marubozu'] == 1 or \
               df.iloc[index - 1]['marubozu'] == 1 or \
               df.iloc[index - 2]['marubozu'] == 1 or \
               df.iloc[index]['up_cross4ma'] == 1 or \
               df.iloc[index - 1]['up_cross4ma'] == 1 or \
               df.iloc[index - 2]['up_cross4ma'] == 1

    def has_gold_cross():
        return df.iloc[index]['ma_gold_cross1'] == 1 or \
               df.iloc[index]['ma_gold_cross2'] == 1 or \
               df.iloc[index]['ma_gold_cross3'] == 1 or \
               df.iloc[index]['ma_gold_cross4'] == 1

    # 收盘价高于MA
    # 最近3日回落均线附近 bias120 < 1
    # 最近3日出现底部K线形态 或 收盘出现金叉
    def long_on_ma120():
        if close[index] > ma120[index] and \
                (low_bias(ma120, index - 1) < 1 or low_bias(ma120, index - 2) < 1) \
                and (has_bottom_patterns_recently() or has_gold_cross() or
                     has_large_vol_recently() or has_long_line_recently()):
            return True
        return False

    if index > 180 and ma120_rise_steady() and long_on_ma120():
        # print(index, 'is_up_wave', df.iloc[index]['trade_date'], long_on_ma60(), long_on_ma120())
        return True

    return False


def is_up_ma_arrange(index, ma):
    # MA多头排列（5/10/20/60）
    ma5 = ma[:, 0]
    ma10 = ma[:, 1]
    ma20 = ma[:, 2]
    ma60 = ma[:, 5]

    def ma_rise():
        flag = True
        for i in range(7):
            # 如果当前 MA <= 前值
            if ma5[index - i] < ma5[index - i - 1] \
                    or ma10[index - i] < ma10[index - i - 1] \
                    or ma20[index - i] < ma20[index - i - 1] \
                    or ma60[index - i] < ma60[index - i - 1] \
                    or not (ma5[index - i] > ma10[index - i] > ma20[index - i] > ma60[index - i]):
                flag = False
        return flag

    if index > 80 and ma_rise():
        return True

    return False


def is_up_short_ma_arrange(index, ma1, ma2, ma3):
    """
    MA/EMA 短期组合多头排列（5/10/20）/（5/10/30）

    :param index:
    :param ma1:
    :param ma2:
    :param ma3:
    :return:
    """

    _count = 7
    _sum = round(np.sum(ma1[index - _count: index]) +
                 np.sum(ma2[index - _count: index]) +
                 np.sum(ma3[index - _count: index]), 3)
    _avg = round(_sum / (3 * _count), 3)
    _wave = round(_avg * 0.03, 3)
    ma_wave = []

    is_wave_steady = True

    for i in range(_count):
        ma_wave.append(math.fabs(ma1[index - i] - _avg))
        ma_wave.append(math.fabs(ma2[index - i] - _avg))
        ma_wave.append(math.fabs(ma3[index - i] - _avg))

        if math.fabs(ma1[index - i] - _avg) > _wave or \
                math.fabs(ma2[index - i] - _avg) > _wave or \
                math.fabs(ma3[index - i] - _avg) > _wave:
            is_wave_steady = False

    def ma_rise():
        flag = True
        for i in range(_count):
            # 如果当前 MA <= 前值
            if ma1[index - i] < ma1[index - i - 1] \
                    or ma2[index - i] < ma2[index - i - 1] \
                    or ma3[index - i] < ma3[index - i - 1] \
                    or not (ma1[index - i] > ma2[index - i] > ma3[index - i]):
                flag = False
        return flag

    if index > 60 and ma_rise() and is_wave_steady:
        return True

    return False


def is_down_short_ma_arrange(index, ma1, ma2, ma3):
    """
    MA/EMA 短期组合空头排列（5/10/20）/（5/10/30）

    :param index:
    :param ma1:
    :param ma2:
    :param ma3:
    :return:
    """

    _count = 7
    _sum = round(np.sum(ma1[index - _count: index]) +
                 np.sum(ma2[index - _count: index]) +
                 np.sum(ma3[index - _count: index]), 3)
    _avg = round(_sum / (3 * _count), 3)
    _wave = round(_avg * 0.03, 3)
    ma_wave = []

    is_wave_steady = True

    for i in range(_count):
        ma_wave.append(math.fabs(ma1[index - i] - _avg))
        ma_wave.append(math.fabs(ma2[index - i] - _avg))
        ma_wave.append(math.fabs(ma3[index - i] - _avg))

        if math.fabs(ma1[index - i] - _avg) > _wave or \
                math.fabs(ma2[index - i] - _avg) > _wave or \
                math.fabs(ma3[index - i] - _avg) > _wave:
            is_wave_steady = False

    def ma_rise():
        flag = True
        for i in range(_count):
            # 如果当前 MA <= 前值
            if ma1[index - i] < ma1[index - i - 1] \
                    or ma2[index - i] < ma2[index - i - 1] \
                    or ma3[index - i] < ma3[index - i - 1] \
                    or not (ma1[index - i] > ma2[index - i] > ma3[index - i]):
                flag = False
        return flag

    if index > 60 and ma_rise() and is_wave_steady:
        return True

    return False


def is_up_middle_ma_arrange(index, ma1, ma2, ma3):
    """
    MA/EMA 中期组合多头排列（10/20/60）/ 10/20/55）

    :param index:
    :param ma1:
    :param ma2:
    :param ma3:
    :return:
    """

    _count = 7
    _sum = round(np.sum(ma1[index - _count: index]) +
                 np.sum(ma2[index - _count: index]) +
                 np.sum(ma3[index - _count: index]), 3)
    _avg = round(_sum / (3 * _count), 3)
    _wave = round(_avg * 0.03, 3)
    ma_wave = []

    is_wave_steady = True

    for i in range(_count):
        ma_wave.append(math.fabs(ma1[index - i] - _avg))
        ma_wave.append(math.fabs(ma2[index - i] - _avg))
        ma_wave.append(math.fabs(ma3[index - i] - _avg))

        if math.fabs(ma1[index - i] - _avg) > _wave or \
                math.fabs(ma2[index - i] - _avg) > _wave or \
                math.fabs(ma3[index - i] - _avg) > _wave:
            is_wave_steady = False

    def ma_rise():
        flag = True
        for i in range(_count):
            # 如果当前 MA <= 前值
            if ma1[index - i] < ma1[index - i - 1] \
                    or ma2[index - i] < ma2[index - i - 1] \
                    or ma3[index - i] < ma3[index - i - 1] \
                    or not (ma1[index - i] > ma2[index - i] > ma3[index - i]):
                flag = False
        return flag

    if index > 90 and ma_rise() and is_wave_steady:
        return True

    return False


def is_up_long_ma_arrange(index, ma1, ma2, ma3):
    """
    MA/EMA 长期组合多头排列 (20/55/120) / (30/60/120)

    :param index:
    :param ma1:
    :param ma2:
    :param ma3:
    :return:
    """

    _count = 9
    _sum = round(np.sum(ma1[index - _count: index]) +
                 np.sum(ma2[index - _count: index]) +
                 np.sum(ma3[index - _count: index]), 3)
    _avg = round(_sum / (3 * _count), 3)
    _wave = round(_avg * 0.03, 3)
    ma_wave = []

    is_wave_steady = True

    for i in range(_count):
        ma_wave.append(math.fabs(ma1[index - i] - _avg))
        ma_wave.append(math.fabs(ma2[index - i] - _avg))
        ma_wave.append(math.fabs(ma3[index - i] - _avg))

        if math.fabs(ma1[index - i] - _avg) > _wave or \
                math.fabs(ma2[index - i] - _avg) > _wave or \
                math.fabs(ma3[index - i] - _avg) > _wave:
            is_wave_steady = False

    def ma_rise():
        flag = True
        for i in range(_count):
            # 如果当前 MA <= 前值
            if ma1[index - i] < ma1[index - i - 1] \
                    or ma2[index - i] < ma2[index - i - 1] \
                    or ma3[index - i] < ma3[index - i - 1] \
                    or not (ma1[index - i] > ma2[index - i] > ma3[index - i]):
                flag = False
        return flag

    if index > 150 and ma_rise() and is_wave_steady:
        return True

    return False


def is_gold_cross(index, ma1, ma2):
    """
    MA/EMA 黄金交叉（5/20）/（10/20）/ （10/30）

    :param index:
    :param ma1:
    :param ma2:
    :return:
    """

    _count = 3

    def ma_rise():
        flag = True
        for i in range(_count):
            # 如果当前 MA <= 前值
            if ma1[index - i] <= ma1[index - i - 1] \
                    or ma2[index - i] <= ma2[index - i - 1]:
                flag = False
        return flag

    if ma_rise() and ma1[index] > ma2[index] and ma1[index - 1] < ma2[index - 1]:
        return True

    return False


def is_ma_glue(index, df):
    """
    均线粘合 (5/10/20)
    最近7个交易日
    模拟计算方差 波动1.5%内

    :param index:
    :param ma:
    :param df:
    :return:
    """
    ma = df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    ma5 = ma[:, 0]
    ma10 = ma[:, 1]
    ma20 = ma[:, 2]
    pct_chg = df['pct_chg'].to_numpy()

    _count = 7
    _sum = round(np.sum(ma5[index - _count: index]) + np.sum(ma10[index - _count: index]) + \
                 np.sum(ma20[index - _count: index]), 3)
    _avg = round(_sum / 21, 3)
    _wave = round(_avg * 0.015, 3)
    ma_wave = []

    avg_wave = True

    for i in range(_count):
        ma_wave.append(math.fabs(ma5[index - i] - _avg))
        ma_wave.append(math.fabs(ma10[index - i] - _avg))
        ma_wave.append(math.fabs(ma20[index - i] - _avg))

        if math.fabs(ma5[index - i] - _avg) > _wave or \
                math.fabs(ma10[index - i] - _avg) > _wave or \
                math.fabs(ma20[index - i] - _avg) > _wave:
            avg_wave = False

    if index > 20 and avg_wave and \
            max(pct_chg[index - _count - 2: index]) < 3 and \
            min(pct_chg[index - _count - 2: index]) > -3:
        # print(df['trade_date'][index], pct_chg[index - _count - 2: index + 1] , pct_chg[index])
        return True
    else:
        return False


def is_general_ma_glue(index, df):
    """
    均线粘合 (5/10/20)
    最近7个交易日
    模拟计算方差 波动3%内

    :param index:
    :param ma:
    :param df:
    :return:
    """
    ma = df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    ma5 = ma[:, 0]
    ma10 = ma[:, 1]
    ma20 = ma[:, 2]
    pct_chg = df['pct_chg'].to_numpy()

    _count = 7
    _sum = round(np.sum(ma5[index - _count: index]) + np.sum(ma10[index - _count: index]) + \
                 np.sum(ma20[index - _count: index]), 3)
    _avg = round(_sum / 21, 3)
    _wave = round(_avg * 0.03, 3)
    ma_wave = []

    avg_wave = True

    for i in range(_count):
        ma_wave.append(math.fabs(ma5[index - i] - _avg))
        ma_wave.append(math.fabs(ma10[index - i] - _avg))
        ma_wave.append(math.fabs(ma20[index - i] - _avg))

        if math.fabs(ma5[index - i] - _avg) > _wave or \
                math.fabs(ma10[index - i] - _avg) > _wave or \
                math.fabs(ma20[index - i] - _avg) > _wave:
            avg_wave = False

    if index > 20 and avg_wave:
        return True
    else:
        return False


def is_ma510_glue(index, df):
    """
    均线粘合 (5/10)
    最近7个交易日
    模拟计算方差 波动1%内

    :param index:
    :param ma:
    :param df:
    :return:
    """
    ma = df[['ma5', 'ma10']].to_numpy()
    ma5 = ma[:, 0]
    ma10 = ma[:, 1]

    _count = 7
    _sum = round(np.sum(ma5[index - _count: index]) + np.sum(ma10[index - _count: index]), 3)
    _avg = round(_sum / 14, 3)
    _wave = round(_avg * 0.015, 3)
    ma_wave = []

    avg_wave = True

    for i in range(_count):
        ma_wave.append(math.fabs(ma5[index - i] - _avg))
        ma_wave.append(math.fabs(ma10[index - i] - _avg))

        if math.fabs(ma5[index - i] - _avg) > _wave or \
                math.fabs(ma10[index - i] - _avg) > _wave:
            avg_wave = False

    if index > 20 and avg_wave:
        # print(df['trade_date'][index], pct_chg[index - _count - 2: index + 1] , pct_chg[index])
        return True
    else:
        return False


def is_ma_hold_moon(index, df):
    """
    MA烘云托月 (5/10/20) / (5/10/30)
    最近 7 个交易日
    均线粘合
    ma20向上 / ma30向上

    :param index:
    :param df:
    :return:
    """
    ma = df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    _count = 8 - 1
    ma20 = ma[:, 2]
    ma30 = ma[:, 3]

    def ma20_rise_steady():
        flag = True
        for i in range(_count):
            # 如果 当前 MA20 < 前值
            if ma20[index - i] < ma20[index - i - 1]:
                flag = False
        return flag

    def ma30_rise_steady():
        flag = True
        for i in range(_count):
            # 如果 当前 MA30 < 前值
            if ma30[index - i] < ma30[index - i - 1]:
                flag = False
        return flag

    # if index > 60 and (ma20_rise_steady() or ma30_rise_steady()) and is_ma_glue(index, df):
    if index > 60 and ma20_rise_steady() and is_ma510_glue(index, df):
        # print(df['trade_date'][index])
        return True
    else:
        return False


def is_ma_out_sea(index, df):
    """
    蛟龙出海 (整理行情末期)
    大阳线 贯穿ma5/ma10/ma20 ma20上行

    :param index:
    :param df:
    :return:
    """

    ma = df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    _ma5 = ma[:, 0][index]
    _ma10 = ma[:, 1][index]
    _ma20 = ma[:, 2][index]
    _ma30 = ma[:, 3][index]
    ma60 = ma[:, 5]
    _open = df['open'][index]
    _close = df['close'][index]

    _count = 7

    def ma_rise():
        flag = True
        for i in range(_count):
            # 如果当前 MA <= 前值
            if ma60[index - i] < ma60[index - i - 1]:
                flag = False
        return flag

    if index > 50 and ma_rise() and is_general_ma_glue(index, df) and \
            ((_open < _ma5 and _open < _ma10 and _open < _ma20 and
              _close > _ma5 and _close > _ma10 and _close > _ma20) or
             (_open < _ma5 and _open < _ma10 and _open < _ma30 and
              _close > _ma5 and _close > _ma10 and _close > _ma30)):
        # print(df['trade_date'][index], 'is_ma_out_sea')
        return True

    return False


def is_ma_over_gate(index, df):
    """
    MA鱼跃龙门(5/10/20)
    大阳线
    K线站上ma5/ma10/ma20/ma60
    昨日出现均线粘合

    :param index:
    :param df:
    :return:
    """
    _count = 13
    candle = df[['open', 'high', 'low', 'close', 'pct_chg', 'trade_date']].to_numpy()
    ma30 = df['ma30'].to_numpy()
    ma60 = df['ma60'].to_numpy()

    def ma60_rise_steady():
        flag = True
        for i in range(_count):
            # 如果 当前 ma60 < 前值
            if ma60[index - i] < ma60[index - i - 1]:
                flag = False
        return flag

    def ma30_rise_steady():
        flag = True
        for i in range(_count):
            # 如果 当前 ma30 < 前值
            if ma30[index - i] < ma30[index - i - 1]:
                flag = False
        return flag

    if index > 20 and is_general_ma_glue(index, df) and patterns.upward_jump(index, candle) and \
            is_stand_up_all_ma(index, df) and (ma60_rise_steady() or ma30_rise_steady()):
        # print(df['trade_date'][index], 'is_ma_over_gate')
        return True
    else:
        return False


def is_ma_up_ground(index, df):
    """
    MA旱地拔葱(5/10/20)
    跳空阳线
    昨日未出现跳空
    K线站上ma5/ma10/ma20/ma60
    昨日出现均线粘合/潜伏底/收敛三角形/矩形/楔形

    :param index:
    :param df:
    :return:
    """
    _count = 5
    candle = df[['open', 'high', 'low', 'close', 'pct_chg', 'trade_date']].to_numpy()

    if (not patterns.upward_jump(index - 1, candle)) and patterns.upward_jump(index, candle) and \
            is_stand_up_all_ma(index, df):
        # print(df['trade_date'][index], 'is_ma_up_ground')
        return True
    else:
        return False


def is_ma_spider(index, ma, ma_gold_cross1, ma_gold_cross2, ma_gold_cross3, ma_gold_cross4):
    # MA金蜘蛛
    # 最近3个交易日ma5/ma10/ma20交叉于一点 (即出现至少1个金叉)
    # 今日ma5/ma10/ma20多头发散
    gold_cross_cnt = 0
    if max(ma_gold_cross1[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1
    if max(ma_gold_cross2[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1
    if max(ma_gold_cross3[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1
    if max(ma_gold_cross4[index - 2: index + 1]) == 1:
        gold_cross_cnt += 1

    flag = False

    # MA金蜘蛛
    if index > 20 and gold_cross_cnt > 0 and \
            (ma[index - 1][0] == ma[index - 1][1] == ma[index - 1][2] or
             ma[index - 1][0] == ma[index - 1][1] == ma[index - 1][3]):
        flag = True

    return flag


def is_ma_silver_valley(index, ma_gold_cross1, ma_gold_cross2, ma_gold_cross3):
    # MA银山谷
    if index >= 10 and (ma_gold_cross2[index] == 1 or ma_gold_cross3[index] == 1):
        gold_cross_cnt = 0
        if max(ma_gold_cross1[index - 9: index + 1]) == 1:
            gold_cross_cnt += 1
        if max(ma_gold_cross2[index - 9: index + 1]) == 1:
            gold_cross_cnt += 1
        if max(ma_gold_cross3[index - 9: index + 1]) == 1:
            gold_cross_cnt += 1

        if gold_cross_cnt >= 2:
            return True

    return False


def is_ma_gold_valley(index, ma, ma_slope, ma_silver_valley):
    # MA金山谷
    # 最近30个交易日内形成两次银山谷视为金山谷
    if index >= 30 and max(ma_silver_valley[index - 29: index - 1]) == 1 and \
            ma_silver_valley[index] == 1 and ma[index - 30][2] < ma[index][2] and \
            ma_slope[index][2] > 0:
        return True
    else:
        return False


def is_stand_up_all_ma(index, df):
    close = df['close'].to_numpy()
    ma5 = df['ma5'].to_numpy()
    ma10 = df['ma10'].to_numpy()
    ma20 = df['ma20'].to_numpy()
    ma60 = df['ma60'].to_numpy()

    if close[index] > ma5[index] and \
            close[index] > ma10[index] and \
            close[index] > ma20[index] and \
            close[index] > ma60[index]:
        return True

    return False


def is_stand_up_ma60(index, df):
    """
    站上MA60
    前55个交易日(除最近3个交易日外) ma60向下运行
    最近3个交易日收盘价高于 ma60
    最近3个交易日 ma60 开始向上

    :param index:
    :param df:
    :return:
    """
    if index < 90:
        return False

    close = df['close'].to_numpy()
    ma60 = df['ma60'].to_numpy()
    ma60_slope = df['ma60_slope'].to_numpy()

    ma60_down_still = True
    close_down_still = True
    ma60_up_recently = False

    if max(ma60_slope[index - 55: index - 2]) >= 0:
        ma60_down_still = False

    if close[index] > ma60[index] and close[index - 1] > ma60[index - 1] and \
            close[index - 2] > ma60[index - 2] and \
            ma60[index] > ma60[index - 1] > ma60[index - 2]:
        ma60_up_recently = True

    if close_down_still and ma60_down_still and ma60_up_recently:
        return True
    else:
        return False


def is_stand_up_ma120(index, df):
    """
    站上MA120
    前89个交易日(除最近3个交易日外) ma120向下运行
    最近3个交易日收盘价高于 ma120
    最近3个交易日 ma120 开始向上

    :param index:
    :param df:
    :return:
    """
    if index < 160:
        return 0

    close = df['close'].to_numpy()
    ma120 = df['ma120'].to_numpy()
    ma120_slope = df['ma120_slope'].to_numpy()

    ma120_down_still = True
    close_down_still = True
    ma120_up_recently = False

    if max(ma120_slope[index - 89: index - 2]) >= 0:
        ma120_down_still = False

    if close[index] > ma120[index] and close[index - 1] > ma120[index - 1] and \
            close[index - 2] > ma120[index - 2] and \
            ma120_slope[index] > 0 and ma120_slope[index - 1] > 0 and \
            ma120[index] > ma120[index - 1] > ma120[index - 2] > ma120[index - 3]:
        ma120_up_recently = True

    if close_down_still and ma120_down_still and ma120_up_recently:
        return True
    else:
        return False


def is_ma60_support(index, df):
    """
    MA60支撑
    最近13个交易日MA60上行
    最近2个交易日跌破MA60 K线收出支撑形态

    :param index:
    :param df:
    :return:
    """
    if index < 90:
        return False

    low = df['low'].to_numpy()
    close = df['close'].to_numpy()
    ma60 = df['ma60'].to_numpy()

    def ma_rise_steady():
        flag = True
        for i in range(13):
            if ma60[index - i] < ma60[index - i - 1]:
                flag = False
        return flag

    if ma_rise_steady() and has_support_patterns(index, df) and close[index] > ma60[index] and \
            (low[index] <= ma60[index] or low[index - 1] <= ma60[index - 1]):
        # print(candle[5], 'support')
        return True
    else:
        return False


def is_ma120_support(index, df):
    """
    MA120支撑
    最近13个交易日 MA120上行
    最近2个交易日跌破MA120 K线收出支撑形态

    :param index:
    :param df:
    :return:
    """
    if index < 150:
        return 0

    low = df['low'].to_numpy()
    close = df['close'].to_numpy()
    ma120 = df['ma120'].to_numpy()

    def steady_on_ma():
        flag = True
        for i in range(13):
            if ma120[index - i] < ma120[index - i - 1]:
                flag = False
        return flag

    if steady_on_ma() and has_support_patterns(index, df) and close[index] > ma120[index] and \
            has_support_patterns(index - 1, df) and \
            (low[index] <= ma120[index] or low[index - 1] <= ma120[index - 1]):
        return True
    else:
        return False


def has_support_patterns(index, df):
    """
    当前Ticker 存在看涨K线形态
    看涨吞没
    下探上涨
    锤头线
    墓碑十字线
    蜻蜓十字线
    探水竿
    孕线
    十字孕线
    刺透形态
    梯底

    :param index:
    :param df:
    :return:
    """
    if df.iloc[index]['swallow_up'] > 0 or \
            df.iloc[index]['down_rise'] > 0 or \
            df.iloc[index]['CDLHAMMER'] > 0 or \
            df.iloc[index]['CDLGRAVESTONEDOJI'] > 0 \
            or df.iloc[index]['CDLDRAGONFLYDOJI'] > 0 \
            or df.iloc[index]['CDLTAKURI'] > 0 \
            or df.iloc[index]['CDLHARAMI'] > 0 \
            or df.iloc[index]['CDLHARAMICROSS'] > 0 \
            or df.iloc[index]['CDLPIERCING'] > 0 \
            or df.iloc[index]['flat_base'] > 0:
        return True

    return False


def has_bottom_patterns(index, df):
    """
    判断当前是否存在底部看涨K线形态
    看涨吞没
    吞噬模式 CDLENGULFING
    旭日东升
    看涨螺旋桨
    锤头 (探水竿)
    倒锤头
    墓碑十字/倒T十字 CDLGRAVESTONEDOJI
    晨星 CDLMORNINGSTAR
    十字晨星 CDLMORNINGDOJISTAR
    刺透心态 CDLPIERCING
    反击线 CDLCOUNTERATTACK
    梯底

    :param index: 当前时间
    :param df:
    :return:
    """

    if df.iloc[index]['swallow_up'] > 0 or \
            df.iloc[index]['CDLENGULFING'] > 0 or \
            df.iloc[index]['sunrise'] > 0 or \
            df.iloc[index]['down_screw'] > 0 or \
            df.iloc[index]['hammer'] > 0 or \
            df.iloc[index]['pour_hammer'] > 0 or \
            df.iloc[index]['CDLGRAVESTONEDOJI'] > 0 or \
            df.iloc[index]['CDLMORNINGSTAR'] > 0 or \
            df.iloc[index]['CDLMORNINGDOJISTAR'] > 0 or \
            df.iloc[index]['CDLPIERCING'] > 0 or \
            df.iloc[index]['CDLCOUNTERATTACK'] > 0 or \
            df.iloc[index]['flat_base'] > 0:
        return True

    return False
