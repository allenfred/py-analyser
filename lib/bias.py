from talib import SMA


# 6 12 24
# N日BIAS=(当日收盘价-N日平均收盘价)/N日平均收盘价*100%

def bias(close):
    ma6 = SMA(close, 6)
    ma12 = SMA(close, 12)
    ma24 = SMA(close, 24)
    ma60 = SMA(close, 60)

    bias6 = []
    bias12 = []
    bias24 = []
    bias60 = []

    for index, value in close.iteritems():
        bias_6 = round((value - ma6.iat[index]) / ma6.iat[index], 5)
        bias_12 = round((value - ma12.iat[index]) / ma12.iat[index], 5)
        bias_24 = round((value - ma24.iat[index]) / ma24.iat[index], 5)
        bias_60 = round((value - ma60.iat[index]) / ma60.iat[index], 5)

        bias6.insert(index, bias_6)
        bias12.insert(index, bias_12)
        bias24.insert(index, bias_24)
        bias60.insert(index, bias_60)

    return bias6, bias12, bias24, bias60
