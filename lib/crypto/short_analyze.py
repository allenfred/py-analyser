# -- coding: utf-8 -
from lib.signal.crypto.ma import is_ma20_down, is_ma30_down, is_ma60_down, is_ma120_down, \
    is_dead_cross


def short_analyze(org_df):
    """
    计算空头信号

    :return: df
    """

    candle = org_df[['open', 'high', 'low', 'close', 'pct_chg', 'trade_date']].to_numpy()
    ma = org_df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    ema = org_df[['ema5', 'ema10', 'ema20', 'ema30', 'ema55', 'ema60', 'ema120']].to_numpy()
    bias = org_df[['bias6', 'bias12', 'bias24', 'bias55', 'bias60', 'bias72', 'bias120']].to_numpy()
    td = org_df[['high_td', 'low_td']].to_numpy()

    ma5 = ma[:, 0]
    ma10 = ma[:, 1]
    ma20 = ma[:, 2]
    ma30 = ma[:, 3]

    ma20_down = [0 for _ in range(len(org_df))]
    ema20_down = [0 for _ in range(len(org_df))]
    ma30_down = [0 for _ in range(len(org_df))]
    ema30_down = [0 for _ in range(len(org_df))]
    ma60_down = [0 for _ in range(len(org_df))]
    ema60_down = [0 for _ in range(len(org_df))]
    ma120_down = [0 for _ in range(len(org_df))]
    ema120_down = [0 for _ in range(len(org_df))]

    ma_dead_cross1 = [0 for _ in range(len(org_df))]
    ma_dead_cross2 = [0 for _ in range(len(org_df))]
    ma_dead_cross3 = [0 for _ in range(len(org_df))]
    ma_dead_cross4 = [0 for _ in range(len(org_df))]

    _start_at = 280

    for index in range(len(candle)):
        if index > _start_at:
            # ma20_down[index] = 1 if is_ma20_down(index, ma) else 0
            # ema20_down[index] = 1 if is_ma20_down(index, ema) else 0
            # ma30_down[index] = 1 if is_ma30_down(index, ma) else 0
            # ema30_down[index] = 1 if is_ma30_down(index, ema) else 0
            # ma60_down[index] = 1 if is_ma60_down(index, ma) else 0
            # ema60_down[index] = 1 if is_ma60_down(index, ema) else 0
            # ma120_down[index] = 1 if is_ma120_down(index, ma) else 0
            # ema120_down[index] = 1 if is_ma120_down(index, ema) else 0

            ma_dead_cross1[index] = 1 if is_dead_cross(index, ma5, ma10) else 0
            ma_dead_cross2[index] = 1 if is_dead_cross(index, ma5, ma20) else 0
            ma_dead_cross3[index] = 1 if is_dead_cross(index, ma10, ma20) else 0
            ma_dead_cross4[index] = 1 if is_dead_cross(index, ma10, ma30) else 0

    org_df['ma20_down'] = ma20_down
    org_df['ema20_down'] = ema20_down
    org_df['ma30_down'] = ma30_down
    org_df['ema30_down'] = ema30_down
    org_df['ma60_down'] = ma60_down
    org_df['ema60_down'] = ema60_down
    org_df['ma120_down'] = ma120_down
    org_df['ema120_down'] = ema120_down

    org_df['ma_dead_cross1'] = ma_dead_cross1
    org_df['ma_dead_cross2'] = ma_dead_cross2
    org_df['ma_dead_cross3'] = ma_dead_cross3
    org_df['ma_dead_cross4'] = ma_dead_cross4

    return org_df
