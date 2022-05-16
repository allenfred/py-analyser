# -- coding: utf-8 -

from .signal.stock.ma60 import is_ma60_first, is_ma60_second, is_ma60_third, is_ma60_fourth, \
    is_ma60_fifth, is_ma60_sixth, is_ma60_seventh, is_ma60_eighth


def ma_analyze(org_df):
    candle = org_df[['open', 'high', 'low', 'close', 'pct_chg', 'trade_date']].to_numpy()
    ma = org_df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    ema = org_df[['ema5', 'ema10', 'ema20', 'ema30', 'ema55', 'ema60', 'ema120']].to_numpy()
    ma_slope = org_df[['ma5_slope', 'ma10_slope', 'ma20_slope', 'ma30_slope', 'ma55_slope',
                       'ma60_slope', 'ma120_slope']].to_numpy()
    ema_slope = org_df[['ema5_slope', 'ema10_slope', 'ema20_slope', 'ema30_slope', 'ema55_slope',
                        'ema60_slope', 'ema120_slope']].to_numpy()
    bias = org_df[['bias6', 'bias12', 'bias24', 'bias55', 'bias60', 'bias72', 'bias120']].to_numpy()

    open = candle[:, 0]
    high = candle[:, 1]
    low = candle[:, 2]
    close = candle[:, 3]
    pct_chg = candle[:, 4]

    ma5 = ma[:, 0]
    ma10 = ma[:, 1]
    ma20 = ma[:, 2]
    ma30 = ma[:, 3]
    ma55 = ma[:, 4]
    ma60 = ma[:, 5]
    ma120 = ma[:, 6]

    ma5_slope = ma_slope[:, 0]
    ma10_slope = ma_slope[:, 1]
    ma20_slope = ma_slope[:, 2]
    ma30_slope = ma_slope[:, 3]
    ma55_slope = ma_slope[:, 4]
    ma60_slope = ma_slope[:, 5]
    ma120_slope = ma_slope[:, 6]

    ema5 = ema[:, 0]
    ema10 = ema[:, 1]
    ema20 = ema[:, 2]
    ema30 = ema[:, 3]
    ema55 = ema[:, 4]
    ema60 = ema[:, 5]
    ema120 = ema[:, 6]

    ema5_slope = ema_slope[:, 0]
    ema10_slope = ema_slope[:, 1]
    ema20_slope = ema_slope[:, 2]
    ema30_slope = ema_slope[:, 3]
    ema55_slope = ema_slope[:, 4]
    ema60_slope = ema_slope[:, 5]
    ema120_slope = ema_slope[:, 6]

    ma60_first = []
    ma60_second = []
    ma60_third = []
    ma60_fourth = []

    ma60_fifth = []
    ma60_sixth = []
    ma60_seventh = []
    ma60_eighth = []

    for index in range(len(candle)):
        _open = open[index]
        _high = high[index]
        _low = low[index]
        _close = close[index]
        _pct_chg = pct_chg[index]

        _ma5 = ma5[index]
        _ma10 = ma10[index]
        _ma20 = ma20[index]
        _ma30 = ma30[index]
        _ma55 = ma55[index]
        _ma60 = ma60[index]
        _ma120 = ma120[index]

        _ma5_slope = ma5_slope[index]
        _ma10_slope = ma10_slope[index]
        _ma20_slope = ma20_slope[index]
        _ma30_slope = ma30_slope[index]
        _ma55_slope = ma55_slope[index]
        _ma60_slope = ma60_slope[index]
        _ma120_slope = ma120_slope[index]

        _ema5 = ema5[index]
        _ema10 = ema10[index]
        _ema20 = ema20[index]
        _ema30 = ema30[index]
        _ema55 = ema55[index]
        _ema60 = ema60[index]
        _ema120 = ema120[index]

        _ema5_slope = ema5_slope[index]
        _ema10_slope = ema10_slope[index]
        _ema20_slope = ema20_slope[index]
        _ema30_slope = ema30_slope[index]
        _ema55_slope = ema55_slope[index]
        _ema60_slope = ema60_slope[index]
        _ema120_slope = ema120_slope[index]

        # MA60 葛南维第一大法则
        if is_ma60_first(index, candle, bias, ma, ma_slope):
            ma60_first.insert(index, 1)
        else:
            ma60_first.insert(index, 0)

        # MA60 葛南维第二大法则
        if is_ma60_second(index, candle, bias, ma, ma_slope):
            ma60_second.insert(index, 1)
        else:
            ma60_second.insert(index, 0)

        # MA60 葛南维第三大法则
        if is_ma60_third(index, candle, bias, ma, ma_slope):
            ma60_third.insert(index, 1)
        else:
            ma60_third.insert(index, 0)

        # MA60 葛南维第四大法则
        if is_ma60_fourth(index, candle, bias, ma, ma_slope):
            ma60_fourth.insert(index, 1)
        else:
            ma60_fourth.insert(index, 0)

        # MA60 葛南维第5大法则
        if is_ma60_fifth(index, candle, bias, ma, ma_slope):
            ma60_fifth.insert(index, 1)
        else:
            ma60_fifth.insert(index, 0)

        # MA60 葛南维第6大法则
        if is_ma60_sixth(index, candle, bias, ma, ma_slope):
            ma60_sixth.insert(index, 1)
        else:
            ma60_sixth.insert(index, 0)

        # MA60 葛南维第7大法则
        if is_ma60_seventh(index, candle, bias, ma, ma_slope):
            ma60_seventh.insert(index, 1)
        else:
            ma60_seventh.insert(index, 0)

        # MA60 葛南维第8大法则
        if is_ma60_eighth(index, candle, bias, ma, ma_slope):
            ma60_eighth.insert(index, 1)
        else:
            ma60_eighth.insert(index, 0)

    org_df['ma60_first'] = ma60_first
    org_df['ma60_second'] = ma60_second
    org_df['ma60_third'] = ma60_third
    org_df['ma60_fourth'] = ma60_fourth

    org_df['ma60_fifth'] = ma60_fifth
    org_df['ma60_sixth'] = ma60_sixth
    org_df['ma60_seventh'] = ma60_seventh
    org_df['ma60_eighth'] = ma60_eighth

    return org_df
