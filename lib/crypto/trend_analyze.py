# -- coding: utf-8 -
from config.common import START_INDEX
import lib.signal.common.trend_strategy as trend


def trend_analyze(org_df):
    candle = org_df[['open', 'high', 'low', 'close', 'pct_chg', 'trade_date']].to_numpy()

    up_trend = [0 for _ in range(len(org_df))]
    down_trend = [0 for _ in range(len(org_df))]
    strong_rise = [0 for _ in range(len(org_df))]
    strong_decline = [0 for _ in range(len(org_df))]

    up_pullback = [0 for _ in range(len(org_df))]
    down_pullback = [0 for _ in range(len(org_df))]
    up_break = [0 for _ in range(len(org_df))]
    down_break = [0 for _ in range(len(org_df))]
    hline_support = [0 for _ in range(len(org_df))]
    hline_resistance = [0 for _ in range(len(org_df))]

    _start_at = len(org_df) - 10

    for index in range(len(candle)):
        if index > _start_at:
            # 强势上涨
            if trend.is_strong_rise(index, org_df):
                strong_rise[index] = 1

            # 强势上涨
            if trend.is_strong_decline(index, org_df):
                strong_decline[index] = 1

            # 上涨趋势
            if trend.is_up_trend(index, org_df):
                up_trend[index] = 1

            # 下跌趋势
            if trend.is_down_trend(index, org_df):
                down_trend[index] = 1

    org_df['up_trend'] = up_trend
    org_df['down_trend'] = down_trend
    org_df['strong_rise'] = strong_rise
    org_df['strong_decline'] = strong_decline

    for index in range(len(candle)):
        if index > _start_at:
            # 上涨回调
            if trend.up_pullback(org_df, index):
                up_pullback[index] = 1

            # 下跌反弹
            if trend.down_pullback(org_df, index):
                down_pullback[index] = 1

            # 向上突破
            if trend.up_break(org_df, index):
                up_break[index] = 1

            # 向下突破
            if trend.down_break(org_df, index):
                down_break[index] = 1

            # 水平支撑
            if trend.hline_support(org_df, index):
                hline_support[index] = 1

            # 水平阻力
            if trend.hline_resistance(org_df, index):
                hline_resistance[index] = 1

    org_df['up_pullback'] = up_pullback
    org_df['down_pullback'] = down_pullback
    org_df['up_break'] = up_break
    org_df['down_break'] = down_break
    org_df['hline_support'] = hline_support
    org_df['hline_resistance'] = hline_resistance

    return org_df
