# -- coding: utf-8 -
from config.common import START_INDEX
import lib.signal.common.limit as limit
import lib.signal.common.trend_strategy as trend


def trend_analyze(org_df):
    candle = org_df[['open', 'high', 'low', 'close', 'pct_chg', 'trade_date']].to_numpy()

    limit_pullback = [0 for _ in range(len(org_df))]
    up_pullback = [0 for _ in range(len(org_df))]
    down_pullback = [0 for _ in range(len(org_df))]
    up_break = [0 for _ in range(len(org_df))]
    down_break = [0 for _ in range(len(org_df))]
    hline_support = [0 for _ in range(len(org_df))]
    hline_resistance = [0 for _ in range(len(org_df))]

    _start_at = START_INDEX

    for index in range(len(candle)):
        if index > _start_at:
            # 涨停回调
            # if limit.limit_pullback(org_df, index):
            #     limit_pullback[index] = 1

            # 上涨回调
            if trend.up_pullback(org_df, index):
                up_pullback[index] = 1

            # 下跌反弹
            if trend.down_pullback(org_df, index):
                down_pullback[index] = 1

            # 向上突破
            # if trend.up_break(org_df, index):
            #     up_break[index] = 1

            # 向下突破
            # if trend.down_break(org_df, index):
            #     down_break[index] = 1

            # 水平支撑
            # if trend.hline_support(org_df, index):
            #     hline_support[index] = 1

            # 水平阻力
            # if trend.hline_resistance(org_df, index):
            #     hline_resistance[index] = 1

    org_df['limit_pullback'] = limit_pullback
    org_df['up_pullback'] = up_pullback
    org_df['down_pullback'] = down_pullback
    org_df['up_break'] = up_break
    org_df['down_break'] = down_break
    org_df['hline_support'] = hline_support
    org_df['hline_resistance'] = hline_resistance

    return org_df
