import pandas as pd
import numpy as np
import mplfinance as mpf
import matplotlib.dates as mpl_dates
from sqlalchemy import text
from klines import get_stock_klines, get_crypto_klines
import lib.signal.common.hline_fractal as Hlines

gran = 900
gran = 3600
exchange = 'binance'
inst_id = 'ETHUSDT'
inst_id = 'DYDXUSDT'
inst_id = 'STORJUSDT'
inst_id = 'RLCUSDT'
inst_id = 'CRVUSDT'
# inst_id = 'CTSIUSDT'
inst_id = 'OCEANUSDT'
inst_id = '1000LUNCUSDT'
inst_id = '1000LUNCUSDT'
inst_id = 'BANDUSDT'
inst_id = 'OCEANUSDT'

df = get_crypto_klines(exchange, inst_id, gran, 300)


def plot_candle():
    hlines = Hlines.calc_hlines(df, len(df))

    mpf.plot(df, volume=True, style='yahoo', type='candle', mav=[10, 20, 60],
             hlines=dict(hlines=hlines, colors=['r'], linestyle='-.', linewidths=1, alpha=0.8),
             figscale=1.35)


"""
breakout & pullback

最近50根K线
水平位位于开盘价和收盘价之间的K线数量不超过5根
收盘位于水平位上方
MA20/MA60上行
加分: 水平位出现较多上影线或下影线


"""

if __name__ == "__main__":
    plot_candle()
