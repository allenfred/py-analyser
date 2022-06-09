# -- coding: utf-8 -

def vol_analyze(df):
    """
    加密货币 成交量分析
    天量 5倍于 vol30 / vol20
    巨量 3倍于 vol30 / vol20
    大量 2倍于 vol30 / vol20
    异常量 vol20_max / vol30_max 2倍于 vol30 / vol20
    常量 大于 vol10 / vol20 / vol30
    地量 小于 vol10 / vol20 / vol30
    放量 1.5倍于 pre & 大于 vol10 / vol20 / vol30
    缩量 0.6倍于 pre
    堆量
    持续放量
    持续缩量

    :param df:
    :return:
    """

    vol = df.vol.to_numpy()
    vol10 = df.vol10.to_numpy()
    vol20 = df.vol20.to_numpy()
    vol30 = df.vol30.to_numpy()

    candle = df[['vol', 'vol5', 'vol10', 'vol20', 'vol30']].to_numpy()

    max_vol = []
    huge_vol = []
    large_vol = []
    high_vol = []
    common_vol = []
    low_vol = []
    increase_vol = []
    decrease_vol = []
    heap_vol = []
    increasingly_vol = []
    decreasingly_vol = []

    for index in range(len(candle)):
        # 天量
        if index > 10 and (vol[index] > vol20[index] * 5 or vol[index] > vol30[index] * 5):
            max_vol.insert(index, 1)
        else:
            max_vol.insert(index, 0)

        # 巨量
        if index > 10 and \
                (vol[index] >= vol20[index] * 3 or vol[index] >= vol30[index] * 3) and \
                (vol[index] < vol20[index] * 5 and vol[index] < vol30[index] * 5):
            huge_vol.insert(index, 1)
        else:
            huge_vol.insert(index, 0)

        # 大量
        if index > 10 and \
                (vol[index] >= vol20[index] * 2 or vol[index] >= vol30[index] * 2) and \
                (vol[index] < vol20[index] * 3 and vol[index] < vol30[index] * 3):
            large_vol.insert(index, 1)
        else:
            large_vol.insert(index, 0)

        # 高量
        if index > 30 and max(high_vol[index - 20: index]) == 0 and \
                (vol[index] > vol20[index] * 2 and vol[index] > vol30[index] * 2) and \
                (vol[index] > max(vol[index - 29: index])):
            high_vol.insert(index, 1)
        else:
            high_vol.insert(index, 0)

        # 常量
        if index > 10 and \
                (vol[index] > vol10[index] or vol[index] > vol20[index] or vol[index] > vol30[index]) and \
                (vol[index] < vol20[index] * 2 or vol[index] < vol30[index] * 2):
            common_vol.insert(index, 1)
        else:
            common_vol.insert(index, 0)

        # 地量
        if index > 10 and \
                (vol[index] < vol10[index] and vol[index] < vol20[index] and vol[index] < vol30[index]):
            low_vol.insert(index, 1)
        else:
            low_vol.insert(index, 0)

        # 放量
        if index > 10 and \
                (vol[index] > vol10[index] and vol[index] > vol20[index] and vol[index] > vol30[index]) and \
                (vol[index] > vol[index - 1] * 1.5):
            increase_vol.insert(index, 1)
        else:
            increase_vol.insert(index, 0)

        # 缩量
        if index > 10 and (vol[index] < vol[index - 1] * 0.6):
            decrease_vol.insert(index, 1)
        else:
            decrease_vol.insert(index, 0)

        # 持续放量
        if index > 30 and vol[index] > vol[index - 1] * 1.5 and \
                vol[index - 1] > vol[index - 2] * 1.5:
            increasingly_vol.insert(index, 1)
        else:
            increasingly_vol.insert(index, 0)

        # 持续缩量
        if index > 30 and vol[index] * 1.5 < vol[index - 1] and \
                vol[index - 1] * 1.5 < vol[index - 2]:
            decreasingly_vol.insert(index, 1)
        else:
            decreasingly_vol.insert(index, 0)

    df['max_vol'] = max_vol
    df['huge_vol'] = huge_vol
    df['large_vol'] = large_vol
    df['high_vol'] = high_vol
    df['common_vol'] = common_vol
    df['low_vol'] = low_vol
    df['increase_vol'] = increase_vol
    df['decrease_vol'] = decrease_vol
    df['increasingly_vol'] = increasingly_vol
    df['decreasingly_vol'] = decreasingly_vol

    return df
