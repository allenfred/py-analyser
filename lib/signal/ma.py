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


def is_up_short_ma_arrange1(index, ma):
    # MA多头排列（5/10/20）
    ma5 = ma[:, 0]
    ma10 = ma[:, 1]
    ma20 = ma[:, 2]

    def ma_rise():
        flag = True
        for i in range(5):
            # 如果当前 MA <= 前值
            if ma5[index - i] < ma5[index - i - 1] \
                    or ma10[index - i] < ma10[index - i - 1] \
                    or ma20[index - i] < ma20[index - i - 1] \
                    or not (ma5[index - i] > ma10[index - i] > ma20[index - i]):
                flag = False
        return flag

    if index > 80 and ma_rise():
        return True

    return False


def is_up_short_ma_arrange2(index, ma):
    # MA多头排列（5/10/30）
    ma5 = ma[:, 0]
    ma10 = ma[:, 1]
    ma30 = ma[:, 3]

    def ma_rise():
        flag = True
        for i in range(5):
            # 如果当前 MA <= 前值
            if ma5[index - i] < ma5[index - i - 1] \
                    or ma10[index - i] < ma10[index - i - 1] \
                    or ma30[index - i] < ma30[index - i - 1] \
                    or not (ma5[index - i] > ma10[index - i] > ma30[index - i]):
                flag = False
        return flag

    if index > 80 and ma_rise():
        return True

    return False


def is_ma60_support(index, candles, ma, ma_slope, df):
    if index < 90:
        return False

    open = candles[:, 0]
    high = candles[:, 1]
    low = candles[:, 2]
    close = candles[:, 3]
    ma60 = ma[:, 5]

    # 最近13个交易日 收盘价稳定在MA120之上 MA120稳定向上运行
    def steady_on_ma():
        flag = True
        for i in range(13):
            if close[index - i] < ma60[index - i] or ma60[index - i] < ma60[index - i - 1]:
                flag = False
        return flag

    if steady_on_ma() and has_support_patterns(index, df) and \
            (low[index] < ma60[index] or low[index - 1] < ma60[index - 1]):
        return True
    else:
        return False


def is_ma120_support(index, candles, ma, ma_slope, df):
    if index < 150:
        return 0

    open = candles[:, 0]
    high = candles[:, 1]
    low = candles[:, 2]
    close = candles[:, 3]
    ma120 = ma[:, 6]

    # 最近21个交易日 收盘价稳定在MA120之上 MA120稳定向上运行
    def steady_on_ma():
        flag = True
        for i in range(21):
            if close[index - i] < ma120[index - i] or ma120[index - i] < ma120[index - i - 1]:
                flag = False
        return flag

    if steady_on_ma() and has_support_patterns(index, df) and \
            has_support_patterns(index - 1, df) and \
            (low[index] < ma120[index] or low[index - 1] < ma120[index - 1]):
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
    if df.iloc[index]['swallow_up'] > 0 or df.iloc[index]['down_rise'] > 0 \
            or df.iloc[index]['CDLHAMMER'] > 0 or df.iloc[index]['CDLGRAVESTONEDOJI'] > 0 \
            or df.iloc[index]['CDLDRAGONFLYDOJI'] > 0 or df.iloc[index]['CDLTAKURI'] > 0 \
            or df.iloc[index]['CDLHARAMI'] > 0 or df.iloc[index]['CDLHARAMICROSS'] > 0 \
            or df.iloc[index]['CDLPIERCING'] > 0 or df.iloc[index]['CDLLADDERBOTTOM'] > 0:
        return True

    return False