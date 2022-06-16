# -- coding: utf-8 -
from lib.signal.common.ma import is_ma20_rise, is_ma30_rise, is_ma60_rise, is_ma120_rise, \
    is_up_ma_arrange, is_up_short_ma_arrange, is_up_middle_ma_arrange, is_up_long_ma_arrange, \
    is_gold_cross, \
    is_ma60_support, is_ma120_support, is_stand_up_ma60, is_stand_up_ma120, \
    is_ma_glue, is_ma_out_sea, is_ma_hold_moon, is_ma_over_gate, is_ma_up_ground, \
    is_ma_gold_valley, is_ma_silver_valley, is_ma_spider


def long_analyze(org_df):
    candle = org_df[['open', 'high', 'low', 'close', 'pct_chg', 'trade_date']].to_numpy()
    ma = org_df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    ema = org_df[['ema5', 'ema10', 'ema20', 'ema30', 'ema55', 'ema60', 'ema120']].to_numpy()

    ma5 = ma[:, 0]
    ma10 = ma[:, 1]
    ma20 = ma[:, 2]
    ma30 = ma[:, 3]

    ma20_up = [0 for _ in range(len(org_df))]
    ema20_up = [0 for _ in range(len(org_df))]
    ma30_up = [0 for _ in range(len(org_df))]
    ema30_up = [0 for _ in range(len(org_df))]
    ma60_up = [0 for _ in range(len(org_df))]
    ema60_up = [0 for _ in range(len(org_df))]
    ma120_up = [0 for _ in range(len(org_df))]
    ema120_up = [0 for _ in range(len(org_df))]

    ma_gold_cross1 = [0 for _ in range(len(org_df))]
    ma_gold_cross2 = [0 for _ in range(len(org_df))]
    ma_gold_cross3 = [0 for _ in range(len(org_df))]
    ma_gold_cross4 = [0 for _ in range(len(org_df))]

    ma_out_sea = [0 for _ in range(len(org_df))]
    ma_hold_moon = [0 for _ in range(len(org_df))]
    ma_up_ground = [0 for _ in range(len(org_df))]
    ma_glue = [0 for _ in range(len(org_df))]

    _start_at = 280

    for index in range(len(candle)):
        if index > _start_at:
            ma20_up[index] = 1 if is_ma20_rise(index, ma) else 0
            ema20_up[index] = 1 if is_ma20_rise(index, ema) else 0
            ma30_up[index] = 1 if is_ma30_rise(index, ma) else 0
            ema30_up[index] = 1 if is_ma30_rise(index, ema) else 0
            ma60_up[index] = 1 if is_ma60_rise(index, ma) else 0
            ema60_up[index] = 1 if is_ma60_rise(index, ema) else 0
            ma120_up[index] = 1 if is_ma120_rise(index, ma) else 0
            ema120_up[index] = 1 if is_ma120_rise(index, ema) else 0

            ma_gold_cross1[index] = 1 if is_gold_cross(index, ma5, ma10) else 0
            ma_gold_cross2[index] = 1 if is_gold_cross(index, ma5, ma20) else 0
            ma_gold_cross3[index] = 1 if is_gold_cross(index, ma10, ma20) else 0
            ma_gold_cross4[index] = 1 if is_gold_cross(index, ma10, ma30) else 0

            ma_out_sea[index] = 1 if is_ma_out_sea(index, org_df) else 0
            ma_glue[index] = 1 if is_ma_glue(index, org_df) else 0
            ma_hold_moon[index] = 1 if is_ma_hold_moon(index, org_df) else 0
            ma_up_ground[index] = 1 if is_ma_up_ground(index, org_df) else 0

    org_df['ma20_up'] = ma20_up
    org_df['ema20_up'] = ema20_up
    org_df['ma30_up'] = ma30_up
    org_df['ema30_up'] = ema30_up
    org_df['ma60_up'] = ma60_up
    org_df['ema60_up'] = ema60_up
    org_df['ma120_up'] = ma120_up
    org_df['ema120_up'] = ema120_up

    org_df['ma_gold_cross1'] = ma_gold_cross1
    org_df['ma_gold_cross2'] = ma_gold_cross2
    org_df['ma_gold_cross3'] = ma_gold_cross3
    org_df['ma_gold_cross4'] = ma_gold_cross4

    org_df['ma_glue'] = ma_glue
    org_df['ma_out_sea'] = ma_out_sea
    org_df['ma_hold_moon'] = ma_hold_moon
    org_df['ma_up_ground'] = ma_up_ground

    return org_df
