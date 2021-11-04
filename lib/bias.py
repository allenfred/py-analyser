from talib import SMA


# 6 12 24 60 72
# N日BIAS=(当日收盘价-N日平均收盘价)/N日平均收盘价*100%

def bias(close):
    ma6 = SMA(close, 6)
    ma12 = SMA(close, 12)
    ma24 = SMA(close, 24)
    ma60 = SMA(close, 60)
    ma72 = SMA(close, 72)

    bias6 = []
    bias12 = []
    bias24 = []
    bias60 = []
    bias72 = []

    for index, value in enumerate(close):
        bias_6 = round((value - ma6[index]) / ma6[index], 5)
        bias_12 = round((value - ma12[index]) / ma12[index], 5)
        bias_24 = round((value - ma24[index]) / ma24[index], 5)
        bias_60 = round((value - ma60[index]) / ma60[index], 5)
        bias_72 = round((value - ma72[index]) / ma72[index], 5)

        bias6.insert(index, round(bias_6 * 100, 1))
        bias12.insert(index, round(bias_12 * 100, 1))
        bias24.insert(index, round(bias_24 * 100, 1))
        bias60.insert(index, round(bias_60 * 100, 1))
        bias72.insert(index, round(bias_72 * 100, 1))

    return bias6, bias12, bias24, bias_60, bias_72
