# -- coding: utf-8 -

from .long_analyze import long_analyze
from .short_analyze import short_analyze

"""
df: indicators with signals (long signals or short signals)
"""


def analyze(org_df):
    candle = org_df[['open', 'high', 'low', 'close', 'pct_chg', 'trade_date']].to_numpy()
    ma = org_df[['ma5', 'ma10', 'ma20', 'ma30', 'ma55', 'ma60', 'ma120']].to_numpy()
    ema = org_df[['ema5', 'ema10', 'ema20', 'ema30', 'ema55', 'ema60', 'ema120']].to_numpy()
    ma_slope = org_df[['ma5_slope', 'ma10_slope', 'ma20_slope', 'ma30_slope', 'ma55_slope',
                       'ma60_slope', 'ma120_slope']].to_numpy()
    ema_slope = org_df[['ema5_slope', 'ema10_slope', 'ema20_slope', 'ema30_slope', 'ema55_slope',
                        'ema60_slope', 'ema120_slope']].to_numpy()
    bias = org_df[['bias6', 'bias12', 'bias24', 'bias55', 'bias60', 'bias72', 'bias120']].to_numpy()
    td = org_df[['high_td', 'low_td']].to_numpy()

    yearly_price_position, yearly_price_position10, yearly_price_position20, \
    yearly_price_position30, yearly_price_position50, yearly_price_position70, \
    ma20_up, ema20_up, ma30_up, ema30_up, ma60_up, ema60_up, ma120_up, ema120_up, ma_arrange, ema_arrange, \
    short_ma_arrange1, short_ma_arrange2, short_ema_arrange1, short_ema_arrange2, \
    middle_ma_arrange1, middle_ma_arrange2, middle_ema_arrange1, middle_ema_arrange2, \
    long_ma_arrange1, long_ma_arrange2, long_ema_arrange1, long_ema_arrange2, \
    ma_gold_cross1, ma_gold_cross2, ma_gold_cross3, ma_gold_cross4, \
    ema_gold_cross1, ema_gold_cross2, ema_gold_cross3, ema_gold_cross4, \
    ma_silver_valley, ema_silver_valley, ma_gold_valley, ema_gold_valley, \
    ma_spider, ma_spider2, ema_spider, ema_spider2, \
    ma_glue, ema_glue, ma_out_sea, ema_out_sea, ma_hold_moon, ema_hold_moon, \
    ma_over_gate, ema_over_gate, ma_up_ground, ema_up_ground, \
    td8, td9, bias6, bias12, bias24, bias60, bias72, bias120, \
    stand_up_ma60, stand_up_ma120, stand_up_ema60, stand_up_ema120, \
    ma60_support, ema60_support, ma120_support, ema120_support, \
    ma_group_glue, ema_group_glue, ma_up_arrange51020, ma_up_arrange5102030, \
    ma_up_arrange510203060, ma_up_arrange203060, ma_up_arrange2060120, \
    ema_up_arrange51020, ema_up_arrange5102030, ema_up_arrange510203060, \
    ema_up_arrange203060, ema_up_arrange2055120, \
    ma55_first, ma55_second, ma55_third, ma55_fourth, \
    ma60_first, ma60_second, ma60_third, ma60_fourth, \
    ema55_first, ema55_second, ema55_third, ema55_fourth, \
    ema60_first, ema60_second, ema60_third, ema60_fourth, \
    hammer, pour_hammer, short_end, swallow_up, attack_short, \
    first_light, sunrise, flat_base, rise_line, down_screw = long_analyze(candle, ma, ema, ma_slope, ema_slope, bias, td)

    org_df['yearly_price_position'] = yearly_price_position
    org_df['yearly_price_position10'] = yearly_price_position10
    org_df['yearly_price_position20'] = yearly_price_position20
    org_df['yearly_price_position30'] = yearly_price_position30
    org_df['yearly_price_position50'] = yearly_price_position50
    org_df['yearly_price_position70'] = yearly_price_position70

    org_df['ma20_up'] = ma20_up
    org_df['ema20_up'] = ema20_up
    org_df['ma30_up'] = ma30_up
    org_df['ema30_up'] = ema30_up
    org_df['ma60_up'] = ma60_up
    org_df['ema60_up'] = ema60_up
    org_df['ma120_up'] = ma120_up
    org_df['ema120_up'] = ema120_up

    org_df['ma_arrange'] = ma_arrange
    org_df['ema_arrange'] = ema_arrange

    org_df['short_ma_arrange1'] = short_ma_arrange1
    org_df['short_ma_arrange2'] = short_ma_arrange2
    org_df['short_ema_arrange1'] = short_ema_arrange1
    org_df['short_ema_arrange2'] = short_ema_arrange2

    org_df['middle_ma_arrange1'] = middle_ma_arrange1
    org_df['middle_ma_arrange2'] = middle_ma_arrange2
    org_df['middle_ema_arrange1'] = middle_ema_arrange1
    org_df['middle_ema_arrange2'] = middle_ema_arrange2

    org_df['long_ma_arrange1'] = long_ma_arrange1
    org_df['long_ma_arrange2'] = long_ma_arrange2
    org_df['long_ema_arrange1'] = long_ema_arrange1
    org_df['long_ema_arrange2'] = long_ema_arrange2

    org_df['ma_gold_cross1'] = ma_gold_cross1
    org_df['ma_gold_cross2'] = ma_gold_cross2
    org_df['ma_gold_cross3'] = ma_gold_cross3
    org_df['ma_gold_cross4'] = ma_gold_cross4

    org_df['ema_gold_cross1'] = ema_gold_cross1
    org_df['ema_gold_cross2'] = ema_gold_cross2
    org_df['ema_gold_cross3'] = ema_gold_cross3
    org_df['ema_gold_cross4'] = ema_gold_cross4

    org_df['ma_silver_valley'] = ma_silver_valley
    org_df['ema_silver_valley'] = ema_silver_valley
    org_df['ma_gold_valley'] = ma_gold_valley
    org_df['ema_gold_valley'] = ema_gold_valley

    org_df['ma_spider'] = ma_spider
    org_df['ma_spider2'] = ma_spider2
    org_df['ema_spider'] = ema_spider
    org_df['ema_spider2'] = ema_spider2

    org_df['ma_glue'] = ma_glue
    org_df['ema_glue'] = ema_glue
    org_df['ma_out_sea'] = ma_out_sea
    org_df['ema_out_sea'] = ema_out_sea
    org_df['ma_hold_moon'] = ma_hold_moon
    org_df['ema_hold_moon'] = ema_hold_moon
    org_df['ma_over_gate'] = ma_over_gate
    org_df['ema_over_gate'] = ema_over_gate
    org_df['ma_up_ground'] = ma_up_ground
    org_df['ema_up_ground'] = ema_up_ground

    org_df['td8'] = td8
    org_df['td9'] = td9

    org_df['bias6'] = bias6
    org_df['bias12'] = bias12
    org_df['bias24'] = bias24
    org_df['bias60'] = bias60
    org_df['bias72'] = bias72
    org_df['bias120'] = bias120

    org_df['stand_up_ma60'] = stand_up_ma60
    org_df['stand_up_ma120'] = stand_up_ma120
    org_df['stand_up_ema60'] = stand_up_ema60
    org_df['stand_up_ema120'] = stand_up_ema120

    org_df['ma60_support'] = ma60_support
    org_df['ema60_support'] = ema60_support
    org_df['ma120_support'] = ma120_support
    org_df['ema120_support'] = ema120_support

    org_df['ma_group_glue'] = ma_group_glue
    org_df['ema_group_glue'] = ema_group_glue

    org_df['ma_up_arrange51020'] = ma_up_arrange51020
    org_df['ma_up_arrange5102030'] = ma_up_arrange5102030
    org_df['ma_up_arrange510203060'] = ma_up_arrange510203060
    org_df['ma_up_arrange203060'] = ma_up_arrange203060
    org_df['ma_up_arrange2060120'] = ma_up_arrange2060120

    org_df['ema_up_arrange51020'] = ema_up_arrange51020
    org_df['ema_up_arrange5102030'] = ema_up_arrange5102030
    org_df['ema_up_arrange510203060'] = ema_up_arrange510203060
    org_df['ema_up_arrange203060'] = ema_up_arrange203060
    org_df['ema_up_arrange2055120'] = ema_up_arrange2055120

    org_df['ma55_first'] = ma55_first
    org_df['ma55_second'] = ma55_second
    org_df['ma55_third'] = ma55_third
    org_df['ma55_fourth'] = ma55_fourth

    org_df['ma60_first'] = ma60_first
    org_df['ma60_second'] = ma60_second
    org_df['ma60_third'] = ma60_third
    org_df['ma60_fourth'] = ma60_fourth

    org_df['ema55_first'] = ema55_first
    org_df['ema55_second'] = ema55_second
    org_df['ema55_third'] = ema55_third
    org_df['ema55_fourth'] = ema55_fourth

    org_df['ema60_first'] = ema60_first
    org_df['ema60_second'] = ema60_second
    org_df['ema60_third'] = ema60_third
    org_df['ema60_fourth'] = ema60_fourth

    org_df['hammer'] = hammer
    org_df['pour_hammer'] = pour_hammer
    org_df['short_end'] = short_end
    org_df['swallow_up'] = swallow_up
    org_df['attack_short'] = attack_short
    org_df['first_light'] = first_light
    org_df['sunrise'] = sunrise
    org_df['flat_base'] = flat_base
    org_df['rise_line'] = rise_line
    org_df['down_screw'] = down_screw

    return org_df

