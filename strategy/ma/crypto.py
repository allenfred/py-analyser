# -------------------
# ----- 做空信号 -----
# -------------------

# 葛南维八大买卖法则
# 均线排列
# 均线拐头
# 关键性K线
# 成交量 异常放大 / 缩量 / 放量

"""
大量（底部/顶部）
缩量下跌
放量上涨
趋势变化（多头排列 / 空头排列）10/20/60 20/60/120
买卖法则
vegas 12 144 169 576 676  MACD(144/169) 过滤假突破
"""

"""
15min
5/10/33 短期组合

"""

"""
K线形态
螺旋桨

"""

"""
做多信号

1. 均线下行(20/60) 阳线突破 (一阳穿三线) (5/10/20 10/20/60) 5/10/20/60/120
2. 多头排列 短期组合*  中期组合 (10/20/60) (10/20/55)  长期组合 (20/55/120 20/60/120)
3. (60/120) 向上突破 均线向上扭转  第一大法则
4. (60/120) 均线上行 回调未跌破  第二大法则
5. (60/120) 均线上行 回调跌破 又重新站上均线  第三大法则
6. (60/120)
"""

"""
做空信号

1. 均线下行(20/60) 阳线突破 (一阳穿三线) (5/10/20 10/20/60) 5/10/20/60/120
2. 多头排列 短期组合*  中期组合 (10/20/60) (10/20/55)  长期组合 (20/55/120 20/60/120)
3. (60/120) 向上突破 均线向上扭转  第一大法则
4. (60/120) 均线上行 回调未跌破  第二大法则
5. (60/120) 均线上行 回调跌破 又重新站上均线  第三大法则
6. (60/120)
"""


def is_cut_down(index, candles, ma, ema, ma_slope, ema_slope):
    """
    MA断头铡刀 (5/10/20 10/20/60)
    大阴线/中阴线
    K线跌破ma5/ma10/ma20
    昨日K线未跌破ma5/ma10/ma20
    昨日出现均线粘合
    过去13个交易日MA20上行

    :param index: int
    :param candles: ndarray
    :param ma: ndarray
    :param ema: ndarray
    :param ma_slope: ndarray
    :param ema_slope: ndarray
    :return: boolean
    """

    candle = candles[index]
    pre_candle = candles[index - 1]
    _close = candle[3]
    pre_close = pre_candle[3]

    _ma5 = ma[:, 0][index]
    _ma10 = ma[:, 1][index]
    _ma20 = ma[:, 2][index]

    _ema5 = ema[:, 0][index]
    _ema10 = ema[:, 1][index]
    _ema20 = ema[:, 2][index]

    if _close < _ma5 and _close < _ma10 and _close < _ma20 and \
            (pre_close > ma[index - 1][0] or pre_close > ma[index - 1][1] or pre_close > ma[index - 1][2]) and \
            ma_slope[index - 1][2] > 0 and ma[index - 1][0] > ma[index - 1][2] \
            and ma[index - 1][1] > ma[index - 1][2]:
        print()
        return True

    return False
